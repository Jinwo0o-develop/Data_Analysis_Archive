## [한글 폰트 설치 및 모듈 불러오기] ##
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

def set_korean_font():
    try:
        font_path="C:/Windows/Fonts/malgun.ttf"
        font = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font)
        plt.rc('axes', unicode_minus=False)
        print("한글 폰트 설정이 완료되었습니다.")
    except Exception as e:
        print("한글 폰트 설정 실패")

## [매핑 자료] ##

#나이
AGE_MAP = { 
    1 : '10세 미만',
    2 : '10대',
    3 : '20대',
    4 : '30대',
    5 : '40대',
    6 : '50대',
    7 : '60대',
    8 : '70대',
    9 : '80대',
    10 : '90대',
    11 : '100세 이상'
}

#시간 : 표, 테이블 용(상세)
TIME_DETAIL_MAP = {
    1 : '00:00 ~ 06:59 (심야)',
    2 : '07:00 ~ 08:59 (출근)',
    3 : '09:00 ~ 10:59',
    4 : '11:00 ~ 12:59 (점심)',
    5 : '13:00 ~ 14:59',
    6 : '15:00 ~ 16:59',
    7 : '17:00 ~ 18:59 (퇴근)',
    8 : '19:00 ~ 20:59',
    9 : '21:00 ~ 22:59',
    10 : '23:00 ~ 23:59'
}

#시간 : 파악용(짧은 버전)
TIME_SHORT_MAP = {
    1 : '00-07시',
    2 : '07-09시',
    3 : '09-11시',
    4 : '11-13시',
    5 : '13-15시',
    6 : '15-17시',
    7 : '17-19시',
    8 : '19-21시',
    9 : '21-23시',
    10 : '23-24시'
}

#요일
DAY_MAP = {
    1 : '월',
    2 : '화',
    3 : '수',
    4 : '목',
    5 : '금',
    6 : '토',
    7 : '일'
}
