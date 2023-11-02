from django.db import models

class MyCarModel(models.Model):
  make_choices = [
      ("Abarth", "Abarth"),
      ("Alfa Romeo", "Alfa Romeo"),
      ("Aston Martin", "Aston Martin"),
      ("Audi", "Audi"),
      ("Bentley", "Bentley"),
      ("BMW", "BMW"),
      ("Bugatti", "Bugatti"),
      ("Cadillac", "Cadillac"),
      ("Chevrolet", "Chevrolet"),
      ("Chrysler", "Chrysler"),
      ("Citroën", "Citroën"),
      ("Dacia", "Dacia"),
      ("Daewoo", "Daewoo"),
      ("Daihatsu", "Daihatsu"),
      ("Dodge", "Dodge"),
      ("Donkervoort", "Donkervoort"),
      ("DS", "DS"),
      ("Ferrari", "Ferrari"),
      ("Fiat", "Fiat"),
      ("Fisker", "Fisker"),
      ("Ford", "Ford"),
      ("Honda", "Honda"),
      ("Hummer", "Hummer"),
      ("Hyundai", "Hyundai"),
      ("Infiniti", "Infiniti"),
      ("Iveco", "Iveco"),
      ("Jaguar", "Jaguar"),
      ("Jeep", "Jeep"),
      ("Kia", "Kia"),
      ("KTM", "KTM"),
      ("Lada", "Lada"),
      ("Lamborghini", "Lamborghini"),
      ("Lancia", "Lancia"),
      ("Land Rover", "Land Rover"),
      ("Landwind", "Landwind"),
      ("Lexus", "Lexus"),
      ("Lotus", "Lotus"),
      ("Maserati", "Maserati"),
      ("Maybach", "Maybach"),
      ("Mazda", "Mazda"),
      ("McLaren", "McLaren"),
      ("Mercedes-Benz", "Mercedes-Benz"),
      ("MG", "MG"),
      ("Mini", "Mini"),
      ("Mitsubishi", "Mitsubishi"),
      ("Morgan", "Morgan"),
      ("Nissan", "Nissan"),
      ("Opel", "Opel"),
      ("Peugeot", "Peugeot"),
      ("Porsche", "Porsche"),
      ("Renault", "Renault"),
      ("Rolls-Royce", "Rolls-Royce"),
      ("Rover", "Rover"),
      ("Saab", "Saab"),
      ("Seat", "Seat"),
      ("Skoda", "Skoda"),
      ("Smart", "Smart"),
      ("SsangYong", "SsangYong"),
      ("Subaru", "Subaru"),
      ("Suzuki", "Suzuki"),
      ("Tesla", "Tesla"),
      ("Toyota", "Toyota"),
      ("Volkswagen", "Volkswagen"),
      ("Volvo", "Volvo")
    ]
  make = models.CharField(max_length=13, choices=make_choices)
  model = models.CharField(max_length = 200)
  year = models.CharField(max_length = 200)
  nickname = models.CharField(max_length = 200)
  

  def __str__(self):
    return self.model
  
# TODO: Potentially add accessors for each attribute



