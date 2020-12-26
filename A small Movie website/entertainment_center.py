import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story",
                       "A story of a boy and his toys",
                       "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

avengers=media.Movie("Avengers Endgame",
                      "Story of super Hero",
                      "https://en.wikipedia.org/wiki/File:Avengers_Endgame_poster.jpg",
                      "https://www.youtube.com/watch?v=TcMBFSGVi1c")

wanda=media.Movie("WandaVision",    
                  "A witch going through a breakdown..!!",
                  "https://en.wikipedia.org/wiki/File:WandaVision_logo.png",
                  "https://www.youtube.com/watch?v=UBhlqe2OTt4")

spiderman=media.Movie("Spiderman",
                      "A radioactive spider bite a boy",
                      "https://en.wikipedia.org/wiki/File:Web_of_Spider-Man_Vol_1_129-1.png",
                      "https://www.youtube.com/watch?v=TYMMOjBUPMM")


movies=[toy_story,avengers,spiderman,wanda]

fresh_tomatoes.open_movies_page(movies)
