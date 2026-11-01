import math

def fun():
    func  = input(f'Write the function in x form: ')
    return func
func=fun()

def inter():
    a,b = input(f'Enter the two boundry numbers a,b such that a<b (Witha comma betweeen them): ').split(',')
    a=int(a)
    b=int(b)
    return a,b
a,b = inter()

def ab_value():
    f_a = eval(func, {'x': a})         #eval is used to put any number in place of variable of a function
    f_b = eval(func, {'x':b})
    if f_a == f_b:
        return f'The statement is either not a function or discontinous! '
    else:
        if f_a*f_b ==0:
            return f'a or b is the zero(root)'
            if f_a==0:
                return f'root is a'
            elif f_a==0 and f_b==0:
                return f'Both a and b are zeros(roots)'
            else:
                return f'HAHA'
        elif f_a*f_b>0:
            return 'There is not any root in it or it has even number of roots'
ab_value()


def itera():
    ask_n = input(f'choose: number of iteration given? yes (y) or no (n):  ')
    if ask_n == 'y':
        num = int(input(f'What is n: '))
        return num

    elif ask_n == 'n':
        eps = float(input(f'What is the tolerence of error Epslon: '))
        num_ex = math.log2((b-a)/eps)
        num_whole = int(num_ex)      
                                #  math.ceil(-3.2)    # -3   this round off to the highest one
        num = num_whole + 1
        return num
                    # Can also used if log2 is not available
                    # num = (math.log10(2)-math.log10(0.1))/math.log10(2)
    else: 
        return f'Wrong entry'
haq=itera()
print(haq)

# # num = 6
def bisec():
    aa=a
    bb=b
    numb=haq
    for i in range(1,numb+1):
        f_a = eval(func, {'x': aa})
        f_b = eval(func, {'x': bb})
        c = (aa+bb)/2
        print(f'c={c}')
        f_c = eval(func, {'x': c})
        if f_c == 0:
            print(f'The root is exactly {c}')
            return c
        elif f_a*f_c<0:
            bb=c
        else:
            aa=c
    print(f'Appr is {c}')
    return c
bisec()