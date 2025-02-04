import os
import django
from django_stor import settings
from django.http import HttpResponse
from checkout import models
from stor.models import Order, Product
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import stripe
import json

# تهيئة Django لاستخدام الإعدادات
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_stor.settings")
django.setup()

@csrf_exempt
def stripe_webhook(request):
    print('✅ Stripe Webhook Received')

    print(f'🔍 Request body: {request.body}')  # طباعة الطلب
    print(f'🔍 Headers: {request.headers}') 
    print('✅ Stripe Webhook Received')

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        print('❌ Invalid payload')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        print('❌ Invalid signature')
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        metadata = payment_intent.get('metadata', {})
        transaction_id = metadata.get('transaction')

        if not transaction_id:
            print("⚠️ Transaction ID is missing in metadata!")
            return HttpResponse(status=400)

        print(f'✅ Payment successful for transaction: {transaction_id}')
        mak_order(transaction_id)
    else:
        print(f'⚠️ Unhandled event type: {event["type"]}')

    return HttpResponse(status=200)

def mak_order(transaction_id):
    print(f"🔄 Processing order for transaction ID: {transaction_id}")

    try:
        # محاولة استرجاع المعاملة بناءً على معرف المعاملة
        transaction = models.Transaction.objects.get(pk=transaction_id)
        items = json.loads(transaction.items) if isinstance(transaction.items, str) else transaction.items
        products = Product.objects.filter(pk__in=items)

        print(f"📦 Products in order: {products}")

        # استخدام بيانات العميل مباشرة من transaction.customer
        customer_email = transaction.customer.get('email')  # استخراج البريد الإلكتروني
        customer_name = f"{transaction.customer.get('first_name', '')} {transaction.customer.get('last_name', '')}"  # الاسم الكامل

        if not customer_email:
            print("⚠️ Customer email is missing!")
            return HttpResponse(status=400)

        # إنشاء الطلب المرتبط بالمعاملة
        order = Order.objects.create(transaction=transaction)  
        for product in products:
            order.orderproduct_set.create(product_id=product.id, price=product.price)
            print(f"✅ OrderProduct created for {product.name} with price {product.price}")

        # تجهيز محتوى البريد الإلكتروني
        msg_html = render_to_string('email/order.html', {
            'order': order,
            'products': products,
            'customer_name': customer_name,  # اسم العميل
            'customer_email': customer_email,  # بريد العميل
        })

        # إرسال البريد الإلكتروني
        send_mail(
            subject='New Order',
            html_message=msg_html,
            message=msg_html,
            from_email='noreply@example.com',
            recipient_list=[customer_email],  # إرسال البريد الإلكتروني إلى العميل مباشرة
            fail_silently=False, 
        )

        print("📨 Email sent successfully!")

    except Exception as e:
        print(f"❌ Error processing order: {e}")
