def polynomial():
    print('Choose degree of Equation ')
    print('1.deg 1 \n2.deg 2 \n3.deg 3 \n')
    d=int(input('Enter the degree'))
    if d == 1:
        degree1()
    elif d ==2:
        degree2()
    elif d ==3:
        degree3()
    else:
        print('Enter a valid choice')
        polynomial()

#------------------

def degree1():
    import matplotlib.pyplot as plt
    import numpy as np
    a=int(input('Enter a=coefficient of x:  '))
    b=int(input('Enter b=constant :'))
    x=np.array(range(10))
    y=a*x+b
    plt.plot(x,y,label='y=ax+b')
    plt.ylabel('y=ax+b')
    plt.title('y=ax+b graph')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.xlabel('x')
    plt.axis([0, 10, 0, 50])
    plt.show()
    plt.show()
#----------------------

def degree2():
    import matplotlib.pyplot as plt
    import numpy as np
    a=int(input('Enter a=coefficient of x2:  '))
    b=int(input('Enter a=coefficient of x:  '))
    c=int(input('Enter b=constant :'))
    x=np.array(range(10))
    y=(a*x*x)+(b*x)+c
    plt.plot(x,y,label='y=(a*x*x)+(b*x)+c')
    plt.title('y=(a*x*x)+(b*x)+c  graph')
    plt.ylabel('y=(a*x*x)+(b*x)+c')
    plt.grid(True, which='both')
    plt.xlabel('x')
    plt.axhline(y=0, color='k')
    plt.axis([0, 10, 0, 50])
    plt.show()
    plt.show()
#----------------------

def degree3():
    import matplotlib.pyplot as plt
    import numpy as np
    a=int(input('Enter coefficient of x3 : '))
    b=int(input('Enter a=coefficient of x2:  '))
    c=int(input('Enter a=coefficient of x:  '))
    d=int(input('Enter b=constant :'))
    x=np.array(range(10))
    y=(a*x*x*x)+(b*x*x)+(c*x)+d
    plt.plot(x,y,label='y=(a*x*x*x)+(b*x*x)+(c*x)+d')
    plt.ylabel('y=(a*x*x*x)+(b*x*x)+(c*x)+d')
    plt.title('y=(a*x*x*x)+(b*x*x)+(c*x)+d  graph')
    plt.xlabel('x')
    plt.axis([0, 10, 0, 50])
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()
    plt.show()
#------------------------

def exponential():
    print('Choose the type')
    print('1.Exponential Equation base(e) \n2.Exponential Equation base other than (e) \n3.Logarithmic Equation \n')
    f=int(input('Enter a choice'))
    if f ==1:
        expo()
    elif f ==2:
        expo1()
    elif f ==3:
        logarithmic()
    else:
        print('Enter a valid choice')
        exponential()
#--------------


def expo():
    import matplotlib.pyplot as plt
    import numpy as np
    plt.axis([0, 10, 0, 50])
    x=np.arange(10)
    y = np.exp(x)
    plt.plot(x,y,label='y=e^x')
    plt.plot(x , y)
    plt.grid(True, which='both')
    plt.ylabel('y=e^x')
    plt.xlabel('x')
    plt.title('y=e^x  graph')
    plt.axhline(y=0, color='k')
    plt.show()
    plt.show()


#--------------------

def expo1():
    import matplotlib.pyplot as plt
    import numpy as np
    h=int(input('Enter base value :'))
    x=np.arange(10)
    y=np.power(h,x)
    plt.plot(x,y,label='y=h^x')
    plt.plot(x , y)
    plt.ylabel('y=h^x')
    plt.xlabel('x')
    plt.title('y=h^x  graph')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axis([0, 10, 0, 50])
    plt.show()
    plt.show()


#-------------------


def logarithmic():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(1,10)
    y2 = np.log10(x) #base 10
    plt.title('plot log10 graph')
    plt.ylabel('y=log 10 x graph')
    plt.xlabel('x')
    plt.plot(x,y2)
    plt.show()

#-----------------------


def trigonometry():
    import matplotlib.pyplot as plt
    import numpy as np
    print('Choose the type')
    print('1.sin \n2.cos \n3.tan \n4.sin inverse \n5.cos inverse \n6.tan inverse \n')
    j=int(input('Enter your choice'))
   

    if j == 1:
        # Get x values of the sine wave
        time        = np.arange(0, 10, 0.1)
        # Amplitude of the sine wave is sine of a variable like time
        amplitude   = np.sin(time)
        #   Plot a sine wave using time and amplitude obtained for the sine wave
        plt.plot(time, amplitude)
        # Give a title for the sine wave plot
        plt.title('Sine wave')
        # Give x axis label for the sine wave plot
        plt.xlabel('Time')
        # Give y axis label for the sine wave plot
        plt.ylabel('Amplitude = sin(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        plt.show()
        # Display the sine wave
        plt.show()
        
    elif j == 2:

        x = np.arange(0,10,0.1)
        y = np.cos(x)
        plt.plot(x,y,label='y=cos x')
        plt.plot(x , y)
        plt.title('cos wave')
        plt.xlabel('Time')
        plt.ylabel('Amplitude = cos(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        plt.show()
        plt.show()
    elif j == 3:
        x = np.arange(0,10,0.1)
        y = np.tan(x)
        plt.plot(x,y,label='y=tan x')
        plt.plot(x , y)
        plt.title('tan wave')
        plt.xlabel('Time')
        plt.ylabel('Amplitude = tan(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        plt.show()
        plt.show()
    elif j == 4:
        x = np.arange(0,10,0.1)
        y = np.arcsin(x)
        plt.plot(x,y,label='y=asin x')
        plt.plot(x , y)
        plt.title('Sine inverse wave')
        plt.xlabel('Time')
        plt.ylabel('Amplitude = asin(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        plt.show()
        plt.show()
    elif j == 5:
        x = np.arange(0,10,0.1)
        y = np.arccos(x)
        plt.plot(x,y,label='y=acos x')
        plt.plot(x , y)
        plt.title('acos wave')
        plt.xlabel('Time')
        plt.ylabel('Amplitude = acos(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        plt.show()
        plt.show()
    elif j == 6:
        x = np.arange(0,10,0.1)
        y = np.arctan(x)
        plt.plot(x,y,label='y=atan x')
        plt.plot(x , y)
        plt.title('atan wave')
        plt.xlabel('Time')
        plt.ylabel('Amplitude = atan(time)')
        plt.grid(True, which='both')
        plt.axhline(y=0, color='k')
        plt.show()
        plt.show()
   
    else:
        print('Enter a valid Choice!')
        trigonometry()


#---------------------------------------
def linear():
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.array(range(10))
    a=int(input('Enter coefficient of x'))
    b=int(input('Enter coefficient of y'))
    c = int(input('Enter constant'))
    y = (c-(a*x))/b
    plt.plot(x,y,label='y=(c-(a*x))/b')
    plt.plot(x,y,label='y=(c-(a*x))/b')
    plt.title('Linear Graph')
    plt.xlabel('x')
    plt.ylabel('y=(c-(a*x))/b')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axis([0, 10, 0, 50])
    plt.show()
    plt.show()

#-----------------------

print("  \n     Enter an Equation to get it's graph! \n" )
print ( '  Choose the type of Equation you want the graph for! \n' )
print ('1. Polynomial Equation \n2. Exponential Equation \n3. Trigonometric Equation \n4. Linear Equation')
ch=int(input ('Enter choice: '))
if ch == 1:
    polynomial()
elif ch == 2:
    exponential()
elif ch == 3:
    trigonometry()
else:
    linear()

