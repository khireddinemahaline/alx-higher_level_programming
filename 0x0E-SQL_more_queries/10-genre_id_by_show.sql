-- Genre ID by 
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
