from django.contrib import admin
from .models import Blog,Comment
from .models import Customer
from .models import Team
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Customer)
admin.site.register(Team)