import math

class Queue:
    """
    Queue class
    """
    def __init__(self):
        self.q = []
        self.back = -1
        
    def is_empty(self):
        return self.back < 0

    def get_back(self):
        return self.back
       
    def enqueue(self,x):
        self.back += 1
        self.q.append(x)
        
    def dequeue(self):
        if not self.is_empty():
            front = self.q[0]
            self.q = self.q[1:]
            self.back -= 1
            return front


class Stack:
    """
    Stack class
    """
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self,x):
        self.stack = [x] + self.stack
        self.top += 1

    def pop(self):
        if self.top >= 0:
            self.top -= 1
            item = self.stack[0]
            self.stack = self.stack[1:]
            return item
        else:
            return "sorry pal it's empty"

    def empty(self):
        return self.top < 0
    
    def __repr__(self):
        return str("\narray:{0}, ptr: {1}".format(self.stack,self.top))



class MyComplex:
    """
    Complex Number class
    """
    def __init__(self,real,imaginary):
        self.r = real
        self.i = imaginary

    def get_r(self):
        return self.r
    
    def get_i(self):
        return self.i
    
    def __add__(self,y):
        real_part = self.get_r() + y.get_r()
        imag_part = self.get_i() + y.get_i()
        return MyComplex(real_part,imag_part)

    def __sub__(self,y):
        real_part = self.get_r() - y.get_r()
        imag_part = self.get_i() - y.get_i()
        return MyComplex(real_part,imag_part)

    def __rmul__(self,y):
        return self.__mul__(y)

    def __mul__(self,y):
        if type(y) in (int,float):
            return MyComplex(self.get_r()*y,self.get_i()*y)
        else:
            a,b = self.get_r(), self.get_i()
            c,d = y.get_r(), y.get_i()
            return MyComplex(a*c - b*d, a*d + b*c)

    def __truediv__(self,y):
        if type(y) in (int,float):
            return MyComplex(self.get_r()/y,self.get_i()/y)
        else:
            a,b = self.get_r(), self.get_i()
            c,d = y.get_r(), y.get_i()
            denominator = c**2 + d**2
            return MyComplex((a*c + b*d)/denominator, (b*c - a*d)/denominator)

    def __repr__(self):
        sign = "-+"[self.get_i()>=0]
        return f"{self.r}{sign}{abs(self.i)}i"


class Graph:
    """
    Graph class
    """
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self,pair):
        start, end = pair
        self.edges[start].append(end)

    def children(self,node):
        return self.edges[node]

    def nodes(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.edges)

def dfs(g, start, goal) -> list:
    """
    Performs depth-first search
    """
    visited = []
    s = Stack()
    s.push(start)
    while not s.empty():
        nnode = s.pop()
        if nnode == goal:
            return [visited, goal]
        if nnode not in visited:
            visited.append(nnode)
            clist = g.children(nnode)
            for n in clist:
                if n not in visited:
                    s.push(n)
    return visited


def bfs(g,start, goal) -> list:
    """
    Performs breadth-first search
    """
    visited = []
    q = Queue()
    q.enqueue(start)
    while not q.empty():
        nnode = q.dequeue()
        if nnode == goal:
            return [visited, goal]
        if nnode not in visited:
            visited.append(nnode)
            clist = g.children(nnode)
            for n in clist:
                if n not in visited:
                    q.enqueue(n)
    return visited

def mod_exp(b,n,m) -> int:
    """
    Performs modular exponentiation
    """
    x = 1
    power = b % m
    k = len(bin(n))
    a = str(bin(n))
    print(a)
    print(power)
    for i in range(k-1,1,-1):
        if a[i] == '1':
            x = (x*power) % m
        power = (power*power) % m
        print(f'digit = {a[i]}, x = {x}, power = {power}')
    return x

def bubsort(array):
    """
    Performs bubble sort
    """
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            print(array)
            print(i,j)
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

def inssort(array):
    """
    Performs insertion sort
    """
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

    
def makeProbability(xlst) -> list:
    """
    Returns probability distribution of a list of data
    """
    newdict = {}
    for i in xlst:
        if i in newdict.keys():
            newdict[i] += 1
        else:
           newdict[i] = 1
    newlist = []
    for k,v in newdict.items():
        newlist += [v/len(xlst)]
    return newlist
    

def entropy(xlst) -> float:
    """
    Returns entropy of a list of data. Entropy is the measure of impurity in data.
    The higher the entropy, the more uncertainty in the data.
    """
    newlist = makeProbability(xlst)
    my_sum = 0
    for i in newlist:
        my_sum += math.log(i,2)*i
    final = round(-1*my_sum,2)
    return final

