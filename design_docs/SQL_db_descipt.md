## Movie Tracking Database

This design uses three tables to efficiently store and manage movie information:

**1. Movies Table**

This table stores core movie information.

| Column Name       | Data Type        | Description                                            |
|-------------------|-------------------|---------------------------------------------------------|
| movie_id          | INT (Primary Key) | Unique identifier for each movie                        |
| title             | VARCHAR(255)      | Title of the movie                                       |
| release_year      | INT               | Year the movie was released                             |
| media_type        | ENUM ('movie', 'series') | Type of media (movie or series)                        |
| length            | INT               | Length of the movie in minutes (or total episode count) |
| imdb_rating       | DECIMAL(2,1)      | IMDB rating (0-10)                                     |
| mpaa_rating       | VARCHAR(5)        | MPAA rating (e.g., G, PG, PG-13)                         |
| description       | TEXT              | Detailed description of the movie                        |
| location          | VARCHAR(255)      | Physical location of the movie (case/disk)              |

**2. Genres Table**

This table stores individual movie genres.

| Column Name  | Data Type        | Description                           |
|--------------|-------------------|----------------------------------------|
| genre_id     | INT (Primary Key) | Unique identifier for each genre        |
| genre_name   | VARCHAR(255)      | Name of the movie genre                 |

**3. Movie_Genres Table (Many-to-Many Relationship)**

This table links movies and genres using foreign keys. A single movie can have multiple genres, and a single genre can be associated with multiple movies.

| Column Name       | Data Type        | Description                                           |
|-------------------|-------------------|---------------------------------------------------------|
| movie_id          | INT (Foreign Key) | References Movies.movie_id                             |
| genre_id          | INT (Foreign Key) | References Genres.genre_id                             |

**4. Content_Triggers Table (Optional)**

This table (optional) stores content trigger warnings associated with movies.

| Column Name       | Data Type        | Description                                           |
|-------------------|-------------------|---------------------------------------------------------|
| trigger_id        | INT (Primary Key) | Unique identifier for each trigger warning             |
| trigger_name     | VARCHAR(255)      | Name of the content trigger warning (e.g., Violence)  |

**5. Movie_Triggers Table (Optional - Many-to-Many Relationship)**

This table (optional) links movies and content trigger warnings using foreign keys. A single movie can have multiple trigger warnings, and a single trigger warning can be associated with multiple movies.

| Column Name       | Data Type        | Description                                           |
|-------------------|-------------------|---------------------------------------------------------|
| movie_id          | INT (Foreign Key) | References Movies.movie_id                             |
| trigger_id        | INT (Foreign Key) | References Content_Triggers.trigger_id                 |


**Searching and Filtering:**

* **Search by Title:** Use a `SELECT` query with a `WHERE` clause on the `title` column in the `Movies` table.
* **Search by Genre:** Utilize a `JOIN` between `Movies`, `Movie_Genres`, and `Genres` tables. Filter based on `genre_name` in the `Genres` table.
* **Filter by IMDB Rating:** Implement a `WHERE` clause on the `imdb_rating` column in the `Movies` table with appropriate comparison operators (e.g., `>=`, `<=`). 
* **Filter by MPAA Rating:** Use a `WHERE` clause on the `mpaa_rating` column in the `Movies` table with exact value comparisons.
* **Filter by Content Triggers (Optional):** If the optional tables are included, utilize joins between `Movies`, `Movie_Triggers`, and `Content_Triggers` tables. Filter based on `trigger_name` in the `Content_Triggers` table. 
