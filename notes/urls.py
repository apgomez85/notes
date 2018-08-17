from django.urls import path
from .views import (
    entry_list,
    entry_detail,
    entry_create,
)


app_name = 'notes'
urlpatterns = [
    path('', entry_list),
    path('create/', entry_create, name="entry-create"),
    path('<int:id>/', entry_detail, name="entry-detail"),

]
