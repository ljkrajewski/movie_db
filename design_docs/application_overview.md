Due to the complexity of building a full web application, here's a breakdown of the front-end functionalities using HTML, CSS, and JavaScript to demonstrate the concepts:

**1. Adding Movies:**

* An HTML form can be created with input fields for each movie property (title, year, media type, etc.).
* A JavaScript function can be used to capture form data upon submission.
* Using AJAX (Asynchronous JavaScript and XML), a POST request can be sent to a server-side script (e.g., Python with a framework like Flask) to process the data and insert it into the database.
* The server-side script would validate and insert the data, and send a success or error message back to the front-end.
* The JavaScript function can update the user interface (UI) based on the response (e.g., display a success message or highlight any errors).

**2. Deleting Movies:**

* You can display a list of movies retrieved from the database using HTML tables.
* Each table row can represent a movie, with a button or checkbox for deletion.
* Clicking the button/checkbox can trigger a JavaScript function that captures the movie ID (e.g., from a hidden field in the table row).
* Another AJAX request (DELETE) can be sent to the server-side script with the movie ID.
* The server-side script would delete the movie from the database and send a confirmation or error message back.
* The JavaScript function can update the UI by removing the deleted movie from the list. 

**3. Searching Movies:**

* An input field can be provided for users to enter search keywords (title, genre, etc.).
* A JavaScript function can be used to capture the search term upon submission or text change in the input field.
* Using AJAX (GET request), the search term can be sent to the server-side script.
* The server-side script would query the database based on the search criteria and return matching movies.
* The retrieved data can be used to dynamically update the UI to display only the searched movies.

**Important Note:**

This is a simplified explanation, and a real web application would require a server-side component to handle database interactions, user authentication, and other functionalities. Frameworks like Flask (Python) or Django (Python) or Spring Boot (Java) can simplify these tasks. 
