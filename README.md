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
      
json형태의 파일을 가져와 배열에 담아 png 파일로 만든다.  