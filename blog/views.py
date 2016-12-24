from django.shortcuts import render

# View'lar buraya yazılacak.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
