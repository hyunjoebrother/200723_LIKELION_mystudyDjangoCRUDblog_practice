from django.db import models

# Create your models here.
class Blog(models.Model): 
    #글쓰기 형태 ㅇㅇ model다 만들고 -> migrate -> 데이터 전송 요청

    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    body=models.TextField()

    #migrate까지 하고 /admin 사이트 들어가니까 로그인 필요 -> admin 계정 만들자
    
    #글 썼는데 제목이 object(1)임
    # -> 내가 입력한 title이 반환되도록 함수를 만들자
    ## Blog 클래스 내부에 함수를 쓰도록 주의!

    def __str__(self):
        return self.title