class Car(object):
 """
 Attributes:
 car_type:The type of the car as a string
 car_model:The model of the car as a string
 car_name: The name of the car as a string
 """
  def __init__(self, car_type = None , car_model = None, car_name =None ):
    self.car_type = car_type
    self.speed = 0
    
    if car_model is None:
      self.car_model = "GM"
    else:
      self.car_model = car_model
    if car_name is None:
      self.car_name = "General"
    else:
      self.car_name = car_name

    
  """ 
  This method returns the number of doors 
  for porsche and koenigsegg it will return 4
  else should return 2.
  """  
  def car_doors(self):
     if self.car_type != "porshe" or "Koenigsegg":
       return 4
     return 2
     
  """This method returns the number of wheels of the given type 
  If the type is a trailler it will return 8 else it will return 4.
 """   
   def num_of_wheels(self):
     if self.car_type != "trailer":
       return 4
     return 8
  """
  This method calculates the speed of the vehicle passed.
  """   
 
  def drive(self, speed):
    if self.v_type == 'trailer':
      speed_calc = str(speed) + str(speed)
      self.speed = int(speed_calc)
    else:
      speed_calc = speed * (3 * 100)
      self.speed = speed_calc + 100
      return self       

""" This is a method that checks the type being saloon car.""" 
  def is_saloon(self, number):
    if self.car_type == "saloon":
      return True
    return False 