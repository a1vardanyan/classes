class my_sqrt:
    
    def __init__(self, a, n, precision = 10**(-5)):
        self.value = a
        self.n = n
        self.precision = precision
    
    def helper(self, x):
        return x**self.n - self.value

    def dhelper(self, x):
        return self.n*x**(self.n-1)

    def root(self, x):
        if abs(self.helper(x)) > self.precision:
            new_x = x - self.helper(x)/self.dhelper(x)
            #print(self.helper(new_x))
            return self.root(new_x)
        else:
            return x
        
    def solution(self):
        return self.root(self.value)
      
 my_sqrt(2, 2).solution()
