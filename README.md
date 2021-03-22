# luna_ws
A very simple ROS workspace setup, with an automated init script.

[init.bash](./init.bash) is a simple script that creates a `src` directory, clones all repos from [luna_repos.txt](./luna_repos.txt) into `src`, then installs dependencies using rosdep. Piece of cake.
