import input_check_num #檢查使用者是否要退出，輸入是否是數字，如果是數字，回傳
import print_option #輸出目前有甚麼功能
import select_over #檢查輸入選項是否超出清單
import date_amount_note #輸入日期金額備註

def record_transaction(): 
    modes = ['print "re" to return\nprint "exit" to quit', '支出', '收入']#記帳功能清單
    while True:    #收入支出選擇

        print_option.print_option(modes) #輸出記帳功能清單
        
        transaction_type = input_check_num.check((input("select:")))#檢查使用者是否要退出，輸入是否是數字，如果是數字，回傳
        if transaction_type == 're':#使用者想回上頁
            break #回到主選單

        if select_over.select(transaction_type, modes): #選擇是否超出選項
            #超出
            break #回到主選單

        if transaction_type == 1:#選擇記錄支出
            while True: #支出類別選擇
                categoreys = ['print "re" to return\nprint "exit" to quit', '食', '衣', '住', '行', '娛樂', '其他']#支出類別清單
                print_option.print_option(categoreys) #輸出支出類別清單
                
                category = input_check_num.check(input("select:"))#檢查使用者是否要退出，輸入是否是數字，如果是數字，回傳

                if category == 're': #使用者想回上個選擇(收入支出選擇)
                    break #回到收入支出選擇
                elif select_over.select(category, categoreys): #選擇是否超出選項
                    #超出
                    break #回到選擇紀錄收入還是支出
                try:
                    date, amount, note = date_amount_note.date_amount_note() #輸入日期金額備註
                    if date: #如果date為空，回到選擇支出類別，因為在date輸入re的話，date不會有資料
                        transaction_data = {                        #將資料放入字典中
                            'type': modes[transaction_type],        #支出/收入選項
                            'category': categoreys[category],       #種類
                            'date': date,                           #日期
                            'amount': amount,                       #金額
                            'note': note                            #備註
                        }
                    # print("\n記錄完成，以下是您的記錄:")
                        print(transaction_data)
                    return transaction_data

                except TypeError: #如果date為空，回到選擇支出類別，因為在date輸入re的話，date不會有資料，會出現錯誤代碼typeerror，進入except區塊
                    pass #不做任何事，繼續while迴圈，回到選擇支出類別

                
        if transaction_type == 2:#選擇記錄收入
            while True: 
                categoreys = ['print "re" to return\nprint "exit" to quit', '薪資', '零用錢', '投資收入', '其他']#收入類別
                print_option.print_option(categoreys)#輸出收入類別清單
                
                category = input_check_num.check(input("select:"))#檢查使用者是否要退出，輸入是否是數字，如果是數字，回傳
                if category == 're':#使用者想回上個選擇(收入支出選擇)
                    break 
                elif select_over.select(category, categoreys):#選擇是否超出選項
                    break
                #輸入日期金額備註
                try:
                    date, amount, note = date_amount_note.date_amount_note() #輸入日期金額備註
                    if date: #如果date為空，回到選擇支出類別，因為在date輸入re的話，date不會有資料
                        transaction_data = {                        #將資料放入字典中
                            'type': modes[transaction_type],        #支出/收入選項
                            'date': date,                           #日期
                            'category': categoreys[category],       #種類
                            'amount': amount,                       #金額
                            'note': note                            #備註
                        }
                    # print("\n記錄完成，以下是您的記錄:")
                    # print(transaction_data)
                        print(transaction_data)
                    return transaction_data

                except TypeError: #如果date為空，回到選擇支出類別，因為在date輸入re的話，date不會有資料，會出現錯誤代碼typeerror，進入except區塊
                    pass #不做任何事，繼續while迴圈，回到選擇支出類別

if __name__ == "__main__":
    record_transaction()
