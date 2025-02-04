from django.contrib import admin
from reports.models import OrderReports
from stor.models import Order
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _
from django.db.models.functions import ExtractYear,ExtractMonth,ExtractWeek
from django.db.models import Sum
import json
# Register your models here.

@admin.register(OrderReports)
class OrderAdmin(admin.ModelAdmin):

    change_list_template = 'admin/reports/orders.html'
    
    def has_change_permission(self, request, obj = None):
        return False

    def has_add_permission(self, request):
        return False
    
    def changelist_view(self, request, extra_context = None): 


        yearly_stats = (
            Order.objects.select_related('transaction')
            .annotate(year=ExtractYear('created_at'))
            .values('year')
            .annotate(num=Sum('transaction__amount'))
        )
        monthly_stats = (
            Order.objects.select_related('transaction')
            .annotate(year=ExtractYear('created_at'))
            .annotate(month=ExtractMonth('created_at'))
            .values('year','month')
            .annotate(num=Sum('transaction__amount'))[:30]
        )
        week_stats = (
            Order.objects.select_related('transaction')
            .annotate(year=ExtractYear('created_at'))
            .annotate(week=ExtractWeek('created_at'))
            .values('year','week')
            .annotate(num=Sum('transaction__amount'))[:30]
        )

        context = {
            **self.admin_site.each_context(request),
            'yearly_stats':json.dumps(list(yearly_stats)),
            'monthly_stats':json.dumps(list(monthly_stats)),
            'week_stats':json.dumps(list(week_stats)),
            'title': _('Order Report')
        }


        return TemplateResponse(
            request, self.change_list_template,context
        )