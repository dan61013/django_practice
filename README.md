# Django 2022 ithelp_note_by_Dan
參考文章: [傳承D的意志~ 邁向Django的偉大航道](https://ithelp.ithome.com.tw/users/20151096/ironman/5130)

---

## Ch.1 MTV == MVC
使用架構的優點是: 可以清楚分工(前、後端工程)
### 1. MTV
    Model: 資料模型，負責資料處理的工作(包含資料庫欄位設計)
    View: 訪客or使用者直觀所看到的畫面
    Controller: 主要負責整體應用程式的運行
### 2. MVC
    Model == Model
    Template == View
    View == Controller
    
    Models: Describes your data
    Views: Controls what users sees
    Templates: How user sees it
    Controller: URL dispatcher(收發)
---
## Ch.2 建立初始環境
### 1. install程式
    安裝anaconda, python and django
    ** cmd: pip install django
### 2. 建立專案
    cmd輸入指令: django-admin startproject myproject_name
### 3. 啟動專案
    py manage.py runserver
---
## Ch3. Model
### 1. App
    a. 創立app
        cmd: py manage.py startmyapp app_name
    b. 進入model
        進入已經建立完成的app model
    c. 建立人物
        在model裡建立class人物
    d. 設定各個屬性
        [DateTimeField參考](https://docs.djangoproject.com/zh-hans/4.1/ref/models/fields/#datetimefield)

        datetime.datetime，與DataField有一樣的額外參數
        class DateTimeField(auto_now=False, auto_now_add=False, **options)

        ** example:
        class Bboy(models.Model):
            name: char
            age: int
            power: bool
            skills: text
            created_time: datetime
### 2. Migration
資料遷移: 在django的model中，利用ORM的技術，將table換成class，而欄位化為其中的屬性，讓我們可以用ORM方式，來透過物件來操作、選取、變更資料
** class, attribute(屬性)

    a. app 註冊在settings.py
        找到INSTALLED_APPS = []，並將app名稱登記在下方
    b. Migration
        cmd: py manage.py makemigrations
        會在app底下產生migration資料夾，以及0001_initial.py
    c. Migrate
        cmd: py manage.py migrate
        該指令會將遷移剛才migration的app
---
## Ch4. 關聯資料庫(Relational Database)
簡而言之，就是建立在關聯模型上的資料庫，可以使多個model之間有關聯屬性，主要有三種:
    ● 一對多
    ● 多對一
    ● 多對多
### 關聯對應關係
    Step1. 分析表
        a. 左表的多條紀錄是否可對應右表的一條紀錄
        b. 右表的多條紀錄是否可對應左表的一條紀錄

#### 多對一 (ForeignKey)
    a. 若只有分析一成立，左表多對一右表，外來鍵foreign key創建在左表，關聯指向右表
    (左多右一，key建左，關聯指右)
    b. 若只有分析二成立，右表多對一左表，外來鍵foreign key創建在右表，關聯指向左表
    (右多左一，key建右，關聯指左)
#### 一對一 (OneToOneField)
    若分析一及分析二皆不成立，則左表的一條紀錄唯一對應右表的一條紀錄。
    此時，我們可以在左表設置OneToOneField，指向右表即可。
    在Django中，最常用於原生User & 客製化的UserProfile model中。
#### 多對多 (ManyToManyField)
若分析一及分析二同時成立，兩表為雙向多對一，即多對多。
需創建一張新表，專門存放左右二表的關係，關聯字段寫在新表中

---
## Ch5. 資料庫正規化
資料庫正規化，是代表一個過程中，將資料庫描述實體資料的各表，依照程序，一個一個將其簡化，最後的理想是將每個表的核心，都簡化為僅單純描述一個特徵或事實。

### 使用資料正規化的目的:
    a. 增進資料儲存以及操作資料庫的效能
    b. 盡量減少資料發生異常的可能
    c. 後續維護資料庫能夠變得更加容易

### 正規化之後的資料庫:
    a. 欄位原子性：每個欄位只儲存一筆資料
    b. 主鍵辨識：每筆資料都有一個主鍵，並以主鍵來做區分
    c. 關聯明確：表與表之間的關聯關係明確
    d. 欄位獨立：表與表的欄位之間沒有遞移相依的問題
    example:
        1. 去除重複性，讓每個儲存格資料都單一化
        2. 每個欄位的資訊，如果有其他關連(性質)，應該再拆分成N表，來做關聯
        3. 遞移: 當某個表改變時，相關聯的表格也會隨之改變
    ※ 簡單的表不一定要用正規化來處理

---
## Ch6. View
基本要素: request & return

    1. 最基本功能: 接收請求，並且Return
    2. 功能可能是渲染畫面(render), 或HttpResponse, 以及自訂的Response

### django的運作邏輯是:
    由url的路徑來使用寫入的view，再由view的功能去渲染(render)我們的畫面

    a. 先在app中的views新增一個function
    b. 然後在到project底下的urls.py新增path
    path('', function, name='function_name')

### T, Template
在django裡，就是html檔，主要用來顯示使用者畫面

    a. in app, views
    def function(request):
        context = {
            'name':'abc'
        }
        return render(request, 'hello.html', context)
    b. in settings
        新增path('hello/', function, name='function'
    c. 在manage.py同層，新增templates>hello.html

### Form表單
在django中，主要有兩種使用表單的方式，form, ModelForm，ModelForm可以按照我們在model裡定義的欄位類型及參數，建立及驗證內容

※注意: 避免與django的models, forms衝突，在import其他module時，要使用"."，來區分

    a. 在app底下，新增一個forms.py
    b. from django import forms, and from .models import module_name
    c. 建立一個class
        class BboyForm(forms.ModelForm):
            class Meta:
                model = Bboy
                fields = '__all__'
    ※ 如果要import指定項目:
        fiedls = ('name', 'age', 'remark', ...)
    d. 編輯views

#### {% csrf_token %}
Cross-Site Request Forgery(跨站請求攻擊)

---
## Ch7. Admin
在adimn裡面，我們可以看到
    1. default User, Group table
    2. 自己新增的model
    3. 套件所產生的model, example: token, social account等等

### 建立管理者帳號
    a. cmd: py manage.py createsuperuser
    b. 輸入使用者, 信箱, 密碼
    c. 到app內的admin.py，註冊model
        from .models import your_app_module
        admin.site.register(your_app_module)
    d. 進入/admin頁面，就可以看到管理後台
---
## Ch8. Django Rest Framework, DRF
[官方說明](https://www.django-rest-framework.org/)

cmd安裝:pip install djangorestframework

優點:
1. 可視化的API
2. 序列化(Serialization)資料
3. 易客製化的Views
4. 強大的社群及套件支援

### 使用方法:
    a. 安裝 djangorestframework
    b. in settings.py, INSTALLED_APPS，最下方加入'rest_framework',
    c. 在app底下新增 'serializers.py'
        from rest_framework import serializers
        from .models import your_module
        class BboySerializer(serializers.ModelSerializer):
            model = your_module
            fields = '__all__'
    d. 接著到views.py新增
        from .models import your_module
        from .serializers import BboySerializer
        from rest_framework import generics

        class BboyListAPIView(generics.ListAPIViwe):
            queryset = Bboy.objects.all()
            serializer_class = BboySerializer
    e. 到urls.py新增
        from bboy.views import BboyListAPIView
            ...
            path('api/', BboyListAPIViwe, name='api')
### RESTful API
#### API: Application Programming Interface, 應用程式介面
應用程式溝通之間的橋樑

[參考網址](https://youtu.be/zvKadd9Cflc)

餐廳舉例:

    進到餐廳的流程:

        1. 看菜單，準備點餐
        2. 請服務生來
        3. 服務生記住餐點
        4. 交給廚房
        5. 廚房製作料理，並送到我們的桌上

    ※ 菜單=前端頁面, 服務生=API, 廚房=後端, 上菜的桌面=渲染過的前端頁面

#### RESTful
REST, Representational State Transfer(表現層狀態轉移)

更精準地說，是一種設計風格 - RESTful

特徵: 

    a. 統一介面 Uniform Interface
    b. 無狀態 Stateless
    c. 與客戶端分離 Client-Server

1. 統一介面: 表示統一的api接口，通常為同一個資料來源定義URL
2. 無狀態表示: 在沒有請求的情況為無狀態，在客戶端向server端發出請求時，一併將狀態method傳至server端
   
優點: 獨立、靈活，可以藉由客戶端請求不同狀態method, 來變更API的使用功能。且RESTful API不用儲存狀態，消除了伺服器的負載，可擴展性大幅提升。

### 回歸DRF
好用的APIview:

    ※ CRDU (建立、讀取、刪除、更新)
    1. generics.ListAPIView (偏向model based views)
    2. Retrieve(): get single instance
    3. Create: post instance(例子)
    4. Destroy: delete instance
    5. Update: put instance

還可以複合使用，example: ListCreate, RetrieveUpdate, Mixin

### Function Based View
** serializers.ModelSerializer

1. 到view.py底下，新增func
   
   主要是使用api_view()裝飾器，以及GET
2. 再加入到urls.py，注意function不需要使用.as_view()

#### 使用field方式
    1. 使用class func_name(serializers.Serializer)，以及serializers.IntegerField, CharField, BooleanField等功能驗證
    ** 有read_only, max_length... 可用
    2. 此功能與ModelSerializer不同，不會有class Meta

---
# Ch9. 使用者註冊

[Django原生auth.user](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User)

原生user基本欄位:
    1. username
    2. last_name
    3. first_name
    4. email
    5. password

教程:

    1. 在models.py新增user model
    2. 建立擴充User的UserProfile，並做1對1關聯

    from django.db import models
    from django.contrib.auth.models import User

    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        phone = models.CharField(max_length=10, blank=True, null=True)
        organization = models.CharField(max_length=100, blank=True, null=True)

        def __str__(self):
            return self.user.username
        
        3. Register API
        先建立serializer, 然後再建立view，最後到urls新增連結
        ※參考bboy>serializers.py & views.py

---

## 登入 & 登出
### 登入
    登入所需的資訊: username, password

    1. 先從serializer開始編輯
    2. 必須 from django.contrib.auth import authenticate
