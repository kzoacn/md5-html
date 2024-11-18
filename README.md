# md5-html

This repo can generate a HTML page that show its own MD5 hash.

## Usage

1. Install [HashClash](https://github.com/cr-marcstevens/hashclash/tree/master)
2. Edit `index.html`, use placeholder `[MD5]` to specify where to show.
3. `python3 prefix.py`
4. `python3 suffix.py`
5. `new_index.html` is the output

## Generate

If you want to update suffix (i.e. content below `[MD5]`), just execute `python3 suffix.py` again after editing `index.hml`.

## Check

[Check it Online](https://emn178.github.io/online-tools/md5_checksum.html)

## How it work?

See My [Zhihu answer](https://www.zhihu.com/question/411191287/answer/34647918511)  (in Chinese).
