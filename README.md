# UTOPIA
![License](https://poser.pugx.org/laravel/lumen-framework/license.svg)

## An exprimental website to explore colors

![cover](documentation/prototype.png)

Programming is hard, but a lot of fun to learn. To me it really depends what you want to do with it. As a graphic designer I care a lot about tools for designers and this is my second attempt of creating a "browsable color picker" for the web.To make it harder for me I am using the Python programming language (in which I'm a total noob) - This is my first output on the main route ("/") loading my template with the Flask framework and rendering 100 ``<div>`` tags with random colors. My next step is to create a restful api with each color as a route & clickable link to a single page with value and brightness tables of the same given color. Wish me luck. 🤓☕


### Python & Flask
The program code is structured in the folder ``code`` and split in two python files (``server.py``, ``colortools.py``) with the main logic.
As assetes I wrote a simple CSS file (``style.css``) and added two HTML templates containing Flask code (``index.html``, ``colors.html``).

#### Done so far
- [x] Flask is running
- [x] Development server working
- [x] Server code is working - no errorchecks
- [x] Added basic color functionalities
- [x] Tested basic logic
- [x] Seperate server and color code
- [x] Solve Flask middleware
- [x] Simplify templates and markup
- [x] Simplify server code and variables

#### To do
- [ ] Calculate better color lists
- [ ] Make different sections
- [ ] Add CSS effects like gradients
- [ ] Start working on the actual ux (postponed)


### Server code
```$ export FLASK_APP=server.py```

### Run the server
```$ flask run```

### Viewing the rendered page in the browser
![cover](documentation/singlepage.png)
