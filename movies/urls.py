from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='movies_index'),
#     path('<int:movie_id>', views.detail, name='movies_detail')
# ]

# A better way to do this is using the app_name variable
app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]