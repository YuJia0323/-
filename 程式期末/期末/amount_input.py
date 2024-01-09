def amount(): #輸入金額模組
    while True:
        amount = input("請輸入金額: ") #輸入金額
        if  amount== 're' or amount.isdigit(): #使用者想回上個選項 或是 輸入的資料是數字
            return amount #回傳輸入的資料
        else: #格式不正確，再輸入一次
            print('格式不對')
            break
if __name__ == "__main__":
 print(amount())