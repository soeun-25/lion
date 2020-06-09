from django.urls import path
from . import views

urlpatterns = [
    # 2. path들 중에서 name이 movie인 path를 실행
    # 여기서 실행이란, path의 두번째 인자(views.movie)를 실행하는것을 말함
    path('movie/', views.movie, name = "movie"),
    path('details1/', views.details1, name = "details1"),
    path('details2/', views.details2, name = "details2"),
    path('details3/', views.details3, name = "details3"),
]
# 여기는 app의 url입니다.
# 따라서 하나의 app에서 관리하는 url을 적어주면 됩니다. 
# firstapp에는 movie, payment가 있네요! 그럼 movie와 payment만 적어주시면 됩니다!
