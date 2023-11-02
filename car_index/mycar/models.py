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
  year_choices = [
    ("2024", "2024"),
    ("2023", "2023"),
    ("2022", "2022"),
    ("2021", "2021"),
    ("2020", "2020"),
    ("2019", "2019"),
    ("2018", "2018"),
    ("2017", "2017"),
    ("2016", "2016"),
    ("2015", "2015"),
    ("2014", "2014"),
    ("2013", "2013"),
    ("2012", "2012"),
    ("2011", "2011"),
    ("2010", "2010"),
    ("2009", "2009"),
    ("2008", "2008"),
    ("2007", "2007"),
    ("2006", "2006"),
    ("2005", "2005"),
    ("2004", "2004"),
    ("2003", "2003"),
    ("2002", "2002"),
    ("2001", "2001"),
    ("2000", "2000"),
    ("1999", "1999"),
    ("1998", "1998"),
    ("1997", "1997"),
    ("1995", "1995"),
    ("1994", "1994"),
    ("1993", "1993"),
    ("1992", "1992"),
    ("1991", "1991"),
    ("1990", "1990"),
    ("1989", "1989"),
    ("1988", "1988"),
    ("1987", "1987"),
    ("1986", "1986"),
    ("1985", "1985"),
    ("1984", "1984"),
    ("1983", "1983"),
    ("1982", "1982"),
    ("1981", "1981"),
    ("1980", "1980")
  ]
  make = models.CharField(max_length=13, choices=make_choices)
  model = models.CharField(max_length = 200)
  year = models.CharField(max_length = 4, choices=year_choices)
  nickname = models.CharField(max_length = 200)
  

  def __str__(self):
    return self.model
  
# TODO: Potentially add accessors for each attribute



