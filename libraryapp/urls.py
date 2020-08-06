from django.urls import include, path
from .views import *
from django.urls import path

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/form', book_form, name='book_form'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
    path('librarians/', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian_details'),
    path('libraries/', library_list, name='libraries'),
    path('libraries/<int:library_id>/', library_details, name='library_details'),
    path('libraries/form', library_form, name='library_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]