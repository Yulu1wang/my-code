from tkinter import *
import tkinter
import random
import tkinter.messagebox

class main_interface(object):

    def __init__(self):
        self.flag=-1
        self.mark=0
        self.a=1
        self.snum=0
        self.b=2

    def show(self,window):
        print("your student number is", self.entry.get())
        self.snum = self.entry.get()
        window.destroy()
        mainloop()

    def open_info_box(self):
        window = tkinter.Tk()
        window.title('Please input your student number')
        window.geometry('400x200')
        self.entry = tkinter.Entry(window, width=20)
        self.entry.place(x=30, y=30)
        button = Button(window, width=8, height=1, command=lambda: self.show(window), text='Done')
        button.place(x=60, y=100)
        window.mainloop()

    def rand_answer(self):
        answer = random.randint(1, 4)
        return answer

    def answer_jud(self,num, answer, test):
        #print(num)
        if num == answer:
            #print(num,answer)
            self.mark += 10
            print('Correct, the sum mark is：{}'.format(self.mark))
            self.flag =-1
            test.destroy()
            if self.a != 5:
                self.a += 1
                self.page()

            return
        else:
            self.flag=0
            tkinter.messagebox.showinfo('Wrong','The correct answer is answer{}'.format(answer))
            #print('Wrong,The correct answer is{}'.format(answer))
            test.destroy()
            if self.a != 5:
                self.a += 1
                self.page()

            return

    def page(self):
        num = [1, 2, 3, 4]
        answer = self.rand_answer()
        print('the right answer is No.{}'.format(answer))
        test = Tk()
        test.geometry('600x400')
        test.title("Test{}".format(self.a))  #
        text = tkinter.Label(test, bd=40, fg='red', bg='white', text="Question{}".format(self.a))
        text.place(relx=0.38, rely=0.2)
        button1 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[0], answer, test),text='answer1')
        button1.place(relx=0.45, rely=0.5)
        button2 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[1], answer, test),text='answer2')
        button2.place(relx=0.45, rely=0.6)
        button3 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[2], answer, test),text='answer3')
        button3.place(relx=0.45, rely=0.7)
        button4 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[3], answer, test),text='answer4')
        button4.place(relx=0.45, rely=0.8)

    def open_test_box(self):
        num=[1,2,3,4]
        answer = self.rand_answer()
        print('the right answer is No.{}'.format(answer))
        test = Tk()
        test.geometry('600x400')
        test.title("Test{}".format(self.a))  #
        text = tkinter.Label(test, bd=40, fg='red', bg='white', text="Question1")
        text.place(relx=0.38, rely=0.2)
        button1 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[0], answer, test), text='Answer1')
        button1.place(relx=0.45, rely=0.5)
        #print('button1 ', self.flag)
        button2 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[1], answer, test), text='Answer2')
        button2.place(relx=0.45, rely=0.6)
        #print('button2 ', self.flag)
        button3 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[2], answer, test),text='Answer3')
        button3.place(relx=0.45, rely=0.7)
        #print('button3 ', self.flag)
        button4 = Button(test, width=8, height=1, command=lambda: self.answer_jud(num[3], answer, test),text='Answer4')
        button4.place(relx=0.45, rely=0.8)
        #print('button4 ', self.flag)
        test.mainloop()

    def open_result_box(self):
        window = tkinter.Tk()
        window.title('Result')
        window.geometry('400x100')
        text = tkinter.Label(window,bd=4,fg='red',bg='white',text="Your student ID is: {}, and your final mark is: {}".format(self.snum,self.mark))
        text.place(relx=0.2,rely=0.2)
        if self.mark < 30 :
            tkinter.messagebox.showinfo('Sorry', 'Sorry, you failed！')
        if self.mark >= 30 and self.mark < 50:
            tkinter.messagebox.showinfo('Congratulations', 'you pass the test！')
        if self.mark == 50:
            tkinter.messagebox.showinfo('1111111111111','Congratulations, All correct!')
        if self.mark >= 60:
            tkinter.messagebox.showinfo('1111111111111','How dare you! Dont cheat!!!!')


if __name__ == '__main__':
    top = Tk()
    top.title("Test System")
    top.geometry('400x100')
    ma=main_interface()
    info = Button(top, text="Input your Info", fg="tomato", width=20, height=1, command=lambda: ma.open_info_box())
    info.pack()
    start = Button(top, text="Start", fg="black", command=lambda:ma.open_test_box())
    start.pack()
    result = Button(top, text="Result", fg="tomato", command=lambda:ma.open_result_box())
    result.pack()
    top.mainloop()
