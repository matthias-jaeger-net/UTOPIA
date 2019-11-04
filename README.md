# UTOPIA
![License](https://poser.pugx.org/laravel/lumen-framework/license.svg)

## An exprimental website to explore colors

![cover](documentation/prototype.png)

Programming is hard, but a lot of fun to learn. To me it really depends what you want to do with it. As a graphic designer I care a lot about tools for designers and this is my second attempt of creating a "browsable color picker" for the web.

### Python & Flask
To make it harder for me I am using the Python programming language (in which I'm a total noob) - This is my first output on the main route ("/") loading my template with the Flask framework and rendering 100 ``<div>`` tags with random colors. My next step is to create a restful api with each color as a route & clickable link to a single page with value and brightness tables of the same given color. Wish me luck. 🤓☕

### Done so far
- [x] Flask is running
- [x] Development server working
- [x] Server code is working - no errorchecks
- [x] Added basic color functionalities
- [x] Tested basic logic
- [x] Seperate server and color code

### To do
- [ ] Solve similarColor and similiarColors
- [ ] Solve Flask middleware
- [ ] Simplify templates and markup
- [ ] Simplify server code and variables

### Server code
I am basically using ideas and methods described in the flask quickstart page. https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart My code is in the file ``server.py``.