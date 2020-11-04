#Basic calculator; performs  few math operations; no errors detected

def calc (operation, o1, o2):
    return operation (o1,o2)

def add (o1,o2):
    return o1+o2

def multiply (o1,o2):
    return o1*o2

def division (o1,o2):
    return o1/o2

def exponentiation (o1,o2):
    return o1**o2

def subtraction (o1,o2):
    return o1-o2

def sumofsquares (o1,o2):
    return o1**2+2*o1*o2+o2**2

def root (o1,o2):
    return o1**(1/o2)

def check (checknr):
    try:
        float(checknr)+1
        return True
    except:
        return False


print ('*'*4+"welcome to Ludwik's calculator"+"*"*4)

def main_loop():
    f1 = input ("Figure 1:")
    while check(f1) ==False:
        f1 = input ("Error. Figure 1:")

    f2 = input ("Figure 2:")
    while check(f2) ==False:
        f2 = input ("Error. Figure 2:")


    command = input ("what operation would you like to perform: ")

    print ('*'*+"results"+"*"*9)
    while (True):
        if command == "add" or command == "+" or command=='addition':
            print(str(f1)+" "+command+" "+str(f2)+" = ...")
            print(calc(add,float(f1),float(f2)))
            break
        elif command == "multiply" or command == "*" or command== 'multiplication':
            print(str(f1)+" "+command+" "+str(f2)+" = ...")
            print(calc(multiply,float(f1),float(f2)))
            break
        elif command == "division" or command == "/" or command == ':' or command=='divide':
            if f2=='0':
                print('You cannot divide by 0!')
                break
            else:
                print(str(f1)+" "+command+" "+str(f2)+" = ...")
                print(calc(division,float(f1),float(f2)))
            break
        elif command == "exponentiation" or command == "power" or command == '**':
            print(str(f1)+" "+command+" "+str(f2)+" = ...")
            print(calc(exponentiation,float(f1),float(f2)))
            break
        elif command == "subtraction" or command == "-" or command == 'subtract':
            print(str(f1)+" "+command+" "+str(f2)+" = ...")
            print(calc(subtraction,float(f1),float(f2)))
            break
        elif command == "sumofsquares" or command == "sumofsquare" or command == 'sum of squares' or command=='(a+b)**2':
            print(str(f1)+" "+command+" "+str(f2)+" = ...")
            print(calc(sumofsquares,float(f1),float(f2)))
            break
        elif command == "root" or command == "nthroot" or command == 'roots' or command=='a**(1/b)':
            if f2=='0':
                print('There is no 0th root!')
                break
            else:
                print(str(f1)+" "+command+" "+str(f2)+" = ...")
                print(calc(root,float(f1),float(f2)))
            break
        else:
            command = input ("One more time. \nWhat operation would you like to perform?  ")

    print ('*'*9+"results"+"*"*9)

def continuation():
    while True:
        decision=input ("Do you want to perform another operation (yes/no)?: ")
        if decision=='yes' or decision=='y':
            main_loop()
        elif decision=='no' or decision=='n':
            break
        
while True:
    main_loop()
    continuation()
    print ("***Thank you for using that awesome software***")
    input ("Press anykey to close")
    exit()
