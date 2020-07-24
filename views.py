from django.shortcuts import render, redirect, get_object_or_404
#HTML 화면에 data가 나오도록 한다

from .models import Blog #model에 있는 Blog 클래스를 import

# Create your views here.
def index(req): #app 기능 구현 -> HTML 화면에 띄우기
    return render(req, 'index.html')

    
#CRUD 시작! 다른 함수들도 만들자

def blog(req):

    blogs = Blog.objects #blogs라는 객체는 저장하고, {}를 html에 넘겨주겠다
    #index.html에 나타날 객체 object blogs 변수를 지정

    return render(req, 'blog.html', {'blogs' : blogs}) #키 값을 블로그로 들여옴
    #'blogs라는 변수 지정' : 객체에 사용한다
    #req요청이 들어오면 return 반환한다 -> index.html을 render(주다)


def new(req):
    return render(req, 'new.html')


def create(req):

    #form을 통해 받은 data를 POST 객체에 넣어준다
    #POST에 저장한 data를 save() method로 DB에 저장
    #다시 'blog'으로 redirect -> redirect 함수는 위에 import해준다

    if req.method == "POST":
        blog=Blog() 
        blog.title=req.POST['title']
        blog.body=req.POST['body']
        blog.save() #DB에 저장하도록
    return redirect('/blog/')

    #redirect 함수는 괄호 안에 string 타입으로 입력해야함
    #blog_id는 int 타입이므로 string 타입으로 형변환해주자

    #새 글쓰기는 완료 ㅇㅇ
    #blog.id는 해당 객체의 번호


#각 게시물마다 각자의 id값을 가진다 -> pk (primary key) = blog_id
#url에서 pk에 해당 게시물의 id값이 들어가게 된다 -> <int:blog_id>
#이렇게 url이 전달해주는 id값을 view의 detail 함수가 받아서
#어떤 게시물의 data를 가져올지 id값을 통해 알 수 있다! 

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    #get_object_or_404()
    #id값(pk)에 해당하는 object를 가져오고, 없으면 404 에러를 띄우는 함수
    #괄호 내부: 원하는 data형식의 model이름과 게시글의 id값

    return render(request, 'detail.html', {'blog' : blog})

    #위에 get~ 이거 import해주기

#수정하기 버튼
def edit(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'edit.html', {'blog' : blog})


#수정 반영

#새 글 만들 때와 다르게 기존 data를 가져와야함
def update(req, blog_id):
    if req.method == "POST":
        edit = get_object_or_404(Blog, pk=blog_id)
        edit.title = req.POST['title']
        edit.body = req.POST['body']
        edit.save()
    return redirect('/detail/'+str(blog_id))

#삭제
def delete(req, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/blog/')