
YouTube Manager

This is a simple text Data management application built using Python and SQLite3. The application allows users to add, view, update, and delete videos from a local SQLite database.

Features

- Add new videos with ID, name, and time.
- View all stored videos.
- Search for a particular video by its ID.
- Update video details.
- Delete a video by ID.
- Simple and intuitive command-line interface.

Requirements

- Python 3.x
- SQLite3 (comes pre-installed with Python)

Installation

1. Clone the repository or download the Python script.
2. Ensure you have Python installed on your machine.
3. Open a terminal/command prompt and navigate to the directory containing the script.

Usage

1. Run the script:

    python youtubemanager.py

2. Choose from the menu options:

    - 1: Add a new video.
    - 2: View all videos.
    - 3: View a particular video by ID.
    - 4: Delete a video by ID.
    - 5: Update the details of an existing video.
    - 6: Exit the program.

Example

- Add a video: Enter a unique ID, video name, and time when prompted.
- View videos: List all available videos or a specific one based on the ID.
- Delete a video: Enter the ID of the video you wish to delete.
- Update a video: Enter the ID of the video, along with the new name and time.

Database Structure

The application uses an SQLite database (youtubemanager.db) with a single table:

- Table Name: youtubemanager
  
  | Column Name | Data Type |
  |-------------|-----------|
  | ID          | INTEGER   |
  | NAME        | TEXT      |
  | TIME        | TEXT      |

License

This project is licensed under the MIT License.
