
class zn_mul_group:
    
    
   def __init__ (self, n):
       self.n = n
       self.G = [i for i in range(n)]
       
   def is_isomorphic(self,H):
       return H
   
   def is_normal(self, H):
       return H
   
   def order(self,a):
       for i in range(1000):
           if (a**(i+1))%self.n == 0:
               return i+1
    
       return float('inf')
   
   
           
   def is_abelian(self):
       for a in self.G:
        for b in self.G:
            if self.binary_operation(a, b) != self.binary_operation(a ,b):
                return False
        return True
   
   def conjugate_class_subgroups(self):
       return []
     
   def cayley_table(self):
       return []
         
   def bynary_operation(self,a,b):
        return (a*b)%self.n
    
   def cayley_table(self):
        return []
        