

---**Dec.2025**
### 그래프 컬럼 설명
**ta_ymd :** 기준 년월일(YYYYMMDD) / **cty_rgn_no :** 시·군·구 코드

**admi_cty_no :** 행정동 코드(행정안전부 기준) / c**ard_tpbuz_cd :** 카드사 업종 분류 코드

**card_tpbuz_nm_1 :** 업종 대분류명 / **card_tpbuz_nm_2 : **업종 중분류명

**sex :** 성별(M/F) / **age :** 연령대 코드(01: 0–9세, 02: 10–19세, …, 11: 100세 이상)

**hour :** 시간대 코드(01: 00–06시, 02: 07–08시, 03: 09–10시, …, 10: 23시)

**day :** 요일 코드(01: 월, 02: 화, 03: 수, 04: 목, 05: 금, 06: 토, 07: 일)

**amt :** 매출 금액 / **cnt : 매출 건수**


# 📅 개발 및 학습 일지 (Development Log)
## 11.Dec.2025 (DAY-1) [Colab에서의 연습내용 포함]
## ※DEV_LOG 파일 및 파일정돈(구조화 시점)

# 📅 개발 및 학습 일지 (Development Log)
## 10.Dec.2025 (DAY-1) [Colab에서의 연습내용 포함]
plt.bar / plt.barh / 
- config.py 모듈
 - plt.gca().spines['postion'].set_visible() / plt.text(x, y, s, weight, ha, va)
## ✅ 한 일
## 배운점(TIL)
### TIL (간단한 Keyword 정리)
## 트러블슈팅 (Troubleshooting)
# 📅 개발 및 학습 일지 (Development Log)
## 09.Dec.2025 (DAY-1) [Colab에서의 연습내용 포함]
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
 - [ ] .collections[0] *무슨 기능인가요 ?* -> 도형들의 리스트(집합) -> 깊이 있는 제어를 할 때 필요
 - [x] cbar = ax.collections[0].colorbar *왜 이렇게 사용하는건가요?* -> 객체지향적으로 세밀하게 다룰 수 있음
 - [ ] Github Markdown -> 학습 중

# 📅 개발 및 학습 일지 (Development Log)
## 08.Dec.2025 (Colab 활동)
## ✅ 한 일
 - [x] 데이터 전처리 방법
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
     - df['컬럼'] 에 다시 넣어주었음
 
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
 - 1. Python 및 데이터 분석 전반에 익숙해지기  

   - (최종 목표: 실무 2~3년차 수준을 향한 성장)

2. 데이터 기반 인사이트 도출 및 패턴 발견  

3. 연령별 타겟 마케팅 전략 수립

4. PPT 발표 수준의 분석 자료 제작

## 분석 환경 및 도구 (Tech Stack)

- **Language:** Python 3.14  

- **Data Handling:** Pandas (데이터 전처리, 피벗테이블)  

- **Visualization:** Matplotlib, Seaborn (히트맵, 서브플롯)  

- **Environment:** VS Code, Git / GitHub  

- **Module:** `config.py` 기반 전역 설정(폰트, 매핑) 모듈화


