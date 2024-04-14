from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples = [
        {'name':'adarsh', 'age': 23},
        {'name':"prajwal", 'age': 11},
        {'name':'avinash', 'age': 21},
        {'name':'vinay', 'age': 12},
        {'name':'abhishek', 'age': 32},
        {'name':'ashik', 'age': 54}
        
        ]
    
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Aliquam iste unde eaque nulla error quidem mollitia ad cupiditate deserunt,
      ipsum maxime obcaecati delectus. Adipisci beatae quaerat rerum ut? Dolore 
      reprehenderit recusandae pariatur quis unde magnam porro, assumenda nam 
      fugiat, ut voluptatum officiis veniam doloribus!"""

    vegetables = ["carrot", "broccoli", "spinach", "tomato", "cucumber", 
                  "bell pepper", "zucchini", "lettuce", "onion", "garlic"]


    return render(request, "index.html", context= {'peoples_d': peoples,'text': text, 'vegetables': vegetables})

def about(request):
    context = {'page':'About Page'}
    return render(request, "about.html", context)

def contact(request):
    return render(request, "contact.html")

def success_page(request):
    print("$" * 10)
    return HttpResponse("<h3> Finally done !!! you are good to go </h3>")