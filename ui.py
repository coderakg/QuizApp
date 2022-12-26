from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain) :
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizApp")
        self.window.minsize(width=500,height=500)
        self.window.config(padx=50,pady=50,bg=THEME_COLOR)
        
        self.quiz_app = Label(text="QuizApp",font=("Arial",20,"italic"),bg=THEME_COLOR,fg="black")
        self.quiz_app.grid(column=0,row=0,pady=10)
        
        self.score = Label(text="Score:0",font=("Arial",20,"italic"),bg=THEME_COLOR,fg="white")
        self.score.grid(column=1,row=0)
        
        self.canvas = Canvas(width=400,height=400,bg="white")
        self.question_text = self.canvas.create_text(200,200,text="Some question",width=380,font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2)

        self.right_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=self.right_img,highlightthickness=0,command=self.true_btn)
        self.right_btn.grid(column=0,row=2,padx=10,pady=10) 

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=self.wrong_img,highlightthickness=0,padx=10,pady=10,command=self.false_btn)
        self.wrong_btn.grid(column=1,row=2,padx=10,pady=10)
        
        self.hscore = Label(text=f"High Score: {self.quiz.high_score} ",font=("Arial",20,"italic"),bg=THEME_COLOR,fg="white")
        self.hscore.grid(column=0,row=3,columnspan=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question() 
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.score.config(text=f"Score:{self.quiz.score}")
        else:
            self.score.config(text=f"Score:{self.quiz.score}")
            self.canvas.config(bg="white")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
            self.canvas.itemconfig(self.question_text,text=f"You've completed the quiz \n Your final score is : {self.quiz.score}/10 ")
            with open("score.txt") as file:
                self.hs = file.read(int(file.read()))
            self.hscore.config(text=f"High Score: {self.hs}")
            self.quiz.highscore()
        
    def true_btn(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_btn(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
     
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        
    
        

        
        
