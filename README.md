# dec 10: things that have been fixed

* https://github.com/rbreu/krita-python-mock allows me to do krita things on vscode (turns out they had issues on vscode but would run perfectly fine in Krita.)
* I was able to make it into an extension that could be viewed in tools -> scripts. But because it requires a while true loop, I can't run it like other Krita plugins (Krita won't let me draw while running python in the background)
* So I altered the code so that it runs in my vscode terminal. and it is able to send heartbeats with status 202 which apparently means they are accepted but not guaranteed to actually work
* ...they don't actually work l o l

# ... I don't know how to make this work oopsie
(I also don't know how to use github I'm sorry if there are rules about forking and stuff I am just trying to make changes without affecting the actual repo)

the difference between some things being named kritatime and some krita-wakatime ToT

my problems: 

* krita import not resolving -> edited pylance path, but gave it the wrong path, don't know the right path to give it
* Extension and Krita are not defined (should be imported from krita but the path is wrong qwq)
* kritatime vs krita-wakatime
* I don't know how to use github/virtual environments/literally anything lol :sob:








# DaVinci Resolve WakaTime

A script to send Wakatime heartbeats from Krita, the free and open source illustration software. Forked from LucasHT22's wonderful DaVinci Resolve script that does the same thing, watching a folder for changes.

Pull Requests and Issues are welcome!

## Setup

Clone the repo

```
git clone https://github.com/Herbeon/kritatime.git
```

In `kritatime.py`, change `WAKATIME_API_KEY` to your WakaTime API Key and change `WATCH_FOLDER`.


Your file path should look like something like this:

### Linux ?? ??? ? ?
```
help
```

> Don't forget to use `\\` for file path! \ or / won't work. <- IDK if this is true on linux I am so confsued

## Compatibility



## How Does It Work?

1. The script looks for changes in `WATCH_FOLDER` every 30 seconds
2. If a change is detected, a WakaTime heartbeat is sent
3. Done!

<video src="assets/davinci-wakatime.mov" width="320" height="240" controls></video>

## Main References

- [WakaTime Developers](https://wakatime.com/developers)
