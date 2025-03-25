-- Script to list all genres of the show Dexter from hbtn_0d_tvshows

-- Select all genres linked to the show Dexter, sorted by genre name
SELECT tv_genres.name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_shows.title = 'Dexter' AND tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_genres.name ASC;