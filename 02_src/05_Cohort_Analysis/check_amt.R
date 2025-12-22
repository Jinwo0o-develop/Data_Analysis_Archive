library(arrow) # read_parquet를 위해 패키지 설치
library(dplyr)

# 파일 로드
file_path <- "C:/Users/owner/Desktop/Git/00_Common_Data/Master_Sales_2025_Total.parquet"
df <- read_parquet(file_path)

# 코드값(Code) 기준 필터링
# Age 3 = '20대', Hour 8 = '19-21시'
validation_df <- df %>%
  filter(
    card_tpbuz_nm_1 == "음식",
    card_tpbuz_nm_2 == "고기요리",
    hour == 8,    # '19-21시'에 해당하는 코드
    age == 3,     # '20대'에 해당하는 코드
    sex == "M"    
  )

# 3. 결과 검증
total_sales_check <- sum(validation_df$amt, na.rm = TRUE)
options(scipen = 999)

print(paste0("매핑 코드 적용 후 검증된 매출 총액: ", total_sales_check, "원"))