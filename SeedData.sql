-- Seed data for Artists
INSERT INTO Artist (name, avatar, biography) VALUES
('Taylor Swift', '/images/artists/taylor.jpg', 'American singer-songwriter.'),
('Drake', '/images/artists/drake.jpg', 'Canadian rapper and singer.'),
('Ed Sheeranuseruser_id', '/images/artists/ed.jpg', 'British singer and songwriter.'),
('Billie Eilish', '/images/artists/billie.jpg', 'American singer known for her unique style.'),
('Adele', '/images/artists/adele.jpg', 'British singer and songwriter.'),
('Kanye West', '/images/artists/kanye.jpg', 'American rapper and producer.'),
('Beyoncé', '/images/artists/beyonce.jpg', 'American singer and performer.'),
('The Weeknd', '/images/artists/weeknd.jpg', 'Canadian singer known for his R&B hits.');

-- Seed data for Genres
INSERT INTO Genre (title, description) VALUES
('Pop', 'Popular music genre.'),
('Hip-Hop', 'Hip-hop music genre.'),
('Rock', 'Rock music genre.'),
('Electronic', 'Electronic music genre.'),
('R&B', 'Rhythm and Blues music genre.'),
('Soul', 'Soul music genre.');

-- Seed data for Albums
INSERT INTO Album (title, cover, release_date, artist_id) VALUES
('1989', '/images/albums/1989.jpg', '2014-10-27', 1),
('Scorpion', '/images/albums/scorpion.jpg', '2018-06-29', 2),
('Divide', '/images/albums/divide.jpg', '2017-03-03', 3),
('Happier Than Ever', '/images/albums/happier.jpg', '2021-07-30', 4),
('25', '/images/albums/25.jpg', '2015-11-20', 5),
('Donda', '/images/albums/donda.jpg', '2021-08-29', 6),
('Lemonade', '/images/albums/lemonade.jpg', '2016-04-23', 7),
('After Hours', '/images/albums/afterhours.jpg', '2020-03-20', 8);

-- Seed data for Tracks
INSERT INTO Track (title, duration, album_id) VALUES
('Blank Space', '00:03:51', 1),
('God\'s Plan', '00:03:19', 2),
('Shape of You', '00:03:53', 3),
('Bad Guy', '00:03:14', 4),
('Hello', '00:04:55', 5),
('Hurricane', '00:04:03', 6),
('Formation', '00:03:26', 7),
('Blinding Lights', '00:03:22', 8),
('All Too Well', '00:05:29', 1),
('Nice For What', '00:03:31', 2),
('Perfect', '00:04:40', 3),
('Ocean Eyes', '00:03:20', 4);

-- Seed data for Track-Artist relationships (with roles)
INSERT INTO TrackArtist (track_id, artist_id, role) VALUES
(1, 1, 'Primary'), -- Taylor Swift - Blank Space
(2, 2, 'Primary'), -- Drake - God's Plan
(3, 3, 'Primary'), -- Ed Sheeran - Shape of You
(4, 4, 'Primary'), -- Billie Eilish - Bad Guy
(5, 5, 'Primary'), -- Adele - Hello
(6, 6, 'Primary'), -- Kanye West - Hurricane
(7, 7, 'Primary'), -- Beyoncé - Formation
(8, 8, 'Primary'), -- The Weeknd - Blinding Lights
(9, 1, 'Primary'), -- Taylor Swift - All Too Well
(10, 2, 'Primary'), -- Drake - Nice For What
(11, 3, 'Primary'), -- Ed Sheeran - Perfect
(12, 4, 'Primary'); -- Billie Eilish - Ocean Eyes

-- Featuring artists
INSERT INTO TrackArtist (track_id, artist_id, role) VALUES
(6, 8, 'Featuring'), -- Kanye West - Hurricane (feat. The Weeknd)
(6, 2, 'Featuring'), -- Kanye West - Hurricane (feat. Drake)
(7, 3, 'Featuring'); -- Beyoncé - Formation (feat. Ed Sheeran)

-- Seed data for Track-Genre relationships
INSERT INTO TrackGenre (track_id, genre_id) VALUES
(1, 1), -- Blank Space - Pop
(2, 2), -- God's Plan - Hip-Hop
(3, 1), -- Shape of You - Pop
(4, 1), -- Bad Guy - Pop
(5, 6), -- Hello - Soul
(6, 2), -- Hurricane - Hip-Hop
(7, 1), -- Formation - Pop
(8, 5), -- Blinding Lights - R&B
(9, 1), -- All Too Well - Pop
(10, 2), -- Nice For What - Hip-Hop
(11, 1), -- Perfect - Pop
(12, 1); -- Ocean Eyes - Pop