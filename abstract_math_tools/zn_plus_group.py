
class zn_plus_group:
    
   def __init__ (self, n):
       self.n = n
       
   def is_isomorphic(self,H):
       return H
   
   def is_normal(self, H):
       return H
   
   def order(self):
       return 2*self.n 
   
   def order_element(self, g):
       for x in self:
            x = g
            if x == 0:
                return g
       g = self.operate(g)
    
       return g
           
   def is_abelian(self, group):
       for a in group:
        for b in group:
            if self.operate(self, a, b) != self.operate(self, a ,b):
                return False
        return True
   
   def conjugate_class_subgroups(self):
       raise NotImplementedError()
  
   def operate(self, elements):
       raise NotImplementedError()
       
   def cayley_graph(self):
        raise NotImplementedError()
    
     
   def operate(self, a,b):
        return (a+b)%self.n
    
   def cayley_table(self):
        return []
        