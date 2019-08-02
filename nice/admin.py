from django.contrib import admin
from .models import Korean, Sforeigner, Lforeigner, K_Comment, Lf_Comment, Sf_Comment
# Register your models here.

admin.site.register(Korean)
admin.site.register(Sforeigner)
admin.site.register(Lforeigner)
admin.site.register(K_Comment)
admin.site.register(Lf_Comment)
admin.site.register(Sf_Comment)