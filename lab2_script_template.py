def main():
    
    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Neha Rose Vembil Denny',
        'student_id' : '10284195.',
        'pizza_toppings': [
            'TOMATO',
            'PEPPER',
            'CHICKEN'
        ],
        'movies': [
            {'title': 'the obsession', 'genre': 'horror'},
            {'title': 'the adam project', 'genre': 'fiction'}
        ]
    }
    # TODO: Step 3 - Add another movie to the data structure
    n_movie = {'title': 'catching killers', 'genre': 'crime'}
    about_me['movies'].append(n_movie)
    add_pizza_toppings(about_me, ('chicken', 'habanero'))
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me["movies"])
    print()
    return

# TODO: Step 4 - Function that prints student name and ID 
def print_student_name_and_id(about_me):
    ful_nam=about_me['full_name']
    fst_nam = ful_nam.split()[0]
    student_id = about_me['student_id']
    print(f'My name is {ful_nam},', f'but you can call me Mam {fst_nam}.')
    print(f'My student ID is {student_id}')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings)
    about_me["pizza_toppings"].sort()
    about_me["pizza_toppings"]=[topping.lower() for topping in about_me["pizza_toppings"]]
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    
    toppings = about_me["pizza_toppings"]
    print(f"\my favorite pizza toppings are:")
    for x in range(len(toppings)-2):
        print("-", toppings[x].upper())

    formatted_toppings = [topping.title() for topping in toppings]
    print(f"\my favorite pizza toppings are:")
    for x in range(len(formatted_toppings)):
        print("-", formatted_toppings[x].lower())

        
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie["genre"] for movie in about_me["movies"]]
    if len(genres) > 1:
        genres[-1] = "and " + genres[-1]
    print(f"\I like to watch {', '.join(genres)} movies.")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    movy_titles = [movie["title"] for movie in movie_list]
    formatted_titles = [title.title() for title in movy_titles]
    if len(formatted_titles) > 1:
        formatted_titles[-1] = "and " + formatted_titles[-1]
    print(f"\Some of my favourite movies are {', '.join(formatted_titles)}!")
    return
    
if __name__ == '_main_':
    main()