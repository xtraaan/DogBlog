from django.urls import path
from entries.views import Home, CreateEntryView

urlpatterns = [
    path('', Home, name = 'blog-home'),
    path('create_entry', CreateEntryView.as_view(success_url='/'), name = 'create_entry')
]