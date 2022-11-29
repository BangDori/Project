from django.shortcuts import redirect, render

from bangdori.utils import getModelByName


def update(request, name, pk):
    """
    update : 게시글 update하는 view
    """
    user = request.user
    Article = getModelByName(name)
    article = Article.objects.all().get(id=pk)
    if article.writer != user:
        return redirect('article', name=name, pk=pk)
    if request.method == "POST":
        # 게시글 수정
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        # 사진 업로드
        try:
            _, img = request.FILES.popitem()
            img = img[0]
            article.img = img
        except:
            pass

        if request.POST.get('write-uploaded-delete', False):
            article.img = None

        article.save()
        return redirect('article', name=name, pk=pk)

    context = {}
    context['title'] = article.title
    context['content'] = article.content
    context['isEdit'] = True
    try:
        context['img'] = article.img.url
    except:
        pass

    return render(request, 'write.html', context)
