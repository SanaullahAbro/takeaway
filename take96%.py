from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import math,random,os
import random
import time
import datetime
import tempfile
import sqlite3

##############################THE GREAT THE GREATE



     
######################################F1 BUTTON#########################################
####F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F
######################################## F  1  ##############################################
##############################L O G I N##################################################
class Main_Window:
    def __init__(self):
        self.db_name = 'win.db'
        self.root = Tk()
        self.fullScreenState = False
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)

        self.root.bind("<Button-1>", self.ttoal_gen)

        self.root.bind("<Button-3>", self.token_dataarea)
          
        self.root.bind("<Button-2>", self.clear_bill)
        
        self.root.geometry('1350x750+0+0')
        self.root.config(bg ='skyblue4')
        self.Frame2 = Frame(self.root, bg ='skyblue4',relief='ridge',bd=6)
        self.Frame2.place(x=0,y=0,height=60,width=1000)
        self.Frame3 = Frame(self.root,bg ='skyblue4',relief='ridge',bd=10)
        self.Frame3.place(x=0,y=60,height=680,width=1000)
        self.Frame4 = Frame(self.root,bg ='skyblue4',relief='ridge',bd=10)
        self.Frame4.place(x=950,y=630,height=100,width=350)
        self.F5 = Frame(self.root,bg ='black',relief='ridge',bd=6)
        self.F5.place(x=2000,y=0,height=500,width=400)
        
        self.bill_title = Label(self.F5,text="Print Area",bg='silver',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(self.F5,bg ='silver',orient= VERTICAL)
        self.textarea=Text(self.F5,bg ='skyblue4',relief='ridge',bd=6,fg ='white',yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

########################TOKEN POPUP
########################TOKEN POPUP  
        self.tokenF6 = Frame(self.root,bg ='black',relief='ridge',bd=6)
        self.tokenF6.place(x=2500,y=0,height=250,width=400)
        
        self.token_title = Label(self.tokenF6,text="FASTFOOD",bg='silver',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(self.tokenF6,bg ='silver',orient= VERTICAL)
        self.txttokenarea=Text(self.tokenF6,bg ='skyblue4',relief='ridge',bd=6,fg ='white',yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txttokenarea.yview)
        self.txttokenarea.pack(fill=BOTH,expand=1)
#######TOKEN POPUP 2
        self.tokenF2 = Frame(self.root,bg ='black',relief='ridge',bd=6)
        self.tokenF2.place(x=2500,y=148,height=250,width=400)
        
        self.token_title2 = Label(self.tokenF2,text="BAR=BQ",bg='silver',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(self.tokenF2,bg ='silver',orient= VERTICAL)
        self.txttokenarea2=Text(self.tokenF2,bg ='skyblue4',relief='ridge',bd=6,fg ='white',yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txttokenarea2.yview)
        self.txttokenarea2.pack(fill=BOTH,expand=1)

#######TOKEN POPUP 3
        self.tokenF3 = Frame(self.root,bg ='black',relief='ridge',bd=6)
        self.tokenF3.place(x=2500,y=348,height=250,width=400)
        
        self.token_title3 = Label(self.tokenF3,text="ROLL",bg='silver',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(self.tokenF3,bg ='silver',orient= VERTICAL)
        self.txttokenarea3=Text(self.tokenF3,bg ='skyblue4',relief='ridge',bd=6,fg ='white',yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txttokenarea3.yview)
        self.txttokenarea3.pack(fill=BOTH,expand=1)


        
########################TOKEN POPUP


        
       
        self.message = Label(self.root, text = '', fg = 'red',bg ='skyblue4')
        self.message.place(x=1000, y=20,width=250,height=25)

           
#############################BUTTONS########GREEN######BUTTON########################################################
        self.btndesign2 = Button(self.Frame3,bg="yellow",relief='ridge',bd=20)
        self.btndesign2.place(x=0, y=0,width=980,height=6)

        self.btnRevenue4 = Button(self.root, text = 'View Dashboard ',bd=3,command=None,font=('arial',14),width = 17,bg="silver")
        self.btnRevenue4.place(x=1050, y=120,width=200,height=25)
        
        self.btnStock = Button(self.root, text = 'View Record',bd=3,font=('arial',14),bg="yellow",command=self.View_Record)
        self.btnStock.place(x=1050, y=180,width=200,height=25)

  #      self.btnStock = Button(self.root, text = 'Sum Data',bd=3,font=('arial',14),bg="silver",command=self.ttoal_gen)
  #      self.btnStock.place(x=1050, y=260,width=200,height=25)


#        self.btnRevenue1 = Button(self.root, text = 'Clear',bd=3, font=('arial',14),bg="silver",command=self.clear_bill)
#        self.btnRevenue1.place(x=1050, y=340,width=200,height=25)


        self.btnRevenue5 = Button(self.root, text = 'Print Bill',bd=3,command=self.bill_area,font=('arial',14),bg="silver")
        self.btnRevenue5.place(x=1050, y=420,width=200,height=25)
        
        
        self.btnRevenue2 = Button(self.Frame3, text = 'Print',command=self.print_notes,font=('arial',12),bg='skyblue4',bd=7,relief=GROOVE)
        self.btnRevenue2.place(x=330, y=450, width=120,height=30)

        self.btnRevenue3 = Button(self.root, text = 'ADD RECORD',command=self.manully_add_data,font=('arial',14),bg='red',bd=3)
        self.btnRevenue3.place(x=1050, y=580,width=200,height=30)

##        self.btnRevenue55 = Button(self.root, text = 'Token',command=self.token_dataarea,font=('arial',12),bg='skyblue4',bd=7,relief=GROOVE)
##        self.btnRevenue55.place(x=1050, y=450, width=120,height=30)
##
##

    





       
        

        
#####################VARIABLES ####################################################

        self.datevar= StringVar()
        self.timevar= StringVar()
        self.datevar.set(time.strftime("%d-%m-%Y"))
        self.timevar.set(time.strftime("%H:%M:%S"))

        self.date_lab=Label(self.root,textvariable=self.datevar,font=("arial",18),bg ='skyblue4').place(x=850,y=14)
        self.time_lab=Label(self.root,textvariable=self.timevar,font=("arial",18),bg ='skyblue4').place(x=650,y=14)

        
        self.box = StringVar()

        self.bill_no = StringVar()
        x=random.randint(1000,9900)
        self.bill_no.set(str(x))


        

        self.box1 = IntVar()
        self.box2 = IntVar()
        self.box3 = IntVar()
        self.box4 = IntVar()
        self.box5 = IntVar()
        self.box6 = IntVar()
        self.box7 = IntVar()

        self.box51 = IntVar()
        self.box52 = IntVar()
        self.box53 = IntVar()

        self.optionalbox_1= StringVar()
        self.optionalbox_1.set('')

        self.optionalbox_2= IntVar()
        self.optionalbox_2.set(0)



######################EARCH################E   N   T   R   Y FOR SEARCH#################################################################
        self.bill_no1 = Entry(self.Frame2,textvariable=self.bill_no,bg ='skyblue4',fg ='white',font=('arial',15))
        self.bill_no1.place(x=70, y=14, width=60,height=25)

#########################OPTIONAL $$$$###############################
        self.optionalbox_label=Label(self.Frame3,text="OPTIONAL", relief='groove',bd=0,bg ='yellow',font=('arial',14))
        self.optionalbox_label.place(x=220,y=350, width=240,height=25)

        self.optionalbox2_label=Label(self.Frame3, relief='groove',bd=5,bg ='yellow',font=('arial',14))
        self.optionalbox2_label.place(x=220,y=430, width=240,height=4)



        self.optionalbox = ttk.Combobox(self.Frame3,textvariable=self.optionalbox_1,font=('arial',15))
        self.optionalbox['values']=('Qormo','Daal','Biryani')
        self.optionalbox.place(x=230, y=390, width=140,height=30)





        self.optionalbox2 = Entry(self.Frame3,textvariable=self.optionalbox_2,font=('arial',15))
        self.optionalbox2.place(x=390, y=390, width=50,height=30)



        self.optionalbox3_title = Label(self.Frame3,text="Notes",bg='skyblue4',bd=7,relief=GROOVE).place(x=230, y=450, width=100,height=30)
        self.notes_txt =Text(self.Frame3,bg ='skyblue4',relief='ridge',bd=6,fg ='white',)
        self.notes_txt.place(x=230, y=480, width=220,height=120)

#














#########################OPTIONAL $$$$###############################

        self.txtbox1 = ttk.Combobox(self.Frame3,textvariable=self.box1,font=('arial',18))
        self.txtbox1['values']=(1,2,3,4,5,6,7,8,9,10,12)
##        self.txtbox1.current(0)
        self.txtbox1.place(x=130, y=100, width=50,height=40)

        self.txtbox2 = ttk.Combobox(self.Frame3,textvariable=self.box2,font=('arial',18))
        self.txtbox2['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox2.place(x=130, y=150, width=50,height=40)


        self.txtbox3 = ttk.Combobox(self.Frame3,textvariable=self.box3,font=('arial',18))
        self.txtbox3['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox3.place(x=400, y=200, width=50,height=40)

        self.txtbox4 = ttk.Combobox(self.Frame3,textvariable=self.box4,font=('arial',15))
        self.txtbox4['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox4.place(x=400, y=60, width=50,height=40)

        self.txtbox5 = ttk.Combobox(self.Frame3,textvariable=self.box5,font=('arial',15))
        self.txtbox5['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox5.place(x=400, y=110, width=50,height=40)

        self.txtbox6 = ttk.Combobox(self.Frame3,textvariable=self.box6,font=('arial',15))
        self.txtbox6['values']=(1,2,3,4,5,6,7,8,9,10,12) 
        self.txtbox6.place(x=400, y=160, width=50,height=40)

        self.txtbox7 = ttk.Combobox(self.Frame3,textvariable=self.box7,font=('arial',15))
        self.txtbox7['values']=(1,2,3,4,5,6,7,8,9,10,12) 
        self.txtbox7.place(x=660, y=200, width=50,height=40)
        


################L    A    B     E    L     E    N   T   R  Y#######FRAME3###############
        self.Bill_no_label=Label(self.Frame2,text="B.No",bg ='skyblue4', font=('arial',15))
        self.Bill_no_label.place(x=10, y=14, width=60,height=25)

        self.BarBQ_label=Label(self.Frame3,text="BarBQ",bg='skyblue4',fg ='black',bd=2,relief=GROOVE, font=('arial',12))
        self.BarBQ_label.place(x=220, y=10, width=240,height=30)

        self.FASTFOOD_label=Label(self.Frame3,text="FASTFOOD",bg='skyblue4',fg ='black',bd=2,relief=GROOVE, font=('arial',12))
        self.FASTFOOD_label.place(x=0, y=10, width=210,height=30)



        self.BarBQ_label_line=Label(self.Frame3,bg='yellow',fg ='black',bd=7,relief=GROOVE, font=('arial',12))
        self.BarBQ_label_line.place(x=210, y=5, width=8,height=652)





        self.boxline=Label(self.Frame2,bg='gray',relief='ridge',bd=6)
        self.boxline.place(x=0, y=90, width=600,height=10)

        self.boxline2=Label(self.Frame2,bg='gray',relief='ridge',bd=6)
        self.boxline2.place(x=590, y=90, width=10,height=60)




        self.box1_label=Label(self.Frame3,text="Zinger", bg ='skyblue4',font=('arial',15))
        self.box1_label.place(x=0, y=100, width=130,height=40)


        self.box2_label=Label(self.Frame3,text="Broast",bg ='skyblue4', font=('arial',15))
        self.box2_label.place(x=0, y=150, width=130,height=40)

        self.box3_label=Label(self.Frame3,text="Chicken-Boti", bg ='skyblue4',font=('arial',15))
        self.box3_label.place(x=250, y=200, width=130,height=40)

        self.box8_label=Label(self.Frame3,text="Boneless-Boti", bg ='skyblue4',font=('arial',15))
        self.box8_label.place(x=250, y=250, width=130,height=40)




        self.box4_label=Label(self.Frame3,text="RashmiKabab",bg ='skyblue4', font=('arial',15))
        self.box4_label.place(x=250, y=60, width=130,height=40)

        self.box5_label=Label(self.Frame3,text="GolaKabab",bg ='skyblue4', font=('arial',15))
        self.box5_label.place(x=250, y=110, width=130,height=40)


        self.box6_label=Label(self.Frame3,text="Tikka",bg ='skyblue4', font=('arial',15))
        self.box6_label.place(x=250, y=160, width=130,height=40)

        self.box7_label=Label(self.Frame3,text="VegeTable",bg ='skyblue4', font=('arial',15))
        self.box7_label.place(x=480, y=200, width=130,height=40)

##############----------------------------------------------------------
        self.box51_label=Label(self.Frame3,text="Fries", bg ='skyblue4',font=('arial',15))
        self.box51_label.place(x=0, y=50, width=130,height=40)

        self.box52_label=Label(self.Frame3,text="Puri Partha",bg ='skyblue4', font=('arial',15))
        self.box52_label.place(x=480, y=500, width=130,height=30)

        self.box53_label=Label(self.Frame3,text="Corn-Soup", bg ='skyblue4',font=('arial',15))
        self.box53_label.place(x=480, y=590, width=130,height=30)
##################___ENTRY BOx51
        self.txtbox51 = ttk.Combobox(self.Frame3,textvariable=self.box51,font=('arial',15))
        self.txtbox51['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox51.place(x=130, y=50, width=50,height=40)

        self.txtbox52 = ttk.Combobox(self.Frame3,textvariable=self.box52,font=('arial',15))
        self.txtbox52['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox52.place(x=660, y=500, width=50,height=30)


        self.txtbox53 = ttk.Combobox(self.Frame3,textvariable=self.box53,font=('arial',15))
        self.txtbox53['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox53.place(x=660, y=590, width=50,height=30)



###-----------------------------ENTRY LABEL 2-------------------------------------------------------##############

        self.boxclient10 = StringVar()
        #self.boxclient10.set('Type Phone no')

        self.box11 = IntVar()
        #self.boxvar11.set('0')
        self.box12 = IntVar()
        self.box13 = IntVar()
        self.box14 = IntVar()
        self.box15 = IntVar()
        self.box16 = IntVar()
        self.box17 = IntVar()
        
        
        



        

##        self.txtbox10 = Entry(self.Frame3,textvariable=self.boxclient10,font=('arial',15))
##        self.txtbox10.place(x=350, y=15, width=140,heigh=25)

        self.txtbox11 = ttk.Combobox(self.Frame3,textvariable=self.box11,font=('arial',15))
        self.txtbox11['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox11.place(x=660, y=100,width=50,height=40)

        self.txtbox12 = ttk.Combobox(self.Frame3,textvariable=self.box12,font=('arial',15))
        self.txtbox12['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox12.place(x=660, y=150, width=50,height=40)


        self.txtbox13 = ttk.Combobox(self.Frame3,textvariable=self.box13,font=('arial',15))
        self.txtbox13['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox13.place(x=660, y=540, width=50,height=40)

        self.txtbox14 = ttk.Combobox(self.Frame3,textvariable=self.box14,font=('arial',15))
        self.txtbox14['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox14.place(x=660, y=250, width=50,height=40)

        self.txtbox15 = ttk.Combobox(self.Frame3,textvariable=self.box15,font=('arial',15))
        self.txtbox15['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox15.place(x=660, y=300, width=50,height=40)

        self.txtbox16 = ttk.Combobox(self.Frame3,textvariable=self.box16,font=('arial',15))
        self.txtbox15['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox16.place(x=130, y=250, width=50,height=40)

        self.txtbox17 = ttk.Combobox(self.Frame3,textvariable=self.box17,font=('arial',15))
        self.txtbox15['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox17.place(x=130, y=300, width=50,height=40)
        


#####--------------------------LABEL 2-------------------------------------------
        
        self.Sabzi_label=Label(self.Frame3,text="DISHES",bg='skyblue4',fg ='black',bd=2,relief=GROOVE, font=('arial',12))
        self.Sabzi_label.place(x=470, y=10, width=250,height=30)

        self.Sabzi_label_line=Label(self.Frame3,bg='yellow',fg ='black',bd=7,relief=GROOVE, font=('arial',12))
        self.Sabzi_label_line.place(x=460, y=5, width=8,height=650)


        self.box11_label=Label(self.Frame3,text="Biryani-Single",bg ='skyblue4', font=('arial',15))
        self.box11_label.place(x=480, y=100, width=130,height=40)

        self.box12_label=Label(self.Frame3,text="Double-Biryani", bg ='skyblue4',font=('arial',15))
        self.box12_label.place(x=480, y=150, width=130,height=40)

        self.box13_label=Label(self.Frame3,text="Chappati",bg ='skyblue4', font=('arial',15))
        self.box13_label.place(x=480, y=540, width=130,height=40)


        self.box14_label=Label(self.Frame3,text="Daal Plate",bg ='skyblue4', font=('arial',15))
        self.box14_label.place(x=480, y=250, width=130,height=40)

        self.box15_label=Label(self.Frame3,text="Qourma-Plate",bg ='skyblue4', font=('arial',15))
        self.box15_label.place(x=480, y=300, width=130,height=40)


        self.box16_label=Label(self.Frame3,text="Chargo",bg ='skyblue4',font=('arial',16))
        self.box16_label.place(x=0, y=250, width=130,height=40)

        self.box17_label=Label(self.Frame3,text="T74 Deal", bg ='skyblue4',font=('arial',16))
        self.box17_label.place(x=0, y=300, width=130,height=40)


###_______________________ENTRY LABEL3_____________________________________________________############
        self.boxclient20 = StringVar()


        self.box21 = IntVar()
        #self.boxvar11.set('0')
        self.box22 = IntVar()
        self.box23 = IntVar()
        self.box24 = IntVar()
        self.box25 = IntVar()
        self.box26 = IntVar()
        self.box27 = IntVar()

##        self.box61 = IntVar()
        self.box62 = IntVar()
        self.box63 = IntVar()

        self.box71 = IntVar()
        self.box72 = IntVar()
        self.box73 = IntVar()

        self.box81 = IntVar()
        self.box82 = IntVar()
        self.box83 = IntVar()


        self.K_Combox_71= StringVar()
        self.K_Combox_71.set('Select')





      


        
        
        






        self.txtbox20 = Entry(self.Frame2,textvariable=self.boxclient20,bg='yellow',font=('arial',15))
        self.txtbox20.place(x=260, y=14, width=240,height=25)

        self.txtbox21 = ttk.Combobox(self.Frame3,textvariable=self.box21,font=('arial',15))
        self.txtbox21['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox21.place(x=900, y=150, width=50,height=40)

        self.txtbox22 = ttk.Combobox(self.Frame3,textvariable=self.box22,font=('arial',15))
        self.txtbox22['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox22.place(x=900, y=100, width=50,height=40)


        self.txtbox23 = ttk.Combobox(self.Frame3,textvariable=self.box23,font=('arial',15))
        self.txtbox23['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox23.place(x=900, y=400, width=50,height=40)

        self.txtbox24 = ttk.Combobox(self.Frame3,textvariable=self.box24,font=('arial',15))
        self.txtbox24['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox24.place(x=900, y=200, width=50,height=40)

        self.txtbox25 = ttk.Combobox(self.Frame3,textvariable=self.box25,font=('arial',15))
        self.txtbox25['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox25.place(x=900, y=250, width=50,height=40)

        self.txtbox26 = ttk.Combobox(self.Frame3,textvariable=self.box26,font=('arial',15))
        self.txtbox26['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox26.place(x=900, y=350, width=50,height=40)

        self.txtbox27 = ttk.Combobox(self.Frame3,textvariable=self.box27,font=('arial',15))
        self.txtbox27['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox27.place(x=900, y=50, width=50,height=40)
        

#####-----------------------------LABEL3------------------------------------------------
        
        self.box20_label=Label(self.Frame2,text="ID:",bg ='skyblue4', font=('arial',15))
        self.box20_label.place(x=200, y=14, width=60,height=25)

        self.ROLL_label=Label(self.Frame3,text="ROLL",bg='skyblue4',fg ='black',bd=2,relief=GROOVE, font=('arial',12))
        self.ROLL_label.place(x=730, y=10, width=250,height=30)

        self.ROLL_label_line=Label(self.Frame3,bg='yellow',fg ='black',bd=7,relief=GROOVE, font=('arial',12))
        self.ROLL_label_line.place(x=720, y=5, width=8,height=650)



        self.box21_label=Label(self.Frame3,text="Plan(Chatni)",bg ='skyblue4', font=('arial',14))
        self.box21_label.place(x=750, y=150, width=130,height=40)

        self.box22_label=Label(self.Frame3,text="Mayo",bg ='skyblue4', font=('arial',14))
        self.box22_label.place(x=750, y=100, width=130,height=40)

        self.box23_label=Label(self.Frame3,text="MayoGarlic",bg ='skyblue4', font=('arial',14))
        self.box23_label.place(x=750, y=400, width=130,height=40)


        self.box24_label=Label(self.Frame3,text="Zinger-Roll",bg ='skyblue4',font=('arial',14))
        self.box24_label.place(x=750, y=200, width=130,height=40)

        self.box25_label=Label(self.Frame3,text="R.Kabab-Roll",bg ='skyblue4', font=('arial',14))
        self.box25_label.place(x=750, y=250, width=130,height=40)


        self.box26_label=Label(self.Frame3,text="Chilli-Garlic",bg ='skyblue4', font=('arial',14))
        self.box26_label.place(x=750, y=350, width=130,height=40)

        self.box27_label=Label(self.Frame3,text="Big Takeaway",bg ='skyblue4', font=('arial',14))
        self.box27_label.place(x=750, y=50, width=130,height=40)

#####################==================BOX61==62====63==============================
        self.box61_label=Label(self.Frame3,text="KARHAI SIZE", relief='groove',bd=0,bg ='yellow',font=('arial',14))
        self.box61_label.place(x=469, y=350, width=252,height=25)

        self.box62_label=Label(self.Frame3,text="T 75",bg ='skyblue4',font=('arial',16))
        self.box62_label.place(x=0, y=200, width=130,height=35)

        self.box63_label=Label(self.Frame3,text="Special Roll", bg ='skyblue4',font=('arial',14))
        self.box63_label.place(x=750, y=445, width=130,height=35)

##        self.txtboxextra = ttk.Combobox(self.Frame3,textvariable=self.box61,font=('arial',15))
##        self.txtboxextra['values']=(1,2,3,4,5,6,7,8,9,10,12)
##        self.txtboxextra.place(x=130, y=350, width=50,height=80)

        self.txtbox62 = ttk.Combobox(self.Frame3,textvariable=self.box62,font=('arial',15))
        self.txtbox62['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox62.place(x=130, y=200, width=50,height=35)

        self.txtbox63 = ttk.Combobox(self.Frame3,textvariable=self.box63,font=('arial',15))
        self.txtbox63['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox63.place(x=900, y=445, width=50,height=35)

#####################==================BOX71==72====73==============================
        self.Karhai_Combox_71=ttk.Combobox(self.Frame3,textvariable=self.K_Combox_71,font=('arial',14))
        self.Karhai_Combox_71['values']=('KarhaiPiece','KarhaiHalf','KarhaiFull')
        self.Karhai_Combox_71.place(x=480, y=380, width=130,height=35)

        self.box73_label=Label(self.Frame3,text="Pizza-ROll", bg ='skyblue4',font=('arial',15))
        self.box73_label.place(x=750, y=300, width=130,height=35)

        self.txtbox71 = ttk.Combobox(self.Frame3,textvariable=self.box71,font=('arial',12))
        self.txtbox71['values']=(250,500,1000,)
        self.txtbox71.place(x=630, y=380, width=80,height=35)

        self.txtbox72 = ttk.Combobox(self.Frame3,textvariable=self.box72,font=('arial',15))
        self.txtbox72['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox72.place(x=400, y=250, width=50,height=40)

        self.txtbox73 = ttk.Combobox(self.Frame3,textvariable=self.box73,font=('arial',15))
        self.txtbox73['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox73.place(x=900, y=300, width=50,height=35)

#####################==================BOX81==82====83==============================
        self.box81_Combox_81 = StringVar()
        self.box81_Combox_81 .set('Select')

        self.box81_Var = IntVar()
        self.box81_Var.set(0)

        self.box81_label=Label(self.Frame3,text="HANDI SIZE", relief='groove',bd=0,bg ='yellow',font=('arial',14))
        self.box81_label.place(x=469, y=420, width=252,height=25)


        self.box81_label=ttk.Combobox(self.Frame3,textvariable=self.box81_Combox_81,font=('arial',14))
        self.box81_label['values']=('HandiPiece','HandiHalf','HandiFull')
        self.box81_label.place(x=480, y=450, width=130,height=40)


        self.box82_label=Label(self.Frame3,text="ChickenPulao", bg ='skyblue4',font=('arial',15))
        self.box82_label.place(x=480, y=60, width=130,height=40)

        self.box83_label=Label(self.Frame3,text="VegetableRoll",bg ='skyblue4',font=('arial',14))
        self.box83_label.place(x=750, y=490, width=130,height=40)

        self.txtbox81 = ttk.Combobox(self.Frame3,textvariable=self.box81_Var ,font=('arial',15))
        self.txtbox81['values']=(310,500,1000,)
        self.txtbox81.place(x=630, y=450, width=80,height=40)



        

        self.txtbox82 = ttk.Combobox(self.Frame3,textvariable=self.box82,font=('arial',15))
        self.txtbox82['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox82.place(x=660, y=60, width=50,height=40)

        self.txtbox83 = ttk.Combobox(self.Frame3,textvariable=self.box83,font=('arial',15))
        self.txtbox83['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox83.place(x=900, y=490, width=50,height=40)
       
 
       
       

####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        
#######################F R A M E 4 BOTTOM##############################################        
        self.boxclient31 = StringVar()
        #self.boxvar11.set('0')
        self.boxclient32 = StringVar()
        self.boxclient33 = StringVar()
        self.boxclient34 = StringVar()
        self.boxclient35 = StringVar()
        self.boxclient36 = StringVar()
    
#######################TOTAL ENTRY BOX##############################################        
        self.txtbox31 = Entry(self.Frame4,textvariable=self.boxclient31,font=('arial',42),fg ='white',bg ='black')
        self.txtbox31.place(x=0, y=0, width=320,height=80)
#######################TOTAL ENTRY BOX##############################################        



##########varible
        self.search_by = StringVar()
        self.search_byitem = StringVar()
        
######open_front_RECORD #############


#    def open_front_rec(self):
#        self.Frame_front = Frame(self.root,bg ='skyblue4',relief='ridge',bd=6)
 #       self.Frame_front.place(x=0,y=0,height=750,width=1350)






    def Welcome_billing(self):
            self.textarea.delete('1.0',END)  
            self.textarea.insert(END,f"\n  Date: {self.datevar.get()} {self.timevar.get()}")
            self.textarea.insert(END,f"\n  Bill Number A1: {self.bill_no.get()}")
            self.textarea.insert(END,f"\n  ID: {self.boxclient20.get()}")
            self.textarea.insert(END,f"\n============================================")
            self.textarea.insert(END,f"\n ITEMS\t\t QTY\t\t AMOUNT")    
            self.textarea.insert(END,f"\n============================================")
            
             
                 
            
    def bill_area(self):
        self.Welcome_billing()
#############FIRST COLUMN VAR##################        
        if self.box1.get()!=0:
            self.textarea.insert(END,f"\n Zinger\t\t {self.box1.get()}\t\t {self.c_s_p1}")
        if self.box2.get()!=0:
            self.textarea.insert(END,f"\n Broast\t\t {self.box2.get()}\t\t {self.c_s_p2}")
        if self.box3.get()!=0:
            self.textarea.insert(END,f"\n Chicken-Boti\t\t {self.box3.get()}\t\t {self.c_s_p3}")
        if self.box4.get()!=0:
            self.textarea.insert(END,f"\n Rashmi-Kabab\t\t {self.box4.get()}\t\t {self.c_s_p4}")
        if self.box5.get()!=0:
            self.textarea.insert(END,f"\n Ch-GolaKabab\t\t {self.box5.get()}\t\t {self.c_s_p5}")
        if self.box6.get()!=0:
            self.textarea.insert(END,f"\n Tikka\t\t {self.box6.get()}\t\t {self.c_s_p6}")
        if self.box7.get()!=0:
            self.textarea.insert(END,f"\n Vegetable\t\t {self.box7.get()}\t\t {self.c_s_p7}")
#############SECOND COLUMN VAR##################        
        if self.box11.get()!=0:
            self.textarea.insert(END,f"\n Biryani\t\t {self.box11.get()}\t\t {self.c_s_p11}")
        if self.box12.get()!=0:
            self.textarea.insert(END,f"\n Dob:Biryani\t\t {self.box12.get()}\t\t {self.c_s_p12}")
        if self.box13.get()!=0:
            self.textarea.insert(END,f"\n Chappati\t\t {self.box13.get()}\t\t {self.c_s_p13}")
        if self.box14.get()!=0:
            self.textarea.insert(END,f"\n Daal\t\t {self.box14.get()}\t\t {self.c_s_p14}")
        if self.box15.get()!=0:
            self.textarea.insert(END,f"\n QourmaPlate\t\t {self.box15.get()}\t\t {self.c_s_p15}")
        if self.box16.get()!=0:
            self.textarea.insert(END,f"\n Ch-Chargo\t\t {self.box16.get()}\t\t {self.c_s_p16}")
        if self.box17.get()!=0:
            self.textarea.insert(END,f"\n T74 Deal\t\t {self.box17.get()}\t\t {self.c_s_p17}")
#############THIRD COLUMN VAR##################        
        if self.box21.get()!=0:
            self.textarea.insert(END,f"\n Chitni(PLAN)\t\t {self.box21.get()}\t\t {self.c_s_p21}")
        if self.box22.get()!=0:
            self.textarea.insert(END,f"\n Mayo ROll\t\t {self.box22.get()}\t\t {self.c_s_p22}")
        if self.box23.get()!=0:
            self.textarea.insert(END,f"\n Mayo Garlic\t\t {self.box23.get()}\t\t {self.c_s_p23}")
        if self.box24.get()!=0:
            self.textarea.insert(END,f"\n Zinger-Roll\t\t {self.box24.get()}\t\t {self.c_s_p24}")
        if self.box25.get()!=0:
            self.textarea.insert(END,f"\n Rashmi-Kabab-ROll\t\t {self.box25.get()}\t\t {self.c_s_p25}")
        if self.box26.get()!=0:
            self.textarea.insert(END,f"\n Garlic-Roll\t\t {self.box26.get()}\t\t {self.c_s_p26}")
        if self.box27.get()!=0:
            self.textarea.insert(END,f"\n Big-Takeaway\t\t {self.box27.get()}\t\t {self.c_s_p27}")


        if self.box51.get()!=0:
            self.textarea.insert(END,f"\n Fries\t\t {self.box51.get()}\t\t {self.c_s_p51}")
        if self.box52.get()!=0:
            self.textarea.insert(END,f"\n Partha\t\t {self.box52.get()}\t\t {self.c_s_p52}")
        if self.box53.get()!=0:
            self.textarea.insert(END,f"\n Corn-Soup\t\t {self.box53.get()}\t\t {self.c_s_p53}")

        if self.box81_Combox_81.get()!='Select' and self.box81_Var.get()!=(0): 
            self.textarea.insert(END,f"\n {self.box81_Combox_81.get()}\t\t \t\t {self.box81_Var.get()}")
        if self.box62.get()!=0:
            self.textarea.insert(END,f"\n T 75 Deal\t\t {self.box62.get()}\t\t {self.c_s_p62}")
        if self.box63.get()!=0:
            self.textarea.insert(END,f"\n Special Roll\t\t {self.box63.get()}\t\t {self.c_s_p63}")

        if self.box72.get()!=0:
            self.textarea.insert(END,f"\n Boneless-Boti\t\t {self.box72.get()}\t\t {self.c_s_p72}")
        if self.box73.get()!=0:
            self.textarea.insert(END,f"\n Pizza-Roll\t\t {self.box73.get()}\t\t {self.c_s_p73}")


        if self.K_Combox_71.get()!='Select' and  self.box71.get()!=(0):
            self.textarea.insert(END,f"\n {self.K_Combox_71.get()}\t\t\t\t {self.box71.get()}")

        if self.box82.get()!=0:
            self.textarea.insert(END,f"\n ChickenPulao\t\t {self.box82.get()}\t\t {self.c_s_p82}")
        if self.box83.get()!=0:
            self.textarea.insert(END,f"\n Vegetable-Roll\t\t {self.box83.get()}\t\t {self.c_s_p83}")

        if self.optionalbox_1.get()!="" and self.optionalbox_2.get()!=(0):
            self.textarea.insert(END,f"\n {self.optionalbox_1.get()}\t\t \t\t {self.optionalbox_2.get()}")

                    




##        if self.box27.get()!=0:
##            self.textarea.insert(END,f"\n Chappti\t\t {self.box27.get()}\t\t {self.c_s_p27}")
        self.textarea.insert(END,f"\n--------------------------------------------")
#######################IST COLUM TAX IN BILL AREA#########################
        if self.boxclient34.get()!="Rs. 0.0":
            self.textarea.insert(END,f"\n Charges:\t\t {self.boxclient34.get()}\t\t ")##Tax Variable 1st Colum    

            self.textarea.insert(END,f"\n Total Bill:\t\t {self.AllvariableTotal}\t\t ")    
            self.textarea.insert(END,f"\n--------------------------------------------")
            self.textarea.insert(END,f"\n---Complain/Comments---03337513043----------")
           
            self.save_bill()
##            self.clear_bill()

    def save_bill(self):
        op=tkinter.messagebox.askyesno("Save Bill","Do you want to save bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bill/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
    
            self.filename = tempfile.mktemp(".txt")
            open(self.filename, "w"). write(self.bill_data)
            os.startfile(self.filename, "print")



############TOKEN POPUP DEF
############TOKEN POPUP DEF

    def Token_billing(self):
        self.txttokenarea.delete('1.0',END)
        self.txttokenarea.insert(END,f"\n  Bill N0:{self.bill_no.get()}\t Token")
        self.txttokenarea.insert(END,f"\n  Date: {self.datevar.get()} {self.timevar.get()}")
        self.txttokenarea.insert(END,f"\n********************************************")
        self.txttokenarea.insert(END,f"\n ITEMS\t\t\tQTY")    
        self.txttokenarea.insert(END,f"\n********************************************")
        if self.box1.get()!=0:
            self.txttokenarea.insert(END,f"\n ZingerBurger\t\t{self.box1.get()}")
        if self.box2.get()!=0:
            self.txttokenarea.insert(END,f"\n Chicken-Broast\t\t{self.box2.get()}")
        if self.box51.get()!=0:
            self.txttokenarea.insert(END,f"\n Fries-Plate\t\t{self.box51.get()}")
        if self.box17.get()!=0:
            self.txttokenarea.insert(END,f"\n T74 Deal\t\t{self.box17.get()}")
        if self.box16.get()!=0:
            self.txttokenarea.insert(END,f"\n Ch-Chargo\t\t{self.box16.get()}")
        if self.box62.get()!=0:
            self.txttokenarea.insert(END,f"\n T 75 Deal\t\t{self.box62.get()}")

        self.txttokenarea.insert(END,f"\n********************************************")
        self.save_bill_token()
            
 







##MANULLY ADD RECROD
##MANULLY ADD RECROD


        

##
##MANULLY ADD RECROD
##MANULLY ADD RECROD
        
    def token_dataarea(self,event):
        if self.boxclient31.get()=="" or self.boxclient31.get()=="0.0":
            tkinter.messagebox.showerror("Error", "No Product purchased!")
        else:
            self.tok_databit()
            self.add_product()        
               

    def tok_databit(self):
        if self.box1.get()!=0 or self.box2.get()!=0 or self.box51.get()!=0 or self.box17.get()!=0 or self.box16.get()!=0 or self.box62.get()!=0:
            self.Token_billing()
        if self.box3.get()!=0 or self.box4.get()!=0 or self.box5.get()!=0 or self.box6.get()!=0 or self.box72.get()!=0 :
            self.Token_billing2()

        if self.box21.get()!=0 or self.box22.get()!=0 or self.box15.get()!=0 or self.box14.get()!=0 or self.box13.get()!=0 or self.box11.get()!=0 or self.box7.get()!=0 or self.box23.get()!=0 or self.box24.get()!=0 or self.box25.get()!=0 or self.box26.get()!=0 or self.box27.get()!=0 or  self.box53.get()!=0 or self.box52.get()!=0 or self.box81_Combox_81.get()!='Select' and self.box81_Var.get()!=(0) or self.box63.get()!=0 or self.K_Combox_71.get()!='Select' and  self.box71.get()!=(0) or  self.box73.get()!=0 or self.box82.get()!=0 or self.box83.get()!=0 or self.optionalbox_1.get()!="" and self.optionalbox_2.get()!=(0):
            self.Token_billing3()
        tkinter.messagebox.showinfo("TOKEN", "Token have been Printed")

#        self.adddata_rec()
        

            

##        self.token_dataarea2()
##        self.token_dataarea3()
#############FIRST TOKEN DEF##################        
            

    def save_bill_token(self):
        q = self.txttokenarea.get('1.0', END)
        filename = tempfile.mktemp(".txt")
        open(filename, "w"). write(q)
        os.startfile(filename, "print")
            

###2nd TOKEN DEF##
    def Token_billing2(self):
        self.txttokenarea2.delete('1.0',END)
        self.txttokenarea2.insert(END,f"\n  Bill N0:{self.bill_no.get()}\t Token")
        self.txttokenarea2.insert(END,f"\n  Date: {self.datevar.get()} {self.timevar.get()}")
     
        self.txttokenarea2.insert(END,f"\n******************************")
        self.txttokenarea2.insert(END,f"\n ITEMS\t\t\tQTY")    
        self.txttokenarea2.insert(END,f"\n******************************")
        if self.box3.get()!=0:
            self.txttokenarea2.insert(END,f"\n Chicken-Boti\t\t{self.box3.get()}")

        if self.box72.get()!=0:
            self.txttokenarea2.insert(END,f"\n Boneless-Boti\t\t{self.box72.get()}")
        if self.box4.get()!=0:
            self.txttokenarea2.insert(END,f"\n Rashmi-Kabab\t\t{self.box4.get()}")
        if self.box5.get()!=0:
            self.txttokenarea2.insert(END,f"\n Ch-GolaKabab\t\t{self.box5.get()}")
        if self.box6.get()!=0:
            self.txttokenarea2.insert(END,f"\n Ch-Tikka\t\t{self.box6.get()}")
        self.txttokenarea2.insert(END,f"\n***************************************")
        self.save_bill_token2()


    def save_bill_token2(self):
        q = self.txttokenarea2.get('1.0', END)
        filename = tempfile.mktemp(".txt")
        open(filename, "w"). write(q)
        os.startfile(filename, "print")
 
        
###2nd TOKEN DEF##


###3rd TOKEN DEF##
       ###3rd TOKEN DEF##
    def Token_billing3(self):
        self.txttokenarea3.delete('1.0',END)
        self.txttokenarea3.insert(END,f"\n  Bill N0:{self.bill_no.get()}\t Token")
        self.txttokenarea3.insert(END,f"\n  Date: {self.datevar.get()} {self.timevar.get()}")
        self.txttokenarea3.insert(END,f"\n******************************")
        self.txttokenarea3.insert(END,f"\n ITEMS\t\t\tQTY")
        self.txttokenarea3.insert(END,f"\n******************************")
        
        if self.box21.get()!=0:
            self.txttokenarea3.insert(END,f"\n Chitni(PLAN)\t\t{self.box21.get()}")
        if self.box22.get()!=0:
            self.txttokenarea3.insert(END,f"\n Mayo ROll\t\t{self.box22.get()}")
        if self.box23.get()!=0:
            self.txttokenarea3.insert(END,f"\n Mayo Garlic\\t\t{self.box23.get()}")
        if self.box24.get()!=0:
            self.txttokenarea3.insert(END,f"\n Zinger-Roll\t\t{self.box24.get()}")
        if self.box25.get()!=0:
            self.txttokenarea3.insert(END,f"\n Kabab-ROll\t\t{self.box25.get()}")
        if self.box26.get()!=0:
            self.txttokenarea3.insert(END,f"\n Garlic-Roll\t\t{self.box26.get()}")
        if self.box27.get()!=0:
            self.txttokenarea3.insert(END,f"\n BigTakeaway\t\t{self.box27.get()}")

        if self.box13.get()!=0:
            self.txttokenarea3.insert(END,f"\n Chappati\t\t{self.box13.get()}")


        if self.box7.get()!=0:
            self.txttokenarea3.insert(END,f"\n Vegetable\t\t{self.box7.get()}")
       
        if self.box11.get()!=0:
            self.txttokenarea3.insert(END,f"\n Biryani\t\t{self.box11.get()}")
        if self.box12.get()!=0:
            self.txttokenarea3.insert(END,f"\n Dob:Biryani\t\t{self.box12.get()}")



        if self.box14.get()!=0:
            self.txttokenarea3.insert(END,f"\n Daaal\t\t{self.box14.get()}")
        if self.box15.get()!=0:
            self.txttokenarea3.insert(END,f"\n QourmaPlate\t\t{self.box15.get()}")




        if self.box53.get()!=0:
            self.txttokenarea3.insert(END,f"\n Corn-Soup\t\t{self.box53.get()}")
        if self.box52.get()!=0:
            self.txttokenarea3.insert(END,f"\n Partha\t\t{self.box52.get()}")

        if self.box81_Combox_81.get()!='Select' and self.box81_Var.get()!=(0): 
            self.txttokenarea3.insert(END,f"\n {self.box81_Combox_81.get()}\t\t{self.box81_Var.get()}")

        if self.box63.get()!=0:
            self.txttokenarea3.insert(END,f"\n Special Roll\t\t{self.box63.get()}")

        if self.K_Combox_71.get()!='Select' and  self.box71.get()!=(0):
            self.txttokenarea3.insert(END,f"\n {self.K_Combox_71.get()}\t\t{self.box71.get()}")


        if self.box73.get()!=0:
            self.txttokenarea3.insert(END,f"\n Pizza-Roll\t\t{self.box73.get()}")

        if self.box82.get()!=0:
            self.txttokenarea3.insert(END,f"\n ChickenPulao\t\t{self.box82.get()}")
        if self.box83.get()!=0:
            self.txttokenarea3.insert(END,f"\n Vegetable-Roll\t\t{self.box83.get()}")

        if self.optionalbox_1.get()!="" and self.optionalbox_2.get()!=(0):
            self.txttokenarea3.insert(END,f"\n {self.optionalbox_1.get()}\t\t{self.optionalbox_2.get()}")
        self.txttokenarea3.insert(END,f"\n***************************************")





        self.save_bill_token3()
        



        
        

    def save_bill_token3(self):
        q = self.txttokenarea3.get('1.0', END)
        filename = tempfile.mktemp(".txt")
        open(filename, "w"). write(q)
        os.startfile(filename, "print")





    def print_notes(self):
        q = self.notes_txt.get('1.0', END)
        filename = tempfile.mktemp(".txt")
        open(filename, "w"). write(q)
        os.startfile(filename, "print")


###3rd TOKEN DEF##
       ###3rd TOKEN DEF##              
            
############TOKEN POPUP DEF
############TOKEN POPUP DEF


####################################################################################################
    def ttoal_gen(self,event):
        self.c_s_p1=self.box1.get()*150
        self.c_s_p2=self.box2.get()*200
        self.c_s_p3=self.box3.get()*80
        self.c_s_p4=self.box4.get()*70
        self.c_s_p5=self.box5.get()*120
        self.c_s_p6=self.box6.get()*150
        self.c_s_p7=self.box7.get()*120
        self.c_s_p51=self.box51.get()*60
        self.c_s_p52=self.box52.get()*30
        self.c_s_p53=self.box53.get()*220

        self.c_s_p11=self.box11.get()*120
        self.c_s_p12=self.box12.get()*220
        self.c_s_p13=self.box13.get()*10
        self.c_s_p14=self.box14.get()*120
        self.c_s_p15=self.box15.get()*120
        self.c_s_p16=self.box16.get()*160
        self.c_s_p17=self.box17.get()*390
##        self.c_s_p61=self.box61.get()*310
        self.c_s_p62=self.box62.get()*950
        self.c_s_p63=self.box63.get()*140

        self.c_s_p71=self.box71.get()
        
        self.c_s_p72=self.box72.get()*100
        self.c_s_p73=self.box73.get()*120

        self.c_s_p82=self.box82.get()*180
        self.c_s_p83=self.box83.get()*60


        self.c_s_p21=self.box21.get()*100
        self.c_s_p22=self.box22.get()*120
        self.c_s_p23=self.box23.get()*120
        self.c_s_p24=self.box24.get()*140
        self.c_s_p25=self.box25.get()*100
        self.c_s_p26=self.box26.get()*100
        self.c_s_p27=self.box27.get()*150
        self.c_s_pb1=self.optionalbox_2.get()
        self.c_s_pb8181=self.box81_Var.get()

        

        

        
        
        
        

        self.boxclient31_total=float(
                                   self.c_s_p1+
                                   self.c_s_p2+
                                   self.c_s_p3+
                                   self.c_s_p4+
                                   self.c_s_p5+
                                   self.c_s_p6+
                                   self.c_s_p7+
                                   self.c_s_p51+
                                   self.c_s_p52+
                                   self.c_s_p53+
                                   self.c_s_pb8181+

                                   self.c_s_p11+
                                   self.c_s_p12+
                                   self.c_s_p13+
                                   self.c_s_p14+
                                   self.c_s_p15+
                                   self.c_s_p16+
                                   self.c_s_p17+
##                                   self.c_s_p61+
                                   self.c_s_p62+
                                   self.c_s_p63+
                                   self.c_s_p71+
                                   self.c_s_p72+
                                   self.c_s_p73+
                                   self.c_s_p82+
                                   self.c_s_pb1+
                                   self.c_s_p83+
                                   self.c_s_p21+
                                   self.c_s_p22+
                                   self.c_s_p23+
                                   self.c_s_p24+
                                   self.c_s_p25+
                                   self.c_s_p26+
                                   self.c_s_p27
                                   
                                   )
        self.boxclient31.set((self.boxclient31_total))
        self.c31_tax=round((self.boxclient31_total*0.02),2)
        self.boxclient34.set((self.c31_tax))
        ###tax round limit
                                                                        #large digit ,2 show two digit
###################################################################################################        
   
        
        
##    
##        self.boxclient32_total = float(
##                                   
##                                   )
##        self.boxclient32.set("Rs."+str(self.boxclient32_total))
##        self.c32_tax=round((self.boxclient32_total*0.02),2)
##        self.boxclient35.set("Rs."+str(self.c32_tax)) ###tax round limit
##         

  ##########################################################################
      
##
##        self.boxclient33_total = float(
##                                  
##                                   )
##        self.boxclient33.set("Rs."+str(self.boxclient33_total))
##        self.c33_tax=round((self.boxclient33_total*0.02),2)
##        self.boxclient36.set("Rs."+str(self.c33_tax)) ###tax round limit
##
        self.AllvariableTotal=float(  self.boxclient31_total
                                    )
        


##################BILL AREA #######################################################
#################################################################################
   
            
            


#######0000000000000000000CLEAR BILL000000000000000000000000000000000000000000000000000000000000000000000
    def clear_bill(self,event):
        self.box1.set(0)
        self.box2.set(0)
        self.box3.set(0)
        self.box4.set(0)
        self.box5.set(0)
        self.box6.set(0)
        self.box7.set(0)

        self.box51.set(0)
        self.box52.set(0)
        self.box53.set(0)

##        self.box61.set(0)
        self.box62.set(0)
        self.box63.set(0)

        
        self.box71.set(0)
        self.box72.set(0)
        self.box73.set(0)

      
        self.box81.set(0)
        self.box82.set(0)
        self.box83.set(0)
      
      
      

        self.box11.set(0)
        self.box12.set(0)
        self.box13.set(0)
        self.box14.set(0)
        self.box15.set(0)
        self.box16.set(0)
        self.box17.set(0)


        self.box21.set(0)
        #self.boxvar11.set('0')
        self.box22.set(0)
        self.box23.set(0)
        self.box24.set(0)
        self.box25.set(0)
        self.box26.set(0)
        self.box27.set(0)
        self.optionalbox_2.set(0)

        self.boxclient31.set("")
        
        self.boxclient32.set("")
        self.boxclient33.set("")
        self.boxclient34.set("")
        self.boxclient35.set("")
        self.boxclient36.set("")
        self.boxclient20.set("")
        self.optionalbox_1.set("")
        self.box81_Combox_81.set('Select')
        self.K_Combox_71.set('Select')
        self.box81_Var.set(0)

        self.box.set("")
        self.boxclient10.set("")
         
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))







##########################SQLITE3
    def View_Record(self):
        self.Record_window = Tk()     
        self.Record_window.geometry('1350x750+0+0')
        self.Record_window.config(bg ='skyblue4')
        self.Frame1 = Frame(self.Record_window, bg ='blue',relief='ridge',bd=6)
        self.Frame1.place(x=0,y=0,height=60,width=1000)
        self.Frame2 = Frame(self.Record_window,bg ='skyblue4',relief='ridge',bd=10)
        self.Frame2.place(x=0,y=60,height=580,width=1000)
        self.Framesum = Frame(self.Record_window,bg ='blue',relief='ridge',bd=10)
        self.Framesum.place(x=0,y=650,height=80,width=1000)

       

           
#############################BUTTONS########GREEN######BUTTON########################################################
        self.btnRevenue1 = Button(self.Record_window, text = 'Sum ',bd=3,command=self.plus_products,font=('arial',14),width = 17,bg="silver")
        self.btnRevenue1.place(x=1050, y=120,width=200,height=25)
        

        self.btnRevenue2 = Button(self.Record_window, text = 'Edit',bd=3,command=None,font=('arial',14),width = 17,bg="silver")
        self.btnRevenue2.place(x=1050, y=160,width=200,height=25)

        self.btnRevenue2 = Button(self.Record_window, text = 'Clear Table',bd=0,command=self.delete_product,bg="skyblue4")
        self.btnRevenue2.place(x=1050, y=260,width=200,height=25)

        self.sum_txt =Text(self.Record_window,bg ='skyblue4',relief='ridge',bd=6,fg ='white',)
        self.sum_txt.place(x=1050, y=460, width=220,height=120)

        scroll_x=Scrollbar(self.Frame2,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.Frame2,orient=VERTICAL)
        self.tree=ttk.Treeview(self.Frame2,columns=('Sr','B_No','ID','ZingerBurger','Broast','ChickenChargo','Tikka','RashmiKabab','GolaKabab','ChickenBoti','Fries','BigTakeawayRoll','ZingerRoll','PlanRoll','MayoRoll','MayogarlicRoll','SpecialRoll','PizzaRoll','RashmiKababRoll','VegetableRoll','T74Deal','ChickenKarhai','ChickenHandi','DaalPlate','QormoPlate','OptionalData','Biryani','ChickenPulao','Chapati','Partha','CornSoup','DobBiryani','GrandTotal','DateTime'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.tree.xview)
        scroll_y.config(command=self.tree.yview)
                                                    
        self.tree.heading('Sr',text='Sr')
        self.tree.heading('B_No',text='B_No')
        self.tree.heading('ID',text='ID')
        self.tree.heading('ZingerBurger',text='ZingerBurger')
        self.tree.heading('Broast',text='Broast')
        self.tree.heading('ChickenChargo',text='ChickenChargo')
        self.tree.heading('Tikka',text='Tikka')
        self.tree.heading('RashmiKabab',text='RashmiKabab')


        self.tree.heading('GolaKabab',text='GolaKabab')
        self.tree.heading('ChickenBoti',text='ChickenBoti')
        self.tree.heading('Fries',text='Fries')
        self.tree.heading('BigTakeawayRoll',text='BigTakeawayRoll')
        self.tree.heading('ZingerRoll',text='ZingerRoll')
        self.tree.heading('PlanRoll',text='PlanRoll')
        self.tree.heading('MayoRoll',text='MayoRoll')
        self.tree.heading('MayogarlicRoll',text='MayogarlicRoll')
        self.tree.heading('SpecialRoll',text='SpecialRoll')                                                    
        self.tree.heading('PizzaRoll',text='PizzaRoll')
        self.tree.heading('RashmiKababRoll',text='RashmiKababRoll')
        self.tree.heading('VegetableRoll',text='VegetableRoll')
        self.tree.heading('T74Deal',text='T74Deal')
        self.tree.heading('ChickenKarhai',text='ChickenKarhai')
        self.tree.heading('ChickenHandi',text='ChickenHandi')
        
        self.tree.heading('DaalPlate',text='DaalPlate')
        self.tree.heading('QormoPlate',text='QormoPlate')
        self.tree.heading('OptionalData',text='OptionalData')
        self.tree.heading('Biryani',text='Biryani')
        self.tree.heading('ChickenPulao',text='ChickenPulao')
        self.tree.heading('Chapati',text='Chapati')
        self.tree.heading('Partha',text='Partha')
        self.tree.heading('CornSoup',text='CornSoup')
        self.tree.heading('DobBiryani',text='DobBiryani')
        self.tree.heading('GrandTotal',text='GrandTotal')
        self.tree.heading('DateTime',text='DateTime')

        self.tree.column('Sr',width=30)

        self.tree.column('B_No',width=40)
        self.tree.column('ID',width=120)
        self.tree.column('ZingerBurger',width=120)
        self.tree.column('Broast',width=100)
        self.tree.column('ChickenChargo',width=120)         
        self.tree.column('Tikka',width=80)
        self.tree.column('RashmiKabab',width=120)
        self.tree.column('GolaKabab',width=120)
        self.tree.column('ChickenBoti',width=120)
        self.tree.column('Fries',width=80)
        self.tree.column('BigTakeawayRoll',width=140)
        self.tree.column('ZingerRoll',width=120)
        self.tree.column('PlanRoll',width=100)
        self.tree.column('MayoRoll',width=100)
        self.tree.column('MayogarlicRoll',width=120)
        self.tree.column('SpecialRoll',width=100)
        self.tree.column('PizzaRoll',width=120)
        self.tree.column('RashmiKababRoll',width=140)
        self.tree.column('VegetableRoll',width=120)
        self.tree.column('T74Deal',width=80)
        self.tree.column('ChickenKarhai',width=140)

        self.tree.column('ChickenHandi',width=140)

        self.tree.column('DaalPlate',width=100)
        self.tree.column('QormoPlate',width=100)
        self.tree.column('OptionalData',width=140)
        self.tree.column('Biryani',width=100)
        self.tree.column('ChickenPulao',width=120)
        self.tree.column('Chapati',width=100)
        self.tree.column('Partha',width=100)
        self.tree.column('CornSoup',width=100)
        self.tree.column('DobBiryani',width=120)
        


        self.tree.column('GrandTotal',width=100)
        self.tree.column('DateTime',width=100)



    

       
        self.tree['show']='headings'
        self.tree.pack(fill=BOTH,expand=1)
        self.get_products()







        scroll_x=Scrollbar(self.Framesum,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.Framesum,orient=VERTICAL)
        self.tree_plus=ttk.Treeview(self.Framesum,columns=('Sr','ZingerBurger','Broast','ChickenChargo','Tikka','RashmiKabab','GolaKabab','ChickenBoti','Fries','BigTakeawayRoll','ZingerRoll','PlanRoll','MayoRoll','MayogarlicRoll','SpecialRoll','PizzaRoll','RashmiKababRoll','VegetableRoll','T74Deal','ChickenKarhai','ChickenHandi','DaalPlate','QormoPlate','OptionalData','Biryani','ChickenPulao','Chapati','Partha','CornSoup','DobBiryani','GrandTotal'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.tree_plus.xview)
        scroll_y.config(command=self.tree_plus.yview)
                                                    
        self.tree_plus.heading('Sr',text='Sr')
        self.tree_plus.heading('ZingerBurger',text='ZingerBurger')
        self.tree_plus.heading('Broast',text='Broast')
        self.tree_plus.heading('ChickenChargo',text='ChickenChargo')
        self.tree_plus.heading('Tikka',text='Tikka')
        self.tree_plus.heading('RashmiKabab',text='RashmiKabab')


        self.tree_plus.heading('GolaKabab',text='GolaKabab')
        self.tree_plus.heading('ChickenBoti',text='ChickenBoti')
        self.tree_plus.heading('Fries',text='Fries')
        self.tree_plus.heading('BigTakeawayRoll',text='BigTakeawayRoll')
        self.tree_plus.heading('ZingerRoll',text='ZingerRoll')
        self.tree_plus.heading('PlanRoll',text='PlanRoll')
        self.tree_plus.heading('MayoRoll',text='MayoRoll')
        self.tree_plus.heading('MayogarlicRoll',text='MayogarlicRoll')
        self.tree_plus.heading('SpecialRoll',text='SpecialRoll')                                                    
        self.tree_plus.heading('PizzaRoll',text='PizzaRoll')
        self.tree_plus.heading('RashmiKababRoll',text='RashmiKababRoll')
        self.tree_plus.heading('VegetableRoll',text='VegetableRoll')
        self.tree_plus.heading('T74Deal',text='T74Deal')
        self.tree_plus.heading('ChickenKarhai',text='ChickenKarhai')
        self.tree_plus.heading('ChickenHandi',text='ChickenHandi')
        
        self.tree_plus.heading('DaalPlate',text='DaalPlate')
        self.tree_plus.heading('QormoPlate',text='QormoPlate')
        self.tree_plus.heading('OptionalData',text='OptionalData')
        self.tree_plus.heading('Biryani',text='Biryani')
        self.tree_plus.heading('ChickenPulao',text='ChickenPulao')
        self.tree_plus.heading('Chapati',text='Chapati')
        self.tree_plus.heading('Partha',text='Partha')
        self.tree_plus.heading('CornSoup',text='CornSoup')
        self.tree_plus.heading('DobBiryani',text='DobBiryani')
        self.tree_plus.heading('GrandTotal',text='GrandTotal')

        self.tree_plus.column('Sr',width=30)
        self.tree_plus.column('ZingerBurger',width=120)
        self.tree_plus.column('Broast',width=100)
        self.tree_plus.column('ChickenChargo',width=120)         
        self.tree_plus.column('Tikka',width=80)
        self.tree_plus.column('RashmiKabab',width=120)
        self.tree_plus.column('GolaKabab',width=120)
        self.tree_plus.column('ChickenBoti',width=120)
        self.tree_plus.column('Fries',width=80)
        self.tree_plus.column('BigTakeawayRoll',width=140)
        self.tree_plus.column('ZingerRoll',width=120)
        self.tree_plus.column('PlanRoll',width=100)
        self.tree_plus.column('MayoRoll',width=100)
        self.tree_plus.column('MayogarlicRoll',width=120)
        self.tree_plus.column('SpecialRoll',width=100)
        self.tree_plus.column('PizzaRoll',width=120)
        self.tree_plus.column('RashmiKababRoll',width=140)
        self.tree_plus.column('VegetableRoll',width=120)
        self.tree_plus.column('T74Deal',width=80)
        self.tree_plus.column('ChickenKarhai',width=140)

        self.tree_plus.column('ChickenHandi',width=140)

        self.tree_plus.column('DaalPlate',width=100)
        self.tree_plus.column('QormoPlate',width=100)
        self.tree_plus.column('OptionalData',width=140)
        self.tree_plus.column('Biryani',width=100)
        self.tree_plus.column('ChickenPulao',width=120)
        self.tree_plus.column('Chapati',width=100)
        self.tree_plus.column('Partha',width=100)
        self.tree_plus.column('CornSoup',width=100)
        self.tree_plus.column('DobBiryani',width=120)
        


        self.tree_plus.column('GrandTotal',width=100)



    

       
        self.tree_plus['show']='headings'
        self.tree_plus.pack(fill=BOTH,expand=1)
        self.plus_products()






            
    def add_product(self):
        conn=sqlite3.connect('win.db')
        c=conn.cursor()
        self.bill_no.get()
        self.boxclient20.get()
        self.box1.get()
        self.box2.get()
        self.box16.get()
        self.box6.get()
        self.box4.get()
        self.box5.get()
        self.box3.get()
        self.box51.get()
        self.box27.get()
        self.box24.get()
        self.box21.get()
        self.box22.get()
        self.box23.get()
        self.box63.get()
        self.box73.get()
        self.box25.get()##rashmiKababRoll
        self.box83.get()###VegetableRoll
        self.box17.get()
        self.box71.get()###Karhai
        self.box81_Var.get()##handi
        self.box14.get()##daal
        self.box15.get()##qormo
        self.optionalbox_2.get()
        self.box11.get()
        self.box82.get()
        self.box13.get(),##Chappti#28
        self.box52.get(),##partha#29
        self.box53.get(),## CORN SOUP#30
        self.box12.get(),## DOuble Biryani#31
        self.boxclient31.get()#32
 
        
        c.execute("INSERT INTO mytab (B_No,ID,ZingerBurger,Broast,ChickenChargo,Tikka,RashmiKabab,GolaKabab,ChickenBoti,Fries,BigTakeawayRoll,ZingerRoll,PlanRoll,MayoRoll,MayogarlicRoll,SpecialRoll,PizzaRoll,RashmiKababRoll,VegetableRoll,T74Deal,ChickenKarhai,ChickenHandi,DaalPlate,QormoPlate,OptionalData,Biryani,ChickenPulao,Chapati,Partha,CornSoup,DobBiryani,GrandTotal) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
        self.bill_no.get(),#1
        self.boxclient20.get(),#2
        self.box1.get(),#3
        self.box2.get(),#4
        self.box16.get(),#5
        self.box6.get(),#6
        self.box4.get(),#7
        self.box5.get(),#8
        self.box3.get(),#9
        self.box51.get(),#10
        self.box27.get(),#11
        self.box24.get(),#12
        self.box21.get(),#13
        self.box22.get(),#14
        self.box23.get(),#15
        self.box63.get(),#16
        self.box73.get(),#17
        self.box25.get(),##rashmiKababRoll#18
        self.box83.get(),###VegetableRoll#19
        self.box17.get(),#20
        self.box71.get(),###Karhai#21
        self.box81_Var.get(),##handi#22
        self.box14.get(),##daal#23
        self.box15.get(),##qormo#24
        self.optionalbox_2.get(),#25
        self.box11.get(),#26
        self.box82.get(),#27
        self.box13.get(),##Chappti#28
        self.box52.get(),##partha#29
        self.box53.get(),## CORN SOUP#30
        self.box12.get(),## DOuble Biryani#31
        self.boxclient31.get()))

        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo("saved", "data have been saved")


  
        self.bill_no.delete(0,END)
        self.boxclient20.delete(0,END)
        self.box1.delete(0,END)
        self.box2.delete(0,END)
        self.box16.delete(0,END)
        self.box6.delete(0,END)
        self.box4.delete(0,END)
        self.box5.delete(0,END)
        self.box3.delete(0,END)
        self.box51.delete(0,END)
        self.box27.delete(0,END)
        self.box24.delete(0,END)
        self.box21.delete(0,END)
        self.box22.delete(0,END)
        self.box23.delete(0,END)
        self.box63.delete(0,END)
        self.box73.delete(0,END)
        self.box25.delete(0,END)
        self.box83.delete(0,END)
        self.box17.delete(0,END)
        self.box71.delete(0,END)
        self.box81_Var.delete(0,END)
        self.box14.delete(0,END)
        self.box15.delete(0,END)
        self.optionalbox_2.delete(0,END)
        self.box11.delete(0,END)
        self.box82.delete(0,END)
        self.box13.delete(0,END)
        self.box52.delete(0,END)
        self.box53.delete(0,END)
        self.box12.delete(0,END)
        self.boxclient31.delete(0,END)
 


    def get_products(self):
        conn=sqlite3.connect('win.db')
        c=conn.cursor()
        c.execute('select * from mytab')
        rows = c.fetchall()
        for row in rows:
            self.tree.insert('', END,values = row)     
        conn.commit()
        conn.close()


    def get_plus_products(self):
        conn=sqlite3.connect('win.db')
        c=conn.cursor()
        c.execute('select * from winsum')
        rows = c.fetchall()
        for row in rows:
            self.tree.insert('', END,values = row)     
        conn.commit()
        conn.close()

    def plus_products(self):
         conn=sqlite3.connect('win.db')
         c=conn.cursor()
         c.execute("SELECT SUM(Sr),SUM(ZingerBurger),SUM(Broast),SUM(ChickenChargo),SUM(Tikka),SUM(RashmiKabab),SUM(GolaKabab),SUM(ChickenBoti),SUM(Fries),SUM(BigTakeawayRoll),SUM(ZingerRoll),SUM(PlanRoll),SUM(MayoRoll),SUM(MayogarlicRoll),SUM(SpecialRoll),SUM(PizzaRoll),SUM(RashmiKababRoll),SUM(VegetableRoll),SUM(T74Deal),SUM(ChickenKarhai),SUM(ChickenHandi),SUM(DaalPlate),SUM(QormoPlate),SUM(OptionalData),SUM(Biryani),SUM(ChickenPulao),SUM(Chapati),SUM(Partha),SUM(CornSoup),SUM(DobBiryani),SUM(GrandTotal)from mytab")
         result = c.fetchall()
         if len(result)!=0:
             self.tree_plus.delete(*self.tree_plus.get_children())
         for row in result:
             self.tree_plus.insert('', END,values = row)


             
         conn.commit()
         conn.close()


#######
    def delete_product(self):
        conn=sqlite3.connect('win.db')
        c=conn.cursor()
        c.execute('DELETE FROM mytab')
        conn.commit()
        conn.close()
        self.get_products()
    
    







    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)
        
        


if __name__ == '__main__':
    app = Main_Window()
    
    
