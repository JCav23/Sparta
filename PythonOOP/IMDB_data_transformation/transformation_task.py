import csv

def transform_movie_details(csv_file_name):
    new_movie_data = []
    with open(csv_file_name, newline='') as csvfile:
        movie_title_csv = csv.reader(csvfile,delimiter=",")

        for movie in movie_title_csv:
            transformation_data = []
            if movie[0] == "movie" and movie[4] >= "2010":
                transformation_data.append(movie[0])
                transformation_data.append(movie[1])
                transformation_data.append(movie[4])
                transformation_data.append(movie[6])
                transformation_data.append(movie[7])
                new_movie_data.append(transformation_data)

    return new_movie_data


print(transform_movie_details("imdbtitles.csv"))


def create_new_movie_details(old_file="imdbtitles.csv", new_file="movies_since_2010.csv"):
    new_movie_data = transform_movie_details(old_file)
    with open(new_file, "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_movie_data)


create_new_movie_details()

