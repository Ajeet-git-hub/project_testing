------------
------------
 POLL
------------
------------

polls is a django web based applications. For each question, visitors
can choose a fixe number of answers.

Detailed information in in docs directory.


Quick start
-------------

1. Add poll in you INSTALLED_APPS setting like this::

	INSTALLED_APPS = [
		...,
		'poll',		
	]

2. Include the poll URLconfig in your project urls.py like this ::

	path('poll/', include('poll.urls')),

3. Run  ``python manage.py migrate`` to create poll models

4. start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need admin app enabled)

5. Visit http://127.0.0.1:8000/poll/ to participate  in the poll.

