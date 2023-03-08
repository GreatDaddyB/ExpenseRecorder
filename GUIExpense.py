from tkinter import *
from tkinter import ttk,messagebox
from datetime import datetime
import csv


GUI = Tk()
GUI.title('โปรแกรมทดสอบเก็บข้อมูล')
GUI.geometry('720x700+500+50')

############## MENU #################
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Google Sheet')
# Help menu
def About():
    messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมทดสอบ\nสามารถ Donate ได้')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
# Donate menu
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)



#####################################

# Tab
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab) # ใส่ ,width=400,height=400 ได้
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1) #fill=x หรือ y ได้

icon_t1 = PhotoImage(file='t1_expense.png') # ใส่รูป
icon_t2 = PhotoImage(file='t2_expenselist.png') #.subsample(2) ใช้สำหรับย่อรูป

Tab.add(T1,text=f'{"เพิ่มค่าใช้จ่าย": ^{30}}',image=icon_t1,compound='top')
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด": ^{30}}',image=icon_t2,compound='top')
# Tab 1 ----------------------------------------
F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()


Font1 = (None,20)

# image
main_icon = PhotoImage(file='icon_money.png')

mainicon = Label(F1,image=main_icon)
mainicon.pack()

# 1
L = ttk.Label(F1,text='รายการ',font=Font1)
L.pack()
v_expense = StringVar()
E1 = ttk.Entry(F1,textvariable=v_expense,font=Font1)
E1.pack()

# 2
L = ttk.Label(F1,text='ราคา',font=Font1)
L.pack()
v_price = StringVar()
E2 = ttk.Entry(F1,textvariable=v_price,font=Font1)
E2.pack()

# 3
L = ttk.Label(F1,text='จำนวน',font=Font1)
L.pack()
v_qty = StringVar()
E3 = ttk.Entry(F1,textvariable=v_qty,font=Font1)
E3.pack()

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์' }

# Function
def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    qty = v_qty.get()


    if expense =='' or price =='' or qty =='':
        print('No Data')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลให้ครบทุกช่อง')
        return

    try:
        total = float(price)*float(qty)
        print('รายการ: {} ราคา {} บาท\nจำนวน {} ชิ้น สุทธิ {} บาท'.format(expense, price, qty, total))
        text = 'รายการ: {} ราคา {} บาท\nจำนวน {} ชิ้น สุทธิ {} บาท'.format(expense, price, qty, total)
        v_result.set(text)
        v_expense.set('')
        v_price.set('')
        v_qty.set('')

        today = datetime.now().strftime('%a') 
        print(today)   
        stamp = datetime.now()
        dt = stamp.strftime('{}-%Y-%m-%d %H:%M:%S'.format(days[today]))
        transactionid = stamp.strftime('%Y%m%d%H%M%f')
        with open('vdata.csv','a',encoding='utf=8',newline='') as f:
            fw = csv.writer(f)
            data = [transactionid,dt,expense,price,qty,total]
            fw.writerow(data)
        E1.focus()
        update_table()
        #update_record()
    except:
        print('ERROR')
        #messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        #messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_expense.set('')
        v_price.set('')
        v_qty.set('')
# Button
icon_b1 = PhotoImage(file='b1_save.png').subsample(2)

B1 = ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command=Save)
B1.pack(ipadx=50,ipady=10,pady=20)

GUI.bind('<Return>',Save)

v_result = StringVar()
v_result.set('--------ผลลัพธ์-------')
result = ttk.Label(F1,textvariable=v_result,font=Font1,foreground='green')
result.pack(pady=20)

# Tab 2 -----------------------------------------------
F2 = Frame(T2)
F2.pack()

def read_csv():
    with open('vdata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data
        # print(data)
        # print('-----')
        # print(data[0][0])
        # for a,b,c,d,e in data:
        #     print(d)
# rs = read_csv()
# print(rs)

# text
# def update_record():
#     getdata = read_csv()
#     v_allrecord.set('')
#     text = ''
#     for d in getdata:
#         txt = '{}---{}---{}---{}---{}\n'.format(d[0],d[1],d[2],d[3],d[4])
#         text = text + txt

#     v_allrecord.set(text)

# v_allrecord = StringVar()
# v_allrecord.set('--------All Record--------')
# Allreccord = ttk.Label(T2,textvariable=v_allrecord,font=(None,15),foreground='red')
# Allreccord.pack()


# table
L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=Font1)
L.pack(pady=20)
header = ['รหัสรายการ','วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=20)
resulttable.pack() 

# วิธีแบบแรก
# for hd in range(len(header)):
#     resulttable.heading(header[hd],text=header[hd])

# วิธีแบบหลัง
for hd in header:
    resulttable.heading(hd,text=hd)

# ตั้งค่าความกว้าง
headerwidth = [120,150,170,80,80,80]

for hd,w in zip(header,headerwidth):
    resulttable.column(hd,width=w)

alltransaction = {}

def update_table():
    resulttable.delete(*resulttable.get_children())
    try:
        data = read_csv()
        for d in data:
            # Creat transaction data
            alltransaction[d[0]] = d # d[0] = transactionid
            resulttable.insert('',0,value=d) # ใช้ 0 หรือ 'end'
        print(alltransaction)

    except:
        print('No File')

update_table()
#update_record()

def updateCSV():
    with open('vdata.csv','w',newline='',encoding='utf-8') as f:
        fw = csv.writer(f)
        # เตรียมข้อมูลจาก alltransaction ให้กลายเป็น list
        data = list(alltransaction.values())
        fw.writerows(data) # maltiple line from neasted list [[],[],[]]
        print('Table was updated.')

# ปุ่ม Delete
def DeleteRecord(event=None):
    check = messagebox.askyesno('Confirm?','คุณต้องการลบข้อมูลใช่หรือไม่')
    print('YES/NO',check)
    if check == True:
        print('delete')
        select = resulttable.selection()
        #print(select)
        data = resulttable.item(select)
        data = data['values']
        transactionid = data[0]
        #print(transactionid)
        del alltransaction[str(transactionid)]
        #print(alltransaction)
        updateCSV()
        update_table()
    else:
        print('Cancle')

BDelete1 = ttk.Button(T2,text='Delete',command=DeleteRecord)
BDelete1.place(x=50,y=550)

resulttable.bind('<Delete>',DeleteRecord)

GUI.bind('<Tab>', lambda x: E2.focus())
GUI.mainloop()
