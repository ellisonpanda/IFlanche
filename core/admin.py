from django.contrib import admin
from .models import CardapioSemanal
from .models import AdminRequest

admin.site.register(CardapioSemanal)
@admin.register(AdminRequest)
class AdminRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'aprovado', 'data_solicitacao')
    list_filter = ('aprovado',)
    actions = ['aprovar_admins']

    def aprovar_admins(self, request, queryset):
        for req in queryset:
            req.aprovado = True
            req.save()
            user = req.user
            user.is_active = True
            user.is_staff = True
            user.save()
        self.message_user(request, "Admins aprovados com sucesso!")

    @admin.register(AdminRequest)
class AdminRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'aprovado', 'data_solicitacao', 'aprovado_por')
    list_filter = ('aprovado',)
    actions = ['aprovar_solicitacoes']

    def aprovar_solicitacoes(self, request, queryset):
        for solicitacao in queryset:
            solicitacao.aprovado = True
            solicitacao.user.is_active = True
            solicitacao.user.is_staff = True
            solicitacao.user.save()
            solicitacao.aprovado_por = request.user
            solicitacao.save()
        self.message_user(request, "Solicitações aprovadas com sucesso!")
    aprovar_solicitacoes.short_description = "Aprovar solicitações selecionadas"