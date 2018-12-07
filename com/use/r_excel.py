#coding=utf-8
'''
Created on 2018年9月28日

@author: Pan
'''

import xlrd

#filename = 'F:\\desktop\\2018\\HRMIS\\data-conversion\\export.xlsx' 
#sql = ' update temp_data_conversion set vtc_emp_id = {0:0.0f} where emp_id = {1:0.0f} and vtcrn = {2:0.0f} and start_date = to_date(\'{3:10s}\', \'yyyy-MM-dd\'); '
filename='F:\\temp\\temp.xlsx'
sql = 'update leave_ent le set le.leave_earn_rate_desc = \'{0}\' where le.leave_ent_id = {1:0.0f} ;'
def open_excel(file= 'file.xls'):
    try:
        print(file)
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

def excel_table_byname(file= filename ,colnameindex=0,by_name='Sheet1'):#修改自己路径
     data = open_excel(file)
     print(data)
     table = data.sheet_by_name(by_name) #获得表格
     nrows = table.nrows  # 拿到总共行数
     colnames = table.row_values(colnameindex)  # 某一行数据 ['姓名', '用户名', '联系方式', '密码']
     list = []
     for rownum in range(1, nrows): #也就是从Excel第二行开始，第一行表头不算
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                 app[colnames[i]] = row[i] #表头与数据对应
             list.append(app)
     return list

def main():
    tables = excel_table_byname()
    for row in tables:
        print(sql.format(row['LEAVE_EARN_RATE_DESC'], float(row['LEAVE_ENT_ID'])))
if __name__ =="__main__":
    main()
