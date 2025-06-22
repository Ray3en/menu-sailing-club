from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("sort_order", "name", "slug")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sort_order",)


@admin.register(Subcategory)
class SubcategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("sort_order", "name", "slug", "category")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("category",)
    ordering = ("sort_order",)


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("sort_order", "title", "price", "is_available", "subcategory", "image_preview")
    list_display_links = ("title",)
    list_filter = ("subcategory",)
    search_fields = ("title",)
    readonly_fields = ("image_preview",)
    ordering = ("sort_order",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = "Превью"
