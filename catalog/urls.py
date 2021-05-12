#part2
from django.urls import path
from . import views

urlpatterns = [
	#part5
	path('', views.index, name='index'),
	#part6
	path('books/', views.BookListView.as_view(), name='books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	#challenge part6
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
]
#part8
urlpatterns += [
	path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
	#challenge part8
	path('allborrows/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]
#part9
urlpatterns += [
	path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
	path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
	path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
	path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
	#challenge part9
	path('book/create/', views.BookCreate.as_view(), name='book-create'),
	path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
	path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]
