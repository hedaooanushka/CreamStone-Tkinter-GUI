import tkinter
from tkinter import Tk, StringVar, ttk, messagebox
import random


root = tkinter.Tk()
root.title("FOOD RESTAURANT SYSTEM")
root.configure(background="purple")

Tops = tkinter.Frame(root, width=1200, height=100, bd=12, relief="raise")
Tops.pack(side=tkinter.TOP)
lblTitle = tkinter.Label(Tops, font=('arial', 30, 'bold'), text="      CREAM STONE      ")
lblTitle.grid(row=0, column=0)

Bottommainframe = tkinter.Frame(root, width=1200, height=540, bd=12, relief="raise")
Bottommainframe.pack(side=tkinter.BOTTOM)

f1 = tkinter.Frame(Bottommainframe, width=400, height=540, bd=12, relief="raise")
f1.pack(side=tkinter.LEFT)
f2 = tkinter.Frame(Bottommainframe, width=400, height=540, bd=12, relief="raise")
f2.pack(side=tkinter.LEFT)
f3 = tkinter.Frame(Bottommainframe, width=400, height=540, bd=12, relief="raise")
f3.pack(side=tkinter.RIGHT)

f2top = tkinter.Frame(f2, width=400, height=360, bd=12, relief="raise")
f2top.pack(side=tkinter.TOP)
f2bottom = tkinter.Frame(f2, width=400, height=140, bd=12, relief="raise")
f2bottom.pack(side=tkinter.BOTTOM)


var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
var3 = tkinter.IntVar()
var4 = tkinter.IntVar()
var5 = tkinter.IntVar()
var6 = tkinter.IntVar()
var7 = tkinter.IntVar()
var8 = tkinter.IntVar()
var9 = tkinter.IntVar()
var10 = tkinter.IntVar()
var11 = tkinter.IntVar()
var12 = tkinter.IntVar()
var13 = tkinter.IntVar()
var14 = tkinter.IntVar()
var15 = tkinter.IntVar()
var16 = tkinter.IntVar()
var17 = tkinter.IntVar()
var18 = tkinter.IntVar()
var19 = tkinter.IntVar()
var20 = tkinter.IntVar()
var21 = tkinter.IntVar()
var22 = tkinter.IntVar()
var23 = tkinter.IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)


varredvelvet = StringVar()
varoreo = StringVar()
varblackforest = StringVar()
varferrero = StringVar()
varnutty = StringVar()
varcream = StringVar()
varstraw = StringVar()
varlitchee = StringVar()
varbelgium = StringVar()
varcaramel = StringVar()
varchoco = StringVar()
varbrownie = StringVar()
varfrench = StringVar()
varnutella = StringVar()
varstrawberry = StringVar()
varcafe = StringVar()
varfruit = StringVar()
varcreamy = StringVar()
varhot = StringVar()
vardeath = StringVar()
varnut = StringVar()
varchange = StringVar()
vartax = StringVar()
varsubtotal = StringVar()
vartotal = StringVar()
varpayment = StringVar()
Name = StringVar()
Receipt_no = StringVar()




varferrero.set("0")
varnutty.set("0")
varblackforest.set("0")
varredvelvet.set("0")
varoreo.set("0")
varcream.set("0")
varstraw.set("0")
varlitchee.set("0")
varbelgium.set("0")
varcaramel.set("0")
varchoco.set("0")
varbrownie.set("0")
varfrench.set("0")
varnutella.set("0")
varstrawberry.set("0")
varcafe.set("0")
varfruit.set("0")
varcreamy.set("0")
varhot.set("0")
vardeath.set("0")
varnut.set("0")
varchange.set("0")
vartax.set("0")
varsubtotal.set("0")
vartotal.set("0")
varpayment.set("0")



def exit_button():
    button = messagebox.askyesno("Cream Stone", "Do you want to exit?")
    if button > 0:
        root.destroy()
        return


