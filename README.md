# jump-to-flask
점프 투 플라스크 학습
- https://wikidocs.net/book/4542

## 세팅

```
pip install flask
pip install black
pip install pylint
```


```
pip freeze > requirements.txt
```
- requirement.txt 설정

## 0장 들어가기 전에
> 어제의 점프 투 플라스크와 오늘의 점프 투 플라스크는 다르다!

파이썬으로 무엇을 할 수 있을까?
- 웹 프로그래밍 추천
- 웹 개념, 데이터베이스, 모델링, 네트워크, 서버 등의 지식 습득 필요.
- 나무가 아닌 숲을 보자.

실제 소스는 아래 공개 되어 있다.
- https://github.com/pahkey/flaskbook
- 각 챕터별로 브랜치가 구성되어 있음

## 1장 플라스크 개발 준비

### 플라스크 시작하기
플라스크는 파이썬 웹 프레임워크이다.
- 마이크로 웹 프레임워크 (프레임워크를 간결하게 유지하고 확장할 수 있다)
- 플라스크는 개발자가 필요 시 확장 모듈이라는 것을 사용한다. 프로젝트의 무게가 가볍다.
- 자유로운 프레임워크이다. 최소한의 규칙만 있다.

### 파이썬 설치하기
- 생략

### 플라스크 개발 환경 준비하기
- 파이썬 가상환경 설정
```sh
python -m venv myproject
```

- Scripts 폴더로 이동 후 아래 명령어로 활성화/비활성화 가능
```sh
activate
deactivate
```

- 플라스크 설치
```sh
pip install flask
```

- pip 최신 버전 설치
```sh
python -m pip install --upgrade pip
```

### 플라스크 프로젝트 생성하기
- 플라스크 프로젝트를 생성하면 웹 사이트를 한 개 생성하는 것과 같다.
- 배치 파일등을 이용하여 가상환경 및 환경변수 설정을 쉽게 할 수 있는데, 이런 부분들은 VSCode에서 지원해 주어 더 쉽게 할 수 있다. (launch.json, settings.json 설정)

### 파이참 설치하고 사용해 보기
- VsCode를 사용할 것으로 생략

### 안녕하세요, 파이보!
- Hello, Pybo!를 출력해 주는 앱

`__name__`이라는 변수에는 모듈명이 담긴다.

## 2장 플라스크 개발 기초 공사!
- 블루프린트를 이용해 라우트 함수를 관리한다.
- 플라스크 ORM을 이용해 데이터베이스를 제어한다.
- 파이보 게시판에 질문 목록과 상세 조회 기능을 만든다.

### 플라스크 기초 다지기
- 규모 있는 프로젝트를 위한 프로젝트 구조 설계

```
├── pybo/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ forms.py
│      ├─ views/
│      │   └─ main_views.py
│      ├─ static/
│      │   └─ style.css
│      └─ templates/
│            └─ index.html
└── config.py
```
- models는 데이터베이스를 처리 한다.
- forms는 서버로 전송된 폼을 처리 한다.
- views는 화면을 구성한다.
- static는 정적 파일을 저장한다 (css, js, image)
- templates는 html 파일을 저장한다.
- config.py는 프로젝트를 설정한다.

### 플라스크 애플리케이션 팩토리
- 플라스크 공식 홈페이지에서 애플리케이션 팩토리를 사용하라고 권고

요기서 pylint 때문에 hello_pybo는 사용하지 않는 함수라고 경고를 띄운다.
이 부분을 유닛 테스트를 추가하면 경고를 없애는 것이 가능할 것으로 보이는데 한번 테스트를 해봐야 될 것 같다.

### 유닛 테스트
```sh
pip install pytest
```
- vscode Python Test Explorer for Visual Studio Code 설치

- settings.json에 아래 설정 추가
```json
"python.testing.pytestEnabled": true,
```

