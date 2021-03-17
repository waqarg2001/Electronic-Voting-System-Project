from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('finalpollings0.db')
cursor = conn.cursor()
#cursor.execute("""CREATE TABLE candidatesfinal (
#   name DATATYPE text NOT NULL,
#  counts DATATYPE integer NOT NULL) """)
#conn.commit()

# window size
root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))
root.title('Electronic Voting System')

bg = PhotoImage(file='C:/Users/intel/Desktop/vote.png')
label = Label(root, image=bg)
label.place(x=-400, y=-30)

loginImage = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_login (5).png')
CEImage = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_create-election (2).png')
aboutuspic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_about-us.png')
exitpic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_exit.png')
submitpic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_submit.png')
backpic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_back (1).png')
votepic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_vote.png')
resltspic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_results.png')
graphspic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_graphs.png')
confirmpic = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_confirm.png')
prev = PhotoImage(file='C:/Users/intel/Desktop/Vote/button_previous-elections .png')
root.wm_iconbitmap('C:/Users/intel/Desktop/Vote/voting hand.ico')


# initial login
def login():
    # close button
    def close():
        root.destroy()

    # create new election
    def newelec():

        br1.place_forget()
        createE.place_forget()
        prevE.place_forget()
        about.place_forget()
        lf1 = LabelFrame(root, borderwidth=1, relief='ridge')
        lf1.place(x=590, y=200, height=350, width=400)
        qname = Label(lf1, text='Name of Election', font=('Helvetica', 10, 'bold'))
        qname.place(x=158, y=0)
        nameentry = Entry(lf1, width=40)
        nameentry.place(x=100, y=20)
        qcan = Label(lf1, text='Provide name of the candidates', font=('Helvetica', 10, 'bold'))
        qcan.place(x=110, y=70)
        lc1 = Label(lf1, text='Candidate 1')
        lc1.place(x=0, y=100)
        ec1 = Entry(lf1, width=40)
        ec1.place(x=100, y=100)
        lc2 = Label(lf1, text='Candidate 2')
        lc2.place(x=0, y=150)
        ec2 = Entry(lf1, width=40)
        ec2.place(x=100, y=150)
        lc3 = Label(lf1, text='Candidate 3')
        lc3.place(x=0, y=200)
        ec3 = Entry(lf1, width=40)
        ec3.place(x=100, y=200)
        lc4 = Label(lf1, text='Candidate 4', pady=10)
        lc4.place(x=0, y=240)
        ec4 = Entry(lf1, width=40)
        ec4.place(x=100, y=240)

        # submit vote to database
        def submit1():

            c1 = ec1.get()
            c2 = ec2.get()
            c3 = ec3.get()
            c4 = ec4.get()
            nameelec = nameentry.get()

            def vote():
                chose = choose.get()
                conn = sqlite3.connect('finalpollings0.db')
                cursor = conn.cursor()

                command = 'UPDATE candidatesfinal SET counts=counts+1 WHERE name=?'
                cursor.execute(command, (chose,))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success!', 'Your vote has been casted!')
                choose.set(0)

            lf1.place_forget()

            lf2 = LabelFrame(root, borderwidth=1, relief='ridge')
            lf2.place(x=550, y=200, height=300, width=440)
            lq = Label(lf2, text='Please cast your vote', font=('Helvetica', 10, 'bold'))
            lq.place(x=160, y=0)
            choose = StringVar()

            r1 = Radiobutton(lf2, text=c1, variable=choose, value=c1)
            r1.place(x=10, y=30)
            r2 = Radiobutton(lf2, text=c2, variable=choose, value=c2)
            r2.place(x=10, y=80)
            r3 = Radiobutton(lf2, text=c3, variable=choose, value=c3)
            r3.place(x=10, y=130)
            r4 = Radiobutton(lf2, text=c4, variable=choose, value=c4)
            r4.place(x=10, y=180)

            l = Label(lf2, text='')
            l.grid(row=5, column=0)
            l2 = Label(lf2, text='')
            l2.grid(row=6, column=0)
            conn = sqlite3.connect('finalpollings0.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO candidatesfinal VALUES (?,?)", (c1, 0))
            cursor.execute("INSERT INTO candidatesfinal VALUES (?,?)", (c2, 0))
            cursor.execute("INSERT INTO candidatesfinal VALUES (?,?)", (c3, 0))
            cursor.execute("INSERT INTO candidatesfinal VALUES (?,?)", (c4, 0))
            conn.commit()
            conn.close()

            # generate results
            def genrslt():

                m = messagebox.askquestion('Generate results', 'Are you sure you want to generate results?',
                                           icon='warning')
                if m == 'yes':

                    log = Toplevel()
                    log.title('Confirmation')

                    log.geometry('+%d+%d' % (650, 300))
                    confirmu = Label(log, text=' Username', padx=10)
                    confirmu.grid(row=1, column=0)
                    confirmp = Label(log, text='Password')
                    confirmp.grid(row=2, column=0)
                    eu = Entry(log, width=30)
                    eu.grid(row=1, column=1, padx=5)
                    ep = Entry(log, width=30, show='*')
                    ep.grid(row=2, column=1)

                    # confirmation to generate results
                    def login1():
                        if ((eu.get() != 'a') and (eu.get() != 'a')):
                            messagebox.showerror('ERROR', 'Incorrect Credentials')

                        else:
                            messagebox.showinfo('Confirmation', 'Credentials confirmed')
                            log.destroy()
                            lf1.place_forget()
                            lf2.place_forget()
                            conn = sqlite3.connect('finalpollings0.db')
                            cursor = conn.cursor()
                            cursor.execute('SELECT name, MAX(counts)  FROM candidatesfinal ')
                            a = cursor.fetchall()
                            conn.commit()
                            conn.close()
                            name = a[0][0]
                            votes = a[0][1]
                            winner = Label(root, text=f'{name.title()} has won this election with {votes} votes.',
                                           font=('Helvetica', 25, 'bold'), borderwidth=2, relief='solid')
                            winner.place(x=550, y=400)
                            who = f'{name.title()} won this election with {votes} votes.'
                            conn = sqlite3.connect('finalpollings0.db')
                            cursor = conn.cursor()
                           # cursor.execute("""CREATE TABLE prevelections (
                            #                name DATATYPE text NOT NULL,
                            #                winner DATATYPE text NOT NULL) """)
                            cursor.execute('INSERT INTO prevelections VALUES (?,?)', (nameelec, who))
                            conn.commit()

                            def graphs():
                                conn = sqlite3.connect('finalpollings0.db')
                                cursor = conn.cursor()
                                cursor.execute('SELECT name, counts FROM candidatesfinal')
                                data = cursor.fetchall()
                                names = []
                                counts = []
                                conn.commit()
                                conn.close()
                                for row in data:
                                    names.append((row[0]))
                                    counts.append(row[1])
                                plt.pie(counts, labels=names, autopct='%1.1f%%', shadow=True)
                                plt.show()
                                plt.bar(names, counts)
                                plt.ylabel('Votes')
                                plt.xlabel('Candidates')
                                plt.show()

                            graph = Button(root, image=graphspic, command=graphs, padx=25, pady=5, border=0,
                                           bg='white smoke'
                                           , activebackground='white smoke')
                            graph.place(x=430, y=600)

                            def exit():
                                conn = sqlite3.connect('finalpollings0.db')
                                cursor = conn.cursor()
                                cursor.execute('DELETE FROM candidatesfinal ')
                                conn.commit()
                                conn.close()
                                root.destroy()

                            exitt = Button(root, image=exitpic, command=exit, border=0, bg='#00acff',
                                           activebackground='#00acff')
                            exitt.place(x=1135, y=600)

                    b1 = Button(log, image=confirmpic, command=login1, border=0)
                    b1.grid(row=3, column=1, pady=15, ipadx=50)




                elif m == 'no':
                    messagebox.showinfo('Return', 'You can continue casting vote.')

            def back():
                conn = sqlite3.connect('finalpollings0.db')
                cursor = conn.cursor()
                cursor.execute('DELETE FROM candidatesfinal ')
                conn.commit()
                conn.close()
                lf2.place_forget()
                return newelec()

            back1 = Button(lf2, image=backpic, border=0, command=back)
            back1.place(x=30, y=245)
            vote = Button(lf2, image=votepic, command=vote, border=0)
            vote.place(x=177, y=245)
            rslt = Button(lf2, image=resltspic, command=genrslt, border=0)
            rslt.place(x=310, y=245)

        su1 = Button(lf1, image=submitpic, command=submit1, border=0)
        su1.place(x=160, y=300)

    def prevE():

        name = []

        window1 = Toplevel()
        conn = sqlite3.connect('finalpollings0.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM prevelections')
        a = cursor.fetchall()
        for i in a:
            name.append(i[0])
        name1 = StringVar()

        namechoosen = ttk.Combobox(window1, width=27, textvariable=name1)
        namechoosen.place(x=0, y=0)
        namechoosen['values'] = name

        def rslt():
            conn = sqlite3.connect('finalpollings0.db')
            cursor = conn.cursor()
            cursor.execute('SELECT winner FROM prevelections where name=?', (namechoosen.get(),))
            b = cursor.fetchall()

            lab1 = Label(window1, text=f'{b}')
            lab1.place(x=10, y=80)

        button0 = Button(window1, image=resltspic, command=rslt,border=0)
        button0.place(x=40, y=40)

        conn.commit()
        conn.close()

    if (e1.get() != 'a' or e2.get() != 'a'):
        messagebox.showerror('ERROR', 'Incorrect Credentials')
    else:
        messagebox.showinfo('Success!', 'Login Successful')
        frame.place_forget()

        br1 = Button(root, image=exitpic, command=close, border=0, bg='#00acff', activebackground='#00acff')
        br1.place(x=980, y=450)
        createE = Button(root, image=CEImage, border=0, command=newelec, bg='white smoke',
                         activebackground='white smoke')
        createE.place(x=490, y=300)

        def about():
            messagebox.showinfo('Developers', """
            Developed By:
            Waqar Gul       
            Shayan Jamil     
            Rizwan Ahmed  
            Umer Siddiqui 
            """)

        prevE = Button(root, image=prev, command=prevE, border=0, bg='White smoke', activebackground='white smoke')
        prevE.place(x=930, y=300)
        about = Button(root, image=aboutuspic, command=about, border=0, bg='White smoke',
                       activebackground='white smoke')
        about.place(x=515, y=450)


# close application by cross
def on_closing():
    conn = sqlite3.connect('finalpollings0.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM candidatesfinal ')
    conn.commit()
    conn.close()
    root.destroy()


# closing window through close x instead of exit button
root.protocol('WM_DELETE_WINDOW', on_closing)
l1 = Label(root, text='')
l1.grid(column=11)

# main label
l0 = Label(root, text='ELECTRONIC VOTING SYSTEM', font=('helvetica', 30, 'bold'), borderwidth=2, relief='solid',
           bg='Gray90')
l0.place(x=500)

# label frame for login
frame = LabelFrame(root, padx=10, pady=10, bg='gray90')
frame.place(x=650, y=320)

l1 = Label(frame, text=' Username', padx=10, bg='gray90')
l1.grid(row=1, column=0)
l2 = Label(frame, text='Password', bg='gray90')
l2.grid(row=2, column=0)

e1 = Entry(frame, width=30)
e1.grid(row=1, column=1, padx=5)
e2 = Entry(frame, width=30, show='*')
e2.grid(row=2, column=1)

b1 = Button(frame, image=loginImage, border=0, command=login, bg='gray90', height=0, width=1)
b1.grid(row=3, column=1, pady=10, ipadx=50, ipady=7)

root.mainloop()