def reset():
    varferrero.set("0")
    varnutty.set("0")
    varblackforest.set("0")
    varredvelvet.set("0")
    varoreo.set("0")
    varcream.set("0")
    varstraw.set("0")
    varlitchee.set("0")
    varbelgium.set("0")
    varcaramel.set("0")
    varchoco.set("0")
    varbrownie.set("0")
    varfrench.set("0")
    varnutella.set("0")
    varstrawberry.set("0")
    varcafe.set("0")
    varfruit.set("0")
    varcreamy.set("0")
    varhot.set("0")
    vardeath.set("0")
    varnut.set("0")
    varchange.set("0")
    vartax.set("0")
    varsubtotal.set("0")
    vartotal.set("0")
    varpayment.set("0")
    txtferrero.configure(state=tkinter.DISABLED)
    txtbelgium.configure(state=tkinter.DISABLED)
    txtblackforest.configure(state=tkinter.DISABLED)
    txtbrownie.configure(state=tkinter.DISABLED)
    txtcafe.configure(state=tkinter.DISABLED)
    txtcaramel.configure(state=tkinter.DISABLED)
    txtchange.configure(state=tkinter.DISABLED)
    txtchoco.configure(state=tkinter.DISABLED)
    txtcream.configure(state=tkinter.DISABLED)
    txtcreamy.configure(state=tkinter.DISABLED)
    txtdeath.configure(state=tkinter.DISABLED)
    txtfrench.configure(state=tkinter.DISABLED)
    txtfruit.configure(state=tkinter.DISABLED)
    txthot.configure(state=tkinter.DISABLED)
    txtlitchee.configure(state=tkinter.DISABLED)
    txtnut.configure(state=tkinter.DISABLED)
    txtnutella.configure(state=tkinter.DISABLED)
    txtnutty.configure(state=tkinter.DISABLED)
    txtoreo.configure(state=tkinter.DISABLED)
    #txtpayment.configure(state=tkinter.DISABLED)
    txtredvelvet.configure(state=tkinter.DISABLED)
    txtstraw.configure(state=tkinter.DISABLED)
    txtstrawberry.configure(state=tkinter.DISABLED)
    txtsubtotal.configure(state=tkinter.DISABLED)
    txttax.configure(state=tkinter.DISABLED)
    txttotal.configure(state=tkinter.DISABLED)


def chkredvelvet():
    if var1.get() == 1:
        txtredvelvet.configure(state=tkinter.NORMAL)
        varredvelvet.set("")
    elif var1.get() == 0:
        txtredvelvet.configure(state=tkinter.DISABLED)
        varredvelvet.set("0")


def chkstrawberry():
    if var15.get() == 1:
        txtstrawberry.configure(state=tkinter.NORMAL)
        varstrawberry.set("")
    elif var15.get() == 0:
        txtstrawberry.configure(state=tkinter.DISABLED)
        varstrawberry.set("0")


def chkfruit():
    if var17.get() == 1:
        txtfruit.configure(state=tkinter.NORMAL)
        varfruit.set("")
    elif var17.get() == 0:
        txtfruit.configure(state=tkinter.DISABLED)
        varfruit.set("0")


def chkhot():
    if var19.get() == 1:
        txthot.configure(state=tkinter.NORMAL)
        varhot.set("")
    elif var19.get() == 0:
        txthot.configure(state=tkinter.DISABLED)
        varhot.set("0")


def chkcreamy():
    if var19.get() == 1:
        txtcreamy.configure(state=tkinter.NORMAL)
        varcreamy.set("")
    elif var19.get() == 0:
        txtcreamy.configure(state=tkinter.DISABLED)
        varcreamy.set("0")


def chkdeath():
    if var20.get() == 1:
        txtdeath.configure(state=tkinter.NORMAL)
        vardeath.set("")
    elif var20.get() == 0:
        txtdeath.configure(state=tkinter.DISABLED)
        vardeath.set("0")


def chknut():
    if var21.get() == 1:
        txtnut.configure(state=tkinter.NORMAL)
        varnut.set("")
    elif var21.get() == 0:
        txtnut.configure(state=tkinter.DISABLED)
        varnut.set("0")


def chkoreo():
    if var2.get() == 1:
        txtoreo.configure(state=tkinter.NORMAL)
        varoreo.set("")
    elif var2.get() == 0:
        txtoreo.configure(state=tkinter.DISABLED)
        varoreo.set("0")


def chkblackforest():
    if var3.get() == 1:
        txtblackforest.configure(state=tkinter.NORMAL)
        varblackforest.set("")
    elif var3.get() == 0:
        txtblackforest.configure(state=tkinter.DISABLED)
        varblackforest.set("0")


def chkferrero():
    if var4.get() == 1:
        txtferrero.configure(state=tkinter.NORMAL)
        varferrero.set("")
    elif var4.get() == 0:
        txtferrero.configure(state=tkinter.DISABLED)
        varferrero.set("0")


