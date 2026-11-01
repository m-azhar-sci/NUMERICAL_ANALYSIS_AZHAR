import math
import sys
import sympy as sym

def newraph():
    func = input('Function: ')
    x_i = float(input('Initial guess: '))
    num = int(input('Number of iteration: '))
    #CHeck:
    f_xi = eval (func, {'x':x_i})
    if f_xi == 0:           #check whether the guess is root
        print('x_i the initial guess is the root')
        sys.exit()
    else:
        x = sym.symbols('x')
        f_sym = sym.sympify(func)  #change into sympy function
        print(type(f_sym))
        df_x = sym.diff(f_sym, x)   # differentiate
        print(type(df_x))
        df_xi = sym.lambdify(x,df_x) #changing to function f(x)
        print(type(df_xi))

        df_xi = df_xi(x_i)
        print(type(df_xi))
        if df_xi == 0:      #check whether der of func at initial guess is zero
            print('initial derivative is zero means the tangent does not touch the x axis so no root can be approximate.')
            sys.exit()
        else:

            for i in range(1,num+1):
                f_xi = eval (func, {'x':x_i})

                f_sym = sym.sympify(func)  #change into sympy function
                df_x_sym = sym.diff(f_sym, x)   # differentiate
                df_x = sym.lambdify(x, df_x_sym)
                df_xi = df_x(x_i)

                if f_xi == 0:
                    print('this is the root')
                    sys.exit()
                elif df_xi == 0:
                    print('Flat tangent! Root is not found')
                    sys.exit()
                else:
                    x_i = x_i - (f_xi/df_xi)
                    print (f'{i} no. of itera: {x_i} ')
            return f'The approximae root is {x_i}'

ans = newraph()
print(ans)