# from django.shortcuts import render
# from django.core.paginator import Paginator, InvalidPage, EmptyPage
# from django.core.urlresolvers import reverse
#
# # Create your views here.
#
# from incidents.models import *
#
#
# def main(request):
#     """Main listing."""
#     incidents = Incident.objects.all().order_by("-created")
#     paginator = Paginator(incidents, 4)
#
#     try:
#         page = int(request.GET.get("page", '1'))
#     except ValueError:
#         page = 1
#
#     try:
#         incidents = paginator.page(page)
#     except (InvalidPage, EmptyPage):
#         incidents = paginator.page(paginator.num_pages)
#
#     return render_to_response("list_incidents.html", dict(incidents=incidents, user=request.user))
#
# # Create your views here.

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from models import Post
from forms import PostForm, CommentForm

@user_passes_test(lambda u: u.is_superuser)
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    return render_to_response('blog/add_post.html',
                              { 'form': form },
                              context_instance=RequestContext(request))

def view_incident(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render_to_response('blog/blog_post.html',
                              {
                                  'post': post,
                                  'form': form,
                              },
                              context_instance=RequestContext(request))