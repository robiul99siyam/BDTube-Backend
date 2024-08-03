from django.contrib import admin
from .models import categoryModel,contentModel,ReviewModel,Notification,WatchLog


class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}
    list_display = ['name','slug']
admin.site.register(categoryModel,categoryAdmin)
admin.site.register(contentModel)
admin.site.register(ReviewModel)
admin.site.register(WatchLog)

