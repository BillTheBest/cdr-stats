.. _installation-overview:

=====================
Installation overview
=====================

.. _install-requirements:

Install requirements
====================

A Requirements file gives you a way to create an environment where you can put
all optional dependencies which are needed for your Project/Application.

To get started with Cdr-stats you must have the following installed:

- python >= 2.5 (programming language)
- Apache / http server with WSGI modules
- Django Framework >= 1.3 (Python based Web framework)
- Celery >= 2.2 (Asynchronous task queue/job queue based on distributed message passing)
- django-celery >= 2.2.4 (Celery integration for Django)
- django-pagination >= 1.0.7 (Utilities for creating robust pagination tools throughout a django application)
- django-uuidfield >= 0.2 (Provides a UUIDField for your Django models)
- django-reusableapps >= 0.1.1 (Python module to enable Django to load reusable, pluggable and egg-based applications)
- docutils >= 0.7 (Text processing system for processing plaintext documentation into useful formats)
- importlib >= 1.0.2 (Implementation of the `import` statement)
- kombu >= 1.0.2 (An AMQP - Advanced Message Queuing Protocol messaging framework for Python)
- pyparsing >= 1.5.5 (A general parsing module for Python)
- python-dateutil >= 1.5 (Extensions to the standard datetime module)
- redis >= 2.2.2 (Redis Python Client)
- simplejson >= 2.1.3 (Simple, fast, complete, correct and extensible JSON)
- uuid >= 1.30 (UUID object and generation functions )
- wsgiref >= 0.1.2 (Validation support for WSGI )
- django-tastypie (Creating delicious APIs for Django)
- django-notification >= 0.1.3 (User notification management for the Django web framework)


Use PIP to install all the requirements,::

    $ pip install -r requirements.txt


.. _installation-script:

Installation Script
===================

You can install CDR-Stats manually or using the shell script provided.

To install CDR-Stats using the script,::

    $ chmod +x install/install-cdrstats.sh

    $ ./install/install-cdrstats.sh

    $ chmod +x install/install-celery.sh

    $ ./install/install-celery.sh


.. _running-cdrstats:

Running a CDR-Stats
===================

Inside CDR-Stats directory you should run::

    $ mkdir database

    $ python manage.py syncdb

    $ python manage.py collectstatic

    $ python manage.py runserver


``syncdb`` will create a database named test.db in ``database`` folder of the
CDR-Stats directory. We have configured Newfies-Dialer to do this, but you
can change this simply by modifying settings.py where DATABASES dictionary is
constructed. You can find more information about this in the 
Django documentation.

``collectstatic`` will fetch all necessary media files and put them into
``static`` folder defined in the settings module.

``runserver`` runs an embedded webserver to test your site.
By default it will run on http://localhost:8000. This is configurable and more
information can be found on ``runserver`` in Django documentation.