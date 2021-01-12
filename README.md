# hypnotixLite
Lite Version of hypnotix

![screnshot](https://github.com/Axel-Erfurt/hypnotixLite/blob/main/screenshot.png)

### Requirements

- python3 >= 3.6
- libmpv1

### Installation

extract it wherever you want

### Start

```cd /path/to/hypnotixLite```

```python3 ./hypnotixLite.py```

### Playlists

Name your lists mychannels[x].txt

[x] from 1 to 9

### Playlist Format

use comma as delimiter, don't use comma in cannel name

```channel name,channel url```

for example

```ARD,http://mcdn.daserste.de/daserste/de/master.m3u8```

or

```my Movie,file:///home/user/Movies/myMovie.mp4```


### Shortcuts

- 1 to 9 -> load list 1 to 9
- F -> toggle Fullscreen
- Escape -> leave Fullscreen
- S -> toggle Sidebar
- wheel -> Zoom in/out
- Q -> Quit
- Key Up -> next Channel
- Key Down -> previous Channel
- Key Plus -> more Volume
- Key Minus -> less Volume

### m3u to mychannels

```python3 m3u_to_channels.py infile.m3u outfile.txt```

- example

```python3 m3u_to_channels.py CA01_CANADA.m3u mychannels4.txt```
