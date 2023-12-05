import tkinter as tk


# Create the main window
window = tk.Tk()
window.title("Grid Layout Example")

# Functional Steps per Button
def insertStep(stepnum):
    print("printing " +stepnum +" " +robo_selected.get()) 
    if stepnum == "step1":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum =="step2":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum =="step3":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum =="step4":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum =="step5":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum == "step6":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum =="step7":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum =="step8":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum == "step9":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    elif stepnum == "step10":
        #insert steps to put in database including robo_selected and user_selected
        print("Step Printed")
    else:
        print("Error")
def CreateError(errortype):
    if errortype == "hardware":
        #insert steps to put in database including robo_selected and user_selected
        print("Error Printed")
    elif errortype == "TipPickup":
        #insert steps to put in database including robo_selected and user_selected
        print("Error Printed")
    else:
        print("Error Encountered")

        



# Creating the elements of the window
methodname = tk.Label(window, text="MethodOverview", font=("Arial", 16), bg="gray")
robo_units = ["D566","I022","Insert","insert1"]
ham7steps = ["Step1","Step2","Step3","Step4","Step5","Step6","Step7","Step8","Step9","Step10"]
robo_selected = tk.StringVar(window)
user_selected = tk.StringVar(window)
select_unit = tk.OptionMenu(window,robo_selected,*robo_units)
user_name = tk.Entry(window,textvariable=user_selected)
hardware_err=tk.Button(window,text="Create Error: Hardware Error",command= lambda:CreateError("hardware"))
tippickup_err=tk.Button(window,text="Create Error: Tip Pickup Error",command=lambda:CreateError("TipPickup"))
resolve_button = tk.Button(window,text = "Resolve")


#Define Ham7 steps
step1 = tk.Button(window,text = ham7steps[0],command = lambda:insertStep("step1"))
step2 = tk.Button(window,text = ham7steps[1],command = lambda:insertStep("step2"))
step3 = tk.Button(window,text = ham7steps[2],command = lambda:insertStep("step3"))
step4 = tk.Button(window,text = ham7steps[3],command = lambda:insertStep("step4"))
step5 = tk.Button(window,text = ham7steps[4],command = lambda:insertStep("step5"))
step6 = tk.Button(window,text = ham7steps[5],command = lambda:insertStep("step6"))
step7 = tk.Button(window,text = ham7steps[6],command = lambda:insertStep("step7"))
step8 = tk.Button(window,text = ham7steps[7],command = lambda:insertStep("step8"))
step9= tk.Button(window,text = ham7steps[8],command = lambda:insertStep("step9"))
step10 = tk.Button(window,text = ham7steps[9],command = lambda:insertStep("step10"))

#Assemble the buttons
methodname.grid(row = 1,column = 0)
select_unit.grid(row = 0,column = 2)
user_name.grid(row = 1,column = 2)
step1.grid(row = 2, column = 0)
step2.grid(row = 2, column = 1)
step3.grid(row = 2, column = 2)
step4.grid(row = 3, column = 0)
step5.grid(row = 3, column = 1)
step6.grid(row = 3, column = 2)
step7.grid(row = 4, column = 0)
step8.grid(row = 4, column = 1)
step9.grid(row = 4, column = 2)
step10.grid(row = 5, column = 1)


















# Start the main event loop
window.mainloop()


