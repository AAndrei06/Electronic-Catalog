# Electronic-Catalog

This is a project on which I have worked a lot. It is an electronic catalog that allows teachers to grade students, give homework and receive homework. Each student has a profile page that helps him monitor his progress such as grades , gpa and others. This platform works almost entirely based on ASGI, which allows the transmission of information through WebSockets so the user does not have to refresh the page.The teacher has the possibility to add a student to the class, remove him and create articles that represent the achieved performance. The site also has a REST API that allows users to integrate the application into other programs but also to communicate with the platform without opening a browser, through this REST API users can authenticate with tokens and search with the Algolia search engine. The basis of the application's functionality is Celery, Celery is a task queue that allows the execution of asynchronous processes, which improves the performance of the application, but also runs programs in the background ( like the deletion of authentication tokens that I have implemented).

<h3>Technologies that I used</h3>

<ul>
  <li>Django (Python Web Framework)</li>
  <li>Django Rest Framework (REST API framework for Django)</li>
  <li>Django Channels (I used this library to build the ASGI app and communicate with websockets)</li>
  <li>Celery and Celery Beat (I used them to run asynchronous tasks and also other programs in the background)</li>
  <li>Redis (I used this as a result backend for Celery and to store information about Channel Layers)</li>
  <li>RabbitMQ (I used this as a message broker for Celery)</li>
  <li>Flower (I used this to monitor the execution of celery tasks)</li>
  <li>Docker (I used this to run all the images that will help Celery work and also to start the database and PgAdmin4)</li>
  <li>Algolia Search Engine (I used this to implement a faster and easier search for the API's of this app)</li>
  <li>PostgreSQL and PgAdmin4 (I used this as a database and to write queries)</li>
  <li>AJAX (I used this for the authentication system but also to send files and data securely without refreshing the page,it is from JQuery)</li>
  <li>Chart.js (I used this to display beautifull charts in JS)</li>
</ul>
<br>
<h3>How to start this project?</h3>
<h5>If you downloaded the zip file for this project or cloned it and you want to see it running do the following: </h5>
<ul>
  <li>Run: <b>pip install -r requirements.txt</b> (copy the requirements.txt file)</li>
  <li>Run: <b>docker-compose up --build</b> to run all the images that are necessary for this project, note that you should be in the same directory as the docker-compose.yml file</li>
  <li>Run: <b>python3 manage.py runserver 127.0.0.1:8000</b> to run the django application</li>
  <li>Run: <b>celery --app=electronic_catalog worker --loglevel=INFO -B</b> to run Celery and Celery Beat (if you only want to run Celery remove <b>-B</b> at the end)</li>
  <h2>Now the project should work</h2>
  <br>
  <h2>If there are some error try to run:</h2>
  <br>
  <ul>
    <li><b>sudo kill -9 `sudo lsof -t -i:5432`</b> to kill a process that runs on the same port as the database, this is for Linux users</li>
    <li><b>sudo service redis-server stop</b> to stop the redis server</li>
  </ul>
  <br>
  <h2>Then try again</h2>
</ul>
