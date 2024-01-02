import math

class dihedral_group:
    
    
   def __init__ (self, n):
       self.n = n
       
         
   def get_n(self):
        return self.n
    
       
   def is_isomorphic(self,H):
       return H
   
   def is_normal(self, H):
       return H
   
   def order(self):
       return 0
   
   def order_element(self, g):
       return g
   
   def is_abelian(self, group):
       for a in group:
        for b in group:
            if operation(self, a, b) != operation(self, a ,b):
                return False
        return True
   
   def conjugate_class_subgroups(self):
       raise NotImplementedError()
  
   def operate(self, elements):
       raise NotImplementedError()
       
   def cayley_graph(self, G):
        raise NotImplementedError()
    
     
   def operation(self, a,b):
        return (a+b)%self.n
        