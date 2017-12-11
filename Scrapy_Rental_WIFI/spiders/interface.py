# f = open('configure.txt', 'w' , encoding = 'UTF-8')

# # 隨機搜尋字
# # 隨機搜尋-修飾字
# # 保護網址
# # 關鍵字
# # 關鍵字-修飾字
# # 瀏覽頁面1-9
# # 頁面停留10-90
# # 目標網址
# # 執行時間
# f.write('抓姦推薦,徵信,抓小三,跟監,抓猴,通姦,通姦罪,通姦犯法嗎,性交,徵信社,跟拍,跟拍多少錢,通姦的定義,通姦案例,配偶與人通姦,第三者,外遇,一夜情,通姦除罪,老公外遇,老公偷吃,老公怪怪的,老婆怪怪的,外遇蒐證,婚前徵信,婚姻恐懼症,尋人,尋人啟事,工商徵信,應收帳款,文書鑑定,鑑定文書,諮詢法律問題,法律問題,公益活動,一統徵信厲害嗎,一統,一桶徵信,一統徵信,徵信必破,徵信價格,婚外情,外遇調查,抓姦訴訟求償,抓姦求償,抓姦訴訟,訴訟求償,婚前,身家調查,家暴蒐證,個人行蹤,離婚專業,反跟蹤,\n')
# f.write('推薦,廣告,\n')
# f.write('www.twgoodspy.com,www.tw07.biz,www.wanqing.org,www.topspy.org,\n')
# f.write('徵信社收費,徵信社費用,徵信社價錢,\n')
# f.write('推薦,廣告,抓姦,抓奸,好評,厲害,第一,最強,最快,徵信,台北,ptt,first,recommend,\n')
# f.write('\n')
# f.write('1,2,\n')
# f.write('10,90,\n')
# f.write('0,24,\n')
# f.close()

import tkinter as tk
import time

f = open('configure.txt', 'r' , encoding = 'UTF-8')
# 隨機搜尋字
confusion_words = f.readline().replace('\ufeff','')
confusion_words = confusion_words.split(',')
del confusion_words[-1]
#print(confusion_words)

# 隨機搜尋-修飾字
modification_words_of_confusion = f.readline()
modification_words_of_confusion = modification_words_of_confusion.split(',')
del modification_words_of_confusion[-1]
#print(modification_words_of_confusion)

# 保護網址
protect_words = f.readline()
protect_words = protect_words.split(',')
del protect_words[-1]
#print(protect_words)

# 關鍵字
keywords = f.readline()
keywords = keywords.split(',')
del keywords[-1]
#print(keywords)

# 關鍵字-修飾字
modification_words_of_keywords = f.readline()
modification_words_of_keywords = modification_words_of_keywords.split(',')
del modification_words_of_keywords[-1]
# print(modification_words_of_keywords)

# 目標網址
target_url = f.readline()
target_url = target_url.split(',')
del target_url[-1]
# print(target_url)

# 瀏覽頁面1-9
surf_page_times = f.readline()
surf_page_times = surf_page_times.split(',')
del surf_page_times[-1]
# print(surf_page_times)

# 頁面停留10-90
page_sleep_times = f.readline()
page_sleep_times = page_sleep_times.split(',')
del page_sleep_times[-1]
# print(page_sleep_times)

# 執行時間
exercise_time = f.readline()
exercise_time = exercise_time.split(',')
del exercise_time[-1]
# print(exercise_time)


f.close()

def exit():
    window.destroy()

def save_and_exit():
    f = open('configure.txt', 'w' , encoding = 'UTF-8')
    f.write(var1_2.get()[1:-1].replace("'" , '').replace(" " , '')+',\n')
    f.write(var2_2.get()[1:-1].replace("'" , '').replace(" " , '')+',\n')
    f.write(var3_2.get()[1:-1].replace("'" , '').replace(" " , '')+',\n')
    f.write(var4_2.get()[1:-1].replace("'" , '').replace(" " , '')+',\n')
    f.write(var5_2.get()[1:-1].replace("'" , '').replace(" " , '')+',\n')
    f.write(var6_2.get()[1:-1].replace("'" , '').replace(" " , '')+',\n')
    f.write(en7_1.get()+','+en7_2.get()+',\n')
    f.write(en8_1.get()+','+en8_2.get()+',\n')
    f.write(en9_1.get()+','+en9_2.get()+',\n')
    f.close()
    exit()

