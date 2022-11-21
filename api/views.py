from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bangdori.models import Article
from bangdori.utils import getModelByName


class ArticleInfo(APIView):
    """
    게시물의 '미리보기' 기능 구현을 위한 API
    """

    # View에서 입력을 위한 객체 설정
    model = Article

    def get(self, request, name, pk):
        """
        GET /api/article
        """
        board = getModelByName(name)
        if board is None:
            return Response({'error': '잘못된 이름입니다.'}, status=status.HTTP_404_NOT_FOUND)

        article = board.objects.all().filter(id=pk).last()
        if article is None:
            return Response({'error': '일치하는 데이터가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        url = article._meta.db_table
        url = url[url.rfind('_') + 1:]

        addr = article.addr
        print(addr)

        data = {'id': article.id, 'title': article.title, 'writer': article.writer.username,
                'content': article.content, 'date': article.date, 'views': article.views,
                'upvote': article.upvote, 'url': url}

        return Response(data, status=status.HTTP_200_OK)
