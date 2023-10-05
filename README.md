# MLH Production Engineering Fellowship (Meta)

This project serves as a showcase of the diverse technologies I harnessed during this fellowship, allowing you to witness the practical application of my expertise and the growth of my capabilities.

## Features
- Hosting a Flask website on a virtual private server (VPS) using a Digital Ocean droplet running CentosOS (Linux)
- Employing Jinja templates for dynamic HTML page rendering and Bootstrap CSS for mobile-responsive design
- Implementing Flask app routing for the root URL, /aboutme URL, and /timeline URL
- Utilizing MySQL for posting and retrieving timeline posts
- Establishing a CI/CD pipeline for automated testing and deployment on the VPS. This pipeline utilizes Bash scripting, Docker containers, and GitHub Actions, with integrated Discord notifications
- HTTPS certification with NGINX
- Containerizing the infrastructure using Docker and Docker Compose, comprising three containers: myportfolio, mysql, and nginx
- Automated unit testing and integration testing on API endpoints and the MySQL database during push or pull requests to the main branch

## Visit the Live Page at https://gabrielaliera.duckdns.org/

### Week 12 Portfolio
<img src='https://github.com/gabrielaliera/ProductionEngineer-portfolio/blob/main/README-img/week12.PNG' title='Week 12 Portfolio' width='1200' heigth="700" alt='Week 12 Portfolio' />

### Week 6 Portfolio
<img src='https://github.com/gabrielaliera/ProductionEngineer-portfolio/blob/main/README-img/week6-portfolio.PNG' title='Week 6 Portfolio' width='1200' heigth="700" alt='Week 6 Portfolio' />

### Week 1 Portfolio
<img src='https://github.com/gabrielaliera/ProductionEngineer-portfolio/blob/main/README-img/start-portfolio.PNG' title='Week 1 Portfolio' width='1200' heigth="700" alt='Week 1 Portfolio' />


## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

## Notes
I’m incredibly grateful for the Major League Hacking Fellowship and Meta , which not only offered hands-on technical experience but also enabled collaboration with exceptional individuals in the tech industry. I’m excited to apply everything I’ve learned and continue contributing to the ever-evolving world of technology!
