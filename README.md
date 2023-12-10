![Wordle](https://github.com/d4r534/Wordle-game-replication/assets/110873154/15a7d849-52bb-4b71-88e5-dad29d8f08e8)

# The Wordle ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
In the realm of academia, where school projects often evoke groans and lackluster efforts, I found myself standing apart from the majority. While many approached assignments solely for the sake of grades, devoid of any genuine enthusiasm, my perspective was quite different. I firmly believed that even tasks pursued for their numerical rewards should be undertaken with a commitment to perfection, creating lasting memories that would echo through the years.

The turning point arrived with the announcement of my class 11 computer science project in December 2022( **My first ever coding project** ). I eagerly seized the opportunity to craft something extraordinary – a project that transcended the mundane and bore the hallmark of true passion. The culmination of my efforts resulted in the creation of a captivating masterpiece: **The Wordle**, a refined rendition of the renowned real-world game owned by the **Wall Street Journal**. 

[![Visit Website](https://img.shields.io/badge/Original%20Game-Click%20Here-black?style=for-the-badge)](https://www.nytimes.com/games/wordle/index.html)

[![GitHub Views](https://komarev.com/ghpvc/?username=d4r534&label=Views)](https://github.com/d4r534/Wordle-game-replication)

[![GitHub Repo Stats](https://github-readme-stats.vercel.app/api/pin/?username=d4r534&repo=Wordle-game-replication&bg_color=000000&title_color=ffffff&text_color=ffffff&icon_color=000000)](https://github.com/d4r534/Wordle-game-replication)

## Share my work on:
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg-black?)](https://twitter.com/intent/tweet?text=Get%20over%20170%20free%20design%20blocks%20based%20on%20Bootstrap%204&url=https://froala.com/design-blocks&via=froala&hashtags=bootstrap,design,templates,blocks,developers)
[![Share on LinkedIn](https://img.shields.io/badge/Share-black?logo=linkedin)](https://www.linkedin.com/sharing/share-offsite/?url=https://your-website-url-here)
[![Share on Discord](https://img.shields.io/badge/Share-black?logo=discord&style=for-the-badge)](https://discordapp.com/channels/@me?tab=popout&referrer=d4r534/Bas.AI)
[![Share on Reddit](https://img.shields.io/badge/Share-000000?logo=reddit&style=for-the-badge)](https://www.reddit.com/submit?url=https://github.com/yourusername/yourrepository&title=Your%20Repository%20Title)

> [!WARNING]
> Please be advised that the outcomes may exhibit variations. It is advisable to conduct preliminary testing, as the code may not be fully optimized to accommodate all potential scenarios.

> [!IMPORTANT]
> This is just a simple python replication of the game wordle and does not include any complex functionality which may be included in the orginial game.


# Dictionary of Words
```
import requests
word_site = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
response = requests.get(word_site)
word = response.content.splitlines()
```
This helped me get the list of words I want, from which the code chooses a word randomly every time its being executed.
