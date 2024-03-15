# Electronic-Catalog

This is a project on which I have worked a lot. It is an electronic catalog that allows teachers to grade students, give homework and receive homework. Each student has a profile page that helps him monitor his progress such as grades , gpa and others. This platform works almost entirely based on ASGI, which allows the transmission of information through WebSockets so the user does not have to refresh the page.The teacher has the possibility to add a student to the class, remove him and create articles that represent the achieved performance. The site also has a REST API that allows users to integrate the application into other programs but also to communicate with the platform without opening a browser, through this REST API users can authenticate with tokens and search with the Algolia search engine. The basis of the application's functionality is Celery, Celery is a task queue that allows the execution of asynchronous processes, which improves the performance of the application, but also runs programs in the background ( like the deletion of authentication tokens that I have implemented).

<h3>Technologies that I used</h3>

<ul>
  <li>Django (Python Web Framework)</li>
</ul>
