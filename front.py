from tkinter import *
import back as bk
window = Tk()
window.title("String Matcher ")
window.geometry('500x500') 
lbl = Label(window, text="String Matcher", font=("Arial Bold", 20)).grid(column=0,row=0)
tt=Label(window, text="Text",font=("Arial",10)).grid(column=0,row=2)
ttt=Label(window, text="Pattern",font=("Arial", 10)).grid(column=0,row=3)
txt = Entry(window,width=30)
txt.grid(column=1, row=2)
    
txt1 = Entry(window,width=30)
txt1.grid(column=1, row=3)
    
head=Label(window,text="Naive Matching",font=("Arial Bold", 10)).grid(column=0,row=5)
head1=Label(window,text="Rabin-Karp",font=("Arial Bold", 10)).grid(column=0,row=8)
head2=Label(window,text="KMP Algorithm",font=("Arial Bold", 10)).grid(column=0,row=11)
head3=Label(window,text="Automata Algorithm",font=("Arial Bold", 10)).grid(column=0,row=14)
    
lsum1= Label(window,text="Index Place -",font=("Arial", 10)).grid(column=0,row=6)
lsm1= Label(window,text="Time Taken -",font=("Arial", 10)).grid(column=0,row=7)
    
lum1= Label(window,text="Index Place -",font=("Arial", 10)).grid(column=0,row=9)
l1= Label(window,text="Time Taken -",font=("Arial", 10)).grid(column=0,row=10)
    
    
kdip= Label(window,text="Index Place -",font=("Arial", 10)).grid(column=0,row=12)
kdip1= Label(window,text="Time Taken -",font=("Arial", 10)).grid(column=0,row=13)
    
        
auto= Label(window,text="Index Place -",font=("Arial", 10)).grid(column=0,row=15)
auto1= Label(window,text="Time Taken -",font=("Arial", 10)).grid(column=0,row=16)
    
lsum = Label(window, text = '_______')
lsum.grid(row=6, column=1, sticky=W, pady=4)
lsm = Label(window, text = '_______')
lsm.grid(row=7, column=1, sticky=W, pady=4) 
ls = Label(window, text = '_______')
ls.grid(row=9, column=1, sticky=W, pady=4)
l = Label(window, text = '_______')
l.grid(row=10, column=1, sticky=W, pady=4)
lkd = Label(window, text = '_______')
lkd.grid(row=12, column=1, sticky=W, pady=4)
lkd1 = Label(window, text = '_______')
lkd1.grid(row=13, column=1, sticky=W, pady=4)


lauto = Label(window, text = '_______')
lauto.grid(row=15, column=1, sticky=W, pady=4)
lauto1 = Label(window, text = '_______')
lauto1.grid(row=16, column=1, sticky=W, pady=4)

fdp=Label(window,text="Best Time is - ").grid(column=0,row=17)
fdp1=Label(window,text="______")
fdp1.grid(column=1,row=17, sticky=W, pady=4)
  
    
def clicked():
       #handle
        text=txt.get()
        patt=txt1.get()
        tm,lst=bk.NaiveSearch(patt,text)
        lsum["text"]=str(" ".join([str(x) for x in lst]))
        lsm["text"]=(tm)
        
        tm1,lst1=bk.RabinSearch(patt,text)
        ls["text"]=str(" ".join([str(x) for x in lst1]))
        l["text"]=(tm1)    
        
        tm2,lst2=bk.KMPSearch(patt,text)
        lkd["text"]=str(" ".join([str(x) for x in lst2]))
        lkd1["text"]=tm2
        
        tm3,lst3=bk.FiniteAutomatonMatcher(patt,text, len(patt))
        lauto["text"]=str(" ".join([str(x) for x in lst3]))
        lauto1["text"]=tm3

        if (tm < tm1) and (tm < tm2) and (tm < tm3):
            smallmest_num = tm
        elif (tm1 < tm) and (tm1 < tm2) and (tm1 < tm3):
            smallest_num = tm1
        elif (tm2 < tm) and (tm2 < tm1) and (tm2 < tm3):
            smallest_num = tm2
        else:
            smallest_num = tm3 
        fdp1["text"]=str(smallest_num)    
        
btn = Button(window, text="Start", command=clicked)
     
btn.grid(column=1, row=4)
     
    
window.mainloop()