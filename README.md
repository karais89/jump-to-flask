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