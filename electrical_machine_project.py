from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import tkinter
from tkinter import *

a = Tk()
a.title("Page: 1/5")
a.geometry("900x600")
a.configure(bg = "#b4e014")

def take_input():
    reg = Tk()
    reg.title("Page: 2/5")
    reg.geometry("900x650")
    reg.configure(bg = "#b4e014")

    Label(reg, text = "Enter Data Points:", font = ("Times New Roman",36,"bold"), fg = "black", bg = "#b4e014").place(x = 50, y = 10)

    Label(reg, text = "Open Circuit Characteristics Parameters", font = ("Times New Roman",28,"bold"), fg = "black", bg = "#b4e014").place(x = 50, y = 60)
    Label(reg, text = "(Minimum 6 Points Separate Using Spaces)", font = ("Times New Roman",12,"bold"), fg = "black", bg = "#b4e014").place(x = 50, y = 105)
    Label(reg, text = "Type Of Voltage              :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 130)
    Label(reg, text = "Open Circuit Voltage      :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 160)
    Label(reg, text = "Field Current                   :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 190)

    Label(reg, text = "Zero Power Factor Characteristics Parameters", font = ("Times New Roman",28,"bold"), fg = "black", bg = "#b4e014").place(x = 50, y = 220)
    Label(reg, text = "(Minimum 6 Points Separate Using Spaces)", font = ("Times New Roman",12,"bold"), fg = "black", bg = "#b4e014").place(x = 50, y = 260)
    Label(reg, text = "ZPF Terminal Voltage     :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 285)
    Label(reg, text = "Field Current                   :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 315)

    Label(reg, text = "Extra Inputs", font = ("Times New Roman",28,"bold"), fg = "black", bg = "#b4e014").place(x = 50, y = 340)
    Label(reg, text = "Pitch Factor                    :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y =385)
    Label(reg, text = "Distribution Factor         :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 415)
    Label(reg, text = "Rotor Slots per Pole       :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 445)
    Label(reg, text = "Total no.of Conductors  :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 119, y = 475)
    Label(reg, text = "Rated Armature Current :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 119, y = 505)
    Label(reg, text = "Rated Terminal Voltage  :", font = ("Times New Roman",16,"bold"), fg = "black", bg = "#b4e014").place(x = 120, y = 535)

    options = ["Line","Phase"]
    clicked = StringVar(reg)
    clicked.set( "Line" )
    drop = OptionMenu(reg, clicked, *options )
    drop.place(x = 375, y = 130, height = 25, width = 100)

    text1 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text1.place(x = 375, y = 160, height = 25, width = 400)

    text2 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text2.place(x = 375, y = 190, height = 25, width = 400)

    text3 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text3.place(x = 375, y = 285, height = 25, width = 400)

    text4 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text4.place(x = 375, y = 315, height = 25, width = 400)

    text5 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text5.place(x = 375, y = 385, height = 25, width = 400)

    text6 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text6.place(x = 375, y = 415, height = 25, width = 400)

    text7 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text7.place(x = 375, y = 445, height = 25, width = 400)

    text8 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text8.place(x = 375, y = 475, height = 25, width = 400)

    text9 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text9.place(x = 375, y = 505, height = 25, width = 400)

    text10 = Entry(reg, font = ("Times New Roman",16,"bold"), fg = "black", bg = "white")
    text10.place(x = 375, y = 535, height = 25, width = 400)

    def clearAll():
        text1.delete(0, END)
        text2.delete(0, END)
        text3.delete(0, END)
        text4.delete(0, END)
        text5.delete(0, END)

    def enter():
        root = Tk()
        root.title("Page: 3/5")
        root.geometry("900x600")
        root.configure(bg = "#b4e014")

        ocv = text1.get()
        ofc = text2.get()
        zv = text3.get()
        zfc = text4.get()
        pf = text5.get()
        df = text6.get()
        rsp = text7.get()
        tnc = text8.get()
        rac = text9.get()
        rtv = text10.get()
        vtype = clicked.get()

        if(vtype=="Line"):
            Voc1 = np.array(list(map(float,ocv.strip().split())))
            Voc1 = np.array([v/(3**0.5) for v in Voc1 ])

        else:
            Voc1 = np.array(list(map(float,ocv.strip().split())))

        If1 =np.array(list(map(float,ofc.strip().split())))

        if(vtype=="Line"):
            Voc2 = np.array(list(map(float,zv.strip().split())))
            Voc2 = np.array([v/(3**0.5) for v in Voc2 ])

        else:
            Voc2 = np.array(list(map(float,zv.strip().split())))

        If2=np.array(list(map(float,zfc.strip().split())))

        kp=float(pf)
        kb=float(df)
        n=float(rsp)
        z=float(tnc)
        Ia=float(rac)

        Vr=float(rtv)
        Vr=np.array([Vr]*len(If2))
        I=If2

        from scipy.interpolate import make_interp_spline

        xnew1 = np.linspace(min(If1), max(If1), 300)
        spl1 = make_interp_spline(If1, Voc1, k=3)
        ynew1 = spl1(xnew1)

        xnew2 = np.linspace(min(If2), max(If2), 300)
        spl2 = make_interp_spline(If2, Voc2, k=3)
        ynew2 = spl2(xnew2)

        xnewr = np.linspace(min(I), max(I), 300)
        splr = make_interp_spline(I, Vr, k=3)
        ynewr = splr(xnewr)

        from shapely.geometry import  LineString

        line_1 = LineString(np.column_stack((ynewr, xnewr)))
        line_2 = LineString(np.column_stack((ynew2, xnew2)))
        intersection = line_1.intersection(line_2)

        x,y = intersection.xy

        xbase=[y[0]-4,y[0]]
        ybase=[x[0],x[0]]

        x_air=[If1[0],If1[1]]
        y_air=[Voc1[0],Voc1[1]]

        ordinate = np.subtract(y_air[1], y_air[0])
        abscissa = np.subtract(x_air[1], x_air[0])
        slope = ordinate/abscissa

        m = xbase[0]
        p = ybase[0]

        x_left = np.array([xbase[0], xbase[0]+2])
        y_left = np.array(slope*(x_left - m) + p)

        line_3 = LineString(np.column_stack((y_left, x_left)))
        line_4 = LineString(np.column_stack((ynew1, xnew1)))
        intersection = line_3.intersection(line_4)

        x1,y1 = intersection.xy

        y_right=[x1[0],x[0]]
        x_right=[y1[0],y[0]]

        x_perp=[y1[0],y1[0]]
        y_perp=[x1[0],x[0]]

        x_occ = [y[0],y[0]]
        y_occ = [x[0],x[0]+150]

        line_5 = LineString(np.column_stack((y_occ, x_occ)))
        line_6 = LineString(np.column_stack((ynew1, xnew1)))
        intersection = line_5.intersection(line_6)

        x2,y2 = intersection.xy

        B=(y[0],x[0])
        C=(y[0]-4,x[0])
        D=(y1[0],x1[0])
        H=(y1[0],x[0])

        BH=((B[0]-H[0])**2 + (B[1]-H[1])**2)**0.5
        CH=((C[0]-H[0])**2 + (C[1]-H[1])**2)**0.5
        DH=((D[0]-H[0])**2 + (D[1]-H[1])**2)**0.5
        DH=round(DH,3)

        Xl = DH/Ia
        Xl=round(Xl, 3)

        kw=kp*kb
        i=BH
        f=(4/3.14)*(n*z*i*kw)/2

        y_f = [0,max(ynew1)]
        x_f = [f,f]

        line_7 = LineString(np.column_stack((y_f, x_f)))
        line_8 = LineString(np.column_stack((ynew1, xnew1)))
        intersection4 = line_7.intersection(line_8)

        x3,y3 = intersection4.xy

        E=x3[0]
        Xar = E/Ia
        E=round(E, 3)
        Xar=round(Xar, 3)

        fig = Figure(figsize=(6, 5), dpi=100)
        fig1=fig.add_subplot(111)
        fig1.plot(xnew1,ynew1,label = 'OCC Curve')
        fig1.plot(xnew2,ynew2,label = 'ZPFC Curve')
        fig1.set_title('OCC and ZPFC Curves')
        fig1.set_ylabel('Voltage (V)')
        fig1.set_xlabel('Field Current (If)')
        fig.add_subplot(111).legend()
        fig.add_subplot(111).grid()

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        def on_key_press(event):
            key_press_handler(event, canvas)

        canvas.mpl_connect("key_press_event", on_key_press)

        def potier():
            pot = Tk()
            pot.title("Page: 4/5")
            pot.geometry("900x600")
            pot.configure(bg = "#b4e014")

            fig = Figure(figsize=(5, 4), dpi=100)
            fig2 = fig.add_subplot(111)
            fig2.plot(xnew1,ynew1,label = 'OCC Curve')
            fig2.plot(xnew2,ynew2,label = 'ZPFC Curve')
            fig2.plot(xbase,ybase)
            fig2.plot(x_air,y_air,linestyle="--")
            fig2.plot(x_left,y_left)
            fig2.plot(x_right,y_right)
            fig2.plot(x_perp,y_perp)
            fig2.set_title('OCC and ZPFC Curves with Potier Triangle')
            fig2.set_ylabel('Voltage (V)')
            fig2.set_xlabel('Field Current (If)')
            fig.add_subplot(111).legend()
            fig.add_subplot(111).grid()

            canvas = FigureCanvasTkAgg(fig, master=pot)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

            toolbar = NavigationToolbar2Tk(canvas, pot)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

            def on_press(event):
                key_press_handler(event, canvas)

            canvas.mpl_connect("key_press_event", on_press)

            def output():
                op = Tk()
                op.title("Page: 5/5")
                op.geometry("900x600")
                op.configure(bg = "#b4e014")

                def _quit():
                    op.quit()
                    op.destroy()
                    pot.quit()
                    pot.destroy()
                    root.quit()
                    root.destroy()
                    reg.quit()
                    reg.destroy()
                    a.quit()
                    a.destroy()


                Label(op, text = "Outputs:", font = ("Times New Roman",36,"bold"), fg = "black", bg = "#b4e014").place(x = 60, y = 30)
                Label(op, text = "Leakage Reactance                  = ", font = ("Times New Roman",20,"bold"), fg = "black", bg = "#b4e014").place(x = 100, y = 100)
                Label(op, text = Xl, font = ("Times New Roman",20,"bold"), fg = "black", bg = "#b4e014").place(x = 520, y = 100)
                Label(op, text = "Ohm", font = ("Times New Roman",20,"bold"), fg = "black", bg = "#b4e014").place(x = 600, y = 100)
                Label(op, text = "Armature Reaction Reactance = ", font = ("Times New Roman",20,"bold"), fg = "black", bg = "#b4e014").place(x = 100, y = 140)
                Label(op, text = Xar, font = ("Times New Roman",20,"bold"), fg = "black", bg = "#b4e014").place(x = 520, y = 140)
                Label(op, text = "Ohm", font = ("Times New Roman",20,"bold"), fg = "black", bg = "#b4e014").place(x = 608, y = 140)

                Button(op, text = "NEW INPUT", font = ("Times New Roman",24,"bold"), fg = "white", bg = "black", command = take_input).place(x = 100, y = 460)
                Button(op, text = "EXIT", font = ("Times New Roman",24,"bold"), fg = "white", bg = "black", command = _quit).place(x = 700, y = 460)

            Button(pot, text = "PROCEED", font = ("Times New Roman",24,"bold"), fg = "white", bg = "black", command = output).pack(side=tkinter.BOTTOM)


        Button(root, text = "PROCEED", font = ("Times New Roman",24,"bold"), fg = "white", bg = "black", command = potier).pack(side=tkinter.BOTTOM)

    Button(reg, text = "CLEAR", font = ("Times New Roman",24,"bold"), fg = "white", bg = "black", command = clearAll).place(x = 120, y = 570)
    Button(reg, text = "ENTER", font = ("Times New Roman",24,"bold"), fg = "white", bg = "black", command = enter).place(x = 640, y = 570)

Label(a, text = "ELECTRICAL MACHINES-II PROJECT", font = ("Times New Roman",35,"bold"), fg = "black", bg = "#b4e014").place(x = 20, y = 50)
Label(a, text = "OCC and ZPFC CURVES with POTIER TRIANGLE", font = ("Times New Roman",26,"bold"), fg = "black", bg = "#b4e014").place(x = 48, y = 150)
Label(a, text = "Guided By: Shubhobrata Rudra", font = ("Times New Roman",20,"bold"), fg = "black", bg = '#b4e014').place(x = 70, y = 285)
Label(a, text = "Submitted By:", font = ("Times New Roman",20,"bold"), fg = "black", bg = '#b4e014').place(x = 640, y = 280)
Label(a, text = "Annesha Sahu", font = ("Times New Roman",16,"bold"), fg = "black", bg = '#b4e014').place(x = 650, y = 320)
Label(a, text = "Priya Ranjan", font = ("Times New Roman",16,"bold"), fg = "black", bg = '#b4e014').place(x = 650, y = 350)
Label(a, text = "Madhusmita Barik", font = ("Times New Roman",16,"bold"), fg = "black", bg = '#b4e014').place(x = 650, y = 380)
Label(a, text = "Amanjeet Pani", font = ("Times New Roman",16,"bold"), fg = "black", bg = '#b4e014').place(x = 650, y = 410)

Button(a, text = "PROCEED", font = ("Times New Roman",28,"bold"), fg = "white", bg = "black", command = take_input).place(x = 346, y =460)

a.mainloop()
