from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.core.mail import send_mail
from django.contrib import messages
# from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,"blog/home.html",context)

class PostListView(ListView):
    model  = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
 
class PostDetailView(DetailView):
    model  = Post
    # template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model  = Post
    fields = ['title','content']
    
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model  = Post
    fields = ['title','content']
    
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model  = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request,'blog/about.html',{'title':'about'})



def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        try:
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=full_message,
                from_email=None,  # Uses DEFAULT_FROM_EMAIL
                recipient_list=['mustafaqasimali72@gmail.com'],  # <-- Change to your dev email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "Failed to send message. Please try again later.")
            print(e)

        return redirect('blog-about')

    return redirect('blog-about')
