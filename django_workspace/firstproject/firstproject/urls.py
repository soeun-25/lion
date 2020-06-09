from django.contrib import admin
from django.urls import path, include
from firstapp import views
from firstapp import urls as firstapp_urls


urlpatterns = [
    path('', views.main),
    path('admin/', admin.site.urls),
    path('firstapp/', include(firstapp_urls)), #firstapp의 url을 모아서 관리하겠다는 코드
]
# 여기는 프로젝트의 url입니다.
# 따라서 제일 기본적인 url만 적어주시면 됩니다!
# 위에 코드처럼 1. admin페이지 url 2. app들의 url모아서 관리하겠다는 코드 등등을 적어주시면 되요
# 만약 secondeapp을 만든다면 path('secondeapp/', include(seconde_urls)),를 추가하시면 됩니다
