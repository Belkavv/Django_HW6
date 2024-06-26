from django.contrib import admin
from .models import Client, Product, Order


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date']
    ordering = ['name', 'phone_number', 'address', 'registration_date']
    list_filter = ['name', 'email', 'address', 'registration_date']
    search_fields = ['name', 'address']
    search_help_text = 'Поиск по полям (имя и адрес)'

    readonly_fields = ['registration_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email', 'phone_number', 'address'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Дата регистрации',
                'fields': ['registration_date'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'added_date', 'image']
    ordering = ['name', 'price', 'quantity', 'added_date']
    list_filter = ['name', 'price', 'quantity', 'added_date']
    search_fields = ['name']
    search_help_text = 'Поиск по названию товара'

    readonly_fields = ['added_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Описание стоимость и количество товара',
            {
                'fields': ['description', 'price', 'quantity'],
            }
        ),
        (
            'Дата создания товара',
            {
                'fields': ['added_date'],
            }
        ),
        (
            'Изображение',
            {
                'fields': ['image'],
            }
        )
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']
    filter_horizontal = ['products']
    ordering = ['client', 'products', 'total_amount', 'order_date']
    list_filter = ['client', 'products', 'total_amount', 'order_date']
    search_fields = ['client']
    search_help_text = 'Поиск по клиентам'

    readonly_fields = ['order_date', 'total_amount']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Товары',
            {
                'fields': ['products'],
            }
        ),
        (
            'Сумма заказа',
            {
                'fields': ['total_amount'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Дата создания заказа',
                'fields': ['order_date'],
            }
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
