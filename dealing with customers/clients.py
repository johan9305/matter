
""" this new module has like  a purpose deal with the list of clients that I will have in the prgram of the drone program """
' this new module has like  a purpose deal with the list of clients that I will have in the prgram of the drone program'

Clients = []

class Client :
  def __init__(self, a_name  , a_dob = None  , a_adress = None) :
    self.name = a_name
    self.DOB = a_dob
    self.adress = a_adress
    self.put_in_list()

  def add_to_list(self):
     Clients.append(self.name)

  def put_in_list(self):
    general_list = [',',self.name,]
    with open('Clients.txt','a') as cl :
      cl.writelines(general_list)     

  def save_in_file(self ,filename):
    general_list = [self.name ,',', self.DOB ,',', self.adress]
    with open(filename , 'w') as f :
      f.writelines(general_list)
      
def get_from_file(filename):
  with open(filename ,'r') as f :
    data = f.readline()
  clena = data.strip().split(',')

  return(Client(clena.pop(0),clena.pop(0),clena.pop(0)))

""" this function needs to be repared because whe you call it would return one (1)
number greater than the value """ """FIXED"""

def Get_lenght() :
  with open ('Clients.txt') as c :
    obj = c.readline()
    e = obj.strip().split(',')
  return len(e)


 
