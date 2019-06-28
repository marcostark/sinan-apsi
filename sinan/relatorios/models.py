from django.contrib import admin
from django.db import models
from django.contrib.admin import ModelAdmin
from django.db.models import DateTimeField
from django.db.models.aggregates import Count, Sum, StdDev, Max, Min
from agravos.models import NotificaoDengue

# RELATORIOS -----------------------------------------------------
from django.db.models.functions import Trunc


class Relatorio(NotificaoDengue):
    class Meta:
        proxy = True
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'



@admin.register(Relatorio)
class SaleSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/notificacao_dengue_change_list.html'
    # date_hierarchy = 'created'
    date_hierarchy = 'agravo__data_notificacao'
    list_filter = (
        'agravo__data_notificacao',
        'agravo__data_primeiros_sintomas',
        'sinais_clinicos'
    )
    #
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
    #
    #
    #
        metrics = {
            'total': Count('id'),
            'valor_total': Sum('sorotipo')
        }

        response.context_data['summary'] = list(
            qs
                .values('agravo__agravo','sorotipo')
                .annotate(**metrics)
                .order_by('-valor_total')
        )
        print(response.context_data['summary'])
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        # summary_over_time = qs.annotate(
        #     period=Trunc(
        #         'agravo__data_notificacao',
        #         'day',
        #         output_field=DateTimeField(),
        #     ),
        # ).values('period').annotate(total=Sum('sorotipo')).order_by('period')
        # #
        # summary_range = summary_over_time.aggregate(
        #     low=Min('total'),
        #     high=Max('total'),
        # )
        # high = summary_range.get('high', 0)
        # low = summary_range.get('low', 0)
        # response.context_data['summary_over_time'] = [{
        #     'period': x['period'],
        #     'total': x['total'] or 0,
        #     'pct': \
        #         ((x['total'] or 0) - low) / (high - low) * 100
        #         if high > low else 0,
        # } for x in summary_over_time]
        # print(summary_over_time)

        return response