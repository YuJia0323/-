from datetime import datetime, date #引入時間函式
#輸入時間 並且檢查輸入有沒有錯誤
def validate_date():
    while True:
        input_date = input("請輸入日期 (yyyy/mm/dd): ") #輸入日期

        if input_date == 're' or input_date == '': 
            #使用者想回上個選項 或是 輸入為空(再查詢程式會使用到)
            return input_date #回傳輸入資料
        try:
            # 將輸入的日期字符串解析為 datetime 對象
            user_date = datetime.strptime(input_date, "%Y/%m/%d").date()
            # 獲取今天的日期
            today = date.today()

            # 檢查用戶輸入的日期是否在今天之前
            if user_date <= today:
                return user_date
            else:
                print(f"日期 {input_date} 不是有效日期。")

        except ValueError: #輸入格式錯誤
            print(f"{input_date} 不是有效的日期。")



if __name__ == "__main__":
    validate_date()
