"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from foodapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saveUser', views.saveUser),
    path('second', views.secondpage),
    path('afterlogin', views.afterlogin),
    path('userlogin', views.userlogin),
    path("", views.index, name="index"),
    path("header/", views.header, name="header"),
    path("about/", views.about, name="about"),
    path("feedback/", views.feedback, name="feedback"),
    path("footer", views.footer, name="footer"),
    path("home/", views.home, name="home"),
    path("menu/", views.about, name="menu"),
    path("dishes", views.dishes, name="dishes"),
    path("cart/", views.cart, name="cart"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    # path("saveUser/", views.saveUser, name="saveUser"),
    path("profile/", views.profile, name="profile"),
    path("staticpage/", views.staticpage, name="static"),
###########################################################################################################
    path("adminindex/", views.adminindex, name="adminindex"),
    path("updatedishes/", views.updatedishes, name="updatedishes"),
    path("userinfo/", views.userinfo, name="userinfo"),
    path("adddishes/", views.adddishes, name="adddishes"),
    #######################################################
    path("insert", views.insert, name="insert"),
    path("show", views.show, name="show"),
    # path('logout',views.logout),
    
    path("edit/<int:id>", views.edit, name="edit"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.destroy, name="delete"),
    path("adddish", views.adddish, name="adddish"),
    path("showproduct", views.showproduct, name="showproduct"),
    path("editproduct/<int:id>", views.editproduct, name="editproduct"),
    path("updateproduct/<int:id>", views.updateproduct, name="updateproduct"),
    path("destroyproduct/<int:id>", views.destroyproduct, name="delete"),
    path("success", views.success, name="success"),    
    
    
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path('adminloginf', views.adminloginf, name="adminloginf"),
    path('adminafterlogin', views.adminafterlogin, name="adminafterlogin"),
    path('product', views.product, name="product"),
    
    path('userloginf', views.userloginf, name="userloginf"),


    path('product/', views.product, name='product'),
    
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
