myapp
===

> This is some boilerplate for Curses apps

setup
---

### Virtual env

setup a virtual environment:
```bash
sudo apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate
```

optional: add an alias to ``.bash_aliases``
```bash
alias activate="source venv/bin/activate/"
```

### Initialize

```make init name='Your AppName'```

this will setup pip, install dependencies and deploy the app locally
so that it can be run with the ``your-app-name`` command.

### Change GIT remote origin

```bash
git remote set-url origin YOUR_REPO_URL
``` 

usage
---

```bash
make run
```
