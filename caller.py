import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imdb.settings")
django.setup()

from imdb_app.models import Movie, Director, Actor

# Steven_Spielberg = Director.objects.create(
#     first_name='Steven',
#     last_name='Spielberg',
#     birth_date='1946-12-18',
#     nationality='American',
#     photo='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/MKr25425_Steven_Spielberg_%28Berlinale_2023%29.jpg/250px-MKr25425_Steven_Spielberg_%28Berlinale_2023%29.jpg',
#     years_of_experience=55
# )
#
# Christopher_Nolan = Director.objects.create(
#     first_name='Christopher',
#     last_name='Nolan',
#     birth_date='1970-06-30',
#     nationality='British',
#     photo='https://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQoNwZ9HSTyrGrvFEV8-yG0OPBjZgU4Qw3melKpEq_JbPg4T6NqSm5m2XqCWJ2mXo9R',
#     years_of_experience=25
# )
#
# Rawson_Thurber = Director.objects.create(
#     first_name='Rawson',
#     last_name='Thurber',
#     birth_date='1975-02-09',
#     nationality='American',
#     photo='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Rawson_Marshall_Thurber_2018.jpg/220px-Rawson_Marshall_Thurber_2018.jpg',
#     years_of_experience=26
# )
#
# Cate_Shortland = Director.objects.create(
#     first_name='Cate',
#     last_name='Shortland',
#     birth_date='1968-08-10',
#     nationality='Australian',
#     photo='https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Cate_Shortland_by_Gage_Skidmore_%28cropped%29.jpg/220px-Cate_Shortland_by_Gage_Skidmore_%28cropped%29.jpg',
#     years_of_experience=23
# )
#
# Chris_Columbus = Director.objects.create(
#     first_name='Chris',
#     last_name='Columbus',
#     birth_date='1956-09-10',
#     nationality='American',
#     photo='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Chris_Columbus.jpg/250px-Chris_Columbus.jpg',
#     years_of_experience=39
# )
#
# Scarlett_Johansson = Actor.objects.create(
#     first_name='Scarlett',
#     last_name='Johansson',
#     birth_date='1984-11-22',
#     nationality='American',
#     photo='https://static.wikia.nocookie.net/marvelcinematicuniverse/images/c/ce/Scarlett_Johansson.jpg/revision/latest?cb=20230510234050',
#     is_awarded=False
# )
#
# Ryan_Reynolds = Actor.objects.create(
#     first_name='Ryan',
#     last_name='Reynolds',
#     birth_date='1976-10-23',
#     nationality='Canadian',
#     photo='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Deadpool_2_Japan_Premiere_Red_Carpet_Ryan_Reynolds_%28cropped%29.jpg/220px-Deadpool_2_Japan_Premiere_Red_Carpet_Ryan_Reynolds_%28cropped%29.jpg',
#     is_awarded=True
# )
#
# Dwayne_Johnson = Actor.objects.create(
#     first_name='Dwayne',
#     last_name='Johnson',
#     birth_date='1972-05-02',
#     nationality='American',
#     photo='https://resizing.flixster.com/-XZAfHZM39',
#     is_awarded=True
# )
#
# Adam_Sandler = Actor.objects.create(
#     first_name='Adam',
#     last_name='Sandler',
#     birth_date='1966-09-09',
#     nationality='American',
#     photo='https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Adam_Sandler_Cannes_2017.jpg/250px-Adam_Sandler_Cannes_2017.jpg',
#     is_awarded=True
# )
#
#
# Movie.objects.create(
#     movie_name='Skyscraper',
#     image='https://m.media-amazon.com/images/M/MV5BOGM3MzQwYzItNDA1Ny00MzIyLTg5Y2QtYTAwMzNmMDU2ZDgxXkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_.jpg',
#     script='Will Sawyer, a former FBI agent, must rescue his family from a newly built Hong Kong skyscraper, the tallest in the world, after terrorists set the building on fire in an attempt to extort the property developer.',
#     release_date='2018-06-13',
#     director=Rawson_Thurber,
#     protagonist=Dwayne_Johnson,
#     duration=102
# )
#
# Movie.objects.create(
#     movie_name='Black Widow',
#     image='https://m.media-amazon.com/images/M/MV5BNjRmNDI5MjMtMmFhZi00YzcwLWI4ZGItMGI2MjI0N2Q3YmIwXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg',
#     script="In 1995, super soldier Alexei Shostakov and Black Widow assassin Melina Vostokoff work as Russian undercover agents, posing as a family in Ohio with Natasha Romanoff and Yelena Belova as their daughters. They steal S.H.I.E.L.D. intel and escape to Cuba where their boss, General Dreykov, has Romanoff and Belova taken to the Red Room for training as Widows. In the following decades, Shostakov is imprisoned in Russia while Romanoff and Belova become successful, dangerous assassins. Romanoff eventually defects to S.H.I.E.L.D. after helping Clint Barton bomb Dreykov's Budapest office, which apparently kills Dreykov and his young daughter Antonia.",
#     release_date='2021-06-09',
#     director=Cate_Shortland,
#     protagonist=Scarlett_Johansson,
#     duration=133
# )
#
# Movie.objects.create(
#     movie_name='Pixels',
#     image='https://m.media-amazon.com/images/M/MV5BMTIzNDYzMzgtZWMzNS00ODc2LTg2ZmMtOTE2MWZkNzIxMmQ0XkEyXkFqcGdeQXVyNjQ3MDg0MTY@._V1_.jpg',
#     script='When aliens misinterpret video feeds of classic arcade games as a declaration of war, they attack the Earth in the form of the video games.',
#     release_date='2015-06-24',
#     director=Christopher_Nolan,
#     protagonist=Adam_Sandler,
#     duration=105
# )

