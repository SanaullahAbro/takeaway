from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import math,random,os
import random
import time
import pymysql
import datetime
import tempfile


                                                        

        
######################################F1 BUTTON#########################################
####F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F1F
######################################## F  1  ##############################################
##############################L O G I N##################################################
class Main_Window:
    def __init__(self):
        self.root = Tk()
        self.root.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.root.bind("<F11>", self.toggleFullScreen)
        self.root.bind("<Escape>", self.quitFullScreen)
        self.root.geometry('1350x750+0+0')
        self.root.config(bg ='black')
        self.Frame2 = Frame(self.root, bg ='skyblue4')
        self.Frame2.place(x=0,y=0,height=146,width=1500)
        self.Frame3 = Frame(self.root,bg ='skyblue4',relief='ridge',bd=6)
        self.Frame3.place(x=0,y=148,height=590,width=900)
        self.Frame4 = Frame(self.root,bg ='skyblue4',relief='ridge',bd=6)
        self.Frame4.place(x=880,y=650,height=146,width=400)
       

           
        self.label=Label(self.root,text="DEVELOPED BY",font=("arial",14),bg ='skyblue4').place(x=890,y=10)
        self.by=Label(self.root,text="0316-1832160--SANAULLAH--ABRO",font=("arial",14),bg ='skyblue4').place(x=890,y=40)
##        self.label2=Label(self.root,text="INVOICE WINDOW",font=("arial",18),bg ='skyblue4').place(x=400,y=30)
        self.label2=Label(self.root,text="ADD INVOICE",font=("impact",25,"bold"),fg="#d77337",bg="skyblue4").place(x=440,y=30)
 
##      self.desc=Label(self.root,text="0316-1832160",font=("arial",35),bg='red').place(x=40,y=0)
####        self.labelred=Label(self.root,bg="blue").place(x=0,y=0,height=146,width=1500)
##

#############################BUTTONS########GREEN######BUTTON########################################################

        self.btnStock = Button(self.Frame2, text = 'Sum',bd=3,font=('arial',20), width = 17,bg="silver",command=self.add_table)
        self.btnStock.place(x=780, y=90,width=160,height=40)

        self.btnStock = Button(self.Frame2, text = 'View',bd=3,font=('arial',20), width = 17,bg="yellow",command=self.open_front)
        self.btnStock.place(x=620, y=90,width=160,height=40)

        
##        self.btnadd = Button(self.Frame2, text = 'Save', font=('arial',18),width = 17,bg="light green",command=None)
##        self.btnadd.place(x=400, y=90,width=200,height=40)

        self.btnclose = Button(self.Frame2, text = 'x', font=('arial',18),width = 17,bg="silver",command=self.Exit_bill)
        self.btnclose.place(x=1255, y=0,width=25,height=25)


        self.btnRevenue = Button(self.Frame2, text = 'Clear',bd=3, font=('arial',20),width = 17,bg="silver",command=self.clear_bill)
        self.btnRevenue.place(x=941, y=90,width=160,height=40)
        
        self.btnRevenue = Button(self.Frame2, text = 'Print',bd=3,command=self.bill_area,font=('arial',20),width = 17,bg="silver")
        self.btnRevenue.place(x=1200, y=90,width=160,height=40)

       
        

