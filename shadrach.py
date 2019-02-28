import media
import fresh_tomatoes
suvartha=media.movies("suvartha sedhyam","Story about godslove",
                      "https://i.ytimg.com/vi/_nU87I6MtFU/maxresdefault.jpg",
                      "https://youtu.be/_nU87I6MtFU")
chinnari=media.movies("chinnari","Story about a small girl",
                      "https://i.ytimg.com/vi/4IXqGnYg4k0/maxresdefault.jpg",
                      "https://youtu.be/4IXqGnYg4k0")
giving=media.movies("Giving","Story of children",
                    "https://lh3.googleusercontent.com/proxy/YT47m2FsDofZjNvLpL-Q30rgJLcwkfKVkNftsdpc9duINco5UvNx0Kxc6_Sq0Tf42J0zyrm5iwflLt0IoETU0BMMgg=w530-h297-n",
                    "https://youtu.be/aU7J9eTvJUA")
love=media.movies("jesus love","The story is about lost son",
                  "http://www.iprayprayer.com/wp-content/uploads/2017/04/LoveofGod.jpg",
                  "https://youtu.be/cD-Eb7Y-QC4")
life=media.movies("christian story","The life of christian",
                  "https://i.ytimg.com/vi/-k1ivxMSWwY/hqdefault.jpg",
                  "https://youtu.be/-k1ivxMSWwY")
bestfriend=media.movies("about hell","The story of two friends",
                        "https://i.pinimg.com/originals/5a/de/3a/5ade3aed5348fc88614a340ca95f1d62.jpg",
                        "https://youtu.be/HMZDOxcPMAM")
movies1=[suvartha,chinnari,giving,love,life,bestfriend]
fresh_tomatoes.open_movies_page(movies1)
