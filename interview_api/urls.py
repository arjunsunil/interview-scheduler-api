from django.urls import path, include

from rest_framework.routers import DefaultRouter

from interview_api import views

from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='Jiffy Swagger Help')

router = DefaultRouter()
router.register('user', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', swagger_view)
]
