import Honest_Trailers
import media

"""All of these movie variables follow the same template (class Movie imported from media), and gives the Title, Storyline, Poster image, and Youtube link. This is where you run the program to open the web page. """
Star_Trek_Darkness = media.Movie("Star Trek into Darkness",
						"Captain Kirk and Spock kick super-human ass in multiple solar-systems. They also descrate an alien culture, and destroy downtown San Francisco.",
						"http://pakistan.jobz.pk/wp-content/uploads/2013/05/Star-Trek-into-Darkness-2013.jpg",
						"https://www.youtube.com/watch?v=6B22Uy7SBe4")

Guardians_Galaxy = media.Movie("Guardians of the Galaxy",
						"Marvel's weird heros crack jokes and protects an alien planet from an alien bad guy.",
						"http://smartbitchestrashybooks.com/images/uploads/GuardiansGalaxe.jpg",
						"https://www.youtube.com/watch?v=dOyJqGtP-wU")

Deadpool = media.Movie("Deadpool",
						"Wade Wilson gets cancer. Undergoes experimental torture/treatment, where he becomes ugly and gains superpowers. He then becomes Deadpool, get's revenge on the man who's responsible, and rescues his girlfriend.",
						"http://pre11.deviantart.net/0773/th/pre/f/2016/026/c/f/deadpool_x_green_lantern_movie_poster_by_m7781-d9petjy.jpg",
						"https://www.youtube.com/watch?v=_qIRtFE6aIc")

Captain_America = media.Movie("Captain America",
						"Captain America tries to save his old friend Bucky who as been brainwashed by the Russians, and turned into a super-assassin.",
						"http://www.blackfilm.com/read/wp-content/uploads/2014/01/Captain-America-The-Winter-Soldier-Poster-Captain-America.jpg",
						"https://www.youtube.com/watch?v=JvHyk2ESFCI")

Dark_Knight_Rises = media.Movie("The Dark Knight Rises",
						"Batman gets his spine shattered by Baine, yet somehow with almost no medical care, money, or equipment, recovers in enough time to break out of prison, and travel across the world to save Gotham.",
						"http://2.bp.blogspot.com/-rUoMkCeG20Q/UAnJdk8_p6I/AAAAAAAACkE/irf0kHgmolk/s1600/the_dark_knight_rises_poster.jpg",
						"https://www.youtube.com/watch?v=WQJuGeqdbn4")

Gladiator = media.Movie("Gladiator",
						"Russel Crowe is a Roman General that get's betrayed by the Emperor's asshole Son. His family is brutally murdered, he becomes a Gladiator and vows to get revenge in this life or the next.",
						"https://www.movieposter.com/posters/archive/main/22/A70-11370",
						"https://www.youtube.com/watch?v=mv-cj6mBkPk")

John_Wick = media.Movie("John Wick 2",
						"John Wick is a super assassin that comes out of retirement to murder dozens of people for killing his dog.",
						"https://68.media.tumblr.com/32f50565ba659a5e83f952ad4be13d3d/tumblr_np9md3GxC01qatrzoo1_500.jpg",
						"https://www.youtube.com/watch?v=wDEWKx0PtUg")

The_Matrix = media.Movie("The Matrix",
						"Neo is the One who is apparently fed up with his boring life. He decides to take a pill that transports him to the real world and discovers that his entire realityis a fake computer simulation. He then becomes the One to save the human race from the robots.",
						"http://www.madmind.de/wp-content/uploads/2009/04/the_matrix_center_small.jpg",
						"https://www.youtube.com/watch?v=fY9UhIxitYM")

Star_Trek = media.Movie("Star Trek",
						"Captain Kirk and Spock kick Alien Space Ass.",
						"http://www.freemovieposters.net/posters/star_trek_2009_213_poster.jpg",
						"https://www.youtube.com/watch?v=OTfBH-XFdSc")


movies = [Star_Trek_Darkness, Guardians_Galaxy, Deadpool, Captain_America, Dark_Knight_Rises, Gladiator, John_Wick, The_Matrix, Star_Trek]
Honest_Trailers.open_movies_page(movies)