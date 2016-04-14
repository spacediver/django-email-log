from django.contrib import admin
from django.template.defaultfilters import linebreaksbr
from .models import Email
from django import forms
from django.contrib.admin import widgets


class EmailAdmin(admin.ModelAdmin):
    list_display = ['recipients', 'from_email', 'subject', 'date_sent', 'ok']
    list_filter = ['date_sent', 'ok']
    readonly_fields = ['from_email', 'recipients', 'subject',
                       'body_formatted',
                       'html_body_formatted',
                       'date_sent', 'ok']
    search_fields = ['subject', 'body', 'recipients']
    exclude = ['body', 'html_body']

    def has_delete_permission(self, *args, **kwargs):
        return False

    def has_add_permission(self, *args, **kwargs):
        return False

    def body_formatted(self, obj):
        return linebreaksbr(obj.body)

    def html_body_formatted(self, obj):
        return linebreaksbr(obj.html_body)

    body_formatted.short_description = "body"
    html_body_formatted.short_description = "html body"


admin.site.register(Email, EmailAdmin)