def chknutty():
    if var5.get() == 1:
        txtnutty.configure(state=tkinter.NORMAL)
        varnutty.set("")
    elif var5.get() == 0:
        txtnutty.configure(state=tkinter.DISABLED)
        varnutty.set("0")


def chkcream():
    if var6.get() == 1:
        txtcream.configure(state=tkinter.NORMAL)
        varcream.set("")
    elif var6.get() == 0:
        txtcream.configure(state=tkinter.DISABLED)
        varcream.set("0")


def chkstraw():
    if var7.get() == 1:
        txtstraw.configure(state=tkinter.NORMAL)
        varstraw.set("")
    elif var7.get() == 0:
        txtstraw.configure(state=tkinter.DISABLED)
        varstraw.set("0")


def chklitchee():
    if var8.get() == 1:
        txtlitchee.configure(state=tkinter.NORMAL)
        varlitchee.set("")
    elif var8.get() == 0:
        txtlitchee.configure(state=tkinter.DISABLED)
        varlitchee.set("0")


def chkbelgium():
    if var9.get() == 1:
        txtbelgium.configure(state=tkinter.NORMAL)
        varbelgium.set("")
    elif var9.get() == 0:
        txtbelgium.configure(state=tkinter.DISABLED)
        varbelgium.set("0")


def chkcaramel():
    if var10.get() == 1:
        txtcaramel.configure(state=tkinter.NORMAL)
        varcaramel.set("")
    elif var10.get() == 0:
        txtcaramel.configure(state=tkinter.DISABLED)
        varcaramel.set("0")


def chkchoco():
    if var11.get() == 1:
        txtchoco.configure(state=tkinter.NORMAL)
        varchoco.set("")
    elif var11.get() == 0:
        txtchoco.configure(state=tkinter.DISABLED)
        varchoco.set("0")


def chkbrownie():
    if var12.get() == 1:
        txtbrownie.configure(state=tkinter.NORMAL)
        varbrownie.set("")
    elif var12.get() == 0:
        txtbrownie.configure(state=tkinter.DISABLED)
        varbrownie.set("0")


def chkfrench():
    if var13.get() == 1:
        txtfrench.configure(state=tkinter.NORMAL)
        varfrench.set("")
    elif var13.get() == 0:
        txtfrench.configure(state=tkinter.DISABLED)
        varfrench.set("0")


def chknutella():
    if var14.get() == 1:
        txtnutella.configure(state=tkinter.NORMAL)
        varnutella.set("")
    elif var14.get() == 0:
        txtnutella.configure(state=tkinter.DISABLED)
        varnutella.set("0")


def chkcafe():
    if var16.get() == 1:
        txtcafe.configure(state=tkinter.NORMAL)
        varcafe.set("")
    elif var16.get() == 0:
        txtcafe.configure(state=tkinter.DISABLED)
        varcafe.set("0")

def costofmeal():
    m1 = float(varstraw.get())
    m2 = float(varbelgium.get())
    m3 = float(varblackforest.get())
    m4 = float(varbrownie.get())
    m5 = float(varcream.get())
    m6 = float(varcafe.get())
    m7 = float(varcaramel.get())
    m8 = float(varchoco.get())
    m9 = float(varcreamy.get())
    m10 = float(vardeath.get())
    m11 = float(varferrero.get())
    m12 = float(varfrench.get())
    m13 = float(varfruit.get())
    m14 = float(varhot.get())
    m15 = float(varlitchee.get())
    m16 = float(varnut.get())
    m17 = float(varnutella.get())
    m18 = float(varnutty.get())
    m19 = float(varoreo.get())
    m20 = float(varredvelvet.get())
    m21 = float(varstrawberry.get())

    t1 = (m1*139)+(m2*79)+(m3*550)+(m4*75)+(m5*119)+(m6*199)+(m7*70)+(m8*70)+(m9*179)+(m10*175)+(m21*179)
    t2 = (m11*799)+(m12*60)+(m13*179)+(m14*150)+(m15*139)+(m16*199)+(m17*199)+(m18*699)+(m19*550)+(m20*650)

    cost = (t1 + t2)
    tax = (cost * 18)/100
    vartotal.set(cost + tax)
    vartax.set(tax)

    if (txtpayment.get() == "Cash"):
        change = float(txtpayment.get())
        cost = (t1 + t2)
        tax = (cost * 3.4) / 100
        tax2 = "Rs", str('%.2f'%(tax))
        vartax.set(tax2)

        cost2 = "Rs", str('%.2f'%(cost))
        varsubtotal.set(cost2)
        total2 = "Rs", str('%.2f'%(cost + tax))
        vartotal.set(total2)
        change2 = (change - (cost + tax))
        change3 = "Rs", str('%.2f'%(change2))
        varchange.set(change3)

    elif(txtpayment.get() == "MasterCard" or "DebitCard" or "VisaCard"):
        varpayment.set(" ")
        cost = (t1 + t2)
        tax = (cost * 3.4) / 100
        tax2 = "Rs", str('%.2f' % (tax))
        vartax.set(tax2)

        cost2 = "Rs", str('%.2f' % (cost))
        varsubtotal.set(cost2)
        total2 = "Rs", str('%.1f' % (cost + tax))
        vartotal.set(total2)
        varchange.set(" ")



