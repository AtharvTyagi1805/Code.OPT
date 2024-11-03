from django.urls import path
from .views import signup, user_login, home, expertIMP, aboutUS, studyMAT

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path('expert_implementaion/', expertIMP, name='expertIMP'),
    path("about-us/",aboutUS, name="about"),
    path("study-material/",studyMAT, name="study"),
]