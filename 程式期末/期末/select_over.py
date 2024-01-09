def select(receive, option):
    
    if receive >= len(option):#檢查輸入的數字是否超過選項數
        print('請輸入正確的選項。')
        return True
    

if __name__ == '__main__':
    a = int(input(':'))
    b = [1, 2, 3]
    print(select(a, b))
    