def add_keyword(en,lb):
    if(en.get() !=''):
        lb.insert(0,en.get())
        en.delete(0,tk.END)
#         print(var1_2.get())
        
def delete_keyword(lb):
    select_keyword = lb.curselection()
    if(select_keyword):
        lb.delete(select_keyword[0])
        lb.select_set(select_keyword[0])
        
window = tk.Tk()
window.title('my window')
window.geometry('1100x750+650+100')
padxy = 10

#frame left
frl = tk.Frame(window)
frl.grid(row=0,column=0)

# frame1
fr1 = tk.Frame(frl)
fr1.grid(row=0,column=0,padx=padxy,pady=padxy)

var1_1 = tk.StringVar()
var1_1.set('隨機搜尋字')
lab1_1 = tk.Label(fr1, textvariable = var1_1)
lab1_1.grid(row=0,column=0,columnspan=2,padx=padxy,pady=padxy)

en1 = tk.Entry(fr1)
en1.grid(row=1,column=0,columnspan=2,padx=padxy,pady=padxy)

btn1_1 = tk.Button(fr1, text = '增加',command = lambda : add_keyword(en1,lb1))
btn1_1.grid(row=2,column=0,padx=padxy,pady=padxy)
btn1_2 = tk.Button(fr1, text = '刪除',command = lambda : delete_keyword(lb1))
btn1_2.grid(row=2,column=1,padx=padxy,pady=padxy)

var1_2 = tk.StringVar()
var1_2.set(confusion_words)
lb1 = tk.Listbox(fr1,listvariable=var1_2)
lb1.grid(row=3,column=0,columnspan=3,padx=padxy,pady=padxy)
sc1 = tk.Scrollbar(fr1, orient="vertical")
sc1.grid(row=3,column=3,padx=padxy,pady=padxy)
lb1.config(yscrollcommand=sc1.set)
sc1.config(command=lb1.yview)

# frame2
fr2 = tk.Frame(frl)
fr2.grid(row=0,column=1,padx=padxy,pady=padxy)

var2_1 = tk.StringVar()
var2_1.set('隨機搜尋-修飾字')
lab2_1 = tk.Label(fr2, textvariable = var2_1)
lab2_1.grid(row=0,column=0,columnspan=2,padx=padxy,pady=padxy)

en2 = tk.Entry(fr2)
en2.grid(row=1,column=0,columnspan=2,padx=padxy,pady=padxy)

btn2_1 = tk.Button(fr2, text = '增加',command = lambda : add_keyword(en2,lb2))
btn2_1.grid(row=2,column=0,padx=padxy,pady=padxy)
btn2_2 = tk.Button(fr2, text = '刪除',command = lambda : delete_keyword(lb2))
btn2_2.grid(row=2,column=1,padx=padxy,pady=padxy)

var2_2 = tk.StringVar()
var2_2.set(modification_words_of_confusion)
lb2 = tk.Listbox(fr2,listvariable=var2_2)
lb2.grid(row=3,column=0,columnspan=3,padx=padxy,pady=padxy)
sc2 = tk.Scrollbar(fr2, orient="vertical")
sc2.grid(row=3,column=3,padx=padxy,pady=padxy)
lb2.config(yscrollcommand=sc2.set)
sc2.config(command=lb2.yview)

# frame3
fr3 = tk.Frame(frl)
fr3.grid(row=0,column=2,padx=padxy,pady=padxy)

var3_1 = tk.StringVar()
var3_1.set('保護網址')
lab3_1 = tk.Label(fr3, textvariable = var3_1)
lab3_1.grid(row=0,column=0,columnspan=2,padx=padxy,pady=padxy)

en3 = tk.Entry(fr3)
en3.grid(row=1,column=0,columnspan=2,padx=padxy,pady=padxy)

