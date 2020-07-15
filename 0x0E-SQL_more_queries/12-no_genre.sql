-- list all the shows
-- with no genre.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.title = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
