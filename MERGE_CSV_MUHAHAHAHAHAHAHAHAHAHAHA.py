import csv

with open('movies.csv',encoding="utf8")as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)

with open("movie_links_photos_noidea.csv",encoding="utf8")as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies_links = data[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_item in all_movies_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 26:
                    with open("final.csv","a+")as f:
                        csvWriter = csv.writer(f)
                        csvWriter.writerow(movie_item)