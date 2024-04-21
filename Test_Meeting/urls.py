from django.urls import path
from Test_Meeting import views
urlpatterns = [

    path('<int:id>',views.detail,name='details'),
    path('room/',views.room_list,name="rooms"),
    path('new/',views.new,name='new'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]