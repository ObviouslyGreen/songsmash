# songsmash
Convert any youtube song (video) to a person of your choice. Pls be ethical. Follow all guidelines of library used (so-vits-svc-fork, demucs, etc).

## Installation
```
pip install requirements.txt
```
Only tested on python 3.10, intel based mac, etc. etc. etc.

## Running
```
python main.py
```

## TODO
This project is all a giant hack to have some fun, not intended to be used in any serious way.

* Figure out why crepe and crepe lite no work on my mac
* Dockerize to make setup and running easier / install docs
* Make directories and temp work folders better
* Clean up vocal tracks with extra filters
* CLI tool / web frontend instead of script
* Tools to slice together different parts of output since some f0 methods perform better in certain parts?
* Proper logging
* Test with gpu, since mainly have ran stuff on intel based mac
* Debug why so-vits-svc-fork has issues spliting up silent vs nonsilent chunks for mp3 files (wav works fine usually)

## Models
Models live in the models directory, a config.json is expected and .pth files for the models themselves. Can find models on [Hugging Face](https://huggingface.co/)


## Misc
Some random youtube links I've been testing with

* [Hey there Delilah](https://www.youtube.com/watch?v=S6XXDw0Mrck)
* [Happier Than Ever](https://www.youtube.com/watch?v=YEbz2Qt3vec)
* [Bohemian Rhapsody](https://www.youtube.com/watch?v=fJ9rUzIMcZQ)
* [Zombie](https://youtu.be/BxrLVldZtmg)
* [What's Up](https://www.youtube.com/watch?v=B6GdsRIbTSk)
* [Creep](https://www.youtube.com/watch?v=zFYEYRcjK2g)
* [Creep acoustic](https://youtu.be/4BX5xpB2DBM)

Main libraries used:
* [youtube-dl](https://github.com/ytdl-org/youtube-dl/tree)
* [demucs](https://github.com/facebookresearch/demucs)
* [so-vits-svc-fork](https://github.com/voicepaw/so-vits-svc-fork)
