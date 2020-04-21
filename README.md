# Yet Another Ekşi Sözlük Clone

# Table of Contents <!-- :TOC: -->
- [Yet Another Ekşi Sözlük Clone](#yet-another-ekşi-sözlük-clone)
- [Installation](#installation)
- [Usage](#usage)
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

![Screenshot-1](screenshots/ss1.png)
![Screenshot-2](screenshots/ss2.png)
![Screenshot-3](screenshots/ss3.png)
![Screenshot-4](screenshots/ss4.png)
![Screenshot-5](screenshots/ss5.png)
![Screenshot-6](screenshots/ss6.png)
![Screenshot-7](screenshots/ss7.png)
![Screenshot-8](screenshots/ss8.png)
![Screenshot-9](screenshots/ss9.png)
![Screenshot-10](screenshots/ss10.png)

# Contributors

- [KaratasFurkan](https://github.com/KaratasFurkan)
- [budancamanak](https://github.com/budancamanak)
- [mertturkmenoglu](https://github.com/mertturkmenoglu)
- [seyyidibrahimgulec](https://github.com/seyyidibrahimgulec)
