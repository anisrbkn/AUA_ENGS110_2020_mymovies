user = input('please log in:')
print("Welcome")


import json
movie_info = '''
{
 "movies": [
   {
      "movie_name": "Joker",
      "release_year": 2019,
      "genre": "drama",
      "rating": 8.5,
      "actor": "Robert De Niro"
   },
   {
      "movie_name": "Knives Out",
      "release_year": 2019  ,
      "genre": "comedy", 
      "rating": 8,
      "actor": "Ana de Armas, Chris Evans"
   },
   {
      "movie_name": "Wonder",
      "release_year": 2017  ,
      "genre": "family", 
      "rating": 8,
      "actor": "Julia Roberts, Jacob Tremblay"
   },
   {
      "movie_name": "Lo imposible",
      "release_year": 2012,
      "genre": "disaster", 
      "rating": 7.6,
      "actor": "Naomi Watts"
   },
   {
      "movie_name": "Room",
      "release_year": 2015,
      "genre": "thriller",
      "rating": 8.1,
      "actor": "Brie Larson"
   }
 ]
}'''
data = json.loads(movie_info)
print(data)

genre = input('select a genre:')
release_year = input('select release_year')
for movies in data['movies']:
  if(movies["genre"] == (genre)):
     print(movies['movie_name'])
for movies in data['movies']:
  if(movies["release_year"] == (release_year)):
         print(movies['movie_name'])

