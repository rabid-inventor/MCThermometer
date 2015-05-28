class MCThermometer:
  def __init__(self):
    self.outline =  [[(0,0),[0,0],[35,0],[0,0],[0,0]],
                    [[0,0],[35,0],[35,14],[35,0],[0,0]],
                    [[35,0],[35,14],[35,14],[35,14],[35,0]],
                    [[35,0],[35,14],[35,14],[35,14],[35,0]],
                    [[0,0],[35,0],[35,14],[35,0],[0,0]]]

  def blockselect(self,x ,y):
    return self.outline[y][x]
      
   

  def draw(self,startposition, step):
    self.currentpos = startposition
    x = step % 5 
    z = int(step/5)
    print(x,z)
    return self.blockselect(x,z)


       
  
   
  
    
