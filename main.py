import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("chords")
        #setting window size
        width=600
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        DoKey=tk.Button(root)
        DoKey["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        DoKey["font"] = ft
        DoKey["fg"] = "#000000"
        DoKey["justify"] = "center"
        DoKey["text"] = "Do"
        DoKey.place(x=60,y=40,width=50,height=100)
        DoKey["command"] = self.DoKey_command

        ReKey=tk.Button(root)
        ReKey["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        ReKey["font"] = ft
        ReKey["fg"] = "#000000"
        ReKey["justify"] = "center"
        ReKey["text"] = "Re"
        ReKey.place(x=120,y=40,width=50,height=100)
        ReKey["command"] = self.ReKey_command

        MiKey=tk.Button(root)
        MiKey["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        MiKey["font"] = ft
        MiKey["fg"] = "#000000"
        MiKey["justify"] = "center"
        MiKey["text"] = "Mi"
        MiKey.place(x=180,y=40,width=50,height=100)
        MiKey["command"] = self.MiKey_command

        FaKey=tk.Button(root)
        FaKey["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        FaKey["font"] = ft
        FaKey["fg"] = "#000000"
        FaKey["justify"] = "center"
        FaKey["text"] = "Fa"
        FaKey.place(x=240,y=40,width=50,height=100)
        FaKey["command"] = self.FaKey_command

        SolKey=tk.Button(root)
        SolKey["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        SolKey["font"] = ft
        SolKey["fg"] = "#000000"
        SolKey["justify"] = "center"
        SolKey["text"] = "Sol"
        SolKey.place(x=300,y=40,width=50,height=100)
        SolKey["command"] = self.SolKey_command

        LaKey=tk.Button(root)
        LaKey["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        LaKey["font"] = ft
        LaKey["fg"] = "#000000"
        LaKey["justify"] = "center"
        LaKey["text"] = "La"
        LaKey.place(x=360,y=40,width=50,height=100)
        LaKey["command"] = self.LaKey_command

        SiKey=tk.Button(root)
        SiKey["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        SiKey["font"] = ft
        SiKey["fg"] = "#000000"
        SiKey["justify"] = "center"
        SiKey["text"] = "Si"
        SiKey.place(x=420,y=40,width=50,height=100)
        SiKey["command"] = self.SiKey_command

        DoDKey=tk.Button(root)
        DoDKey["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        DoDKey["font"] = ft
        DoDKey["fg"] = "#ffffff"
        DoDKey["justify"] = "center"
        DoDKey["text"] = "Do#"
        DoDKey.place(x=100,y=40,width=30,height=60)
        DoDKey["command"] = self.DoDKey_command

        ReDKey=tk.Button(root)
        ReDKey["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        ReDKey["font"] = ft
        ReDKey["fg"] = "#ffffff"
        ReDKey["justify"] = "center"
        ReDKey["text"] = "Re#"
        ReDKey.place(x=160,y=40,width=30,height=60)
        ReDKey["command"] = self.ReDKey_command

        FaDKey=tk.Button(root)
        FaDKey["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        FaDKey["font"] = ft
        FaDKey["fg"] = "#ffffff"
        FaDKey["justify"] = "center"
        FaDKey["text"] = "Fa#"
        FaDKey.place(x=280,y=40,width=30,height=60)
        FaDKey["command"] = self.FaDKey_command

        SolDKey=tk.Button(root)
        SolDKey["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        SolDKey["font"] = ft
        SolDKey["fg"] = "#ffffff"
        SolDKey["justify"] = "center"
        SolDKey["text"] = "Sol#"
        SolDKey.place(x=340,y=40,width=30,height=60)
        SolDKey["command"] = self.SolDKey_command

        LaDKey=tk.Button(root)
        LaDKey["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        LaDKey["font"] = ft
        LaDKey["fg"] = "#ffffff"
        LaDKey["justify"] = "center"
        LaDKey["text"] = "La#"
        LaDKey.place(x=400,y=40,width=30,height=60)
        LaDKey["command"] = self.LaDKey_command

    def DoKey_command(self):
        return


    def ReKey_command(self):
        return


    def MiKey_command(self):
        return


    def FaKey_command(self):
        return


    def SolKey_command(self):
        return


    def LaKey_command(self):
        return


    def SiKey_command(self):
        return


    def DoDKey_command(self):
        return


    def ReDKey_command(self):
        return


    def FaDKey_command(self):
        return


    def SolDKey_command(self):
        return


    def LaDKey_command(self):
        return

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
