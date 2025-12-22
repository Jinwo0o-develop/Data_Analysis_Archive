# 1. 분석 변수
analysis_df <- df %>%
  filter(card_tpbuz_nm_1 == "음식",
         card_tpbuz_nm_2 == "고기요리") %>%
  mutate(
    # 연령대 그룹핑 (Code 3 = 20대, Code 4~7 = 30~60대)
    age_group = case_when(
      age == 3 ~ "20s",
      age %in% c(4, 5, 6, 7) ~ "Main_Group", # 30~60대
      TRUE ~ NA_character_
    ),
    # 점심 시간대 정의 (Code 4 = 11-13시)
    is_lunch = if_else(hour == 4, "Lunch", "Other")
  ) %>%
  filter(!is.na(age_group)) # 분석 대상 외 연령(10대, 70대 등) 제외

# 2. 교차표 생성 및 검정
contingency_table <- table(analysis_df$age_group, analysis_df$is_lunch)

print("=== [데이터 분포] 연령대별 점심(11-13시) 이용 건수 ===")
print(contingency_table)

# 3. 카이제곱검정 수행
chisq_result <- chisq.test(contingency_table)

print("=== [통계 검증] 카이제곱검정 결과 ===")
print(chisq_result)

# 4. 비율 확인
prop <- prop.table(contingency_table, margin = 1) * 100
print("=== [결과 해석] 그룹별 점심 이용 비율(%) ===")
print(round(prop, 2))