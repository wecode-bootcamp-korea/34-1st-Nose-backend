## ✅ 프로젝트 Repository 개요

<p align="center">
  <br>
  <img src="./images/nose_main_image.png">
  <br>
  위 사진은 프론트엔드 구현 화면입니다.
</p>

📍 **설명**

해당 레포지토리는 [위코드 부트캠프](https://github.com/wecode-bootcamp-korea)의 34기 백엔드 1차 팀 프로젝트 레포지토리입니다.

프론트엔드 레포지토리는 [여기](https://github.com/wecode-bootcamp-korea/34-1st-Nose-frontend)로 이동해주세요.

<br>

📍 **목차**

1. 프로젝트 개요

2. 기술 스택

3. 구현 기능

4. 배운 점 & 아쉬운 점

<br>
<br>

## ✅ 프로젝트 개요

해당 프로젝트는 [PAFFEM](https://paffem.cafe24.com/)이라는 향수 추천 웹사이트 중 일부 기능을 배우고 적용해보는 목적으로 진행되었습니다.

저작권 문제로 이미지는 [pixabay](https://pixabay.com/ko/)의 이미지들을 사용하였습니다.

협업 툴로는 `Trello`와 `Notion`을 사용하였습니다.

<p align="center">
  <br>
  <img src="./images/nose_trello.png">
  <br>
  Trello
</p>

<p align="center">
  <br>
  <img src="./images/nose_notion.png">
  <br>
  Notion
</p>

<br>

### 📌 프로젝트 목표

1. Python의 `Django` 프레임워크를 활용한 백엔드 서버 구축하기.

2. MySQL을 활용하여 데이터베이스를 구축하고, ORM 이해하기.

3. 다양한 협업 툴을 사용하여 커뮤니케이션 역량 강화하기.

4. Scrum 방식 업무 경험하기.

<br>

### 📌 팀원 소개 및 역할

해당 프로젝트는 2명의 백엔드 개발자가 참여하였습니다.

**김상웅 [sangwoong03](https://github.com/sangwoong03)**

- `dbdiagram`을 활용한 모델링

- `Django` 프로젝트 초기 설정

- 로그인 기능 및 `bcrpyt`, `pyjwt`를 회원 인증/인가 API 구현

- 상품 리스트 API 구현

- 상품 상세페이지 API 구현

<br>

**김지영 [KJY0627](https://github.com/KJY0627)**

- `dbdiagram`을 활용한 모델링

- MySQL 기본 데이터 구축 및 저장

- 회원가입 기능 및 `bcrypt`를 통해 암호화된 회원정보 DB 저장

- 장바구니 API 구현 - POST, GET, DELETE

<br>
<br>

## ✅ 기술 스택

---

기본 기술 스택은 다음과 같습니다.

`requirements.txt` 파일에서 프로젝트에 사용된 모듈 및 패키지의 버전을 확인할 수 있습니다.

<br>

### 📌 Backend 기술스택

|                                                Language                                                |                                                Framwork                                                |                                               Database                                               |                                                     ENV                                                      |                                                   HTTP                                                   |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=black"> | <img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |

<br>
<br>

## ✅ 구현 기능

이번 프로젝트에서 구현한 기능은 총 4가지입니다.

**1. 회원가입 API**

- 회원 정보에 대한 `유효성 검사 `

- 회원 비밀번호 `bcrypt` 암호화

<br>

**2. 로그인 API**

- `bcrypt`를 활용한 비밀번호 암호화/복호화

- `jwt`를 활용한 토큰 발급 및 토큰 인가

  1. 토큰의 인가 과정 중 토큰에 대한 에러 예외처리.

<br>

**3. 상품 API**

- `Shop` 페이지 이동 시 상품의 전체리스트 정보 불러오기

- `Qeury Parameter`로 특정 상품 필터링하기

  1. 기존 `Q()` 객체를 활용하여 특정 향과 카테고리에 대한 필터링 적용
  2. 조건 사항이 더욱 많아질 경우 `if 조건문`을 더욱 많이 작성해야하고 처리 속도를 고려하여, `dictionary comprehension`을 활용한 리팩토링

- `Path Parameter`로 특정 상품 상세 정보 불러오기

<br>

**4. 장바구니 API**

- 상품 상세 페이지에서 해당 상품 장바구니에 추가하기

- 로그인 한 유저의 장바구니에 담긴 상품 확인하기

- 로그인 한 유저의 장바구니에서 선택된 상품 삭제하기

<br>
<br>

## ✅ 회고

블로그 포스팅 : [1차 프로젝트 회고](https://velog.io/@sangwoong/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0)

### 📌 배운점

1. IT 개발 직군에서 사용하는 전문 용어와 협업툴에 대한 경험

2. 웹 페이지 분석과 기획에 따라 필요한 데이터베이스를 생성하고 데이터의 관계 이해

3. `miniconda3`와 `git`을 통해 코드 버전 관리 방법 경험

4. `Django`에서 사용하는 다양한 ORM을 적용해볼 수 있는 기회

<br>

### 📌 잘했던 점

1. Trello를 통한 명확한 개발 계획 수립 및 의도한 sprint 목표 모두 완성

2. React.js에 대한 이해도와 관심으로 front-end 개발자와의 적극적인 소통

3. git flow에 대한 명확한 이해와 PR request 작성 방법에 대한 터득

<br>

### 📌 아쉬운 점

1. 명확한 API 명세서가 필요성 (2차 프로젝트에서는 POSTMAN 활용 예정)

2. 추가 기능 구현 부족 (2차 프로젝트 혹은 부트캠프가 끝나면 사이드프로젝트로 반드시 구현 예정)

3. 오히려 같은 back-end 개발자 사이의 적은 의사소통 (코드 리뷰, Daily Meeting 간 소통 필요)
