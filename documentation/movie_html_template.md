Here's the `movies.html` template to display a list of movies retrieved from the database:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Movie Database</title>
</head>
<body>
  <h1>My Movie Collection</h1>
  <table>
    <thead>
      <tr>
        <th>Title</th>
        <th>Year</th>
        <th>Media Type</th>
        <th>Length</th>
        <th>IMDB Rating</th>
      </tr>
    </thead>
    <tbody>
      {% for movie in movies %}
      <tr>
        <td>{{ movie[1] }}</td>  <td>{{ movie[2] }}</td>  <td>{{ movie[3] }}</td>  <td>{{ movie[4] }}</td>  <td>{{ movie[5] if movie[5] else "-" }}</td>  </tr>
      {% endfor %}
    </tbody>
  </table>
</body>
</html>
```

**Explanation:**

* This is a basic HTML template with a title and a table to display movie information.
* We use Jinja templating syntax (`{% ... %}`) to iterate through the list of movies passed as context from the Flask application (`movies_list` function).
* Inside the loop (`{% for movie in movies %} ... {% endfor %}`), we access individual movie details using their index within the tuple (`movie`). For example, `movie[1]` refers to the movie title (assuming the order matches how you retrieve data from the database).
* The `if` statement within the IMDB rating column checks if a value exists (`movie[5]`). If not (`else`), it displays a hyphen (`-`).

**Customization:**

* You can add more columns to the table to display additional movie information (e.g., MPAA rating, description).
* You can style the table with CSS for better presentation.
* You can add search functionality by including a search bar and modifying the Flask application to handle search queries.
