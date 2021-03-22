# luna_ws
A very simple ROS workspace setup, with an automated init script.

[init.py](./init.py) is a simple script that creates a `src` directory, clones all repos from [luna_repos.json](./luna_repos.json) into `src`, then installs dependencies using rosdep. Piece of cake. The only thing that really neads to be maintained is luna_repos.json.

Is this overengineering? Maybe. But it creates a consistent setup for every developer, every time, and that could save some headaches.

## Setup
```
$ python3 init.py
```
