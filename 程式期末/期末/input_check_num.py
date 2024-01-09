def check(enter):#輸入="exit"直接關閉程式
    if enter == 'exit':
        exit()

    elif enter == 're' or enter == '':#輸入=re可以回上個選擇
        return enter
    
    elif enter.isdigit() and enter != 0:#輸入是否為數字
        enter = int(enter)
        return enter
    else:
        return print('請輸入正確格式')
    

if __name__ == "__main__":
    check(input(':'))