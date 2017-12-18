import sys
pasoapaso=False
breakpoints={9:True, 14:True}

def debug(comand,my_arg,my_locals):
    global pasoapaso
    global breakpoints
    if comand.find(" ")>0:
        arg=comand.split(" ")[1]
    else:
        arg=None
    if comand.startswith('s'):
        pasoapaso=True
        return True
    elif comand.startswith('c'):
        pasoapaso=False
        return True
    elif comand.startswith('q'):
        sys.exit(0)
    elif command.startswith('p'):
        #print(command, my_locals)
        if arg is not None:
            if arg in my_locals.keys():
                print(arg+" = "+repr(my_locals[arg]))
            else:
                print("No such variable: "+arg)
    elif command.startswith('b'):    # breakpoint         
        if arg is not None:
            breakpoints[int(arg)]=True
        else:
            print('You must supply a line number')
    elif command.startswith('w'):    # watch variable
        if arg is not None and arg in my_locals.keys():
            watchpoints[arg]=True
        else:
            print('You must supply a variable name')
            
        
comand=["q","s","s"]

def input_comand():
    global comand
    #comand=input("(my-spider)")
    return comand.pop()

def rastrea(frame, event, arg):
    global pasoapaso
    global breakpoints

    if event== "line":
        if pasoapaso or frame.f_lineno in breakpoints.keys():
            resume=False
            while not resume:
                print(event,frame.f_lineno,frame.f_code.co_name,frame.f_locals)
                comand=input_comand()
                resume= debug(comand,arg,frame.f_locals)
            return rastrea