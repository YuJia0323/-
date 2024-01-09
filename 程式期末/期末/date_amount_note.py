import input_check_num #檢查輸入是否要退出，輸入是否是數字，如果是數字，回傳
import date_input
import amount_input
#輸入日期、金額、備註
def date_amount_note():
    while True:
        date = date_input.validate_date() #呼叫輸入日期模組
        if date == 're': #使用者想回上個選項
            break

        while True:
            amount = amount_input.amount() #呼叫輸入金額模組
            if amount == 're': #使用者想回上個選項
                break #回上個選項

            while True:
                note = input("請輸入備註: ") #輸入備註
                if note == 're': #回上個選項
                    break
                return date, amount, note #回傳日期、金額、備註
        
if __name__ == "__main__":
    a, b, c = date_amount_note()
    print(a, b, c)