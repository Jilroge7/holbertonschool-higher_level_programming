-- list all genres
-- shared by show Dexter
SELECT tv_genres.name 
FROM tv_genres
JOIN tv_shows 
WHERE tv_genres.id = tv_shows.id; 
