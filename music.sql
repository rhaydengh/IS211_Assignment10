CREATE TABLE Artists (
id INTEGER PRIMARY KEY ASC, 
ArtistName TEXT
);

CREATE TABLE Albums (
id INTEGER PRIMARY KEY ASC, 
AlbumName TEXT, ArtistName TEXT
);

CREATE TABLE songs (
id INTEGER PRIMARY KEY, 
SongName TEXT, 
ArtistName INTEGER, 
AlbumName INTEGER, 
Track INTEGER, 
Length INTEGER
);

