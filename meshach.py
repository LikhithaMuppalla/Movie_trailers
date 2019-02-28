import webbrowser
class movies:
    def __init__(self,moviename,movie_story_line,movie_image,trailer_url):
        self.moviename=moviename
        self.movie_story_line=movie_story_line
        self.movie_image=movie_image
        self.trailer_url=trailer_url
    def show_trailer(self):
         webbrowser.open(self.trailer_url)         
