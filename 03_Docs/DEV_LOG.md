
**Dec.2025**
---
### 그래프 컬럼 설명
**ta_ymd :** 기준 년월일(YYYYMMDD) / **cty_rgn_no :** 시·군·구 코드

**admi_cty_no :** 행정동 코드(행정안전부 기준) / c**ard_tpbuz_cd :** 카드사 업종 분류 코드

**card_tpbuz_nm_1 :** 업종 대분류명 / **card_tpbuz_nm_2 : **업종 중분류명

**sex :** 성별(M/F) / **age :** 연령대 코드(01: 0–9세, 02: 10–19세, …, 11: 100세 이상)

**hour :** 시간대 코드(01: 00–06시, 02: 07–08시, 03: 09–10시, …, 10: 23시)

**day :** 요일 코드(01: 월, 02: 화, 03: 수, 04: 목, 05: 금, 06: 토, 07: 일)

**amt :** 매출 금액 / **cnt : 매출 건수**



# 📅 개발 및 학습 일지 (Development Log)
## 12.Dec.2025 [DAY-5]
## ※DEV_LOG 파일 및 파일정돈 (구조화 적용일) [TIL 참고]
## ✅ 한 일
 - [X] Monorepo(모노레포)도입
 - [X] Rename Refactoring (리네임 리팩토링)
 - [X] 사용자 코드 조각(User Snippets) 

## 배운점(TIL)
사용자 코드 조각(User Snippets) 진짜 없을까 싶어서 다시 검색하니까 나옴. 
### TIL (간단한 Keyword 정리)
- Monorepo
- Rename Refactorin
- User Snippets
## 트러블슈팅 (Troubleshooting)

