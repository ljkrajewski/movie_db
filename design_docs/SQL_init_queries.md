Absolutely, here are the SQL queries to create the tables for your movie tracking database:

**1. Movies Table:**

```sql
CREATE TABLE Movies (
  movie_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  release_year INT NOT NULL,
  media_type ENUM('movie', 'series') NOT NULL,
  length INT,
  imdb_rating DECIMAL(2,1),
  mpaa_rating VARCHAR(5),
  description TEXT,
  location VARCHAR(255)
);
```

**2. Genres Table:**

```sql
CREATE TABLE Genres (
  genre_id INT PRIMARY KEY AUTO_INCREMENT,
  genre_name VARCHAR(255) NOT NULL
);
```

**3. Movie_Genres Table (Many-to-Many Relationship):**

```sql
CREATE TABLE Movie_Genres (
  movie_id INT NOT NULL,
  genre_id INT NOT NULL,
  FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
  FOREIGN KEY (genre_id) REFERENCES Genres(genre_id),
  PRIMARY KEY (movie_id, genre_id)
);
```

**4. Content_Triggers Table (Optional):**

```sql
CREATE TABLE Content_Triggers (
  trigger_id INT PRIMARY KEY AUTO_INCREMENT,
  trigger_name VARCHAR(255) NOT NULL
);
```

**5. Movie_Triggers Table (Optional - Many-to-Many Relationship):**

```sql
CREATE TABLE Movie_Triggers (
  movie_id INT NOT NULL,
  trigger_id INT NOT NULL,
  FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
  FOREIGN KEY (trigger_id) REFERENCES Content_Triggers(trigger_id),
  PRIMARY KEY (movie_id, trigger_id)
);
```

Remember to replace `NOT NULL` with `NULL` for any columns that allow empty values. These queries create the core structure for your movie tracking database. You can add the optional `Content_Triggers` tables if needed.
