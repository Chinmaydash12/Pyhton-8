#closure function
'''def add(a,b=4):
    print(a+b)
#add(3)
add(3,5)'''
'''def add(a):
    def inner(b):
        print(a+b)
    return inner
#r=add(5)
#r(10)
#r(16)
#r=add(10)
#r(20)
#r(5)
add(4)(5)'''#directly executing all function
#for two inner
'''def add(a):
    def inner(b):
        def inner1(c):
            print(a+b+c)
        return inner1
    return inner'''
'''r=add(5)
r1=r(10)
r1(20)'''
'''r=add(5)(10)
r(20)'''
'''r=add(5)
r(10)(20)'''
#add(5)(10)(20)
#25/02/2021 Program

'''def show():
    for x in range(5):
        yield x'''
#show()
#print(show())
#print(list(show()))
'''for x in show():
    print(x)'''
'''for x in show():
    if x>2:
        print(x)
    else:
        print('end')'''
'''def show(a,b=0,c=1):
    if b==0:
        i=0
        while i<a:
            yield i
            i=i+c
    elif b!=0:
        while a<b:
            yield a
            a=a+c'''
'''for x in show(5):
    print(x)'''
'''for x in show(5,10):
    print(x)'''
'''for x in show(5,10,2):
    #if x>5:
        #print('end')
    print(x)'''
#Generator function
'''def show(a,b=0,c=1):
    if b==0:
        i=0
        while i<a:
            yield i
            i=i+c
    elif b!=0:
        while a<b:
            yield a
            a=a+c
for x in show(5):
    print(x)
for x in show(5,10):
    print(x)
for x in show(5,10,2):
    print(x)'''
#With normal function
def fun(n):
    l=['happy','bat','hi','sat','gant']
    for x in l:
        if len(x)==n:
            print(x)
fun(2)
#With Closure function
'''def fav():
    def tev():'''
#With Generator function
'''def gen():
    l=['happy','bat','sat','gant']'''

#Decorator 26.02.2021

'''def add(a):
    def inner(x,y):
        print('Start')
        a(x,y)
    return inner              #part1
        print('End')
def go(a,b):
    print('Heloo')
    print(a+b)'''
#r=add(go)
#r(3,4)                    #part 2
#@add
                    #It can be called connection
'''def show(a,b):
    print('heloo')
    print(a+b)
show(5,7)'''

#Defcorator for two function

'''def add(a):
    def inner():
        print('Start')
        a()
        print('End')
    return inner
def sub(b):
    def inner():
        print('Start sub')
        b()
        print('End sub')
    return inner
@sub
@add
def show():
    print('This is show')'''

        

