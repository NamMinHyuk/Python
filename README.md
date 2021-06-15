## Python-Study 1일차  
        
        
***   
      
파이썬 가상환경에 패키지 관리한다      
python -m venv basic        : basic 파일 만듦            
.\basic\Scripts\activate.bat : basic 들어가는법      
deactivate                  : basic 나오는법      
      
eclipse에 PyDev로 사용중이다       
      
REPL : Read Eval Print Loop      
Interactive shell (대화형 프로그래밍 환경)      
      
파이썬의 모든 것들은 다 객체 <class 'int'>    
          
## Python-Study 2일차  

        
***   
       
if __name__ == '__main__':   -> main 함수       
underbar 두개는 프로그래밍에서 보통 내부에서 쓰는걸 뜻함       
       
tuple -> ( ) , list -> [ ] , dictionary(key,value타입) -> { }       
       
file       
r : 읽기              
w : 쓰기 (기존 내용 덮어쓰기)       
a : 쓰기 (기존 내용 이어서 쓰기)       
x : 새로운 파일 만들어서 쓰기              
t / b : text / binary (default : t)       

          
## Python-Study 3일차  

        
***   
       
firefox : dom 탐색하기 편하다       
      
zip : list 두개를 하나의 dict로 만든다. ex) sido_dict = dict(zip(sido_code, sido name))      
ensure_ascii=False 한글      

          
## Python-Study 4일차  

        
***   
       
@app.route('/', methods=['GET', 'POST'])  -> get,post로 root로 왔을 때      
def 함수명():      
CORS 에러 - 알아둬야함!!    
    
          
## Python-Study 5일차      
    
        
***   
    
mongo db + python    
pymongo install     
from pymongo import MongoClient     
client = MongoClient('localhost' , 27017)    
db = client.test    
collection = db.score    
      
## WordCloud      
           
      
***      
      
anaconda 가상환경 
conda create -n 가상환경명 python openssl - 가상환경 생성
conda activate 가상환경명 - 가상환경 들어가기 
conda deactivate 가상환경명 - 가상환경 나오기

json형태의 파일을 가져와 배열에 담아 png 파일로 만들 수 있다.    
      
## Django      
           
      
***      
      
pip install django - django 설치      
* window powershell -> Set-ExecutionPolicy Unrestricted    -> A       
django-admin startproject mysite - 프로젝트 만들기       
cd mysite      
python manage.py runserver localhost:8888 - 서버 가동 (포트번호 포함가능)      
python manage.py startapp hello02 - hello02라는 app 생성      
      
manage.py -> project 관리       
asgi.py -> 비동기통신 지원하는 python interface      
settings.py -> application 환경 설정      
urls.py -> URLconf      
wsgi.py -> 비동기 통신 지원이 어려워서 asgi로 대체      
      
MVT      
Model - DataBase 연동  ORM(Object Realtion Mapping) - 객체랑 관계형 디비를 매핑해준다      
View - Data 구성 (business logic)      
Template - Data 표현 (presentation layer)      
* controller 는 django framework 자체이다      
      
Django에 대해 더 배우고 싶으면 vue.js node.js react.js 프론트랑 연결 해보고 Flask 사용해보기!      
     
{{}} -   <%= %>     
{% %} -   <% %>     
{% for i in numbers %}     
{% endfor %}     
endif도 써야함     
     
sqlite  - manage.py에 sqldiff,sqlite3,sqlite3_analyzer 넣고      
python manage.py migrate     
sqlite3 db.sqlite3     
.quit     
python manage.py makemigrations dbtest     
python manage.py sqlmigrate dbtest 0001     
python manage.py migrate     
sqlite3 db.sqlite3     
.table      
.schema dbtest_myboard     
.quit     