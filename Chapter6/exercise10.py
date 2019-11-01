"""
Heber Cooke 10/31/2019
Chapter 6 Exercise 10

Define and test a function myRange() 

"""



def myRange( stop, start = None, step = None): # Note the stop is arg #1 start arg #2 and step arg #3

    if start == None:
        start = 0
    if step == None:
        step = 1

    myList = [] # empty list
    count = start
    if start < stop:
        while  count <= stop:
            myList.append(count)
            count += step
        return myList
    else:
        while  count >= stop:         
            myList.append(count)
            count -= step
        return myList

print("start 50 stop 100 step 5\n",myRange(100,50,5))
print("start 5 stop 100 \n",myRange(100,5))
print("Stop 100\n",myRange(100))
print("start 35 stop 0 \n",myRange(0,35))
print("start 60 stop 0  step 6\n",myRange(0,60,6))