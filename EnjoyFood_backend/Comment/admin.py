from django.contrib import admin

from Comment.models import CommentPlan


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['r_star', 'r_content', 'user', 'plan', 'r_data']


admin.site.register(CommentPlan, CommentAdmin)
