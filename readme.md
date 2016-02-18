# Emotion
Ever found yourself suddenly requiring an emoticon of a person flipping a table or an emoji whale?
This script helps you streamline emoji/emoticon lookups.

### To Use:
```
$ emotion whale
🐳
```
There, now that little whale should be in your clipboard. Go spam all your friends!

### Customize:
You can define your own emoji with a json file in your home directory called: "~/.emotes.json"

```
$ cat ~/.emotes.json
{
    "poop":"💩"
}
```

```
$ emote -l
shrug                         ¯\_(ツ)_/¯
whale                         🐳
tableflip                     (╯°□°)╯︵ ┻━┻
poop                          💩
```
