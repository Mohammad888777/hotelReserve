from django.contrib import admin
from .models import FirstSlider,Service,ServiceFeatcher


admin.site.register([
    FirstSlider,Service,ServiceFeatcher
])
