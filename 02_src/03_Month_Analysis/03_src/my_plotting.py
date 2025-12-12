import seaborn as sns
import matplotlib.pyplot as plt

def draw_top_categories(data, title, ax, color_pallette='Blues_r'):
    """
    특정 세대의 상위 소비 업종을 그려주는 함수

    Parameters:
    - data: 이미 집계가 완료된 Series (index=업종, value=금액)
    - title: 그래프 제목(str)
    - ax: 그림을 그릴 도화지 (matplotlib Axes)
    - color_palette: 색상 팔레트 이름 (str)
    """

    # 1. 색상 설정
    colors = sns.color_palette(color_pallette, len(data.index))

    # 2. 그래프 그리기(barh)
    sns.barplot(x=data.values, y=data.index, palette=colors, ax=ax, order=data.index)

    # 3. 꾸미기
    ax.set_title(title, weight='bold', fontsize=15, pad=15)
    ax.set_xlabel("총 소비 금액", fontsize=10)
    ax.set_ylabel("") 
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible('gray')
    ax.tick_params(axis='x', bottom=False, labelbottom=False)
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    #4. 숫자 달기
    total_sum = data.sum()
    for i, (index, value) in enumerate(data.items()):
        pct = (value/total_sum) * 100
        text = f"{value/1000000:,.0f}백만원\n ({pct:.1f}%)"
        ax.text(x=value*1.01, y=i, s=text, ha='left', va='center', weight='bold', fontsize=9)