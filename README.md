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
