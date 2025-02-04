import math
from django.http import JsonResponse
from django_stor import settings
from .forms import UserForms
from .models import Transaction, PaymenMethod
from stor.models import Product, Cart, Order
from django.shortcuts import redirect
from django.utils.translation import gettext as _
import stripe
def stripe_config(request):
   return JsonResponse({
       'public_key': settings.STRIPE_PUBLISHABLE_KEY
   })

def stripe_transaction(request):
    transaction = make_transaction(request, PaymenMethod.Stripe)
    if not transaction:
        return JsonResponse({
            'message': _('Please enter valid information.')
        }, status=400)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=transaction.amount * 100,
        currency=settings.CURRENCY,
        payment_method_types=['card'],
        metadata={
            'transaction': transaction.id
        }
    )

    return JsonResponse({
            'client_secret': intent['client_secret']

    })
def paypal_transaction(request):
    transaction = make_transaction(request, PaymenMethod.Stripe)




def make_transaction(request, pm):
    form = UserForms(request.POST)
    if form.is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.items)


        total = 0
        for item in products:
            total += item.price

        if total <= 0:
            return redirect('store.cart')


        return Transaction.objects.create(
            customer=form.cleaned_data,
            session =request.session.session_key,
            payment_method=pm,
            items=cart.items,
            amount=math.ceil(total)
        )

def send_order_email(order, products):
    msg_html = render_to_string('emails/order.html',{
        'order': order,
        'products': products
    })

    send_mail(
        subject='New Order',
        html_message=msg_html,
        message=msg_html,
        from_email='noreply@example.com',
        recipient_list=[order.customer['email']]
    )