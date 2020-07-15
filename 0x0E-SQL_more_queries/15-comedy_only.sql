-- List all shows
-- with genre comedy.
SELECT tv_shows.title
FROM tv_shows
JOIN tv_genres
ON tv_shows.id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
