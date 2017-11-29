# Metassistant
Django wrapper for managing webapp rapid-prototyping

*under development*

This code contains a lot of 'shell=True', 'sys.path.append(..., os.pardir, os.pardir, ...)', and 'socket.getaddrinfo(...)'.
I would suggest you don't use this unless you know how it all works, and understand the potential security issues.

## Tutorial
-  First you need to clone or download this project
   - git clone https://github.com/tylerjohnhaden/Metassistant.git
-  Using the assistant.py script, you can run three different commands
   - *init* to build the Django project, wraps Django's startproject
     - `python assistant.py init`
   - *app* to create a new webapp, wraps Django's startapp
     - `python assistant.py app NAME`
   - *run* to run server, wraps Django's runserver
     - `python assistant.py run [--port PORT] [--public]`