##################00000000000000000000000FRAME 1 Bill
##################area000000000000000000000000000000000000000000000000000
###################BILL AREA
        self.F5 = Frame(self.root,bg ='black',relief='ridge',bd=6)
        self.F5.place(x=880,y=148,height=500,width=400)
        
        self.bill_title = Label(self.F5,text="Print Area",bg='silver',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(self.F5,bg ='silver',orient= VERTICAL)
        self.textarea=Text(self.F5,bg ='skyblue4',relief='ridge',bd=6,fg ='black',yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

    

        
#####################VARIABLES ####################################################

        self.datevar= StringVar()
        self.timevar= StringVar()
        self.datevar.set(time.strftime("%d-%m-%Y"))
        self.timevar.set(time.strftime("%H:%M:%S"))

        self.date_lab=Label(self.root,textvariable=self.datevar,font=("arial",18),bg ='skyblue4').place(x=30,y=30)
        self.time_lab=Label(self.root,textvariable=self.timevar,font=("arial",18),bg ='skyblue4').place(x=240,y=30)

        

        self.box = StringVar()

        self.bill_no = StringVar()
        x=random.randint(100,300)
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
        self.optionalbox_1.set('')
        
        

######################EARCH################E   N   T   R   Y FOR SEARCH#################################################################
        self.bill_no1 = Entry(self.Frame2,textvariable=self.bill_no,bg ='skyblue4',fg ='white',font=('arial',15))
        self.bill_no1.place(x=70, y=110, width=60,height=25)

#########################OPTIONAL $$$$###############################
        self.optionalbox = Entry(self.Frame3,textvariable=self.optionalbox_1,font=('arial',15))
        self.optionalbox.place(x=300, y=10, width=140,height=30)

        self.optionalbox2 = Entry(self.Frame3,textvariable=self.optionalbox_2,font=('arial',15))
        self.optionalbox2.place(x=450, y=10, width=50,height=30)

#########################OPTIONAL $$$$###############################

        self.txtbox1 = ttk.Combobox(self.Frame3,textvariable=self.box1,font=('arial',18))
        self.txtbox1['values']=(1,2,3,4,5,6,7,8,9,10,12)
##        self.txtbox1.current(0)
        self.txtbox1.place(x=180, y=100, width=50,height=40)

        self.txtbox2 = ttk.Combobox(self.Frame3,textvariable=self.box2,font=('arial',18))
        self.txtbox2['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox2.place(x=180, y=150, width=50,height=40)


        self.txtbox3 = ttk.Combobox(self.Frame3,textvariable=self.box3,font=('arial',18))
        self.txtbox3['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox3.place(x=180, y=200, width=50,height=40)

        self.txtbox4 = ttk.Combobox(self.Frame3,textvariable=self.box4,font=('arial',15))
        self.txtbox4['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox4.place(x=180, y=250, width=50,height=40)

        self.txtbox5 = ttk.Combobox(self.Frame3,textvariable=self.box5,font=('arial',15))
        self.txtbox5['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox5.place(x=180, y=300, width=50,height=40)

        self.txtbox6 = ttk.Combobox(self.Frame3,textvariable=self.box6,font=('arial',15))
        self.txtbox6['values']=(1,2,3,4,5,6,7,8,9,10,12) 
        self.txtbox6.place(x=180, y=350, width=50,height=40)

        self.txtbox7 = ttk.Combobox(self.Frame3,textvariable=self.box7,font=('arial',15))
        self.txtbox7['values']=(1,2,3,4,5,6,7,8,9,10,12) 
        self.txtbox7.place(x=180, y=400, width=50,height=40)
        


################L    A    B     E    L     E    N   T   R  Y#######FRAME3###############
        self.Bill_no_label=Label(self.Frame2,text="B.No",bg ='skyblue4', font=('arial',15))
        self.Bill_no_label.place(x=10, y=110, width=60,height=25)

        self.boxline=Label(self.Frame2,bg='gray',relief='ridge',bd=6)
        self.boxline.place(x=0, y=90, width=600,height=10)

        self.boxline2=Label(self.Frame2,bg='gray',relief='ridge',bd=6)
        self.boxline2.place(x=590, y=90, width=10,height=60)

        self.btndesign = Button(self.Frame3, bd=2,width = 17,bg="yellow")
        self.btndesign.place(x=0, y=0,width=280,height=25)
        
        self.btndesign2 = Button(self.Frame3, bd=2,width = 17,bg="yellow")
        self.btndesign2.place(x=550, y=0,width=330,height=25)





        self.box1_label=Label(self.Frame3,text="Zinger", bg ='skyblue4',font=('arial',15))
        self.box1_label.place(x=30, y=100, width=130,height=40)


        self.box2_label=Label(self.Frame3,text="Broast",bg ='skyblue4', font=('arial',15))
        self.box2_label.place(x=30, y=150, width=130,height=40)

        self.box3_label=Label(self.Frame3,text="Chicken-Boti", bg ='skyblue4',font=('arial',15))
        self.box3_label.place(x=30, y=200, width=130,height=40)


        self.box4_label=Label(self.Frame3,text="RashmiKabab",bg ='skyblue4', font=('arial',15))
        self.box4_label.place(x=30, y=250, width=130,height=40)

        self.box5_label=Label(self.Frame3,text="GolaKabab",bg ='skyblue4', font=('arial',15))
        self.box5_label.place(x=30, y=300, width=130,height=40)


        self.box6_label=Label(self.Frame3,text="Tikka",bg ='skyblue4', font=('arial',15))
        self.box6_label.place(x=30, y=350, width=130,height=40)

        self.box7_label=Label(self.Frame3,text="VegeTable",bg ='skyblue4', font=('arial',15))
        self.box7_label.place(x=30, y=400, width=130,height=40)

##############----------------------------------------------------------
        self.box51_label=Label(self.Frame3,text="Fries", bg ='skyblue4',font=('arial',15))
        self.box51_label.place(x=30, y=60, width=130,height=30)

        self.box52_label=Label(self.Frame3,text="Partha",bg ='skyblue4', font=('arial',15))
        self.box52_label.place(x=300, y=60, width=130,height=30)

        self.box53_label=Label(self.Frame3,text="Katchup Roll", bg ='skyblue4',font=('arial',15))
        self.box53_label.place(x=600, y=60, width=130,height=30)
##################___ENTRY BOx51
        self.txtbox51 = ttk.Combobox(self.Frame3,textvariable=self.box51,font=('arial',15))
        self.txtbox51['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox51.place(x=180, y=60, width=50,height=30)

        self.txtbox52 = ttk.Combobox(self.Frame3,textvariable=self.box52,font=('arial',15))
        self.txtbox52['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox52.place(x=450, y=60, width=50,height=30)


        self.txtbox53 = ttk.Combobox(self.Frame3,textvariable=self.box53,font=('arial',15))
        self.txtbox53['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox53.place(x=760, y=60, width=50,height=30)



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
        self.txtbox11.place(x=450, y=100,width=50,height=40)

        self.txtbox12 = ttk.Combobox(self.Frame3,textvariable=self.box12,font=('arial',15))
        self.txtbox12['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox12.place(x=450, y=150, width=50,height=40)


        self.txtbox13 = ttk.Combobox(self.Frame3,textvariable=self.box13,font=('arial',15))
        self.txtbox13['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox13.place(x=450, y=200, width=50,height=40)

        self.txtbox14 = ttk.Combobox(self.Frame3,textvariable=self.box14,font=('arial',15))
        self.txtbox14['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox14.place(x=450, y=250, width=50,height=40)

        self.txtbox15 = ttk.Combobox(self.Frame3,textvariable=self.box15,font=('arial',15))
        self.txtbox15['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox15.place(x=450, y=300, width=50,height=40)

        self.txtbox16 = ttk.Combobox(self.Frame3,textvariable=self.box16,font=('arial',15))
        self.txtbox15['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox16.place(x=450, y=350, width=50,height=40)

        self.txtbox17 = ttk.Combobox(self.Frame3,textvariable=self.box17,font=('arial',15))
        self.txtbox15['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox17.place(x=450, y=400, width=50,height=40)
        


#####--------------------------LABEL 2-------------------------------------------
        
##        self.box10_label=Label(self.Frame3,text="Mob:", font=('arial',15))
##        self.box10_label.place(x=300, y=15, width=45,height=25)

        self.box11_label=Label(self.Frame3,text="Biryani-Single",bg ='skyblue4', font=('arial',15))
        self.box11_label.place(x=300, y=100, width=130,height=40)

        self.box12_label=Label(self.Frame3,text="Double-Biryani", bg ='skyblue4',font=('arial',15))
        self.box12_label.place(x=300, y=150, width=130,height=40)

        self.box13_label=Label(self.Frame3,text="Chappti",bg ='skyblue4', font=('arial',15))
        self.box13_label.place(x=300, y=200, width=130,height=40)


        self.box14_label=Label(self.Frame3,text="Daal Plate",bg ='skyblue4', font=('arial',15))
        self.box14_label.place(x=300, y=250, width=130,height=40)

        self.box15_label=Label(self.Frame3,text="Qourma-Plate",bg ='skyblue4', font=('arial',15))
        self.box15_label.place(x=300, y=300, width=130,height=40)


        self.box16_label=Label(self.Frame3,text="T 07",bg ='skyblue4',font=('arial',16))
        self.box16_label.place(x=300, y=350, width=130,height=40)

        self.box17_label=Label(self.Frame3,text="T 74", bg ='skyblue4',font=('arial',16))
        self.box17_label.place(x=300, y=400, width=130,height=40)


###_______________________ENTRY LABEL3_____________________________________________________############
        self.boxclient20 = StringVar()
        self.boxclient20.set('Type Name\Address ')

        self.box21 = IntVar()
        #self.boxvar11.set('0')
        self.box22 = IntVar()
        self.box23 = IntVar()
        self.box24 = IntVar()
        self.box25 = IntVar()
        self.box26 = IntVar()
        self.box27 = IntVar()

        self.box61 = IntVar()
        self.box62 = IntVar()
        self.box63 = IntVar()

        self.box71 = IntVar()
        self.box72 = IntVar()
        self.box73 = IntVar()

        self.box81 = IntVar()
        self.box82 = IntVar()
        self.box83 = IntVar()



      


        
        
        






        self.txtbox20 = Entry(self.Frame2,textvariable=self.boxclient20,bg='yellow',font=('arial',15))
        self.txtbox20.place(x=260, y=110, width=240,height=25)

        self.txtbox21 = ttk.Combobox(self.Frame3,textvariable=self.box21,font=('arial',15))
        self.txtbox21['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox21.place(x=760, y=100, width=50,height=40)

        self.txtbox22 = ttk.Combobox(self.Frame3,textvariable=self.box22,font=('arial',15))
        self.txtbox22['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox22.place(x=760, y=150, width=50,height=40)


        self.txtbox23 = ttk.Combobox(self.Frame3,textvariable=self.box23,font=('arial',15))
        self.txtbox23['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox23.place(x=760, y=200, width=50,height=40)

        self.txtbox24 = ttk.Combobox(self.Frame3,textvariable=self.box24,font=('arial',15))
        self.txtbox24['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox24.place(x=760, y=250, width=50,height=40)

        self.txtbox25 = ttk.Combobox(self.Frame3,textvariable=self.box25,font=('arial',15))
        self.txtbox25['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox25.place(x=760, y=300, width=50,height=40)

        self.txtbox26 = ttk.Combobox(self.Frame3,textvariable=self.box26,font=('arial',15))
        self.txtbox26['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox26.place(x=760, y=350, width=50,height=40)

        self.txtbox27 = ttk.Combobox(self.Frame3,textvariable=self.box27,font=('arial',15))
        self.txtbox27['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox27.place(x=760, y=400, width=50,height=40)
        

#####-----------------------------LABEL3------------------------------------------------
        
        self.box20_label=Label(self.Frame2,text="ID:",bg ='skyblue4', font=('arial',15))
        self.box20_label.place(x=200, y=110, width=60,height=25)

        self.box21_label=Label(self.Frame3,text="Plan(Chatni)",bg ='skyblue4', font=('arial',15))
        self.box21_label.place(x=600, y=100, width=130,height=40)

        self.box22_label=Label(self.Frame3,text="Mayo-Roll",bg ='skyblue4', font=('arial',15))
        self.box22_label.place(x=600, y=150, width=130,height=40)

        self.box23_label=Label(self.Frame3,text="MayoGarlic",bg ='skyblue4', font=('arial',14))
        self.box23_label.place(x=600, y=200, width=130,height=40)


        self.box24_label=Label(self.Frame3,text="Broast-Zinger-Roll",bg ='skyblue4',font=('arial',12))
        self.box24_label.place(x=600, y=250, width=130,height=40)

        self.box25_label=Label(self.Frame3,text="R-Kabab-Roll",bg ='skyblue4', font=('arial',15))
        self.box25_label.place(x=600, y=300, width=130,height=40)


        self.box26_label=Label(self.Frame3,text="Chilli-Garlic",bg ='skyblue4', font=('arial',15))
        self.box26_label.place(x=600, y=350, width=130,height=40)

        self.box27_label=Label(self.Frame3,text="Big Takeaway",bg ='skyblue4', font=('arial',14))
        self.box27_label.place(x=600, y=400, width=130,height=40)

        self.box25_label=Label(self.Frame3,text="R-Kabab-Roll",bg ='skyblue4',font=('arial',15))
        self.box25_label.place(x=600, y=300, width=130,height=40)

#####################==================BOX61==62====63==============================
        self.box61_label=Label(self.Frame3,text="Piece Karhai", bg ='skyblue4',font=('arial',15))
        self.box61_label.place(x=30, y=445, width=130,height=35)

        self.box62_label=Label(self.Frame3,text="T 75",bg ='skyblue4',font=('arial',16))
        self.box62_label.place(x=300, y=445, width=130,height=35)

        self.box63_label=Label(self.Frame3,text="Special Roll", bg ='skyblue4',font=('arial',14))
        self.box63_label.place(x=600, y=445, width=130,height=35)

        self.txtbox61 = ttk.Combobox(self.Frame3,textvariable=self.box61,font=('arial',15))
        self.txtbox61['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox61.place(x=180, y=445, width=50,height=35)

        self.txtbox62 = ttk.Combobox(self.Frame3,textvariable=self.box62,font=('arial',15))
        self.txtbox62['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox62.place(x=450, y=445, width=50,height=35)

        self.txtbox63 = ttk.Combobox(self.Frame3,textvariable=self.box63,font=('arial',15))
        self.txtbox63['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox63.place(x=760, y=445, width=50,height=35)

#####################==================BOX71==72====73==============================
        self.box71_label=Label(self.Frame3,text="Half Karhai", bg ='skyblue4',font=('arial',14))
        self.box71_label.place(x=30, y=485, width=130,height=35)

        self.box72_label=Label(self.Frame3,text="T 20", bg ='skyblue4',font=('arial',15))
        self.box72_label.place(x=300, y=485, width=130,height=35)

        self.box73_label=Label(self.Frame3,text="Pizza-ROll", bg ='skyblue4',font=('arial',15))
        self.box73_label.place(x=600, y=485, width=130,height=35)

        self.txtbox71 = ttk.Combobox(self.Frame3,textvariable=self.box71,font=('arial',15))
        self.txtbox71['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox71.place(x=180, y=485, width=50,height=35)

        self.txtbox72 = ttk.Combobox(self.Frame3,textvariable=self.box72,font=('arial',15))
        self.txtbox72['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox72.place(x=450, y=485, width=50,height=35)

        self.txtbox73 = ttk.Combobox(self.Frame3,textvariable=self.box73,font=('arial',15))
        self.txtbox73['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox73.place(x=760, y=485, width=50,height=35)

#####################==================BOX81==82====83==============================
        self.box81_label=Label(self.Frame3,text="Full-Karhai",bg ='skyblue4',font=('arial',14))
        self.box81_label.place(x=30, y=525, width=130,height=40)

        self.box82_label=Label(self.Frame3,text="T 22", bg ='skyblue4',font=('arial',15))
        self.box82_label.place(x=300, y=525, width=130,height=40)

        self.box83_label=Label(self.Frame3,text="VegetableRoll",bg ='skyblue4',font=('arial',14))
        self.box83_label.place(x=600, y=525, width=130,height=40)

        self.txtbox81 = ttk.Combobox(self.Frame3,textvariable=self.box81,font=('arial',15))
        self.txtbox81['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox81.place(x=180, y=525, width=50,height=40)

        self.txtbox82 = ttk.Combobox(self.Frame3,textvariable=self.box82,font=('arial',15))
        self.txtbox82['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox82.place(x=450, y=525, width=50,height=40)

        self.txtbox83 = ttk.Combobox(self.Frame3,textvariable=self.box83,font=('arial',15))
        self.txtbox83['values']=(1,2,3,4,5,6,7,8,9,10,12)
        self.txtbox83.place(x=760, y=525, width=50,height=40)
       
 
       
       

####,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        
#######################F R A M E 4 BOTTOM##############################################        
        self.boxclient31 = StringVar()
        #self.boxvar11.set('0')
        self.boxclient32 = StringVar()
        self.boxclient33 = StringVar()
        self.boxclient34 = StringVar()
        self.boxclient35 = StringVar()
        self.boxclient36 = StringVar()
    




        self.box31_label=Label(self.Frame4,text="=",bg ='skyblue4', font=('arial',16))
        self.box31_label.place(x=40, y=20, width=50,height=25)

        self.box132_label=Label(self.Frame4,text="=",bg ='skyblue4',font=('arial',40))
        self.box132_label.place(x=900, y=0, width=50,height=60)

##        self.box33_label=Label(self.Frame4,text="=", font=('arial',16))
##        self.box33_label.place(x=640, y=20, width=50,height=25)
##
##        self.box134_label=Label(self.Frame4,text="tax", font=('arial',15))
##        self.box134_label.place(x=890, y=30, width=50,height=25)

        #self.box135_label=Label(self.Frame4,text="tax 2 column", font=('arial',15))
        #self.box135_label.place(x=830, y=10, width=150,height=32)

        #self.box136_label=Label(self.Frame4,text="Tax 3rd column", font=('arial',15))
        #self.box136_label.place(x=890, y=90, width=150,height=32)


        

        self.txtbox31 = Entry(self.Frame4,textvariable=self.boxclient31,font=('arial',42),bg ='skyblue4')
        self.txtbox31.place(x=15, y=0, width=280,height=60)
##
##        self.txtbox32 = Entry(self.Frame4,textvariable=self.boxclient32,font=('arial',15))
##        self.txtbox32.place(x=360, y=20, width=180,height=35)
##
##        self.txtbox33 = Entry(self.Frame4,textvariable=self.boxclient33,font=('arial',15))
##        self.txtbox33.place(x=700, y=20, width=100,height=25)
##
##        self.txtbox34 = Entry(self.Frame4,textvariable=self.boxclient34,font=('arial',15))
##        self.txtbox34.place(x=930, y=30, width=80,height=25)

        #self.txtbox35 = Entry(self.Frame4,textvariable=self.boxclient35,font=('arial',15))
        #self.txtbox35.place(x=300, y=10, width=160,height=32)

        #self.txtbox36 = Entry(self.Frame4,textvariable=self.boxclient36,font=('arial',15))


        #self.txtbox36.place(x=50, y=90, width=160,height=32)


        
######FRONT WINDOW #############
######FRONT WINDOW #############
######FRONT WINDOW #############        

##########varible
        self.fbox11 = StringVar()
         

    def open_front(self):
        self.Frame_front = Frame(self.root,bg ='skyblue4',relief='ridge',bd=6)
        self.Frame_front.place(x=0,y=0,height=750,width=1350)

        self.Frame_front2 = Frame(self.Frame_front,bg ='gray',relief='ridge',bd=6)
        self.Frame_front2.place(x=60,y=60,height=600,width=1010)

############BTN 
        self.btnRevenue = Button(self.Frame_front, text = '< Back',bd=3,command=self.Exit_front,font=('arial',18),width = 17,bg="yellow")
        self.btnRevenue.place(x=1090, y=10,width=160,height=30)
        
        self.btnRevenue = Button(self.Frame_front, text = 'Search',bd=3,command=self.bill_area,font=('arial',20),width = 17,bg="silver")
        self.btnRevenue.place(x=1090, y=150,width=160,height=40)


        self.btnRevenue = Button(self.Frame_front, text = 'Show All',bd=3,command=self.bill_area,font=('arial',20),width = 17,bg="silver")
        self.btnRevenue.place(x=1090, y=200,width=160,height=40)
        
        self.btnRevenue = Button(self.Frame_front, text = 'Print',bd=3,command=self.bill_area,font=('arial',20),width = 17,bg="silver")
        self.btnRevenue.place(x=1090, y=250,width=160,height=40)

        self.btnRevenue = Button(self.Frame_front, text = 'Update',bd=3,command=self.bill_area,font=('arial',20),width = 17,bg="silver")
        self.btnRevenue.place(x=1090, y=300,width=160,height=40)
        
        self.btnRevenue = Button(self.Frame_front, text = 'Exit',bd=3,command=self.Exit_bill,font=('arial',20),width = 17,bg="silver")
        self.btnRevenue.place(x=1090, y=350,width=160,height=40)

        self.fboxf11 = ttk.Combobox(self.Frame_front,state='readonly',font=('arial',15))
        self.fboxf11['values']=('name','item')
        self.fboxf11.place(x=700, y=10,width=180,height=30)

        self.btnRevenue = Button(self.Frame_front, text = 'Search',bd=3,command=self.bill_area,font=('arial',18),width = 17,bg="silver")
        self.btnRevenue.place(x=890, y=10,width=180,height=30)

        scroll_x=Scrollbar(self.Frame_front2,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.Frame_front2,orient=VERTICAL)
        student_table=ttk.Treeview(self.Frame_front2,columns=('BILL NO','ITEM','QTY','AMOUNT','TOTAL'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)

        student_table.heading('BILL NO',text='BILL NO')
        student_table.heading('ITEM',text='ITEM')
        student_table.heading('QTY',text='QTY')
        student_table.heading('AMOUNT',text='AMOUNT')
        student_table.heading('TOTAL',text='TOTAL')
        
        student_table.column('BILL NO',width=200)
        student_table.column('ITEM',width=200)
        student_table.column('QTY',width=200)
        student_table.column('AMOUNT',width=200)
        student_table.column('TOTAL',width=200)
 

       
        student_table['show']='headings'
        student_table.pack(fill=BOTH,expand=1)

    def add_table(self):
        con=pymysql.connect(host="localhost",user="root",password="0Director",datbases="abro")
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.box1.get(),self.box2.get(),self.box3.get(),
                                                                        self.textarea.get('1.0',END)))
######FRONT WINDOW #############
######FRONT WINDOW #############
######FRONT WINDOW #############        
        
        
    
 

    

####################################################################################################
    def ttoal_gen(self):
        self.c_s_p1=self.box1.get()*150
        self.c_s_p2=self.box2.get()*200
        self.c_s_p3=self.box3.get()*70
        self.c_s_p4=self.box4.get()*60
        self.c_s_p5=self.box5.get()*120
        self.c_s_p6=self.box6.get()*150
        self.c_s_p7=self.box7.get()*120
        self.c_s_p51=self.box51.get()*60
        self.c_s_p52=self.box52.get()*30
        self.c_s_p53=self.box53.get()*100

        self.c_s_p11=self.box11.get()*120
        self.c_s_p12=self.box12.get()*220
        self.c_s_p13=self.box13.get()*10
        self.c_s_p14=self.box14.get()*120
        self.c_s_p15=self.box15.get()*160
        self.c_s_p16=self.box16.get()*330
        self.c_s_p17=self.box17.get()*390
        self.c_s_p61=self.box61.get()*250
        self.c_s_p62=self.box62.get()*950
        self.c_s_p63=self.box63.get()*140

        self.c_s_p71=self.box71.get()*500
        
        self.c_s_p72=self.box72.get()*210
        self.c_s_p73=self.box73.get()*120

        self.c_s_p81=self.box81.get()*950
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

                                   self.c_s_p11+
                                   self.c_s_p12+
                                   self.c_s_p13+
                                   self.c_s_p14+
                                   self.c_s_p15+
                                   self.c_s_p16+
                                   self.c_s_p17+
                                   self.c_s_p61+
                                   self.c_s_p62+
                                   self.c_s_p63+
                                   self.c_s_p71+
                                   self.c_s_p72+
                                   self.c_s_p73+
                                   self.c_s_p81+
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
        self.boxclient31.set("Rs."+str(self.boxclient31_total))
        self.c31_tax=round((self.boxclient31_total*0.02),2)
        self.boxclient34.set("Rs."+str(self.c31_tax)) ###tax round limit
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
   
            
            
##################BILL area FUNCTION######################
        #self.areatxtfor = StringVar()
        

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
            self.textarea.insert(END,f"\n Chappti\t\t {self.box13.get()}\t\t {self.c_s_p13}")
        if self.box14.get()!=0:
            self.textarea.insert(END,f"\n Daal\t\t {self.box14.get()}\t\t {self.c_s_p14}")
        if self.box15.get()!=0:
            self.textarea.insert(END,f"\n QourmaPlate\t\t {self.box15.get()}\t\t {self.c_s_p15}")
        if self.box16.get()!=0:
            self.textarea.insert(END,f"\n T 07 Deal\t\t {self.box16.get()}\t\t {self.c_s_p16}")
        if self.box17.get()!=0:
            self.textarea.insert(END,f"\n T 74 Deal\t\t {self.box17.get()}\t\t {self.c_s_p17}")
#############THIRD COLUMN VAR##################        
        if self.box21.get()!=0:
            self.textarea.insert(END,f"\n Chitni(PLAN)\t\t {self.box21.get()}\t\t {self.c_s_p21}")
        if self.box22.get()!=0:
            self.textarea.insert(END,f"\n Mayo ROll\t\t {self.box22.get()}\t\t {self.c_s_p22}")
        if self.box23.get()!=0:
            self.textarea.insert(END,f"\n Mayo Garlic\t\t {self.box23.get()}\t\t {self.c_s_p23}")
        if self.box24.get()!=0:
            self.textarea.insert(END,f"\n Broast(Zinger)-Roll\t\t {self.box24.get()}\t\t {self.c_s_p24}")
        if self.box25.get()!=0:
            self.textarea.insert(END,f"\n Kabab-ROll\t\t {self.box25.get()}\t\t {self.c_s_p25}")
        if self.box26.get()!=0:
            self.textarea.insert(END,f"\n Garlic-Roll\t\t {self.box26.get()}\t\t {self.c_s_p26}")
        if self.box27.get()!=0:
            self.textarea.insert(END,f"\n Takeaway\t\t {self.box27.get()}\t\t {self.c_s_p27}")


        if self.box51.get()!=0:
            self.textarea.insert(END,f"\n Fries\t\t {self.box51.get()}\t\t {self.c_s_p51}")
        if self.box52.get()!=0:
            self.textarea.insert(END,f"\n Corn-Soup\t\t {self.box52.get()}\t\t {self.c_s_p52}")
        if self.box53.get()!=0:
            self.textarea.insert(END,f"\n Katchup-Roll\t\t {self.box53.get()}\t\t {self.c_s_p53}")

        if self.box61.get()!=0:
            self.textarea.insert(END,f"\n Piece-Karhai\t\t {self.box61.get()}\t\t {self.c_s_p61}")
        if self.box62.get()!=0:
            self.textarea.insert(END,f"\n T 75 Deal\t\t {self.box62.get()}\t\t {self.c_s_p62}")
        if self.box63.get()!=0:
            self.textarea.insert(END,f"\n Special Roll\t\t {self.box63.get()}\t\t {self.c_s_p63}")

        if self.box71.get()!=0:
            self.textarea.insert(END,f"\n Half-Karhai\t\t {self.box71.get()}\t\t {self.c_s_p71}")
        if self.box72.get()!=0:
            self.textarea.insert(END,f"\n T 20 Deal\t\t {self.box72.get()}\t\t {self.c_s_p72}")
        if self.box73.get()!=0:
            self.textarea.insert(END,f"\n Pizza-Roll\t\t {self.box73.get()}\t\t {self.c_s_p73}")

        if self.box81.get()!=0:
            self.textarea.insert(END,f"\n Piece Karhai\t\t {self.box81.get()}\t\t {self.c_s_p81}")
        if self.box82.get()!=0:
            self.textarea.insert(END,f"\n T 22 Deal\t\t {self.box82.get()}\t\t {self.c_s_p82}")
        if self.box83.get()!=0:
            self.textarea.insert(END,f"\n Full Karhai\t\t {self.box83.get()}\t\t {self.c_s_p83}")

        if self.optionalbox_1.get()!=0:
            self.textarea.insert(END,f"\n {self.optionalbox_1.get()}\t\t \t\t {self.c_s_pb1}")

                    




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
            self.clear_bill()

    def save_bill(self):
        op=tkinter.messagebox.askyesno("Save Bill","Do you want to save bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bill/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            self.filename= tempfile.mktemp(".txt")
            open(self.filename, "w"). write(self.bill_data)
            os.startfile(self.filename, "print")

#######0000000000000000000CLEAR BILL000000000000000000000000000000000000000000000000000000000000000000000
    def clear_bill(self):
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

        self.box61.set(0)
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

        self.box.set("")
        self.boxclient10.set("")
        
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.Welcome_billing()


    def Exit_bill(self):
        op=tkinter.messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()

    def Exit_front(self):
        self.Frame_front.destroy()



        

        

      


 
        
        
        
        
        




    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.root.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.root.attributes("-fullscreen", self.fullScreenState)
        


if __name__ == '__main__':
    app = Main_Window()
    
