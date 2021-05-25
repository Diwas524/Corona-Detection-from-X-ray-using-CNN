import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import model


Height=735
Width=1375


root1=tk.Tk()
root1.attributes("-fullscreen", True)

root1.geometry('1366x768')
root1.title("COVID 19")
background_image1=tk.PhotoImage(file=('suru.png'))
background_label1=tk.Label(root1,image=background_image1)
background_label1.place(relwidth=1,relheight=1)

f1=Frame(root1)
f1.grid(row=0,column=0)




#Button(f1, text='Proceed',command=lambda:swap(f2)).pack()
frame4=tk.Frame(root1,bd=5,bg='gray')
frame4.place(relx=0.516, rely=0.8, relwidth=0.2, relheight=0.1 , anchor='n')




Button2 = tk.Button(frame4,text='PROCEED',font=("bold", 30),bg='skyBlue1',command=lambda:create())
Button2.place(relx=0,rely=0,relwidth=1, relheight=1)


frame_5=tk.Frame(root1,bd=5,bg='gray')
frame_5.place(relx=0.93, rely=0.88, relwidth=0.08, relheight=0.08 , anchor='n')



button_3 = tk.Button(frame_5, text="Exit",font=("bold", 30),command=root1.destroy)
button_3.place(relx=0,rely=0,relwidth=1, relheight=1)




def create():


	def change(*args):
	    global home
	    home = var.get()
	    


	
	    
	def frame11():
		root2=Toplevel(root1)
		canvs=tk.Canvas(root2,height=Height,width=Width)
		canvs.pack()

		root2.title(" Corona Detection ")
		root2.geometry('0x0')
		


		background_image=tk.PhotoImage(file='corona.png')
		background_label=tk.Label(root2,image=background_image)
		background_label.place(relwidth=1,relheight=1)
		root2.mainloop()
		
	
	root=Toplevel(root1)
	canvs=tk.Canvas(root,height=Height,width=Width)
	canvs.pack()

	root.title(" Corona Detection ")
	root.attributes("-fullscreen", True)


	background_image=tk.PhotoImage(file='corona.png')
	background_label=tk.Label(root,image=background_image)
	background_label.place(relwidth=1,relheight=1)

	OPTIONS=[
		"0.jpeg",
		"1.jpeg",
		"2.jpeg",
		'3.jpeg',
		"4.jpeg",
		"5.jpeg",
		"6.jpeg",
		"7.jpeg",
		"8.jpeg",
		"9.jpg",
		
		]


	var=tk.StringVar(root)
	var.set(OPTIONS[0])
	var.trace("w",change)

	frame2=tk.Frame(root,bd=5,bg='peach puff')
	frame2.place(relx=0.2252, rely=0.28, relwidth=0.263, relheight=0.08 , anchor='n')

	
	dropDownMenu=tk.OptionMenu(frame2,var,OPTIONS[0],OPTIONS[1],OPTIONS[2],OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8],OPTIONS[9])
	dropDownMenu.config(width=6,)
	dropDownMenu.place(relx=0,rely=0,relwidth=1, relheight=1)


	frame=tk.Frame(root,bd=5,bg='green')
	frame.place(relx=0.502, rely=0.48, relwidth=0.198, relheight=0.1 , anchor='n')

	label_7 = Label(root, text="DETECT CORONA PATIENT", width=24, font=("bold", 15),bg='skyBlue1')
	label_7.place(x=550,y=340)

	photo22=tk.PhotoImage(file='np.png')
	button2 = tk.Button(frame, text="Predict",image=photo22,command=lambda:result_function(home))
	button2.place(relx=0,rely=0,relwidth=1, relheight=1)

	

	label_7 = Label(root, text="SELECT IMAGE ", width=20, font=("bold", 20),bg='peach puff')
	label_7.place(x=130, y=185)

	

	frame3=tk.Frame(root,bd=5,bg='gray')
	frame3.place(relx=0.93, rely=0.88, relwidth=0.08, relheight=0.08 , anchor='n')

	
	button1 = tk.Button(frame3, text="Exit",font=("bold", 30),command=root.destroy)
	button1.place(relx=0,rely=0,relwidth=1, relheight=1)

	def result_function(home):
		predict = model.predictwin(home)
		if predict==1:
			frame=tk.Frame(root,bd=5,bg='gray')
			frame.place(relx=0.502, rely=0.65, relwidth=0.325, relheight=0.21 , anchor='n')

			label_1 = Label(root, text="RESULT ", width=30, font=("bold", 15),bg='peach puff')
			label_1.place(x=463, y=480)
			photo2=tk.PhotoImage(file='positive.png')
			button = tk.Button(frame, text="result",image=photo2)
			button.place(relx=0,rely=0,relwidth=1, relheight=1)
			print("You tested corona Positive")
			label_2=Label(root,width=25, font=("bold", 20),bg='Azure3')
			label_2['text']="You tested corona Positive"
			label_2.place(x=463, y=510)
		else:
			frame=tk.Frame(root,bd=5,bg='gray')
			frame.place(relx=0.502, rely=0.65, relwidth=0.325, relheight=0.21 , anchor='n')

			label_1 = Label(root, text="RESULT ", width=40, font=("bold", 15),bg='peach puff')
			label_1.place(x=463, y=480)
			photo2=tk.PhotoImage(file='n.png')
			button = tk.Button(frame, text="result",image=photo2)
			button.place(relx=0,rely=0,relwidth=1, relheight=1)
			print("You tested corona Negative")
			label_2=Label(root,width=25, font=("bold",20),bg='Azure3')
			label_2['text']="You tested corona Negative"
			label_2.place(x=463, y=510)
		
		frame11()


	root.mainloop()







root1.mainloop()
