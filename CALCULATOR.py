import tkinter as MOSES_CALCULATOR

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    test_result.delete(1.0, "end")
    test_result.insert(1.0, calculation)
    

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        test_result.delete(1.0, "end")
        test_result.insert(1.0, result)
    except:
        clear_field()
        test_result.insert(1.0,"Error")    
    
def clear_field():
    global calculation
    calculation = ""
    test_result.delete(1.0, "end")


root = MOSES_CALCULATOR.Tk()
root.geometry("300x275")
test_result = MOSES_CALCULATOR.Text(root, height=2, width=17, font=("Arial",24))
test_result.grid(columnspan=5)

btn_1 = MOSES_CALCULATOR.Button(root, text="1",command=lambda: add_to_calculation(1), width=5, font=("Arial",14))
btn_1.grid(row=2,column=1)
btn_2 = MOSES_CALCULATOR.Button(root, text="2",command=lambda: add_to_calculation(2), width=5, font=("Arial",14))
btn_2.grid(row=2,column=2)
btn_3 = MOSES_CALCULATOR.Button(root, text="3",command=lambda: add_to_calculation(3), width=5, font=("Arial",14))
btn_3.grid(row=2,column=3)
btn_4 = MOSES_CALCULATOR.Button(root, text="4",command=lambda: add_to_calculation(4), width=5, font=("Arial",14))
btn_4.grid(row=3,column=1)
btn_5 = MOSES_CALCULATOR.Button(root, text="5",command=lambda: add_to_calculation(5), width=5, font=("Arial",14))
btn_5.grid(row=3,column=2)
btn_6 = MOSES_CALCULATOR.Button(root, text="6",command=lambda: add_to_calculation(6), width=5, font=("Arial",14))
btn_6.grid(row=3,column=3)
btn_7 = MOSES_CALCULATOR.Button(root, text="7",command=lambda: add_to_calculation(7), width=5, font=("Arial",14))
btn_7.grid(row=4,column=1)
btn_8 = MOSES_CALCULATOR.Button(root, text="8",command=lambda: add_to_calculation(8), width=5, font=("Arial",14))
btn_8.grid(row=4,column=2)
btn_9 = MOSES_CALCULATOR.Button(root, text="9",command=lambda: add_to_calculation(9), width=5, font=("Arial",14))
btn_9.grid(row=4,column=3)
btn_0 = MOSES_CALCULATOR.Button(root, text="0",command=lambda: add_to_calculation(0), width=5, font=("Arial",14))
btn_0.grid(row=5,column=2)
btn_plus = MOSES_CALCULATOR.Button(root, text="+",command=lambda: add_to_calculation("+"), width=4, font=("Arial",14))
btn_plus.grid(row=2,column=4)
btn_minus = MOSES_CALCULATOR.Button(root, text="-",command=lambda: add_to_calculation("-"), width=4, font=("Arial",14))
btn_minus.grid(row=3,column=4)
btn_mul = MOSES_CALCULATOR.Button(root, text="*",command=lambda: add_to_calculation("*"), width=4, font=("Arial",14))
btn_mul.grid(row=4,column=4)
btn_divide = MOSES_CALCULATOR.Button(root, text="/",command=lambda: add_to_calculation("/"), width=4, font=("Arial",14))
btn_divide.grid(row=5,column=4)
btn_leftpar = MOSES_CALCULATOR.Button(root, text="(",command=lambda: add_to_calculation("("), width=4, font=("Arial",14))
btn_leftpar.grid(row=5,column=1)
btn_rightpar = MOSES_CALCULATOR.Button(root, text=")",command=lambda: add_to_calculation(")"), width=5, font=("Arial",14))
btn_rightpar.grid(row=5,column=3)
btn_equals = MOSES_CALCULATOR.Button(root, text="=",command=evaluate_calculation, width=13, font=("Arial",14))
btn_equals.grid(row=6,column=1,columnspan=2)
btn_clear = MOSES_CALCULATOR.Button(root, text="c",command=clear_field, width=12, font=("Arial",14))
btn_clear.grid(row=6,column=3,columnspan=3)
root.mainloop()