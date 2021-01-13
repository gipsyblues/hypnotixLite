## Hypnotix Lite

![screnshot](https://github.com/Axel-Erfurt/hypnotixLite/blob/main/screenshot2.png)

### Voraussetzungen

- python3 >= 3.6
- libmpv1

### Installation

entpacke es irgendwohin

### Start

```cd /Pfad/zu/hypnotixLiteOrdner```

```python3 ./hypnotixLite.py```

### Playlists

benenne die Listen mychannels[x].txt

[x] von 1 bis 9

### Playlist Format

Nutze Komma as delimiter, benutze kein Komma in Kanalnamen

```channel name,channel url```

z.B.

```ARD,http://mcdn.daserste.de/daserste/de/master.m3u8```

oder

```my Movie,file:///home/user/Movies/myMovie.mp4```


### Tastenkürzel

- 1 bis 9 -> lade Liste 1 bis 9
- F -> Vollbild an/aus
- Escape -> Vollbild aus
- S -> Sidebar ein/aus
- Mausrad -> Zoom größer/kleiner
- Q -> Beenden
- Pfeil nach unten -> nächster Kanal in Liste
- Pfeil nach oben -> vorheriger Kanal in Liste
- Plus -> lauter
- Minus -> leiser
- i -> Import m3u

### Hinweis

- mychannels2.txt enthält Pluto TV Kanäle
- beim Abspielen wird die Seitenleiste automatisch ausgeblendet
- Verschieben des Fensters mit ALT + linke Maustaste

### m3u to mychannels

```python3 m3u_to_channels.py infile.m3u outfile.txt```

- Beispiel

```python3 m3u_to_channels.py CA01_CANADA.m3u mychannels4.txt```
