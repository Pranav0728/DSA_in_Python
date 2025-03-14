import ctypes
class DynamicArray:
    def __init__(self):
        self.size = 1
        self.n = 0
    #create an array with size n
        self.A = self.__make_array(self.size)
    def lenn(self):
        return self.n

    def append(self,item):
        if self.size == self.n:
            self.__resize(2*self.size)
        self.A[self.n]= item
        self.n = self.n+1
    
    def show(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ', '
        return '[' + result[:-2] + ']'
    def clear(self):
        self.size = 1
        self.n = 0
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'Not Found'
    def insert(self,pos,item):
        if self.size == self.n:
            self.__resize(2*self.size)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n = self.n+1
    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            self.delete_by_pos(pos)
        else:
            return 'Not Found'
    def pop(self):
        if self.n == 0:
            return IndexError('Array is empty')
        else:
            print(self.A[self.n-1])
            self.n = self.n-1
            self.size = self.size-1
    def delete_by_pos(self,pos):
        if self.n == 0:
            return IndexError('Array is empty')
        else:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n-1
            self.size = self.size-1
    def __getItem__(self,item):
        if item<0 or item>=self.n:
            return IndexError('Index out of bounds')
        return self.A[item]
    def sort(self):
        for i in range(self.n):
            for j in range(self.n-1):
                if self.A[j]>self.A[j+1]:
                    self.A[j],self.A[j+1] = self.A[j+1],self.A[j]
    
    def __resize(self, newSize):
        B = self.__make_array(newSize)
        self.size = newSize
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
    def __make_array(self,size):
        return (size*ctypes.py_object)()

myArray = DynamicArray()
myArray.append(1)
myArray.append(2)
myArray.append(3)
myArray.append(8)
myArray.sort()
myArray.show()