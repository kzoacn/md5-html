# md5-html

This repo can generate a HTML page that show its own MD5 hash like [my homepage](https://kzoacn.github.io/).

## Usage

1. Install [HashClash](https://github.com/cr-marcstevens/hashclash/tree/master)
2. Download and unzip this repo inside the folder `hashclash`
3. Edit `index.html`, use placeholder `[MD5]` to specify where to show.
4. `cd md5-html-main`
5. `mkdir backup`
6. `python3 prefix.py`
7. `python3 suffix.py`
8. `new_index.html` is the output

## Generate

The total runnig time will be roughly 5 days on a 64 cores server, but after the first running, updating suffix is ~0.5 hour.

If you want to update suffix (i.e. content below `[MD5]`), just execute `python3 suffix.py` again after editing `index.hml`.

## Check

[Check it Online](https://emn178.github.io/online-tools/md5_checksum.html)

## How it work?

See [My Zhihu answer](https://www.zhihu.com/question/411191287/answer/34647918511)  (in Chinese).
