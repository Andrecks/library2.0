from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BookForm, NewUserForm
from .models import Book
from django.conf import settings

User = get_user_model()

@login_required(login_url='signup')
def home(request):
    book_list = Book.objects.all()
    # paginator = Paginator(book_list, settings.BOOKS_PER_PAGE)
    # page_number = request.GET.get('page')
    # page = paginator.get_page(page_number)
    return render(request, 'index.html', {'books': book_list})

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = NewUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


def validate_username(request):
    """Проверка доступности логина"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


def book_form(request):
    form = BookForm()
    if request.method == "POST" and request.is_ajax():
        form = BookForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['title']
            form.save()
            
            return redirect('home')
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "addbook.html", {"form": form})

@login_required(login_url='signup')
def book_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})