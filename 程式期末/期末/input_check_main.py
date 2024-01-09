def check(enter):#輸入="exit"直接關閉程式
    if enter == 'exit':
        exit()
    
    elif enter.isdigit() and enter != 0:#檢查輸入是否為數字 且 不能為0
        enter = int(enter)
        return enter
    else: #輸入格式錯誤
        return  print('請輸入正確選項')
    

if __name__ == "__main__":
    print(check(input(':')))