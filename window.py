from tkinter import Label, Button
from ip import IP


class Window:

    def __init__(self, window):

        window.title("Get Private and Public IP")

        window.geometry('300x300')

        lbl = Label(window, text="Hi, this little script use python built-in libraries to \nget private IP and Public IP from the device running it.")

        lbl.grid(column=1, row=1)

        btn = Button(window, text="Get IP", command=lambda: self.clicked(window))

        btn.grid(column=1, row=2)

    def clicked(self, window):
        
        ip = IP()
        #private ip
        private = Label(window, text="Private IP: "+ip.lan_ip)
        private.grid(column=1, row=3)
        #public ip
        private = Label(window, text="Public IP: "+ip.wan_ip)
        private.grid(column=1, row=4)
        