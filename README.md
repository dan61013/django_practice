# Learn Django 2022

參考文章: [傳承D的意志~ 邁向Django的偉大航道](https://ithelp.ithome.com.tw/users/20151096/ironman/5130)

- [Learn Django 2022](#learn-django-2022)
  - [Chapter 01 MTV \& MVC](#chapter-01-mtv--mvc)
  - [Chapter 02 建立初始環境](#chapter-02-建立初始環境)
    - [2-1 Project](#2-1-project)
  - [Chapter 03 Model](#chapter-03-model)
    - [3-1 App](#3-1-app)
    - [3-2 Migration](#3-2-migration)
  - [Chapter 04 關聯資料庫(Relational Database)](#chapter-04-關聯資料庫relational-database)
    - [4-1 關聯對應關係](#4-1-關聯對應關係)
      - [4-1-1 多對一 (ForeignKey)](#4-1-1-多對一-foreignkey)
      - [4-1-2 一對一 (OneToOneField)](#4-1-2-一對一-onetoonefield)
      - [4-1-2 多對多 (ManyToManyField)](#4-1-2-多對多-manytomanyfield)
  - [Chapter 05 資料庫正規化](#chapter-05-資料庫正規化)
    - [5-1 使用資料正規化的目的](#5-1-使用資料正規化的目的)
    - [5-2 正規化之後的資料庫](#5-2-正規化之後的資料庫)
  - [Chapter 06 View](#chapter-06-view)
    - [6-1 django的運作邏輯](#6-1-django的運作邏輯)
    - [6-2 Template](#6-2-template)
    - [6-3 Form表單](#6-3-form表單)
  - [Chapter 07 Admin](#chapter-07-admin)
    - [7-1 Create Super User](#7-1-create-super-user)
  - [Chapter 08 Django Rest Framework](#chapter-08-django-rest-framework)
    - [8-1 基本操作方法](#8-1-基本操作方法)
    - [8-2 RESTful API](#8-2-restful-api)
      - [8-2-1 RESTful](#8-2-1-restful)
    - [8-3 DRF常見用法](#8-3-drf常見用法)
    - [8-4 Function Based View](#8-4-function-based-view)
  - [Chapter 09 使用者註冊](#chapter-09-使用者註冊)
  - [Chapter 10 Login \& Logout](#chapter-10-login--logout)
  - [Chapter 11 CRUD](#chapter-11-crud)
    - [11-1 Create](#11-1-create)
    - [11-2 Read](#11-2-read)
    - [11-3 Update](#11-3-update)
      - [11-3-1 Put](#11-3-1-put)

---

## Chapter 01 MTV & MVC

Django是一個有完整架構的系統，使用架構的優點主要為**可以清楚分工**(前後端)

MVC:

- Model: 資料模型，負責資料處理的工作(包含資料庫欄位設計)
- View: 訪客or使用者直觀所看到的畫面
- Controller: 主要負責整體應用程式的運行

MTV:

- Model == Model
- Template == View
- View == Controller

各功能主要目的:

- Models: Describes your data
- Views: Controls what users sees
- Templates: How user sees it
- Controller: URL dispatcher(收發)

---

## Chapter 02 建立初始環境

Set Environment:

- Anaconda
- VSCode
- Django
  - `pip install django`

### 2-1 Project

啟動專案:

1. 建立專案: `django-admin startproject project_name`
2. 執行`py manage.py runserver`

---

## Chapter 03 Model

### 3-1 App

針對各個功能，在Django中會使用建立App的方式。

1. 建立app -> `py manage.py startapp appName`
2. Edit Model -> 進入App中的`models.py`
3. 建立人物: 在models中建立class類型
4. 設定各個屬性: [DateTimeField參考資料](https://docs.djangoproject.com/zh-hans/4.1/ref/models/fields/#datetimefield)，`datetime.datetime`，與`DataField`有一樣的額外參數。

Example:

```python
# class DateTimeField(auto_now=False, auto_now_add=False, **options)

class Bboy(models.Model):
    name: char
    age: int
    power: bool
    skills: text
    created_time: datetime
```

### 3-2 Migration

資料遷移: 在Django的model中，利用ORM的技術，將table換成class，而欄位化為其中的屬性，讓我們可以用ORM方式，來透過物件來操作、選取、變更資料

※ ORM: Object Relation Mapping (物件關聯對映)

流程:

1. 把app註冊在`settings.py`，找到`INSTALLED_APPS = [...,'app_name',]`，並輸入新增的App名稱
2. Migration -> `py manage.py makemigrations`，輸入後會在app底下產生migration的資料夾，以及`0001_initial.py`(按照流水號產生)
3. Migrate -> `py manage.py migrate`，該指令會將遷移剛才的migration資料

---

## Chapter 04 關聯資料庫(Relational Database)

| 就是建立在關聯模型上的資料庫，可以讓多個model之間有關聯屬性。

主要有三種性質:

- 一對多
- 多對一
- 多對多

### 4-1 關聯對應關係

分析表資料:

1. 左表的多條紀錄是否可對應右表的一筆記錄
2. 右表的多條紀錄是否可對應左表的一筆紀錄

#### 4-1-1 多對一 (ForeignKey)

1. 若只有分析一成立，左表多對一右表，外來鍵foreign key創建在左表，關聯指向右表(左多右一，key建左，關聯指右)
2. 若只有分析二成立，右表多對一左表，外來鍵foreign key創建在右表，關聯指向左表(右多左一，key建右，關聯指左)

#### 4-1-2 一對一 (OneToOneField)

若分析一及二皆不成立，則左表的一條紀錄唯一對應右表的一條紀錄。
我們可以在左表設置`OneToOneField`，指向右表即可。

> 在Django中，最常用於原生User & 客製化的UserProfile model中。

#### 4-1-2 多對多 (ManyToManyField)

若分析一及分析二同時成立，則兩表為雙向多對一，即多對多。

※ 需創建一張新表，專門存放左右二表的關係，關聯字段寫在新表中

---

## Chapter 05 資料庫正規化

> 資料庫正規化，是代表一個過程中，將資料庫描述實體資料的各表，按照程序，將每一個簡化，最終的理想是將每個表的核心，都化為只單純描述一個特徵或事實。

### 5-1 使用資料正規化的目的

- 增進資料儲存以及操作資料庫的效能
- 盡量減少資料發生**異常**的可能
- 後續**維護**資料庫能更**容易**

### 5-2 正規化之後的資料庫

- 欄位原子性: 每個欄位只儲存一筆資料
- 主鍵辨識: 每筆資料都有一個主鍵，並以主鍵來做區分
- 關聯明確: 表與表之間的關聯關係明確
- 欄位獨立: 表與表的欄位之間沒有遞移相依的問題

Example:

1. 去除重複性，讓每個儲存格資料都單一化，如不要讓日期與品名同時出現在同一儲存格中。
2. 每個欄位的資訊，如果有其他關連(性質)，應該再拆分成N表，來做關聯
3. 遞移: 當某個表改變時，相關聯的表格也會隨之改變

※ 簡單的表則不一定要用正規化來處理

---

## Chapter 06 View

基本要素包含`request` & `return`

 1. 最基本功能: 接收請求(request)，並且return
 2. 功能: 渲染畫面(render), 或`HttpResponse`, 以及自訂的response

### 6-1 django的運作邏輯

由url的路徑來使用寫入的**View**，再由**View**的功能去渲染(render)畫面。

1. 先在App中的Views新增一個`function` or `class`
2. 然後再到**Project**底下的`urls.py`新增path -> `path('url/', function(or class.as_view()), name='自定義')`

### 6-2 Template

在django中，Template就是html檔，主要用來顯示使用者畫面

1. 在App中的**Views**新增:

    ```python
    def function(request):
        context = {
            'name':'abc'
        }
        return render(request, 'hello.html', context)
    ```

2. 在`settings.py`中新增 -> `path('hello/', function, name='function')`
3. 在`manage.py`同層，新增`templates` -> `hello.html`

### 6-3 Form表單

在django中，主要有兩種使用表單的方式，分別為`form` & `ModelForm`，而`ModelForm`可以按照我們在model裡定義的欄位類型及參數，建立及驗證內容

※ 為避免與django的models -> forms衝突，在import其他module時，要使用`.`進行區分

步驟:

1. 在App中新增一個`forms.py`，並輸入:

    ```python
    from django import forms
    from .models import moduleName

    ```

2. 建立一個`class`

    ```python
    class BboyForm(forms.ModelForm):
        class Meta:  # Meta是必要屬性
            model = Bboy
            fields = '__all__'
    ```

    ※ 如果要import指定項目: `fiedls = ('name', 'age', 'remark', ...)`

3. Edit Views

---

## Chapter 07 Admin

在`/adimn`頁面中，我們可以看到

- default User and Group table
- 自己新增的model
- 套件所產生的model，example: token, social account等

### 7-1 Create Super User

1. 輸入`py manage.py createsuperuser`
2. 按照指示依序輸入使用者、信箱、密碼
3. 到app內的admin.py，註冊model

    ```python
    from .models import your_app_module
    admin.site.register(your_app_module)
    ```

4. 進入`/admin`頁面，就可以看到管理後台

---

## Chapter 08 Django Rest Framework

[DRF官方文件](https://www.django-rest-framework.org/)

優點:

1. 可視化的API
2. 序列化(Serialization)資料
3. 易客製化的Views
4. 豐富的社群及套件支援

### 8-1 基本操作方法

1. 安裝`djangorestframework`
2. 在`settings.py` -> `INSTALLED_APPS` List的最下方加入`rest_framework`
3. 在App底下新增`serializers.py`

    ```python
    from rest_framework import serializers
    from .models import yourModule

    class BboySerializer(serializers.ModelSerializer):
        model = yourModule
        fields = '__all__'
    ```

4. 接著到`views.py`新增

    ```python
    from .models import yourModule
    from .serializers import BboySerializer
    from rest_framework import generics

    class BboyListAPIView(generics.ListAPIView):
        queryset = Bboy.objects.all()
        serializer_class = BboySerializer
    ```

5. 到`urls.py`新增

    ```python
    from bboy.views import BboyListAPIView
        ...
        path('api/', BboyListAPIViwe, name='api')
    ```

### 8-2 RESTful API

> Application Programming Interface (API): 應用程式介面應用程式溝通之間的橋樑

[參考網址](https://youtu.be/zvKadd9Cflc)

以進到餐廳的流程進行解釋:

1. 客人(User)看菜單(Frontend)，準備點餐
2. 請服務生(API)來
3. 服務生(API)記住餐點
4. 交給廚房(Backend)
5. 廚房製作料理(Models)，並由服務生(API)送到我們的桌上

※ 菜單=前端頁面、服務生=API、廚房=後端、上菜的桌面=渲染(render)過的前端頁面

#### 8-2-1 RESTful

> Representational State Transfer (REST) :表現層狀態轉移，更精準地說，是一種設計風格 - **RESTful**

特徵:

- 統一介面 Uniform Interface: 表示統一的api接口，通常為同一個資料來源定義URL
- 無狀態 Stateless: 在沒有請求的情況為無狀態，在客戶端向server端發出請求時，一併將狀態method傳至server端
- 與客戶端分離 Client-Server

優點: 獨立、靈活，可以藉由客戶端請求不同狀態method, 來變更API的使用功能。且RESTful API不用儲存狀態，消除了伺服器的負載，可擴展性大幅提升。

### 8-3 DRF常見用法

好用的APIview:

1. `generics.ListAPIView` (偏向model based views)
2. `Retrieve()`: get single instance
3. Create: post instance(例子)
4. Destroy: delete instance
5. Update: put instance

※ CRDU (建立、讀取、刪除、更新)

※ 還可以複合使用，example: ListCreate, RetrieveUpdate, Mixin

### 8-4 Function Based View

`serializers.ModelSerializer`

1. 到`view.py`底下，新增function，主要是使用`api_view()`裝飾器，以及**GET**
2. 再加入到`urls.py`，注意function不需要使用`.as_view()`

使用**field**方式:

1. 使用`class func_name(serializers.Serializer)`，以及`serializers.IntegerField`、`CharField`、`BooleanField`等功能驗證，如包含有`read_only`、`max_length`等參數可用
2. 此功能與ModelSerializer不同，不會有`class Meta`

---

## Chapter 09 使用者註冊

[Django原生auth.user](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User)

原生user基本欄位:
- username
- last_name
- first_name
- email
- password

Tutorial:

1. 在`models.py`新增user_model
2. 建立擴充User的`UserProfile`，並做1對1關聯

    ```python
    from django.db import models
    from django.contrib.auth.models import User

    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        phone = models.CharField(max_length=10, blank=True, null=True)
        organization = models.CharField(max_length=100, blank=True, null=True)

        def __str__(self):
            return self.user.username
    ```

3. Register API: 先建立serializer, 然後再建立view，最後到urls新增連結

※參考[bboy/serializers.py]("./bboy/serializers.py") & [bboy/views.py](/bboy/views.py)

---

## Chapter 10 Login & Logout

Login:

登入所需的資訊為**username** & **password**

1. 先從serializer開始編輯
2. 必須導入驗證function -> `from django.contrib.auth import authenticate`

Logout:

只需要建立`ViewAPI`, 然後設定好urls即可

※ 先登入使用者 -> 輸入Logout網址 -> 再回到後台就會是登出的狀態

## Chapter 11 CRUD

API主要也分為CRUD這四類，Create、Read、Update、Delete

> 對於後端來說，最重要的要點之一，就是提供資料的api給前端用實作CRUD的API製作

### 11-1 Create

使用: `Generics.CreateAPIView`

1. 建立好model，以及serializer
2. 再到views，建立`Generics.CreateAPIView`
3. 共有2個參數: `queryset=model.objects.all()` & `serializers_class=model_serializer`

### 11-2 Read

Read + Filter，get特定的object，並搭配filter完成

[參考網址](https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#adding-a-filterset-with-filterset-class)

1. `pip install django-filter`
2. 在`INSTALLED_APPS`裡，新增`django_filters`
3. 在`settings.py`裡，新增:

    ```python
    REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS" = ['django_filters.rest_framework.DjangoFilterBackend'],
    }
    ```

4. 在App資料夾底下，新增`filters.py`, 並`import django_filters, FilterSet...`
5. 回到views, 在`generics.ListAPIView`，import剛才新增的`filter module`，並在底下新增 -> `filterset_class = the_filters_class_name`

### 11-3 Update

RESTful API可以利用無狀態特性，接收request中的method來改變功能

#### 11-3-1 Put

Update的功能，可以使用post或update的方式來實行，此次教程選擇使用put method實行，使用之前建立的model以及serializer，引用即可完成API

1. 新增以下功能 (Update & Delete同時存在)

    ```python
    from .models import your_module
    from .serializers import your_serializer
    from rest_framework import generics

    class NameUpdateAPIView(generics.RetrieveUpdateDestroy)
    queryset = Module.objects.all()
    serializer_class = Your_module_name_serializer
    ```

2. 新增`urls.py`即完成
