from django.contrib import admin
from .models import Blog
from .models import Customer
from .models import Team
# Register your models here.

admin.site.register(Blog)
admin.site.register(Customer)
admin.site.register(Team)