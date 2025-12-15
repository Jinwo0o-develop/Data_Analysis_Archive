import pandas as pd
import os
import glob # 패턴 매칭 모듈

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "00_Common_Data")

def get_sales_data():
    file_pattern = os.path.join(DATA_PATH, "*이천시.csv")
    file_list = glob.glob(file_pattern)

    if not file_list:
        print(f"[Error] '{DATA_PATH}'경로에서 파일을 찾지 못했습니다.")
        return pd.DataFrame()
    
    print(f"[System] 총 {len(file_list)}개의 파일을 발견하여 병합을 시작합니다...")
    
    df_list = []
    for file_path in file_list:
        try:
            temp_df = pd.read_csv(file_path, encoding='utf-8')
            df_list.append(temp_df)
        except Exception as e:
            print(f"[Warning] 파일 로드 실패: {file_path} / 사유: {e}")
    
    df = pd.concat(df_list,ignore_index=True)

    df['ta_ymd'] = pd.to_datetime(df['ta_ymd'], format='%Y%m%d')
    df['month'] = df['ta_ymd'].dt.month
    
    # 요일 변환
    df['day'] = df['ta_ymd'].dt.day_name()
    day_mapping = {
        'Monday': '월요일', 'Tuesday': '화요일', 'Wednesday': '수요일',
        'Thursday': '목요일', 'Friday': '금요일', 'Saturday': '토요일', 'Sunday': '일요일'
    }
    df['day'] = df['day'].map(day_mapping)

    # 데이터 타입 최적화 (Memory Optimization)
    target_cols = ['cty_rgn_no', 'admi_cty_no', 'card_tpbuz_cd', 
                   'card_tpbuz_nm_1', 'card_tpbuz_nm_2', 
                   'sex', 'age', 'day', 'hour']
    
    for col in target_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')

    # 계절 분류 (헬퍼 함수 사용)
    df['period'] = df['month'].apply(_classify_period)
    
    return df

def _classify_period(month):
    if (1<=month<=2) or (month == 12):
        return '겨울'
    elif 3<= month <=5:
        return '봄'
    elif 6<= month <=8:
        return '여름'
    else:
        return '가을'


