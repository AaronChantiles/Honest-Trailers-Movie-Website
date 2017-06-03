import webbrowser

class Movie():
	# Class Movie serves as a template for all of my movies to have the same functionality without creating additional code.
	def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
		#This is the actual template they use. Title, Storyline, Poster Image, and Youtube Trailer.
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer

	def show_trailer(self):
		#This uses webbrowser import to open the youtube webpage for each movie.
		webbrowser.open(self.trailer_youtube_url)
		