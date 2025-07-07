# md5-html

This repo can generate a HTML page that show its own MD5 hash like [my old homepage]([https://kzoacn.github.io/](https://github.com/kzoacn/md5-html/blob/main/old-md5.html)).

## Usage

1. Install [HashClash](https://github.com/cr-marcstevens/hashclash/tree/master)
2. Download and unzip this repo inside the folder `hashclash`
3. Edit `index.html`, use placeholder `[MD5]` to specify where to show.
4. `cd md5-html-main`
5. `mkdir backup`
6. `mv textcoll.sh ../scripts/textcoll.sh`
7. `chmod +x ../scripts/textcoll.sh`
8. `python3 prefix.py`
9. `python3 suffix.py`
10. `new_index.html` is the output

## Generate

The total runnig time will be roughly 5 days on a 64 cores server, but after the first running, updating suffix is ~0.5 hour.

Checkpoints are stored and loaded automaticly, so you can freely execute / stop `prefix.py`.

If you want to update suffix (i.e. content below `[MD5]`), just execute `python3 suffix.py` again after editing `index.hml`.

## Check

[Check it Online](https://emn178.github.io/online-tools/md5_checksum.html)

## How it work?

See [My Zhihu answer](https://www.zhihu.com/question/411191287/answer/34647918511)  (in Chinese).
