from tkinter import *
import os
import sys

root=Tk()
root.title("OS Project")
root.geometry("400x200")
prompt=Label(root,text="This is the Multi threaded Download Manager",font=("Times New Roman",12,"bold"))
prompt1=Label(root,text="",font=("Times New Roman",12))

prompt.grid(row=0,columnspan=5)
prompt1.grid(row=1,columnspan=5)



lab1=Label(root,text="Url of file :",fg="blue")
lab2=Label(root,text="No of threads :",fg="blue")
lab3=Label(root,text="Save As :",fg="blue")

url=StringVar()
name=StringVar()
nthread=StringVar()

entry1=Entry(root,textvariable=url)
entry2=Entry(root,textvariable=nthread)
entry3=Entry(root,textvariable=name)


lab1.grid(row=2,sticky=E)
lab2.grid(row=3,sticky=E)
lab3.grid(row=4,sticky=E)

entry1.grid(row=2,column=1,sticky=E) 
entry2.grid(row=3,column=1,sticky=E)
entry3.grid(row=4,column=1,sticky=E)

def printt():
	print("Downloading")
	os.system("python Projectver1.0.py --number_of_threads "+str(nthread.get())+" --name "+str(name.get())+" "+str(url.get()))	
	sys.exit()


frame=Frame(root)
frame.grid()
download_button=Button(frame, text="Download",fg="green",command=printt)
quit=Button(frame,text="Cancel",fg="red",command=frame.quit)
#	bu=Button(frame)
download_button.grid(row=5,column=0,sticky=E+W)
quit.grid(row=5,column=1,sticky=E+W)

status=Label(root,text= "Developed by Kaushal Patel and Naitik Dodia",bd=1,relief=SUNKEN, anchor=W)
status.grid(columnspan=8,sticky=W)
#frame.grid_rowconfigure(0, weight=1)
#frame.grid_columnconfigure(0, weight=1)
root.mainloop()
