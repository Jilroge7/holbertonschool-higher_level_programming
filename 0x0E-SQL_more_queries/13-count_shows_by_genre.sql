-- list all genres
-- that are linked to a show
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
WHERE tv_genres IS NOT NULL
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY number_of_shows DESC; 
