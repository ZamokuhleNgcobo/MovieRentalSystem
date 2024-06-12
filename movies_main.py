import streamlit as st

def display_movie_details():
    st.title("ALPHA MOVIES")
    st.sidebar.write("Welcome to ALPHA MOVIES! Please enter the details below:")

    movie_title = st.sidebar.text_input("Enter Movie Title:")
    release_year = st.sidebar.number_input("Enter Release Year:", min_value=1800, max_value=2024, step=1)
    genre = st.sidebar.selectbox("Select Genre:", ("Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Thriller", "Romantic"))

    search_button = st.sidebar.button("Search")

    return movie_title, release_year, genre, search_button

def display_movie_search_results(movie_title, release_year, genre):
    st.write(f"Movie Title: {movie_title}")
    st.write(f"Release Year: {release_year}")
    st.write(f"Genre: {genre}")

def main():
    movie_title, release_year, genre, search_button = display_movie_details()

    if search_button:
        display_movie_search_results(movie_title, release_year, genre)

if __name__ == "__main__":
    main()
