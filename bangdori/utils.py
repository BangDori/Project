import hashlib
import hmac
import base64
import os

from django.db.models import QuerySet
from dotenv import load_dotenv

from bangdori.models import *


def make_signature(timestamp):
    load_dotenv()

    access_key = os.getenv('ncloud_private_Accesskey')
    secret_key = os.getenv('ncloud_private_Secretkey')

    secret_key = bytes(secret_key, 'UTF-8')

    uri = "/sms/v2/services/ncp:sms:kr:292652557635:sms_auth/messages"
    # uri 중간에 Console - Project - 해당 Project 서비스 ID 입력 (예시 = ncp:sms:kr:263092132141:sms)

    message = "POST" + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(
        hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    return signingKey


def getModelByName(name, is_all=False):
    """
    getModelByName : name에 따라 적절한 Model 객체를 반환하는 클래스

    Parameters
    ----------
    name : url에 사용된 이름
    is_all : 모든 객체를 가져올지 결정
    """

    articles = None

    # URL로부터 넘겨받은 게시판 유형에 따라 다른 context 전달
    if name == 'board':
        articles = BoardArticle
    elif name == 'dabang':
        articles = DabangArticle
    elif name == 'succession':
        articles = SuccessionArticle
    elif name == 'essentials':
        articles = EssentialsArticle
    elif name == 'notice':
        articles = NoticeArticle
    elif name == 'contact':
        articles = ContactArticle
    elif name == 'group':
        articles = GroupArticle
    elif is_all:
        articles = [BoardArticle, DabangArticle, SuccessionArticle,
                    EssentialsArticle, NoticeArticle, ContactArticle, GroupArticle]

    return articles


def getArticlesByAddress(user: CustomerUser, articles: QuerySet):
    try:
        # addr : 게시글을 Key로, 사용자와의 거리를 Value로 가지는 dict
        addr = {article: user.addr.calcDistance(article.addr) for article in articles}
    except:
        return articles

    # 거리가 가까운 순으로 정렬
    addr = {k: v for k, v in sorted(addr.items(), key=lambda x: x[1])}

    # list로 변환하여 반환
    return list(addr.keys())


def getAllArticles():
    # 모든 게시판 객체 가져옴
    boards = getModelByName(None, True)

    result = list()
    for board in boards:
        articles = board.objects.all().filter()
        # 게시글이 없는 게시판은 제외
        if articles.count() > 0:
            for article in articles:
                # dict로 변환하여 저장
                result.append(article.to_dict())

    return result
