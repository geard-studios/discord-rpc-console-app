# Discord-RPC Console App

Make it look like you're playing whatever you want on Discord!

## Usage:

First, you have to create an app with Discord. Go [here](https://discord.com/developers/applications).

You have to click the "New Application" button and select a name

This name will show up as your status

If you make the application name "The Guitar", it will show on Discord as "Playing The Guitar".

Now, copy the client ID, you will need this later

### Downloading Binaries

The easiest way to get the Discord-RPC Console App is by downloading and running the binaries.

First, go [here](https://github.com/geard-dev/discord-rpc-console-app/releases/tag/v1.1) and click on where it says ` main.exe `. This will download the file.

Now, run ` main.exe `.

### Downloading from GitHub

First, you clone the git repository by doing

` git clone https://github.com/geard-dev/discord-rpc-console-app.git `

Next, you have 2 options, running the Python file, or building it yourself

#### Running Python File

First, you have to get the pypresence package by doing

` pip install pypresence `

Next, you just do:

` python main.py `

to run it

#### Build the binaries

First, you want to get the dependencies by doing

` pip install pypresence auto-py-to-exe `

Next, run

` auto-py-to-exe `

This starts the compiler/builder using a web GUI

For the script location, go to browse and select ` main.py `

Choose onefile so the output is only one exe file

Click ` Convert .py to .exe ` and that starts building it

When its done, go to the output folder, there you will find the main.exe file

## Using:

[PyPresence](https://github.com/qwertyquerty/pypresence)
[Auto-PY-to-EXE](https://github.com/brentvollebregt/auto-py-to-exe)