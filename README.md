![Wordle](https://github.com/d4r534/Wordle-game-replication/assets/110873154/15a7d849-52bb-4b71-88e5-dad29d8f08e8)

# The Wordle
In the realm of academia, where school projects often evoke groans and lackluster efforts, I found myself standing apart from the majority. While many approached assignments solely for the sake of grades, devoid of any genuine enthusiasm, my perspective was quite different. I firmly believed that even tasks pursued for their numerical rewards should be undertaken with a commitment to perfection, creating lasting memories that would echo through the years.

The turning point arrived with the announcement of my class 11 computer science project in December 2022( **My first ever coding project** ). I eagerly seized the opportunity to craft something extraordinary – a project that transcended the mundane and bore the hallmark of true passion. The culmination of my efforts resulted in the creation of a captivating masterpiece: **The Wordle**, a refined rendition of the renowned real-world game owned by the **Wall Street Journal**. 

# Dictionary of Words
```
import requests
word_site = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
response = requests.get(word_site)
word = response.content.splitlines()
```
This helped me get the list of words I want, from which the code chooses a word randomly every time its being executed.
