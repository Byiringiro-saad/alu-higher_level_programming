-- Script to list all Comedy shows from hbtn_0d_tvshows

-- Select all tv show titles linked to the Comedy genre, sorted by show title
SELECT tv_shows.title
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_genres.name = 'Comedy' AND tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC;