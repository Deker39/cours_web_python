from django.shortcuts import render, HttpResponse

# from newprog.models import Author, Book


def index(request):

    # author = Author.objects.create(name='John Doe', email='alex@gmail.com')
    # book1 = Book.objects.create(title='Book', author=author)
    # book2 = Book.objects.create(title='Book', author=author)
    # author.books.add(book1,book2)
    # author.save()
    # book.save()

    # author = Author.objects.get(id=3)
    # books = author.books.all()
    # print(books)
    #
    # author.name = 'Deker'
    # author.save()
    #
    # book.title = 'My book'
    # book.save()
    return HttpResponse(f'<h1>book</h1>')
