from django.shortcuts import render
from django.http import HttpResponse

class House:
  def __init__(self, address, rooms_baths, sqft, gas_stove, notes, allows_dogs):
    self.address = address
    self.rooms_baths = rooms_baths
    self.sqft = sqft
    self.gas_stove = gas_stove
    self.notes = notes
    self.allows_dogs = allows_dogs

houses = [
  House('3509 Roller Xing', '4/3', 1921, 'Yes', 'Love it. Would like more counter space but I think we can work with it. The location is too far north.', 'Large Dogs OK'),
  House('16008 Hampton Bliss Trce', '3/2', 2020, 'No', 'A little far north for me. Good counter/cabinet space. Nice huge rooms, but can''t see the closets. No gas stove.', 'Dogs OK'),
  House('14009 Osmarea Dr', '3/3', 1645, 'Yes', 'Great location. Adequate size house. I like the cabinets and built in cubbies.', 'Size limit'),
  House('10617 Barnhill Dr', '3/2', 1482, 'Yes', 'I like the covered porch and gas stove. There is adequate cabinet space and a nice front yard.', 'Dogs OK'),
  House('16105 Hawthorne Heights Trl', '4/3', 2268, 'No', 'A little too far north but really big house. Nice back yard with a lot of space.', 'Small dogs OK'),
  House('8817 White Ibis Dr', '3/3', 1597, 'No', 'Love the neighborhood. Size is adequate and exterior is nice.', 'Negotiable'),
  House('12009 Aspendale Dr', '4/2', 1607, 'Yes', 'Good location. Adequate size. Nice porch. Nice kitchen.', 'Negotiable'),
  House('13214 Vendrell Dr', '4/3', 2193, 'Yes', 'Great location. Big living area. Like the gas stove and cabinet space.', 'Dogs OK'),
  House('13400 Briarwick Dr #2403', '3/3', 2015, 'Yes', 'Love this house. Our number one pick. Great neighborhood and great kitchen and floor plane.', 'Small dogs OK'),
  House('4200 Everest Ln', '4/3', 2010, 'Yes', 'Great neighborhood. Like the 2 car garage and big kitchen.', 'Medium dogs OK')
]

def home(request):
  return HttpResponse('<h1>Welcome to the House Collector</h1>')

def about(request):
    return render(request, 'about.html')

def houses_index(request):
  return render(request, 'houses/index.html', { 'houses': houses })