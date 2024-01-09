import datetime #時間模組
import date_input #輸入時間的模組
import input_check_num #檢查輸入是否是數字的模組

def filter(date): #將記帳資料傳進模組

    result_type = []        #篩選完[項目]過後的結果
    result_category = []    #篩選完[種類]過後的結果
    result_date = []        #篩選完[日期]過後的結果
    result_amount = []      #篩選完[金額]過後的結果
    result = [] #最終結果

    #篩選項目
    query_input_type = input('支出/收入:') #[輸入]查詢[項目]的資訊

    for found_date in date: #將記帳資料一個一個拉出來檢查
        if query_input_type == found_date['type'] or query_input_type == '':
            #如果[輸入]查詢[項目]的資訊 == 記帳資料key['type']的話 或是 [輸入]查詢[項目]的資訊為空
            result_type.append(found_date) #將資料新增進 篩選完[項目]過後的結果清單中

    if result_type == []: #如果沒有找到任何結果，回傳查無資料
        return print('查無資料')
    
    #篩選種類
    query_input_category = input('種類:') #[輸入]查詢[種類]的資訊

    for found_date in result_type: #將篩選[項目]過後的資料一個一個拉出來
        if query_input_category == found_date['category'] or query_input_category == '':
            #如果[輸入]查詢[種類]的資訊 == 記帳資料key['category']的話 或是 [輸入]查詢[種類]的資訊為空
            result_category.append(found_date) #將資料新增進 篩選完[種類]過後的結果清單中

    if result_category == []: #如果沒有找到任何結果，回傳查無資料
        return print('查無資料')

    #篩選日期
    query_input_date = date_input.validate_date() #呼叫[輸入]日期模組
    if query_input_date == '': #如果[輸入]為空
        result_date = result_category #篩選完[種類]過後的結果 放入 篩選完[日期]過後的結果
    else: #[輸入]不為空且[輸入]正確
        for found_date in result_category: #將篩選[種類]過後的資料一個一個拉出來
            if query_input_date == found_date['date'] :
                #如果[輸入]查詢[日期]的資訊 == 記帳資料key['date']的話
                result_date.append(found_date) #將資料新增進 篩選完[日期]過後的結果清單中

    if result_date == []: #如果沒有找到任何結果，回傳查無資料
        return print('查無資料')

    #篩選金額
    query_input_amount = input_check_num.check(input('金額:')) #呼叫檢查[輸入]是否是數字的模組
    for found_date in result_date: #將篩選[日期]過後的資料一個一個拉出來
        if query_input_amount == found_date['amount'] or query_input_amount == '':
            #如果[輸入]查詢[金額]的資訊 == 記帳資料key['amount']的話 或是 [輸入]查詢[金額]的資訊為空
            result_amount.append(found_date) #將資料新增進 篩選完[金額]過後的結果清單中

    if result_amount == []: #如果沒有找到任何結果，回傳查無資料
        return print('查無資料')

    #篩選備註
    query_input_note = input('備註:') #[輸入]查詢[備註]的資訊
    for found_date in result_amount: #將篩選[金額]過後的資料一個一個拉出來
        if query_input_note == found_date['note'] or query_input_note == '':
            #如果[輸入]查詢[備註]的資訊 == 記帳資料key['note']的話 或是 [輸入]查詢[備註]的資訊為空
            result.append(found_date) #將資料新增進 結果清單中

    if result == []: #如果沒有找到任何結果，回傳查無資料
        return print('查無資料')

    return result #回傳結果清單


if __name__ == '__main__':
    transaction_data1 = {'type': '支出', 'category': '食', 'date': datetime.date(2005, 8, 25), 'amount': 500.0, 'note': '無'}
    transaction_data2 = {'type': '收入', 'category': '投資', 'date': datetime.date(2005, 9, 25), 'amount': 50000.0, 'note': '好吃'}
    transaction_data3 = {'type': '支出', 'category': '衣', 'date': datetime.date(2005, 9, 25), 'amount': 500.0, 'note': '棒'}
    transaction_data4 = {'type': '收入', 'category': '食', 'date': datetime.date(2004, 9, 25), 'amount': 50056.0, 'note': '00'}
    transaction_data5 = {'type': '支出', 'category': '零用錢', 'date': datetime.date(2005, 8, 25), 'amount': 55600.0, 'note': '好吃'}
    record_date = [transaction_data1, transaction_data2, transaction_data3, transaction_data4, transaction_data5]

    print(filter(record_date))