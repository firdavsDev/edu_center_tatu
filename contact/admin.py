from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contact

admin.site.site_header = "Python Academy Admin Portal"
admin.site.site_title = "Python Academy Admin Portal"
admin.site.index_title = "Welcome to Python Academy Admin Portal"
admin.site.empty_value_display = "Ma'lumot yo'q"
admin.site.unregister(Group)

# Register Contact model


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'tg_username', 'is_asnwered', 'created')
    list_filter = ('is_asnwered', 'created')
    search_fields = ('name', 'phone', 'tg_username')
    date_hierarchy = 'created'
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = True
    list_display_links = ('name', 'phone')
    list_editable = ('is_asnwered',)
    actions = ('make_answered', 'make_unanswered')

    def make_answered(self, request, queryset):
        queryset.update(is_asnwered=True)
        self.message_user(request, 'Xabarlar muvaffaqiyatli javoblandi!')
    make_answered.short_description = 'Xabarlar javoblandi'

    def make_unanswered(self, request, queryset):
        queryset.update(is_asnwered=False)
        self.message_user(request, 'Xabarlar muvaffaqiyatli javoblanmadi!')
    make_unanswered.short_description = 'Xabarlar javoblanmadi'
