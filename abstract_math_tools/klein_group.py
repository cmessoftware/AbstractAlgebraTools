class klein_group:
    
   def __init__ (self, n):
       self.n = n
       
   def is_isomorphic(self,H):
       return H
   
   def is_normal(self, H):
       return H
   
   def order(self):
       return 0
   
   def order_element(self, g):
       return g
   
   def is_abelian(self):
       return self
   
   def conjugate_class_subgroups(self):
       return self
  
   def operate(self, elements):
       return elements
       
   def cayley_table(self, G):
        return G