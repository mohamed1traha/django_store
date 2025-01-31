from django.shortcuts import render 
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.translation import gettext as _ 
from . import models





# Create your views here.

def index(request):
    products = models.Product.objects.select_related('author').filter(featured = True)
    sliders = models.Slider.objects.order_by('order')
    return render(
        request, 'index.html',
        {
            'products' : products,
            'sliders' : sliders,
        }
    )


def product(request,pid):
    product = models.Product.objects.select_related('author').get(id = pid)
    return render(
        request, 'product.html',
        {
            'product':product
        }
    )


def category(request,cid=None):
    cat = None
    where = {}
    query = request.GET.get('query')
    cid = request.GET.get('category',cid)

    if cid:
        cat = models.Category.objects.get(pk=cid)
        where['category_id'] = cid
        
    if query:
        where['name__icontains'] = query

    products = models.Product.objects.filter(**where)
    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')  # الحصول على رقم الصفحة
    page_obj = paginator.get_page(page_num)

    return render(
        request, 'category.html',
        {
            'page_obj' : page_obj,
            'category' : cat,
        }
    )




def cart(request):
    return render(request, 'cart.html')


  # تأكد من استيراد النموذج Cart بشكل صحيح

def cart_update(request, pid):
    # التأكد من وجود session_key
    if not request.session.session_key:
        request.session.create()

    session_id = request.session.session_key

    # البحث عن العربة بناءً على session_id
    cart_model = models.Cart.objects.filter(session_id=session_id).last()

    if cart_model is None:
        # إنشاء عربة جديدة إذا لم تكن موجودة
        cart_model = models.Cart.objects.create(session_id=session_id, items=[pid])
    elif pid not in cart_model.items:
        # إضافة المنتج إلى العربة
        cart_model.items.append(pid)
        cart_model.save()

    return JsonResponse({
        'message': _('The product has been added to your cart.'),
        'items_count': len(cart_model.items),
    })

    


def cart_remove(request, pid):
    session_id = request.session.session_key

    if not session_id:
        # إعادة استجابة فارغة إذا لم يكن هناك جلسة
        return JsonResponse({'message': 'No session found.'}, status=400)
    
    # البحث عن عربة التسوق بناءً على session_id
    cart_model = models.Cart.objects.filter(session_id=session_id).first()

    if cart_model is None:
        # إعادة استجابة إذا لم يتم العثور على العربة
        return JsonResponse({'message': 'Cart not found.'}, status=404)
    
    # التحقق من وجود المنتج داخل العناصر
    if pid in cart_model.items:
        cart_model.items.remove(pid)  # إزالة المنتج من القائمة
        cart_model.save()  # حفظ التغييرات
        return JsonResponse({
            'message': 'The product has been removed from your cart.',
            'items_count': len(cart_model.items),
        })
    
    # إذا كان المنتج غير موجود
    return JsonResponse({'message': 'Product not found in cart.'}, status=404)



def checkout(request):
    return render(request, 'checkout.html')


def checkout_complete(request):

    return render(request, 'checkout_complete.html')
