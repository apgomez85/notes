from django.urls import path
from .views import (
    entry_list,
    entry_detail,
    entry_create,
    entry_update,
)


app_name = 'notes'
urlpatterns = [
    path('', entry_list, name='entry-list'),
    path('create/', entry_create, name="entry-create"),
    path('<int:id>/', entry_detail, name="entry-detail"),
    path('<int:id>/update/', entry_update, name="entry-update"),

]
