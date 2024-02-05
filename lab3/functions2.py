# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
"""
#TASK 1
def func(movie):
    if movie["imdb"] > 5.5:
        return True
    return False
"""

#TASK 2
"""
def sublist(movies):
    list = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            list.append(movie["name"])
    return list
print(sublist(movies))
"""

#TASK 3
"""
def cat(categ):
    list = []
    for movie in movies:
        if movie["category"] == categ:
            list.append(movie["name"])
    return list
print(cat("Romance"))
"""

#TASK 4
"""
def average(movies):
    count = 0
    sum = 0
    for movie in movies:
        sum += movie["imdb"]
        count += 1
    return float (sum) /count
print(average(movies))
"""

#TASK 5
"""
def average(categ):
    sum = 0 
    count = 0
    for movie in movies:
        if movie["category"] == categ:
            sum += movie["imdb"]
            count +=1
    return float(sum)/count
print(average("Romance"))
"""