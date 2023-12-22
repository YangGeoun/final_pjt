# 1. 팀원 정보 및 업무 분담 내역

  부수환 : 전반적인 프론트 담당 <br>
        1. 메인화면 주요웹기능, 데일리 뉴스, 데일리 유튜브의 캐로젤 구현 <br>
        2. 주식차트, 게시판글, 환율계산기 모달 구현 <br>
        3. 로그인, 회원가입, 게시글 삭제, 예적금 가입시 컴파인 화면 구현 <br>
        4. 메인 화면 진입시 진입화면 구현 <br>
        5. 거의 모든 화면 요소에 인터섹션옵져버로 애니메이션 구현  <br>
        6. 버튼 이미지 호버, 클릭 이벤트시 애니메이션 구현 <br>
        7. 퀴즈의 필터 적용 <br>
 <br>
  양건우 : 전반적인 백 담당 <br>
        1. 게시판, 회원가입 로직 구현 <br>
        2. 유저 커스터 마이징 및 유저 더미데이터 생성 <br>
        3. 금감원, 유튜브, 네이버 api로 예적금, 영상, 뉴스 정보 db데이터 저장 <br>
        4. 주식정보, 다양한 db에 필요한 정보 크롤링 <br>
        5. 금융 상품 추천 알고리즘 구현  <br>
        6. 금융 상품 목록 페이지, 금융 상품 추천 페이지, 카드 추천 페이지 프론트 구현 <br>
 <br>
# 2. 설계 내용(아키텍처 등) 및 실제 구현 정도

### - 메인 화면 구성![캡처2.PNG](./readme_img/캡처.PNG)

![캡처.PNG](./readme_img/캡처2.PNG)

구현한 기능으로 가는 카드를 캐로젤 형식으로 구현

금융 관련 데일리 유튜브, 데일리 뉴스 카드를 캐로젤 형식으로 구현

오늘 국내, 해외 지수와 지수를 누를 시 그와 관련된 주식정보 모달이 열림

간단한 금융 퀴즈

#### - 환율계산기

![환율.PNG](./readme_img/환율.PNG)

환율 계산기는 간단한 기능으로 어떤 페이지에서든 모달로 뜰 수 있도록 구현

![지도.PNG](./readme_img/지도.PNG)

지역 정보를 입력하면 그 지역 은행을 모두 추천

왼쪽에는 은행 리스트가 지도에는 은행위치가 핀으로 찍힌다.

#### - 유저 소통 게시판

![게시판.PNG](./readme_img/게시판.PNG)

![게시글생성.PNG](./readme_img/게시글생성.PNG)

일반적인 게시판 및 댓글 구현

게시글 상세및 작성을 모달로 구현

#### - 프로필 페이지

![메인.PNG](./readme_img/메인.PNG)

프로필을 유저 정보를 하나하나 변경 가능하다.

월급 재산 등 민감한 정보는 아래의 디테일에서 눌러야 보이게 만들었다.

![프로필게시판.PNG](./readme_img/프로필게시판.PNG)

내가 작성한 게시글을 조회 가능하다.

![프로필예적금.PNG](./readme_img/프로필예적금.PNG)

내가 가입한 상품 조회와 되회된 상품의 그래프를 볼 수 있다.

#### - 예적금 비교 페이지

![예금적금.PNG](./readme_img/예금적금.PNG)

내가 원하는 예금 적금으로 나누어 은행, 이자 계산 방식, 저축기간을 선택해서 검색가능

상품을 눌러 상세정보를 보고 가입가능

#### - 금융 상품 추천 페이지

![추천.PNG](./readme_img/추천.PNG)

내가 가입한 상품과 추천 상품을 한번에 보면서 비교 가능하다.

# 3. 데이터베이스 모델링(ERD)

![ERD.PNG](./readme_img/ERD.PNG)

# 4. 금융 상품 추천 알고리즘에 대한 기술적 설명

#### 예적금 추천 알고리즘

전체 유저 데이터에서 월급, 제산, 나이 데이터를 뽑아 유저간의 코사인 유사도를 계산한다.

그 후 나와 비슷한 사람 100명을 뽑아서 그 사람들이 가입한 상품을 추합하여 가장 많이 가입한 예금 상품 3개 적금 상품 3개를 추천해준다.

### 카드 추천 알고리즘

주요 혜택에 대한 긍정과 부정 입력을 받아 조건문으로 필터링하여 추천

# 5. 서비스 대표 기능들에 대한 설명

처음 화면에서 물이 흐르는 듯한 애니메이션 

메인 페이지에서 간단한 금융 정보(유튜브, 뉴스, 주식정보, 경제지수, 금융퀴즈) 조회 가능

환율계산기

내 근처 은행 검색

유저 소통 게시판

프로필 페이지

예적금 비교 페이지

금융 상품 추천 페이지

# 6. 기타(느낀 점, 후기 등)

양건우 : 싸피에서 공부하면서 많은 것을 배웠다는 것을 알게 되었습니다. 그렇지만 막상 프로젝트를 만들고 하니 생각보다 모르는 것이 많았고 프로젝트를 진행하면 더 많은 것을 배울 수 있다는 것을 알게 되었습니다. 잘 맞는 사람과 팀이 되어하고 싶은 것에 집중할 수 있었고 만들고 싶은 것들을 전부 만들어 볼 수 있었습니다.
