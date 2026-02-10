# 1. 데이터 전처리 및 필터링 (day 컬럼 문자열 대응)
target_2030 <- df %>%
  filter(age %in% c(3, 4)) %>%
  filter(card_tpbuz_nm_2 %in% c("패스트푸드", "고기요리"))

# 2. 분석 집단 세분화 (day 필터를 문자열로 수정)
# Group A: 패스트푸드 (평일 점심)
# 제공해주신 df 예시에서 day가 "수요일"이므로 문자열로 매칭해야 합니다.
fastfood_lunch <- target_2030 %>%
  filter(card_tpbuz_nm_2 == "패스트푸드",
         day %in% c("월요일", "화요일", "수요일", "목요일", "금요일"), 
         hour == 4) %>% # 규격서상 4: 11-13시 점심
  mutate(ATV = amt / cnt, group = "FastFood(Lunch)")

# Group B: 고기요리 (주말 저녁)
meat_dinner <- target_2030 %>%
  filter(card_tpbuz_nm_2 == "고기요리",
         day %in% c("토요일", "일요일"), 
         hour == 8) %>% # 규격서상 8: 19-21시 저녁
  mutate(ATV = amt / cnt, group = "Meat(Dinner)")

# 3. 데이터 통합 전 데이터 유무 확인 (중요!)
cat("패스트푸드 데이터 건수:", nrow(fastfood_lunch), "\n")
cat("고기요리 데이터 건수:", nrow(meat_dinner), "\n")

if (nrow(fastfood_lunch) > 0 & nrow(meat_dinner) > 0) {
  
  final_df <- bind_rows(fastfood_lunch, meat_dinner)
  # group 컬럼을 Factor로 변환하여 T-test가 인식하게 함
  final_df$group <- as.factor(final_df$group)
  
  # 4. 통계적 검정 수행 (Welch's T-test)
  # alternative = "greater"이므로 Meat(B) > FastFood(A)인지 확인합니다.
  # 단, T-test는 알파벳 순서(Fastfood vs Meat)로 그룹을 나누므로 
  # Meat의 평균이 더 큰지 확인하려면 적절한 대조가 필요합니다.
  t_test_result <- t.test(ATV ~ group, 
                          data = final_df, 
                          alternative = "less", # F < M 이므로 group A < group B 검정
                          var.equal = FALSE)
  
  # 5. 결과 출력
  print(t_test_result)
  
  # 6. 시각화
  ggplot(final_df, aes(x = group, y = ATV, fill = group)) +
    geom_boxplot(alpha = 0.7, outlier.alpha = 0.2) +
    scale_y_continuous(labels = scales::comma, 
                       limits = c(0, quantile(final_df$ATV, 0.99, na.rm=TRUE))) +
    labs(title = "2030 세대: 가성비 vs 보상 소비 ATV 비교",
         subtitle = paste("Welch T-test P-value:", format.pval(t_test_result$p.value)),
         x = "소비 유형", y = "건당 결제 금액(ATV)") +
    theme_minimal() +
    scale_fill_manual(values = c("#69b3a2", "#ff9999"))
  
} else {
  cat("오류: 필터링된 데이터가 부족하여 T-test를 수행할 수 없습니다.\n")
  cat("day 또는 hour 조건을 확인해 주세요.")
}
