import tkinter as tk
import time

def exit():
    window.destroy()

def add_keyword():
    if(en1.get() !=''):
        lb1.insert(0,en1.get())
def delete_keyword():
    select_keyword = lb1.curselection()
    if(select_keyword):
        lb1.delete(select_keyword[0])
        
window = tk.Tk()
window.title('my window')
window.geometry('800x600')

fr1 = tk.Frame(window)
fr1.grid(row=0,column=0)

var1_1 = tk.StringVar()
var1_1.set('關鍵字')
lab1_1 = tk.Label(fr1, width = 10, textvariable = var1_1,bg = 'yellow')
lab1_1.grid(row=0,column=0,columnspan=2)

en1 = tk.Entry(fr1, width = 15)
en1.grid(row=1,column=0,columnspan=2)

btn1_1 = tk.Button(fr1,width = 10, text = '增加',command = add_keyword)
btn1_1.grid(row=2,column=0)
btn1_2 = tk.Button(fr1,width = 10, text = '刪除',command = delete_keyword)
btn1_2.grid(row=2,column=1)

var1_2 = tk.StringVar()
var1_2.set(('11','22','33'))
lb1 = tk.Listbox(fr1,width = 20,listvariable=var1_2)
lb1.grid(row=3,column=0,columnspan=3)
sc1 = tk.Scrollbar(fr1, orient="vertical")
sc1.grid(row=3,column=3)
lb1.config(yscrollcommand=sc1.set)
sc1.config(command=lb1.yview)

# var1 = tk.StringVar()    #创建变量
# l =tk.Label(window,bg='yellow',width=4,textvariable=var1)
# l.pack()

# def print_selection():
#     value = lb.get(lb.curselection())   #获取当前选中的文本
#     var1.set(value)     #为label设置值
    
# b1 = tk.Button(window, text='print selection', width=15,
#               height=2, command=print_selection)
# b1.pack()

# var2 = tk.StringVar()
# var2.set((11,22,33,44)) #为变量设置值

# #创建Listbox

# lb = tk.Listbox(window, listvariable=var2)  #将var2的值赋给Listbox

# #创建一个list并将值循环添加到Listbox控件中
# list_items = [1,2,3,4]
# for item in list_items:
#     lb.insert('end', item)  #从最后一个位置开始加入值
# lb.insert(1, 'first')       #在第一个位置加入'first'字符
# lb.insert(2, 'second')      #在第二个位置加入'second'字符
# lb.delete(2)                #删除第二个位置的字符
# lb.pack()

#显示主窗口
window.mainloop()

# time.sleep(10)
# window.destroy()