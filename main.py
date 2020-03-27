user = input('please log in:')
print("Welcome")

import json
with open("movies_info.json") as f:
    data = json.load(f)
for movie_info in data ['movies']:
    print(movie_info)

genre = input('select a genre:')
release_year = input('select release_year:')
for movies in data['movies']:
  if(movies["genre"] == (genre)):
     print(movies['movie_name'])
for movies in data['movies']:
  if(movies["release_year"] == (release_year)):
      print(movies['movie_name'])