btn3_1 = tk.Button(fr3, text = '增加',command = lambda : add_keyword(en3,lb3))
btn3_1.grid(row=2,column=0,padx=padxy,pady=padxy)
btn3_2 = tk.Button(fr3, text = '刪除',command = lambda : delete_keyword(lb3))
btn3_2.grid(row=2,column=1,padx=padxy,pady=padxy)

var3_2 = tk.StringVar()
var3_2.set(protect_words)
lb3 = tk.Listbox(fr3,listvariable=var3_2)
lb3.grid(row=3,column=0,columnspan=3,padx=padxy,pady=padxy)
sc3 = tk.Scrollbar(fr3, orient="vertical")
sc3.grid(row=3,column=3,padx=padxy,pady=padxy)
lb3.config(yscrollcommand=sc3.set)
sc3.config(command=lb3.yview)

# frame4
fr4 = tk.Frame(frl)
fr4.grid(row=1,column=0,padx=padxy,pady=padxy)

var4_1 = tk.StringVar()
var4_1.set('關鍵字')
lab4_1 = tk.Label(fr4, textvariable = var4_1)
lab4_1.grid(row=0,column=0,columnspan=2,padx=padxy,pady=padxy)

en4 = tk.Entry(fr4)
en4.grid(row=1,column=0,columnspan=2,padx=padxy,pady=padxy)

btn4_1 = tk.Button(fr4, text = '增加',command = lambda : add_keyword(en4,lb4))
btn4_1.grid(row=2,column=0,padx=padxy,pady=padxy)
btn4_2 = tk.Button(fr4, text = '刪除',command = lambda : delete_keyword(lb4))
btn4_2.grid(row=2,column=1,padx=padxy,pady=padxy)

var4_2 = tk.StringVar()
var4_2.set(keywords)
lb4 = tk.Listbox(fr4,listvariable=var4_2)
lb4.grid(row=3,column=0,columnspan=3,padx=padxy,pady=padxy)
sc4 = tk.Scrollbar(fr4, orient="vertical")
sc4.grid(row=3,column=3,padx=padxy,pady=padxy)
lb4.config(yscrollcommand=sc4.set)
sc4.config(command=lb4.yview)

#frame 5
fr5 = tk.Frame(frl)
fr5.grid(row=1,column=1,padx=padxy,pady=padxy)

var5_1 = tk.StringVar()
var5_1.set('關鍵字-修飾字')
lab5_1 = tk.Label(fr5, textvariable = var5_1)
lab5_1.grid(row=0,column=0,columnspan=2,padx=padxy,pady=padxy)

en5 = tk.Entry(fr5)
en5.grid(row=1,column=0,columnspan=2,padx=padxy,pady=padxy)

btn5_1 = tk.Button(fr5, text = '增加',command = lambda : add_keyword(en5,lb5))
btn5_1.grid(row=2,column=0,padx=padxy,pady=padxy)
btn5_2 = tk.Button(fr5, text = '刪除',command = lambda : delete_keyword(lb5))
btn5_2.grid(row=2,column=1,padx=padxy,pady=padxy)

var5_2 = tk.StringVar()
var5_2.set(modification_words_of_keywords)
lb5 = tk.Listbox(fr5,listvariable=var5_2)
lb5.grid(row=3,column=0,columnspan=3,padx=padxy,pady=padxy)
sc5 = tk.Scrollbar(fr5, orient="vertical")
sc5.grid(row=3,column=3,padx=padxy,pady=padxy)
lb5.config(yscrollcommand=sc5.set)
sc5.config(command=lb4.yview)

#frame 6
fr6 = tk.Frame(frl)
fr6.grid(row=1,column=2,padx=padxy,pady=padxy)

var6_1 = tk.StringVar()
var6_1.set('目標網址')
lab6_1 = tk.Label(fr6, textvariable = var6_1)
lab6_1.grid(row=0,column=0,columnspan=2,padx=padxy,pady=padxy)

en6 = tk.Entry(fr6)
en6.grid(row=1,column=0,columnspan=2,padx=padxy,pady=padxy)