#################################################  Frame1  ###########################################################

Lname = tkinter.Label(f1, text = "Customer Name: ", font=('arial', 12, 'bold'))
Lname.grid(row=0, column=0, padx=2, pady=2, sticky='w')
Ename = tkinter.Entry(f1, textvariable=Name, font=('arial', 12, 'bold'), width=18)
Ename.place(x=180, y=5)


Lreceipt = tkinter.Label(f1, text="Receipt No:  ", font=('arial', 12, 'bold'))
Lreceipt.grid(row=1, column=0,padx=2, pady=2, sticky='w')
Ereceipt = tkinter.Entry(f1, textvariable=Receipt_no, font=('arial', 12, 'bold'), width=18)
Ereceipt.place(x=180, y=32)
Receipt_no.set(random.randint(0, 1000))


lblIcecake = tkinter.Label(f1, font=('comic sans MS', 18, 'bold'), text="ICECREAM CAKES")
lblIcecake.grid(row=3, column=0, padx=2, pady=2, sticky='w')


redvelvet = tkinter.Checkbutton(f1, text="Red Velvet Cake\t\t650", variable=var1, onvalue=1, offvalue=0,
                                font=('Microsoft New Tai Lue', 12), command=chkredvelvet).grid(row=4, column=0)
txtredvelvet = tkinter.Entry(f1, font=('arial', 12), textvariable=varredvelvet, width=6, justify='left',
                             state=tkinter.DISABLED)
txtredvelvet.grid(row=4, column=1)

oreo = tkinter.Checkbutton(f1, text="Oreo  Cake\t\t550", variable=var2, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkoreo).grid(row=5, column=0)
txtoreo = tkinter.Entry(f1, font=('arial', 12), textvariable=varoreo, width=6, justify='left', state=tkinter.DISABLED)
txtoreo.grid(row=5, column=1)

blackforest = tkinter.Checkbutton(f1, text="Black Forest Cake\t\t550", variable=var3, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkblackforest).grid(row=6, column=0)
txtblackforest = tkinter.Entry(f1, font=('arial', 12), textvariable=varblackforest, width=6, justify='left',
                               state=tkinter.DISABLED)
txtblackforest.grid(row=6, column=1)

ferrero = tkinter.Checkbutton(f1, text="Ferrero Rocher Cake\t\t799", variable=var4, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkferrero).grid(row=7, column=0)
txtferrero = tkinter.Entry(f1, font=('arial', 12), textvariable=varferrero, width=6, justify='left',
                           state=tkinter.DISABLED)
txtferrero.grid(row=7, column=1)

nutty = tkinter.Checkbutton(f1, text="Nutty Almond Cake\t\t699", variable=var5, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chknutty).grid(row=8, column=0)
txtnutty = tkinter.Entry(f1, font=('arial', 12), textvariable=varnutty, width=6, justify='left', state=tkinter.DISABLED)
txtnutty.grid(row=8, column=1)

lblIcecake = tkinter.Label(f1, font=('comic sans MS', 18, 'bold'), text="BLISS IN THE BOTTLE")
lblIcecake.grid(row=10, column=0)

cream = tkinter.Checkbutton(f1, text="Creamy Vanilla\t\t119", variable=var6, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkcream).grid(row=11, column=0)
txtcream = tkinter.Entry(f1, font=('arial', 12), textvariable=varcream, width=6, justify='left', state=tkinter.DISABLED)
txtcream.grid(row=11, column=1)

