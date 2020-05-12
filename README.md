# Yet Another Ekşi Sözlük Clone

Here is a live version of the application: https://yasozluk.herokuapp.com/

# Table of Contents <!-- :TOC_3: -->
- [Yet Another Ekşi Sözlük Clone](#yet-another-ekşi-sözlük-clone)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
  - [Homepage](#homepage)
  - [Signup](#signup)
  - [Login](#login)
  - [Entries of a topic](#entries-of-a-topic)
  - [New topic](#new-topic)
  - [Search topic](#search-topic)
  - [List topics by a channel](#list-topics-by-a-channel)
  - [User dropdown](#user-dropdown)
  - [User entries](#user-entries)
  - [User votes](#user-votes)
  - [User favorites](#user-favorites)
  - [Private messages](#private-messages)
- [Contributors](#contributors)

# Installation

1. Clone this repository:

    `$ git clone https://github.com/seyyidibrahimgulec/yasozluk.git`

2. Create a [virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments
   "Official documentation") in the project folder:

    `$ python -m venv venv`

3. Activate the virtual environment:

    `$ source venv/bin/activate`

4. Install the requirements:

    `$ pip install -r requirements.txt`

5. Create database

    `$ psql`
    `$ CREATE DATABASE yasozluk;`

6. Migrate database

    `$ python manage.py migrate`

# Usage

1. To start server, run this command in the project directory:

    `$ python manage.py runserver`

2. Open http://localhost:8000 to view it in the browser.

# Screenshots
## Homepage
![homepage](screenshots/homepage.png)
## Signup
![signup](screenshots/signup.png)
## Login
![login](screenshots/login.png)
## Entries of a topic
![topic_entries](screenshots/topic_entries.png)
## New topic
![new_topic](screenshots/new_topic.png)
## Search topic
![search_topic](screenshots/search_topic.png)
## List topics by a channel
![list_topic_by_channel](screenshots/list_topic_by_channel.png)
## User dropdown
![user_dropdown](screenshots/user_dropdown.png)
## User entries
![user_profile_entries](screenshots/user_profile_entries.png)
## User votes
![user_profile_votes](screenshots/user_profile_votes.png)
## User favorites
![user_profile_favorites](screenshots/user_profile_favorites.png)
## Private messages
![messages](screenshots/messages.png)

# Contributors

- [KaratasFurkan](https://github.com/KaratasFurkan)
- [budancamanak](https://github.com/budancamanak)
- [mertturkmenoglu](https://github.com/mertturkmenoglu)
- [seyyidibrahimgulec](https://github.com/seyyidibrahimgulec)