btn6_1 = tk.Button(fr6, text = '增加',command = lambda : add_keyword(en6,lb6))
btn6_1.grid(row=2,column=0,padx=padxy,pady=padxy)
btn6_2 = tk.Button(fr6, text = '刪除',command = lambda : delete_keyword(lb6))
btn6_2.grid(row=2,column=1,padx=padxy,pady=padxy)

var6_2 = tk.StringVar()
var6_2.set(target_url)
lb6 = tk.Listbox(fr6,listvariable=var6_2)
lb6.grid(row=3,column=0,columnspan=3,padx=padxy,pady=padxy)
sc6 = tk.Scrollbar(fr6, orient="vertical")
sc6.grid(row=3,column=3,padx=padxy,pady=padxy)
lb6.config(yscrollcommand=sc6.set)
sc6.config(command=lb4.yview)

#frame right
frr = tk.Frame(window)
frr.grid(row=0,column=1)

#frame 7
fr7 = tk.Frame(frr)
fr7.grid(row=0,column=0,padx=padxy,pady=padxy)

var7_1 = tk.StringVar()
var7_1.set('瀏覽頁面次數')
lab7_1 = tk.Label(fr7, textvariable = var7_1)
lab7_1.grid(row=0,column=0,columnspan=3,padx=padxy,pady=padxy)

en7_1 = tk.Entry(fr7,width=5)
en7_1.insert(0,surf_page_times[0])
en7_1.grid(row=1,column=0,padx=padxy,pady=padxy)

var7_2 = tk.StringVar()
var7_2.set('-')
lab7_2 = tk.Label(fr7, textvariable = var7_2)
lab7_2.grid(row=1,column=1,padx=padxy,pady=padxy)

en7_2 = tk.Entry(fr7,width=5)
en7_2.insert(0,surf_page_times[1])
en7_2.grid(row=1,column=2,padx=padxy,pady=padxy)

#frame 8
fr8 = tk.Frame(frr)
fr8.grid(row=1,column=0,padx=padxy,pady=padxy)

var8_1 = tk.StringVar()
var8_1.set('頁面停留秒數')
lab8_1 = tk.Label(fr8, textvariable = var8_1)
lab8_1.grid(row=0,column=0,columnspan=3,padx=padxy,pady=padxy)

en8_1 = tk.Entry(fr8,width=5)
en8_1.insert(0,page_sleep_times[0])
en8_1.grid(row=1,column=0,padx=padxy,pady=padxy)

var8_2 = tk.StringVar()
var8_2.set('-')
lab8_2 = tk.Label(fr8, textvariable = var8_2)
lab8_2.grid(row=1,column=1,padx=padxy,pady=padxy)

en8_2 = tk.Entry(fr8,width=5)
en8_2.insert(0,page_sleep_times[1])
en8_2.grid(row=1,column=2,padx=padxy,pady=padxy)

#frame 9
fr9 = tk.Frame(frr)
fr9.grid(row=2,column=0,padx=padxy,pady=padxy)

var9_1 = tk.StringVar()
var9_1.set('執行時間')
lab9_1 = tk.Label(fr9, textvariable = var9_1)
lab9_1.grid(row=0,column=0,columnspan=3,padx=padxy,pady=padxy)

en9_1 = tk.Entry(fr9,width=5)
en9_1.insert(0,exercise_time[0])
en9_1.grid(row=1,column=0,padx=padxy,pady=padxy)

var9_2 = tk.StringVar()
var9_2.set('-')
lab9_2 = tk.Label(fr9, textvariable = var9_2)
lab9_2.grid(row=1,column=1,padx=padxy,pady=padxy)

en9_2 = tk.Entry(fr9,width=5)
en9_2.insert(0,exercise_time[1])
en9_2.grid(row=1,column=2,padx=padxy,pady=padxy)

#frame 0

fr_0 = tk.Frame(frr)
fr_0.grid(row=3,column=0,padx=padxy,pady=padxy)
btn0_1 = tk.Button(fr_0, text = '保存並退出',command = save_and_exit)
btn0_1.grid(row=0,column=0,padx=padxy,pady=padxy)
btn0_2 = tk.Button(fr_0, text = '不儲存離開',command = exit)
btn0_2.grid(row=0,column=1,padx=padxy,pady=150)

#显示主窗口
window.mainloop()