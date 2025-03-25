-- Script to list all TV shows with at least one genre from hbtn_0d_tvshows

-- Select tv show titles and their corresponding genre_id in one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows, tv_show_genres 
WHERE tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;