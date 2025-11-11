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