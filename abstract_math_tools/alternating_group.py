class alternating_group:
   
   def __init__ (self, n):
       self.n = n
       
   def is_isometric(self,H):
       return H
   
   def is_normal(self, H):
       return H
   
   def order(self):
       return 0
   
   def order_element(self, g):
       return g
   
   def is_abelian(self):
       pass
   
   def conjugate_class_subgroups(self):
       raise NotImplementedError()
  
   def operate(self, elements):
       raise NotImplementedError()
       
   def cayley_graph(self, G):
        raise NotImplementedError()