import json


def find_films():
    data = open('movie_info.json')
    return json.load(data)


data_movie = find_films()


def choose_genre():
    return input("Please,enter the genre of the movie: ")



p1 = choose_genre()


def choose_year():

     return int(input("Please,enter the year of the movie: "))



p2 = choose_year()


def choose_actor():
    return input("Please,enter the actor: ")



p3 = choose_actor()


def choose_movie(p1, p2, p3):
    for k in data_movie["movies"]:
        if (k["genre"] == p1) and (k["release_year"] == p2) and (k["actor"] == p3):
            return (k["movie_name"])
    for k in data_movie["movies"]:
        if (k["genre"] != p1) and (k["release_year"] == p2) and (k["actor"] == p3):
            return "Update films genre!!!"
    for k in data_movie["movies"]:
        if (k["release_year"] != p2) and (k["genre"] == p1) and (k["actor"] == p3):
            return "Update films year!!!"
    for k in data_movie["movies"]:
        if (k["actor"] != p3) and (k["release_year"] == p2) and (k["genre"] == p1):
            return "Update films actor!!!"
    for k in data_movie["movies"]:
        if (k["actor"] == p3) and (k["release_year"] != p2) and (k["genre"] != p1):
            return "No match found for the requested parameters!!!"
    for k in data_movie["movies"]:
        if (k["actor"] != p3) and (k["release_year"] != p2) and (k["genre"] == p1):
            return "No match found for the requested parameters!!!"
    for k in data_movie["movies"]:
        if (k["actor"] != p3) and (k["release_year"] == p2) and (k["genre"] != p1):
            return "No match found for the requested parameters!!!"
    for k in data_movie["movies"]:
        if (k["actor"] != p3) and (k["release_year"] != p2) and (k["genre"] != p1):
            return "No match found for the requested parameters!!!"


choose_movie(p1, p2, p3)
print(choose_movie(p1, p2, p3))
