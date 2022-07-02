from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.flash,name='flash'),
    path('signin/',views.sign_in,name='signin'),
    path('signup/',views.sign_up,name='signup'),
    path('home/',views.home,name='home'),
    path('add/',views.addnote,name='add_note'),
    path('delete/',views.deletenote,name='delete'),
    path('edit/',views.edit_note,name='edit'),
    path('logout/',views.logout_user,name='logout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


