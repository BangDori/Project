import datetime
from io import StringIO

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# AbstractUser를 상속받는 모델로 변경
class CustomerUser(AbstractUser):
    """
    CustomerUser : 사용자 정보를 저장하는 Model

    Parameters
    ----------
    email : CharField
        이메일 저장
    birthday : CharField
        수정할 것
    phone : CharField
        전화번호 영역
    """

    ''' # 부모 클래스에서 제공하는 부분은 비활성화
    # userid = models.CharField(
    #     max_length=50, db_column='userid', verbose_name='userid', primary_key=True)
    # passwd = models.CharField(
    #     max_length=50, db_column='passwd', verbose_name='passwd') '''
    email = models.CharField(
        max_length=30, db_column='email', verbose_name='email', blank=True)
    birthday = models.DateField(
        default=datetime.MINYEAR, db_column='birth', verbose_name='birth')
    phone = models.CharField(
        max_length=30, db_column='phone', verbose_name='phone')

    def __str__(self):
        return self.username


class Authentication(models.Model):
    phone_number = models.CharField('휴대폰 번호', max_length=30)
    auth_number = models.CharField('인증번호', max_length=30)

    class Meta:
        db_table = 'authentications'  # DB 테이블명
        verbose_name_plural = "휴대폰인증 관리 페이지"  # Admin 페이지에서 나타나는 설명


class Article(models.Model):
    """
    Article : 게시물 정보를 저장하는 Model

    Parameters
    ----------
    id : AutoField
        Integer 형식의 SeqID를 나타내는 PK
    title : CharField
        게시글 제목
    writer : ForeignKey
        작성자, CustomerUser의 username를 FK로 함
        1:N 특성을 가지므로, 계정 삭제시 같이 삭제될 수 있는 CASCADE 특성 사용
    date :
        글 작성 일자, auto_now_add 파라미터를 True로 하여 INSERT시 자동으로 날짜가 생성되는 옵션 사용
    views : PositiveIntegerField
        조회수, 음수가 없으므로 unsigned int 사용
    upvote : PositiveIntegerField
        추천수, 조회수와 마찬가지의 형식 사용
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='제목')
    writer = models.ForeignKey(
        'CustomerUser', on_delete=models.CASCADE, verbose_name='글쓴이')
    date = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    views = models.PositiveIntegerField(default=0, verbose_name='조회')
    upvote = models.PositiveIntegerField(default=0, verbose_name='추천')

    def __str__(self):
        # __str__ 오버라이드로 제목만 표시
        return self.title

    class Meta:
        # Meta 클래스 오버라이드로 상세 내용 지정 (Form을 위함)
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
