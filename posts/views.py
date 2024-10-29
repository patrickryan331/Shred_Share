from django.views.generic import TemplateView, ListView, DetailView
from .models import Mountain, Post, Comment
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms  import PostCreateForm, ContactForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Mountain
from django.core.mail import send_mail



class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = (
            Post.objects.order_by("date").reverse()
        )
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.object
        comments =  Comment.objects.filter(post=post)

        context["comments"] = comments

        return context



class CreatePostView(CreateView):
    template_name  = 'posts/create.html'
    form_class =  PostCreateForm

    def  get_success_url(self):
        return reverse('posts')
    

    


def save_post_for_page(request):
    print(request.POST)
    mountain_id = request.POST.get('mountain_id')
    name = request.POST.get('mountain_name')
    title = request.POST.get('title')
    body = request.POST.get('body')
    slug = request.POST.get('slug')

    # retrive mountain
    mountain = Mountain.objects.get(id=mountain_id)

    # create your record
    post = Post.objects.create(
        title=title,
        body=body,
        slug=slug,
        mountain=mountain,
        author=request.user
    )

    post.save()

    return redirect(name)


def create_comment(request):
    #get the form data
    post_id = request.POST.get('post_id')
    comment_text = request.POST.get('text')
    user = request.user

    post_obj = Post.objects.get(id=post_id)

    #create your record
    comment = Comment.objects.create(
        text=comment_text,
        post  = post_obj,
        author = user
    )

    comment.save()

    return redirect("details", pk=post_id)



def my_view(request):
    my_object = Mountain.objects.get(pk=1)
    context = {'my_object': my_object}
    return render(request, 'my_template.html', context)




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)


        # send email
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail("Email from" +  name, message, email, ['patrick.ryan0331@gmail.com'])

            return redirect("home")

        else:
            print("Invalid data")

    else:
        # create an empty form
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})