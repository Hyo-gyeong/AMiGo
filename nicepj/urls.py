from django.contrib import admin
from django.urls import path
import nice.views
import account.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


urlpatterns = [
    #chat봇 url
    url(r'^chat/', include('chat.urls')),
    url(r'^admin/', admin.site.urls),

    # main pages
    path('', nice.views.index, name="index"),
    path('korean', nice.views.korean, name = "korean"),
    path('lforeigner', nice.views.lforeigner, name = "lforeigner"),
    path('sforeigner', nice.views.sforeigner, name = "sforeigner"),
    path('about/', nice.views.about, name="about"),

    #검색기능 관련
    path('korean_search', nice.views.korean_search, name = "korean_search"),

    # create & detail & delete & update
    path('create_korean', nice.views.create_korean, name="create_korean"),
    path('create_lforeigner', nice.views.create_lforeigner, name = "create_lforeigner"),
    path('create_sforeigner', nice.views.create_sforeigner, name = "create_sforeigner"),
    
    path('korean/<int:korean_id>', nice.views.korean_detail, name="korean_detail"),
    path('lforeigner/<int:lforeigner_id>', nice.views.lforeigner_detail, name="lforeigner_detail"),
    path('sforeigner/<int:sforeigner_id>', nice.views.sforeigner_detail, name="sforeigner_detail"),

    path('korean/delete/<int:korean_id>', nice.views.korean_delete, name="korean_delete"),
    path('lforeigner/<int:lforeigner_id>/delete', nice.views.lforeigner_delete, name="lforeigner_delete"),
    path('sforeigner/delete/<int:sforeigner_id>', nice.views.sforeigner_delete, name="sforeigner_delete"),

    path('korean_updateForm/<int:korean_id>', nice.views.korean_updateForm, name = "korean_updateForm"),
    path('iforeigner_updateForm/<int:lforeigner_id>', nice.views.lforeigner_updateForm, name = "lforeigner_updateForm"),
    path('sforeigner_updateForm/<int:sforeigner_id>', nice.views.sforeigner_updateForm, name = "sforeigner_updateForm"),

    # comment & comment_delete
    path('<int:korean_id>/kcomment/create', nice.views.kcomment_create, name="kcomment_create"),
    path('<int:lforeigner_id>/lfcomment/create', nice.views.lfcomment_create, name="lfcomment_create"),
    path('<int:sforeigner_id>/sfcomment/create', nice.views.sfcomment_create, name="sfcomment_create"),

    path('<int:korean_id>/kcomment/<int:kcomment_id>/delete', nice.views.kcomment_delete, name="kcomment_delete"),
    path('<int:lforeigner_id>/lfcomment/<int:lfcomment_id>/delete', nice.views.lfcomment_delete, name="lfcomment_delete"),
    path('<int:sforeigner_id>/sfcomment/<int:sfcomment_id>/delete', nice.views.sfcomment_delete, name="sfcomment_delete"),



    #계정관련 url
    path('account/signin', account.views.signin, name = "signin"),
    path('account/signup', account.views.signup, name = 'signup'),
    path('account/logout', account.views.logout, name= "logout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