straw = tkinter.Checkbutton(f1, text="Strawberry\t\t139", variable=var7, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkstraw).grid(row=12, column=0)
txtstraw = tkinter.Entry(f1, font=('arial', 12), textvariable=varstraw, width=6, justify='left', state=tkinter.DISABLED)
txtstraw.grid(row=12, column=1)

litchee = tkinter.Checkbutton(f1, text="Litchee\t\t\t139", variable=var8, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chklitchee).grid(row=13, column=0)
txtlitchee = tkinter.Entry(f1, font=('arial', 12), textvariable=varlitchee, width=6, justify='left',
                           state=tkinter.DISABLED)
txtlitchee.grid(row=13, column=1)

###################################################### Frame2  ##################################################################################

lblIcecake = tkinter.Label(f2top, font=('comic sans MS', 18, 'bold'), text="SIMPLY DELICIOUS SCOOPS")
lblIcecake.grid(row=0, column=0)

belgium = tkinter.Checkbutton(f2top, text="Belgium Dark Chocolate\t\t79", variable=var9, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkbelgium).grid(row=1, column=0)
txtbelgium = tkinter.Entry(f2top, font=('arial', 12), textvariable=varbelgium, width=6, justify='left', state=tkinter.DISABLED)
txtbelgium.grid(row=1, column=1)

caramel = tkinter.Checkbutton(f2top, text="Caramel Nuts\t\t\t70", variable=var10, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkcaramel).grid(row=2, column=0)
txtcaramel = tkinter.Entry(f2top, font=('arial', 12), textvariable=varcaramel, width=6, justify='left', state=tkinter.DISABLED)
txtcaramel.grid(row=2, column=1)

choco = tkinter.Checkbutton(f2top, text="Choco Fudge\t\t\t70", variable=var11, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkchoco).grid(row=3, column=0)
txtchoco = tkinter.Entry(f2top, font=('arial', 12), textvariable=varchoco, width=6, justify='left', state=tkinter.DISABLED)
txtchoco.grid(row=3, column=1)

brownie = tkinter.Checkbutton(f2top, text="Brownie Delight\t\t\t75", variable=var12, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkbrownie).grid(row=4, column=0)
txtbrownie = tkinter.Entry(f2top, font=('arial', 12), textvariable=varbrownie, width=6, justify='left', state=tkinter.DISABLED)
txtbrownie.grid(row=4, column=1)

french = tkinter.Checkbutton(f2top, text="French Vanilla\t\t\t60", variable=var13, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkfrench).grid(row=5, column=0)
txtfrench = tkinter.Entry(f2top, font=('arial', 12), textvariable=varfrench, width=6, justify='left', state=tkinter.DISABLED)
txtfrench.grid(row=5, column=1)
#################################################3    Frame 2 bottom  ###########################################################################

lblPayment = tkinter.Label(f2bottom, font=('arial', 14, 'bold'), text="PAYMENT METHOD", bd=10, width=16, anchor='w')
lblPayment.grid(row=0, column=0)

lblchange = tkinter.Label(f2bottom, font=('arial', 18, 'bold'), text="Change   ", bd=10, anchor='w')
lblchange.grid(row=0, column=1)
txtchange = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=varchange, width=10, justify='left', state=tkinter.DISABLED)
txtchange.grid(row=0, column=2)

cmbPayment = ttk.Combobox(f2bottom, textvariable = var22, state='readonly', font=('arial', 10, 'bold'), width=20)
cmbPayment['value'] = ('Cash','MasterCard', 'DebitCard', 'VisaCard')
cmbPayment.current(0)
cmbPayment.grid(row=1, column=0)

lbltax = tkinter.Label(f2bottom, font=('arial', 18, 'bold'), text="Tax   ", bd=10, anchor='w')
lbltax.grid(row=1, column=1)
txttax = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=vartax, width=10, justify='left', state=tkinter.DISABLED)
txttax.grid(row=1, column=2)

txtpayment = tkinter.Entry(f2bottom, font=('arial', 12, 'bold'), textvariable=varpayment, width=6, justify='left', state=tkinter.DISABLED)
txtpayment.grid(row=2, column=0)
lblsubtotal = tkinter.Label(f2bottom, font=('arial', 14, 'bold'), text="Subtotal   ", bd=10, anchor='w')
lblsubtotal.grid(row=2, column=1)
txtsubtotal = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=varsubtotal, width=10, justify='left',
                            state=tkinter.DISABLED)
