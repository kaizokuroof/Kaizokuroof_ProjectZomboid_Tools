# kaizokuroof project zomboid tools
All Kaizokuroof's python tools that he made for Project Zomboid
You'll need tkinter, python3 and whatever modules I've included in the scripts.
Quick break down of each folder/script

Bulding Randomiser
This python script allows you to respin vanilla buildings externally via python. The way it works is you simply run: python3 building_randomiser.py and the dialog window will prompt for some things.

To modify what tiles it respins, you'll need to modify the existing script, specifically the last for loop. At the moment it generates 30 random buildings, just adjust the loop to desired count.
There are also comments for what tiles and what lists etc.

If you want to make your own lists, you can use the other script inside BuidlingRandomiserTilesetListGenerator, another GUI app that allows you to make tile lists in the format requiired for the building randomiser, that you can then import and use. You run the script and point it to the PNG files, not the pack files, of your tiles. You would then select the ones you want in a list. Yes it's tedious, but less tedious than manually typing it out :)

Some other stuff in there too, I used to data mining might be useful to others, who knows.

I'm in the PZ Unofficial Mapping discord and if you want help, head over there and ping me.

Enjoy
