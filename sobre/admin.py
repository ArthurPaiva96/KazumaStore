from django.contrib import admin

# Register your models here.
from sobre.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['texto', 'estilo', 'classe']
    search_fields = ['texto', 'estilo', 'classe']

admin.site.register(Quote,QuoteAdmin)