txtsubtotal.grid(row=2, column=2)

lbltotal = tkinter.Label(f2bottom, font=('arial', 14, 'bold'), text="Total   ", bd=10, anchor='w')
lbltotal.grid(row=3, column=1)
txttotal = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=vartotal, width=10, justify='left',
                         state=tkinter.DISABLED)
txttotal.grid(row=3, column=2)



########################################################   Frame 3     ##########################################################################

lblIcecake = tkinter.Label(f3, font=('comic sans MS', 18, 'bold'), text="THICK SHAKES")
lblIcecake.grid(row=0, column=0)

nutella = tkinter.Checkbutton(f3, text="Nutella Brownie Blast\t199", variable=var14, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chknutella).grid(row=1, column=0)
txtnutella = tkinter.Entry(f3, font=('arial', 12), textvariable=varnutella, width=6, justify='left', state=tkinter.DISABLED)
txtnutella.grid(row=1, column=1)

strawberry = tkinter.Checkbutton(f3, text="Strawberry Shake\t\t179", variable=var15, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkstrawberry).grid(row=2, column=0)
txtstrawberry = tkinter.Entry(f3, font=('arial', 12), textvariable=varstrawberry, width=6, justify='left', state=tkinter.DISABLED)
txtstrawberry.grid(row=2, column=1)

cafe = tkinter.Checkbutton(f3, text="Cafe Frappe\t\t199", variable=var16, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkcafe).grid(row=3, column=0)
txtcafe = tkinter.Entry(f3, font=('arial', 12), textvariable=varcafe, width=6, justify='left', state=tkinter.DISABLED)
txtcafe.grid(row=3, column=1)

fruit = tkinter.Checkbutton(f3, text="Fruit Bash\t\t\t179", variable=var17, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkfruit).grid(row=4, column=0)
txtfruit = tkinter.Entry(f3, font=('arial', 12), textvariable=varfruit, width=6, justify='left', state=tkinter.DISABLED)
txtfruit.grid(row=4, column=1)

creamy = tkinter.Checkbutton(f3, text="Creamy Oreo\t\t179", variable=var18, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkcreamy).grid(row=5, column=0)
txtcreamy = tkinter.Entry(f3, font=('arial', 12), textvariable=varcreamy, width=6, justify='left', state=tkinter.DISABLED)
txtcreamy.grid(row=5, column=1)


lblIcecake = tkinter.Label(f3, font=('comic sans MS', 18, 'bold'), text="SUNDAES TO SAVOUR")
lblIcecake.grid(row=7, column=0)

hot = tkinter.Checkbutton(f3, text="Hot Choco Fudge\t\t150", variable=var19, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkhot).grid(row=9, column=0)
txthot = tkinter.Entry(f3, font=('arial', 12), textvariable=varhot, width=6, justify='left', state=tkinter.DISABLED)
txthot.grid(row=9, column=1)

death = tkinter.Checkbutton(f3, text="Death By Chocolate\t\t175", variable=var20, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkdeath).grid(row=10, column=0)
txtdeath = tkinter.Entry(f3, font=('arial', 12), textvariable=vardeath, width=6, justify='left', state=tkinter.DISABLED)
txtdeath.grid(row=10, column=1)

nut = tkinter.Checkbutton(f3, text="Nutty Death By Chocolate\t199", variable=var21, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chknut).grid(row=11, column=0)
txtnut = tkinter.Entry(f3, font=('arial', 12), textvariable=varnut, width=6, justify='left', state=tkinter.DISABLED)
txtnut.grid(row=11, column=1)

############################################################ Button  ######################################################################
btntotal = tkinter.Button(f2bottom, padx=16, pady=1, bd=4, fg='black', font=('arial',16,'bold'), width=5, text='Total', command = costofmeal)\
    .grid(row=5, column=0)


btnreset = tkinter.Button(f2bottom,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Reset',
                          command=reset).grid(row=5,column=1)

btnexit = tkinter.Button(f2bottom,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Exit',
                          command=lambda: exit_button()).grid(row=5,column=2)

lblspace=tkinter.Label(f2bottom,text='\n\n\n\n\n\n\n\n\n')
lblspace.grid(row=5,column=0)
root.mainloop()