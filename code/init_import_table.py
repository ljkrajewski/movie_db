'''
Things to note:

Replace the database connection details with your actual credentials.
Update the csv_file variable with the path to your CSV file.
This code assumes the first row of your CSV contains column headers. Modify the code to handle different CSV formats if needed.
Error handling is included for database connection and basic data type conversion. You may want to add more robust validation for data in the CSV file.
'''
import csv
import psycopg2

# Database connection details (replace with your own)
dbname = "your_database_name"
dbuser = "your_username"
dbpassword = "your_password"
dbhost = "localhost"  # or hostname/IP of your database server

# CSV file path (replace with your actual file path)
csv_file = "movies.csv"


def connect_to_db():
    """Connects to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbhost)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def import_movies_from_csv():
    """Reads data from CSV and inserts into Movies and Movie_Genres tables."""
    conn = connect_to_db()
    if not conn:
        return

    cursor = conn.cursor()

    # Assuming the first row of CSV contains column headers (modify as needed)
    with open(csv_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            movie_data = [row[0], int(row[1]), row[2], int(row[3] if row[3] else None), float(row[4] if row[4] else None), row[5], row[6], row[7]]
            genres = row[8].split(",")  # Assuming genres are comma-separated

            # Insert movie data
            insert_movie_query = """
                INSERT INTO Movies (title, release_year, media_type, length, imdb_rating, mpaa_rating, description, location)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING movie_id;
            """
            cursor.execute(insert_movie_query, movie_data)
            conn.commit()

            # Get movie ID for genre association
            movie_id = cursor.fetchone()[0]

            # Insert movie genres (one by one)
            for genre in genres:
                genre_name = genre.strip()  # Remove leading/trailing whitespaces
                insert_genre_query = """
                    INSERT INTO Genres (genre_name)
                    SELECT * FROM (VALUES (%s)) AS tmp (genre_name)
                    WHERE NOT EXISTS (SELECT 1 FROM Genres WHERE genre_name = %s);
                """
                cursor.execute(insert_genre_query, (genre_name, genre_name))
                conn.commit()

                # Get genre ID (if genre already exists, it won't be inserted again)
                cursor.execute("SELECT genre_id FROM Genres WHERE genre_name = %s", (genre_name,))
                genre_id = cursor.fetchone()[0]

                # Link movie and genre
                insert_link_query = "INSERT INTO Movie_Genres (movie_id, genre_id) VALUES (%s, %s);"
                cursor.execute(insert_link_query, (movie_id, genre_id))
                conn.commit()

    cursor.close()
    conn.close()
    print("Movies imported successfully!")


if __name__ == "__main__":
    import_movies_from_csv()
