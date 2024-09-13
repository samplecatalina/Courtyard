# Courtyard

• Engineered web app with Vue.js front end and Django back end, with Redis for caching and MySQL as persistence.

• Supported user registration/authentication via Email/SMS with Celery, supported SSO with Django REST
framework JWT, enabled drf-extensions to cache frequently queried data into Redis.

• Implemented distributed file storage system in Django with FastDFS to handle multimedia resources of SKU.

• Setup automated timed task with django-crontab to staticize frequently visited pages to optimize app performance.

• Implemented optimistic locking in MySQL with Django atomic for concurrent requests and roll-back.

• Deployed through dockerization containers with Nginx(Vue) + uwsgi(Django)



Landing page at: 121.4.47.229:8080

Add to hosts file:

121.4.47.229 image.courtyard.site

121.4.47.229 www.courtyard.site