# 📅 개발 및 학습 일지 (Development Log)
## 11.Dec.2025 [DAY-4]
## ✅ 한 일
- 이미지 파일 (Cohort와 Month) 생성 및 폴더 정리
- 프로젝트 분석 방향 설정
- 분석할 일수(월,주,일) 선택
- 
## 배운점(TIL)
 - **이중축(Duelaxis)**그래프 도전
 - **객체생성** ax2, ax1
     - ax1 도화지에는 barplot, ax2 도화지는 ax2 = ax1.twinx() 적용
         - '.twinx()'는 서로 단위가 다른 두 데이터를 하나의 그래프에 겹쳐 보고 싶을 때 사용
         - 즉, ax1 도화지에 ax2를 같이 사용함.

 - 일 컬럼
 - 기존 df['ta_ymd'] 컬럼을 사용하기에는 너무 길다는 문제점이 있음
     - 전부 7월의 데이터이므로 title에 2025년 07월이라고 명시
     - pd.to_datetime(df['ta_ymd'], format="%Y%m%d) 함수로 데이터 포맷
     - df['ta_ymd'].dt.day -1 적용(index 맞추기 위함)

 - 막대그래프
     - 막대그래프는 '#4c72b0' 색으로 매출총액을 나타냄
     - plt.axvline()을 사용하여 일주일이 지나면 검정색 선(linestyle='-.')으로 표시
     - '매출총액' 글자가 겹치자 rotation=0(수평), labelpad()=10 으로 조정하여 해결함.

 - 라인그래프
     - 라인그래프는 'orange' 색으로 매출건수를 나타냄
     - ax2.tick_params(axis='y', labelcolor='orange') 적용 -> y축 사용 / y축 레이블 색은 주황색
     - '매출건수' 글자를 rotation=0 (수평)으로 조절함

 - 그래프 조정
 - 발표용 강조 자료
     - 기존 막대그래프들에게 '#6f9dbd' 색깔 적용 ( 기존보다 연함 )
     - bar와 line의 투명도를 'alpha=0.7'로 설정함
     - 특정강조 그래프에는 'red' 색깔 적용
     - axvline()은 4구간이 있었으나 if문을 적용하여 하나만 범례에 띄웠음.
     - [막대그래프 도화지] ax1.set_xticklabels(range(1,32)) 가로축 조정

    **전체 흐름 시각화로 인해 상세분석할 날(일)과 프로젝트 분석 방향을 정할 수 있었음**
    *__15,16,17,18,19,25일(월급날)__*

 - **요일별 매출총액/매출건수 비교**
 
 - 요일 별 막대그래프
     - 막대그래프는 '#ff9873' 색으로 색칠, 강조 색깔은 'red'임
     - df['day'] 컬럼이 'category' 였기 때문에 또 다시 ㄱ,ㄴ,ㄷ 순으로 정렬
     - 값이 월,화,수, ... 일 순으로 정렬되어 있지 않아 값으로도 정렬 불가능

 - 요일 정렬
     - my_order[월-일] 생성 후 order=my_order 도입
     - plt.text에서도 정렬이 되어있지 않아 .reindex(my_order)로 정리
 
 - 그래프 조정
     - 몰입도를 위해 ax.patch.face_color / ax.face_color를 사용해 '#f0f0f0ed'로 색깔 조정

 - 결과
     - 화,수,목 요일이 '금','토'보다 높았음

 - 검증
 - 다른 월도 그러한지 (6월, 8월 데이터를 가져와 시각화)
     - 이중축 그래프에서는 항상 화,수,목 은 꾸준했으며 금,토에 매출건수와 매출총액이 많이 증가함.
     - 6월, 8월 그래프는 화,수,목요일이 '토'요일을 넘긴적이 없었음.
     - Colab 환경에서 제작했던 '수원시'의 요일별 그래프 역시 그러함.
     - axhline()으로 표시하여 발표자료로써 이해하기 쉽게 만듬
 

 - 파일정리
 - 현재 구조의 비효율성
     - 파일들을 넣을 정확한 명칭을 찾음
     - 'images' 폴더를 만들어 사진들을 정리
     - 'data' 폴더를 만들어 '.csv'파일 정리
     - 'src' 폴더를 만들어 '.py' 모듈 정리


### TIL (간단한 Keyword 정리)
 - 객체지향방법 + .twinx()로 이중축(Duelaxis)그래프 생성
 - 심화분석할 날(일) 탐색 및 프로젝트 진행방향 결정
 - 요일별 막대그래프 생성
 - reindex(), my_order 생성으로 커스터마이징 정렬
 - 같은년도 다른 월 데이터로 요일별 그래프의 이상 검증(탐지)
 - axvline, axhline 으로 구분 및 기준 생성 ( 범례는 하나 )
 - 데이터포맷 및 투명도 조정, 강조색상 사용으로 그래프 강조
 - 'images', 'data', 'src' 등 폴더를 만들어 정리

## 트러블슈팅 (Troubleshooting)

### 1. 정렬방법
- **문제 :** df['day']는 'category'타입에 값이 들쭉날쭉해 값으로도 정렬 불가
- **방법 :** my_order로 원하는 정렬기준 생성
- **결과 :** 원하는 방식으로 정렬 + plt.text에 '.reindex(my_order)' 사용으로 텍스트 정렬

### 2. 값
- **문제 :** df.items()를 사용하지 않으면 개인적으로 값을 꺼내기 힘들어 했음
- **방법 :** iloc / loc 사용법 숙지
- **결과 :** 원하는 값 꺼내기 용이해짐.

### 3. 인덱스
- **문제 :** bar와 line 그래프의 인덱스가 일치하지 않는 문제(범주형, 수치형)
- **방법 :** df['ta_ymd'].dt.day -1 적용
- **결과 :** 분석 데이터 왜곡현상 해결

## 추가 공부
 - [x] ax.set_ticks -> 눈금(Tick)이 찍힐 **'수학적 좌표(위치)'**를 정함
 - [x] ax.set_ticklabels-> 위에서 정한 위치에 적힐 **'글자(이름표)'**를 정함
 - [x] ax.set_label -> Y축 전체를 대표하는 **'제목'**을 달아줌.
 - [x] ax.tick_params -> 눈금(Tick)과 눈금 라벨(Label)의 스타일을 **미세 조정**함.

# 📅 개발 및 학습 일지 (Development Log)
## 10.Dec.2025 [DAY-3]
## ✅ 한 일
 - [x] 매핑자료 'config.py', 그래프 시각화 함수 'my_plotting.py' 모듈화
 - [x] bar(barh) 학습
 - [x] 그래프 디테일 학습


## 배운점(TIL)
 - 그래프 생성
 - 새로운 프로젝트 파일을 생성하면 다시 매핑자료 입력과 한글설치를 하는 일련의 과정들이 너무 귀찮게 느껴짐
     - 따라서, 'config.py'를 생성해 모듈화 함.(매핑자료와 한글설치 함수생성)
     - import 라이브러리 역시 모듈화 하려했음 -> '네임스페이스 오염'과 '명시적인 중요성'으로 인해 사용 비추천 -> 오류찾기도 어려움
     - ![Font_Module](../02_src/02_Cohort_Practice/images/Font.png)
    **간단하게 시간을 절약하고 작업의 효율성을 증가시킬 수 있었음**
 
 - 분석하는 연령대를 나누어 'card_tpbuz_nm_1'분석 (세그멘테이션) 
     - 일반적인 상향식 막대그래프는 가독성도 떨어지고 보기 불편하다고 느꼈음
         - label의 갯수가 많아 가독성이 떨어지고, 금액확인이 어려웠음
     - barh(수평막대그래프) 처럼 눕히는 방법 선택 (sns.barplot은 x와 y값만 바꾸면 됨)
     - 큰 값에서 작은 값으로 정렬하고 싶으나 'category' 타입은 ㄱ,ㄴ,ㄷ 순으로 정렬
         - 첫 번째, 데이터전처리 :  ```groupby```를 할 때 .sort_values(ascending=False)
         - order = data.index 파라미터를 추가 -> '데이터 순서 = 막대 순서 = 색상 리스트'로 1:1 매칭

 - 생성한 barh 그래프가 밋밋
     - sns.color_palette('Blues_r', len(x)) 으로 그라데이션 색깔을 x개만큼 생성 (큰 값이 가장 진함)
     - 참고로 palette('색깔_r')에서 _r 은 reverse의 약자임. -> 큰 값을 가장 진하게 하고 싶을 때 사용
     - 그래프의 외곽선이 답답하고 불편함
         - plt.gca().spines['position'].set_visible(False)을 통해 제거하고 왼쪽 축만 남김

 - **저번 *추가학습* 때 배운 객체지향적 방법적용**
     - fig, ax = plt.subplots(figsize=(x,y))를 통해 ax (그래프를 그릴 도화지) 생성
         - 앞으로 ax의 세부 설정이 가능해짐
         - 그래프의 x축을 지우기 위해 plt.xticks([]) 사용
             - 하지만 plt.grid(axis='x')를 표현할 수 없었음.
             - ax.tick_params()를 사용하고, ax.grid(axis='x') 사용으로 x축 수직선 적용 및 해결
    
    **그래프에서 객체지향적 접근과 상세한 튜닝으로 가독성, 심미성, 전문성을 챙길 수 있게 됨**
 
 - 데이터 레이블링
     - plt.text(x, y, s, weight, ha, va) 학습
     - 반복문(for)과 `enumerate`를 활용하여 모든 막대 위치에 정확한 수치 텍스트(`ax.text`)를 자동 배치.
         - Before : 퍼센트(pct)와 금액 값을 리스트를 따로 제작하고 text에 기입 ( 2번의 반복 )
         - After : 논리 구조 개선과 enumerate(df.items())를 통해 반복문 한번으로 기입.

 - 그래프 변수
 - 생성한 그래프에 집단마다 변수와 내용물을 바꿔줘야 함 -> VScode의 ```F2``` 단축키 역시 불편함
     - 생성한 그래프를 함수로 변환(data, "그래프 제목", ax, 색깔(기본은 Blues_r))
     - barh 그래프는 많이 사용할 것 같아 'my_plotting.py' 모듈화

 - 'my_plotting.py' 수정사항이 있을 때마다 VSCode를 껏다 켜야 하는 불편함
     - importlib.reload(mp)를 통해 적용
         - 나아가 '%reload_ext autoreload' / '%autoreload 2' 적용으로 자동화
    
    **유지보수가 용이해졌고 수정도 간단함**
    
### TIL (간단한 Keyword 정리)
- 'config.py', 'my_plotting.py' 모듈화
- seaborn 기준 bar(x, y, palette, ax, order) / plt.text(x, y, s, weight, ha, va) 학습
- plt.gca().spines['postion'].set_visible(), ax 객체지향적 방법 도입 -> 그래프 전문성, 심미성, 가독성 확보

## 트러블슈팅 (Troubleshooting)

### 1. 아쉬운 시각화
- **문제 :** plt.xticks 사용 -> plt.grid() x수직선 사용불가
- **방법 :** ax를 통한 객체지향적접근과 세부설정(ax.set_ylabel, ax.grid(axis='x', alpha=0.5))
- **결과 :** 그래프에 대한 전문적인 접근과 가독성, 심미성 향상 가능.

### 2. 비효율적인 코드
- **문제 :** plt.text를 사용하기 위한 비효율(2번의 반복문)
- **방법 :** 논리구조 개선, enumerate 함수 사용
- **결과 :** 비효율(2번의 반복) 개선

### 3. 수정 적용
- **문제 :** 'my_plotting.py' 파일 수정마다 VSCode를 껏다켜야하는 불편함
- **방법 :** importlib.reload(mp)로 해결
- **결과 :** '%reload_ext autoreload' / '%autoreload 2' 적용으로 자동화

## 추가 공부
 - __pycache__ : 파이썬 인터프리터가 소스 코드(.py)를 컴파일하여 만든 **바이트코드(Bytecode, .pyc)** 저장소
  -> 다음에 프로그램을 실행할 때, 컴파일 과정을 건너뛰어 **로딩 속도(Start-up time)**를 높일 수 있음
   -> 소스 코드만 있으면 언제든 자동 생성 -> Git에 올릴 필요 없는 파일

# 📅 개발 및 학습 일지 (Development Log)
## 09.Dec.2025 [DAY-2]
## ✅ 한 일
 - [x] Git과 VSCode 연결
 - [x] 기본적인 EDA(탐색적 데이터 분석)
 - [x] 함수와 파라미터 학습


## 배운점(TIL)
 - HEATMAP
 - 나이에 따른 시간대 별 매출총액을 보고 싶었음
     - 하지만, 일일이 Line그래프로 보기에는 양도많고 불편하고 가독성이 떨어짐
     - Heatmap이라는 함수 채택
     - Parameter(파라미터) 학습

 - Heatmap에 ```groupby```된 결과를 바로 넣으려다가 오류 발생
     - Heatmap은 2차원 행렬 구조가 필요함 -> pivot_table 학습

 - Heatmap의 숫자가 너무 커서 ( + 지수 표기법 표현) 읽기 어려웠음
     - 단위를 천만으로 맞추고 단위를 표시함.
     - fmt 파라미터를 사용하여 숫자를 정리

 - Heatmap 숫자가 밋밋하다는 생각이 듦.
     - '*_kws'를 사용해 숫자크기, bold체 등 세밀하게 제어
     - 컬러바(범례) 유무 및 레이블 설정

 **연령에 따른 시간대 별 소비성향을 색깔을 통해 한눈에 파악할 수 있었음.**

 - Pivot_Table
 - Heatmap에 사용하기 위해 필요한 데이터 가공단계 ( SQL과 같은 기능 )
     - ```groupby()```는 세로로 긴 형태의 결과물 / ```Pivot_Table```은 2차원 매트릭스 형태로 펼쳐줌
     - index = 행 / columns = 열 / values = 교차지점의 값 / aggfunc = 계산방식
     - aggfunc의 기본은 mean(평균) -> sum(합)으로 바꿔주어야 의도와 일치함

 - sns.그래프형태
 - 상세한 그래프는 matplotlib로, 빠르고 예쁜 시각화는 seaborn으로 작성
 - 파라미터에서 hue를 통해 간단한 값 분리를 할 수 있었음
 - color가 아닌 palette 파라미터로 색 조정 가능.
 
 - plt.axvline() (axv : 수직선, axh : 수평선)
 - 학습 중 마주친 새로운 함수였고, 강조와 구분에 탁월하겠다 생각해 학습함.

 - 그래프 원(￦) 표시 -> 깨짐 현상 발생
     - 한글폰트 설치와 마이너스 부호 깨짐 방지 코드 적용

 **한글로 된 매핑자료를 만들고 **시각화**와 **전처리**에 용이해짐**


### TIL (간단한 Keyword 정리)
 - Heatmap(data, cmap, annot, annot_kws, fmt, cbar, cbar_kws )
     - Heatmap을 사용하기 위해서는 Pivot_Table로 먼저 가공해야한다는 점.
     - '*_kws'를 통한 폰트 설정, label 설정

 - Pivot_Table(index, column, values, aggfunc)
 - .reset_index() / sns.그래프형태 ->(hue='원하는 구분', palette='')
 - plt.axvline(x, color, labels, linewidth, linestyle) 수직선.

 - 한글폰트 설치법(마이너스 부호 깨짐 방지)

## 트러블슈팅 (Troubleshooting)

### 1. 불편한 시각화
- **문제 :** Heatmap맵 데이터 구조 불일치 
- **방법 :** Pivot_Table 학습
- **결과 :** 연령대별 시간대 소비 집중 구간을 직관적으로 도출

### 2. 한글 폰트 깨짐  

- **문제 :** 시각화 과정에서 한글 및 기호가 깨지는 현상 발생  
- **방법 :** 원인 파악 및 한글폰트 설치
- **결과 :** '시각화'와 '전처리'에 용이해졌음
- **추가 기능** 한글로 된 매핑자료를 만들었고 데이터를 다루기 편해짐.

### 추가 공부
 - [x] .collections[0] *무슨 기능인가요 ?* -> 도형들의 리스트(집합) -> 깊이 있는 제어를 할 때 필요
 - [x] cbar = ax.collections[0].colorbar *왜 이렇게 사용하는건가요?* -> 객체지향적으로 세밀하게 다룰 수 있음
 - [ ] Github Markdown -> 학습 중

# 📅 개발 및 학습 일지 (Development Log)
## 08.Dec.2025 [DAY-1] (Colab 활동)
## ✅ 한 일
 - [x] 데이터 전처리 방법 숙지
 - [x] 함수와 파라미터 학습


### 상황
 - 당시 노트북 성능문제로 Colab에서 데이터 전처리 시작.

## 배운점(TIL)
 - 데이터 불러오기
 - '.csv'파일을 pd.read_excel로 불러오는 바람에 실패했음
     - '.csv'와 '.xlsx' 구분
     - 컴퓨터가 파일경로를 읽는 법 파악.
     - .copy()를 통한 데이터 복사
 
 - 컬럼 가공
     - 책에서 학습한 기능들을 직접 사용해보고자 함
     - df.drop() 사용할 때 axis(축)을 지정해줘야하며 즉시 적용은 inplace=T임. 
     - .map() 함수를 사용해 매핑

 - 메모리 사용량
 - 데이터의 양이 많아 메모리 사용량을 줄이고자 함.
     - .astype()을 통한 컬럼의 category 타입화
     - 하지만 바뀌지 않았고 df.drop()안에 있는 inplace=T 파라미터를 사용해도 불가능했음
     - df['컬럼'] = df['컬럼'].astype('category')코드를 통해 적용시음
 
 - Pieplot
 - Pieplot으로 시각화
     - 컬럼의 값들이 많아 비중이 적을 수록 글씨가 겹침.
     - 적은 비중의 값들은 기준값변수를 생성하고 'etc' 컬럼을 만들어 합침
     - 퍼센트 뿐 만 아니라 금액(KRW)을 추가하고 싶었음
         - plt.text를 통해 값이 담긴 리스트 생성 후 적용
         - autopct 값을 None으로 조정하고 리스트 생성에 {value;,} / {value:.1f} 등 표현방법 구현
         - 글씨 크기와 글씨 조정을 위해 labeldistance 파라미터, textprops로 조정
     - seaborn의 color_palette()를 통해 pieplot에 colors 파라미터 사용

 - Pieplot의 범례
     - etc 값들을 범례로 따로 표시하고 싶었음
         - 숙련도 이슈로 실패함
         - 대신 '텍스트 박스'라는 개념을 도입(bbox_to_anchor)

## TIL(간단한 Keyword 정리)
 - plt.figure(figsize=(x,y))
 - plt.pie(x, labels, autopct, colors, explode, labeldistance, textprops)
 - df.groupby('')[''] -> ()묶은 그룹의 []원하는 컬럼
 - {value:.1f} or (value:,) 등 표현방법

### 추가 공부
 - [x] plt.legend(bbox_to_anchor) -> *bbox_to_anchor(bbox)* : 배경상자 속성으로, 네모난 경계 영역을 생성함

---
## 프로젝트 목표
1. Python 및 데이터 분석 전반에 익숙해지기  

   - (최종 목표: **실무 2~3년차 수준**을 향한 성장)

2. 데이터 기반 **인사이트 도출 및 패턴 발견**

3. 연령별 **타겟 마케팅 전략** 수립

4. **PPT 발표 수준의 분석 자료 제작**

## 분석 환경 및 도구 (Tech Stack)

- **Language:** Python 3.14  

- **Data Handling:** Pandas (데이터 전처리, 피벗테이블)  

- **Visualization:** Matplotlib, Seaborn (히트맵, 서브플롯)  

- **Environment:** VS Code, Git / GitHub  

- **Module:** `config.py` 기반 전역 설정(폰트, 매핑) 모듈화


