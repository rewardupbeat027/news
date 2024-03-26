from django.contrib import admin

# Register your models here.
from .models import News, SuperModel, MyModel, VisitedPage

admin.site.register(News)
admin.site.register(SuperModel)
admin.site.register(MyModel)
admin.site.register(VisitedPage)

