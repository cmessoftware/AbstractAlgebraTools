from itertools import permutations
from ..utils.nt_basics import has_unique_numbers, has_bijections, phi_function, gcd, is_generator
import math

class   zn_group:
   
   def __init__(self, n=None, G=None):
       if n is not None and G is None:
           self.n = n
           self.G = []
           self.G = list(range(1, self.n + 1))
       elif n is not None and G is not None:
           self.n = n
           self.G = G
       
   def is_isomorphic(self,H):
       if self.order(H) != self.order(self.G):
           return False
       if not has_unique_numbers(H):
           return False
       if not has_bijections(H,self.G):
           return False
        
       return True                 
           
   
   def is_normal(self, H):
       if len(self.G) != len(H):
           return False
       
       for i in self.G:
           for j in H:
               if self.binary_operation(i,j) != self.binary_operation(j,i):
                   return False
       return True
       
   def order(self,H):
       return self.cardinality(H)
   
   def order_element(self,e):
       if e == 0:
              return 1
       order = 1
       acum = e
       x = 0
       while x <= self.n:
              if self.binary_operation(acum,e) != 0:
                     order += 1
                     acum += e
              else:
                     order += 1
                     break
       
              x += 1 
                     
       return order
      
           
   def is_abelian(self):
       for a in self.G:
        for b in self.G:
            if self.binary_operation(a, b) != self.binary_operation(a ,b):
                return False
        return True
   
   def conjugate_class_subgroups(self, n):
    def conjugate(perm, g):
        return tuple(g[i - 1] for i in perm)

    def find_conjugacy_classes(elements):
        conjugacy_classes = []
        while elements:
            current = [elements.pop()]
            to_remove = []
            for perm in elements:
                is_conjugate = False
                for g in current:
                    conjugated = conjugate(perm, g)
                    if conjugated in elements:
                        is_conjugate = True
                        current.append(perm)
                        to_remove.append(conjugated)
                        break
                if is_conjugate:
                    break
            for r in to_remove:
                elements.remove(r)
            conjugacy_classes.append(current)
        return conjugacy_classes

    symmetric_group = list(permutations(range(1, n + 1)))
    return find_conjugacy_classes(symmetric_group)

   def cardinality(self,H):
       return len(list(H))
  
   def binary_operation(self,a,b):
       return (a+b)%self.n
   
   #Get genetatos using the phi function approach   
   def gens(self,H):
       c = self.cardinality(H)
       generators = []
       for a in range(2, c):
           if is_generator(a, c):
               generators.append(a)
               
       return generators

           

   
       
        
   def cayley_table(self):
        return []
        