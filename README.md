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

### Windows
```
TBD
```

### Mac
```
TBD
```
### Linux ?? ??? ? ?
```
help
```

> Don't forget to use `\\` for file path! \ or / won't work. <- this is true

## Compatibility

Tests incoming!

| OS | Tested |
| -- | ------ |
| Windows |  |
| Mac | |

## How Does It Work?

1. The script looks for changes in `WATCH_FOLDER` every 30 seconds
2. If a change is detected, a WakaTime heartbeat is sent
3. Done!

<video src="assets/davinci-wakatime.mov" width="320" height="240" controls></video>

## Main References

- [WakaTime Developers](https://wakatime.com/developers)
