from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index),
    path("users/", views.users_view),
    path("forum/", views.forum_view),
    path("forum/delete/<int:id>/", views.forum_delete),
    path("contact/", views.contact_view),
    path("arxiv/", views.arxiv_view),
    path("<str:name>/", views.user_page),
]
