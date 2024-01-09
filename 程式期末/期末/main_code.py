import record  #記帳模組
import input_check_main #專屬主程式的輸入檢查模組
import print_option #輸出功能清單
import select_over #檢查輸入的選項是否超出功能
import filter #查詢模組


modes = ['print "exit" to quit', '登帳', '查詢', ]  #功能清單
record_list = [] #登帳紀錄

while True : #執行[選擇功能]
    print_option.print_option(modes)#輸出[功能清單]

    selection = input_check_main.check(input('select:'))#檢查[輸入]是否要退出，輸入是否是數字，如果是數字，回傳
    
    if select_over.select(selection, modes):#檢查[輸入]的數字是否超過選項
        break

    elif selection == 1:#登帳功能
        record_list.append(record.record_transaction()) #呼叫登帳程式
        print("\n記錄完成，以下是您的記錄:")
        print(record_list[-1], '\n') #[輸出]新增的紀錄
        
    elif selection == 2: #查詢功能
        print(record_list, '\n') #輸出所有登帳紀錄
        a = filter.filter(record_list) #呼叫查詢模組
        if a != None:
            print('以下是篩選紀錄')
            for b in a:
                print(b) 
            print('\n')
