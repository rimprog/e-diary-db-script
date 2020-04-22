# e-diary db-script

This script work with database [e-diary](https://github.com/rimprog/e-diary). Whit it, you can fix marks, remove chastisements, create commendation. All you need is schoolkid name.

### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

1. Put `scripts.py` in the root [e-diary website project](https://github.com/rimprog/e-diary) and run terminal
2. Open python interactive shell in django with `python3 manage.py shell` ([e-diary website project](https://github.com/rimprog/e-diary) must already be configured)
3. In interactive shell import required functions from `scripts.py` with `from scripts import fix_marks, remove_chastisements, create_commendation`
4. Pass arguments and run required function. Examples of use bellow.

Fix marks EXAMPLE:
```
In:
fix_marks("SCHOOLKID NAME")
Out:

```

Remove chastisements EXAMPLE:
```
In:
remove_chastisements("SCHOOLKID NAME")
Out:

```

Create commendation EXAMPLE:
```
In:
create_commendation("SCHOOLKID NAME", "SUBJECT NAME")
Out:

```

Replace "SCHOOLKID NAME" on name required schoolkid, like "Фролов Иван" and "SUBJECT NAME" on name of educational subject like " Математика"

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