### 블루프린트로 라우트 함수 관리하기
- create_app 함수 안에 hello_pybo 함수가 들어 있는 형태.
- api 추가 시 create_app 함수 안에 계속해서 함수를 만들어 줘야 하는 불편함이 있음.
- 블루프린트를 사용하면 함수를 구조적을 관리할 수 있다.

### 모델로 데이터 처리하기
- ORM을 사용하여 데이터베이스를 다룬다.
- ORM을 사용하면 별도의 SQL 문법을 배우지 않아도 된다는 장점이 있어 훨씬 좋다.
- ORM은 데이터베이스 종류에 상관 없이 일관된 코드를 유지할 수 있어 프로그램의 유지보수 하기가 편리하다.

#### 플라스크 ORM 라이브러리 사용하기
- 파이썬 ORM 중 가장 유명한 SQLAlchemy를 사용
- Flask-Migrate 라이브러리도 함께 사용 (테이블 생성, 컬럼 추가등 작업)
- https://github.com/pallets/flask-sqlalchemy

```bash
pip install Flask-Migrate
```

- db, migrate 객체를 만든 다음 create_app 함수 안에서 init_app 메서드를 이용해 초기화함.
  - flask에서는 이러한 패턴을 자주 사용한다.
    - db 객체를 create_app 함수 안에서 생성하면 블루프린트와 같은 다른 모듈에서 불러올 수 없다.
    - db, migrate와 같은 객체를 create_app 함수 밖에서 생성하고, 실제 객체 초기화는 create_app 함수 안에서 수행한다.

```bash
set FLASK_APP=pybo
flask db init

flask db migrate # 모델을 새로 생성하거나 변경할 때
flask db upgrade # 모델의 변경 내용을 실제 데이터베이스에 적용할 때
```

#### 모델 만들기
- 복합키(Composite Key) 설정하는 부분은 찾아봐야 될듯.
- https://docs.sqlalchemy.org/en/13/core/type_basics.html

#### 모델을 이용해 테이블 자동으로 생성하기
```bash
flask db migrate # 모델을 새로 생성하거나 변경할 때
flask db upgrade # 모델의 변경 내용을 실제 데이터베이스에 적용할 때
```

#### 모델 사용하기
- 플라스크 쉘
```bash
flask shell

>>> from pybo.models import Question, Answer
>>> from datetime import datetime
>>> q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())

>>> from pybo import db
>>> db.session.add(q)
>>> db.session.commit()

>>> q.id

>>> q = Question(subject='플라스크 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())
>>> db.session.add(q)
>>> db.session.commit()
>>> q.id
```

#### 데이터 조회하기
- https://docs.sqlalchemy.org/en/13/orm/query.html

```bash
>>> Question.query.all()

>>> Question.query.filter(Question.id==1).all()

>>> Question.query.get(1)

>>> Question.query.filter(Question.subject.like('%플라스크%')).all()
```

#### 데이터 수정하기

```bash
>>> q = Question.query.get(2)
>>> q
>>> q.subject = 'Flask Model Question'
>>> db.session.commit()
```

#### 데이터 삭제하기
```bash
>>> q = Question.query.get(1)
>>> db.session.delete(q)
>>> db.session.commit()

>>> Question.query.all()
```

#### 답변 데이터 생성 후 저장하기
```bash
>>> from datetime import datetime
>>> from pybo.models import Question, Answer
>>> from pybo import db
>>> q = Question.query.get(2)
>>> a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=datetime.now())
>>> db.session.add(a)
>>> db.session.commit()

>>> a.id
>>> a = Answer.query.get(1)
>>> a
```

#### 답변에 연결된 질문 찾기 vs 질문에 달린 답변 찾기
```bash
>>> a.question

>>> q.answer_set
```

### 질문 목록과 질문 상세 기능 만들기

#### 질문 목록 기능 만들기
- 템플릿 태그 등을 사용하여 동적으로 페이지를 만듬
- https://jinja.palletsprojects.com/en/2.11.x/templates/

#### 질문 상세 기능 만들기


#### 블루프린트로 기능 분리하기
- url_for 함수를 사용하면 유지보수 하기 쉬워진다.