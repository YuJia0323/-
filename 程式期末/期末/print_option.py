def print_option(option):  #輸出功能選單
    num = len(option)  #取得選單長度
    print(option[0])   #單獨輸出第零項
    for i in range(1, num): #讓i從1開始，在選單項目長度停止
        print(f'{i}.{option[i]}')  #輸出數字i。輸出"."。輸出在功能選單中的第i項。 

if __name__ == "__main__":
    a = [0, 1, 2]
    print_option(a)