# James_Cameron = Director.objects.create(
#     first_name='James',
#     last_name='Cameron',
#     birth_date='1954-08-16',
#     nationality='Canadian',
#     photo='https://kulturni-novini.info/news/images/19695_1.jpg',
#     years_of_experience=39
# )
#
# Kate_Winslet = Actor.objects.create(
#     first_name='Kate',
#     last_name='Winslet',
#     birth_date='1975-10-05',
#     nationality='British',
#     photo='https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Kate_Winslet_at_the_2017_Toronto_International_Film_Festival_%28cropped%29.jpg/250px-Kate_Winslet_at_the_2017_Toronto_International_Film_Festival_%28cropped%29.jpg',
#     is_awarded=False
# )
#
# Movie.objects.create(
#     movie_name='Titanic',
#     image='https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_FMjpg_UX1000_.jpg',
#     script='The movie is about the 1912 sinking of the RMS Titanic. It stars Kate Winslet and Leonardo DiCaprio. The two play characters who are of different social classes. They fall in love after meeting aboard the ship, but it was not good for a rich girl to fall in love with a poor boy in 1912.',
#     release_date='1997-12-19',
#     director=James_Cameron,
#     protagonist=Kate_Winslet,
#     duration=194
# )

# Movie.objects.create(
#     movie_name='Interstellar',
#     image='https://m.media-amazon.com/images/I/A1JVqNMI7UL._AC_UF1000,1000_QL80_.jpg',
#     script="Interstellar is about Earth's last chance to find a habitable planet before a lack of resources causes the human race to go extinct. The film's protagonist is Cooper (Matthew McConaughey), a former NASA pilot who is tasked with leading a mission through a wormhole to find a habitable planet in another galaxy.",
#     release_date='2014-11-07',
#     director=Director.objects.get(first_name='Christopher', last_name='Nolan'),
#     protagonist=Actor.objects.get(first_name='Matthew', last_name='McConaughey'),
#     duration=169
# )


# Movie.objects.create(
#     movie_name='Avengers: Infinity War',
#     image='https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_.jpg',
#     script='The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.',
#     release_date='2018-04-27',
#     director=Director.objects.get(first_name='Joe', last_name='Russo'),
#     protagonist=Actor.objects.get(first_name='Josh', last_name='Brolin'),
#     duration=149
# )

# Movie.objects.create(
#     movie_name='Avengers: Endgame',
#     image='https://lumiere-a.akamaihd.net/v1/images/p_avengersendgame_19751_e14a0104.jpeg',
#     script="Avengers: Endgame is set after Thanos' catastrophic use of the Infinity Stones randomly wiped out half of Earth's population in Avengers: Infinity War. Those left behind are desperate to do anything to bring back their lost loved ones.",
#     release_date='2019-04-26',
#     director=Director.objects.get(first_name='Joe', last_name='Russo'),
#     protagonist=Actor.objects.get(first_name='Josh', last_name='Brolin'),
#     duration=182
# )


# Movie.objects.create(
#     movie_name="Fast X",
#     image='https://upload.wikimedia.org/wikipedia/en/f/f2/Fast_X_poster.jpg',
#     script="In 2011, Dante Reyes, the son of drug lord Hernán Reyes, attempts to stop Dominic Toretto and Brian O Conner from stealing the vault containing the fortune of his father. However, Dom uses the vault to ram Dante's turreted SUV into the ocean, but Dante survives and swears revenge against Dom.",
#     release_date='2023-05-19',
#     director=Director.objects.get(first_name='Louis', last_name='Leterrier'),
#     protagonist=Actor.objects.get(first_name='Vin', last_name='Diesel'),
#     duration=141
# )

# Movie.objects.create(
#     movie_name="Dumb and Dumber",
#     genre='Comedy',
#     image='https://m.media-amazon.com/images/M/MV5BZDQwMjNiMTQtY2UwYy00NjhiLTk0ZWEtZWM5ZWMzNGFjNTVkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_FMjpg_UX1000_.jpg',
#     script="Starring Jim Carrey and Jeff Daniels, it tells the story of Lloyd Christmas and Harry Dunne, two dumb but well-meaning friends from Providence, Rhode Island, who set out on a cross-country trip to Aspen, Colorado, to return a briefcase full of money to its owner, thinking it was abandoned.",
#     release_date='1994-12-06',
#     director=Director.objects.get(first_name='Peter', last_name='Farrelly'),
#     protagonist=Actor.objects.get(first_name='Jim', last_name='Carrey'),
#     duration=113
# )

# Movie.objects.create(
#     movie_name='Red Notice',
#     genre='Comedy',
#     image='https://cineboom.bg/wp-content/uploads/2021/10/rednoticeposter1.jpg',
#     script="An Interpol agent successfully tracks down the world's most wanted art thief with help from a rival thief. But nothing is as it seems as a series of double-crosses ensues.",
#     release_date='2021-11-04',
#     director=Director.objects.get(first_name='Rawson', last_name='Thurber'),
#     protagonist=Actor.objects.get(first_name='Dwayne', last_name='Johnson'),
#     duration=118
# )
