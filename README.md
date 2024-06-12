#Alpha Movies Rental System

Overview
Alpha Movies is a movie rental system built using Streamlit and Pandas. This web application allows users to search for movies, view details, and add them to their cart for potential rental. The app is designed to provide a seamless and user-friendly experience with a clean and intuitive interface.

Features
Search Functionality: Users can search for movies by title, release year, and genre.

Movie Display: Movies are displayed in a grid format with posters and titles.

Movie Details: Detailed information about each movie is available upon selection.

Cart Management: Users can add movies to their cart and view their selections.

Installation
Clone the Repository:


git clone https://github.com/your-username/alpha-movies.git
cd alpha-movies
Install Dependencies:


pip install -r requirements.txt
Run the Application:

streamlit run app.py
File Structure
app.py: Main application file containing the Streamlit code.

movies_cleaned_dataset.csv: Dataset containing movie details.

requirements.txt: List of Python dependencies required for the project.

App Description
Page Configuration
The page is configured with a wide layout and a custom title and icon. The sidebar's initial state is collapsed.

Session State
An empty cart list is initialized in st.session_state to keep track of user selections.

Main Function
The main function of the app includes:

A centered title with a custom style.

Loading the movie dataset from a CSV file.

Sidebar inputs for movie title, release year, and genre.

Displaying the movies in a grid layout with columns and rows.

Filter Function
The filter_movie function filters the movies based on the search criteria provided by the user.

Show Movie Details Function
The show_movie_details function displays detailed information about the selected movie and includes options to add or cancel the movie in the cart.

Usage
Search for Movies:

Enter the movie title, release year, or select a genre from the sidebar.
Click the "Search" button.
View Movie Details:

Movies matching the search criteria are displayed in a grid format.
Click the "View" button next to a movie to see its details.
Manage Cart:

Use the "Add to Cart" button to add a movie to your cart.
Use the "Cancel Cart" button to remove a movie from your cart.
View your cart in the sidebar.
Future Improvements
User Authentication: Implement user login and registration for a personalized experience.

Payment Integration: Add functionality for users to complete the rental payment process.

Enhanced Search: Improve search capabilities with more filters and sorting options.

Recommendations: Provide movie recommendations based on user preferences and viewing history.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or bug fixes.
