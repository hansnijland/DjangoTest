from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Voetbalspeler
from .models import Wielrenner


admin.site.register(Post)
admin.site.register(Voetbalspeler)
admin.site.register(Wielrenner)
