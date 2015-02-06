#!/usr/bin/python2.7
#! -*- coding: utf-8 -*-
import Tkinter

def main():
    win = Tkinter.Tk()
    win.title("My tools")
    win.geometry('300x300+300+300')
    xinyun = Tkinter.StringVar(win)
    xinyun.set("猜猜我是谁")
    #banbie.set("10")
    cq_lblxinyun = Tkinter.Label(win, textvariable=xinyun, fg="red",
                          font=("黑体", 30, "bold"),
                          relief="sunken", borderwidth=5)
    cq_btstar = Tkinter.Button(win, text="开始抽签", font =("宋体", 14,
                      "normal"), command=chouqian)
    cq_lblban = Tkinter.Entry(win, textvariable=banbie, width="4",
                          font=("宋体", 12, "normal"))
    cq_lblban1 = Tkinter.Label(win, text="组", width="2", justify="left",
                          font=("宋体", 12, "normal"))
    win.mainloop()


if __name__ == "__main__":
    main()
