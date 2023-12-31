"""
URL configuration for studio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('manager/edit_order/<int:order_id>/', edit_order, name='edit_order'),
    path('manager/requests/', requests, name='requests'),
    path('manager/executors/', executors, name='executors'),
    path('manager/executors/<int:pk>/delete/', delete_executor, name='delete_executor'),
    path('manager/executors/<int:pk>/edit/', edit_executor, name='edit_executor'),
    path('manager/feedback/', feedback_list, name='feedback'),
    path('manager/feedback/<int:pk>/delete/', delete_feedback, name='delete_feedback'),
    path('manager/', manager, name='manager'),

    path('client/order/', order, name='order'),
    path('client/myorders/', myorders, name='myorders'),
    path('delete_request/<int:request_id>/', delete_request, name='delete_request'),
    path('client/answers/', answers, name='answers'),
    path('client/', client, name='client'),
    path('register/', registration_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


