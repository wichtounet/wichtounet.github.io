I'm happy to announce the release of budgetwarrior 1.0. This is a major change
over the previous version.

Web Interface
+++++++++++++

Until now, budgetwarrior could only be used in command line. This is fine for
me, but not for every body. Since I wanted to share my budget with my
girlfriend, I needed something less nerdy ;)

Therefore, I added support for *a web interface for budgetwarrior*. Every feature
of the console application is now available in the web version. Moreover, since
the web version offers *slightly better* graphical capabilities, I added a few
more graphs and somewhat more information at some places.

The web server is coded in C++ (who would have guessed...) and is embedded in
the application, you need to use the command **server** to use it::

    budget server

and the server will be launched (by default at localhost:8080). You can
configure the port with :code:`server_port=X` in the configuration file and the
listen address with :code:`server_listen=X`. You can access your server at
http://localhost:8080.

Here is what this will display:

.. image:: /images/budgetwarrior_web_index.png
   :alt: Web interface index

Note: All the data is randomized

The main page shows your assets, the current net worth, your monthly cash-flow
and the state of your objectives.

The menu will give you access to all the features of the application. You can
add expenses and earnings, see reports, manage your assets and your objectives
and so on. Basically, you can do everything you did in the application, but you
have access to more visualization tools than you would on the console. For
instance, you can access your fortune over time:

.. image:: /images/budgetwarrior_web_fortune.png
   :alt: Web interface fortune graph

or see how your portfolio does in terms of currency:

.. image:: /images/budgetwarrior_web_portfolio_currency.png
   :alt: Web interface portofolio currency breakdown

Normally, unless I forgot something (in which case, I'll fix it), everything
should be doable from the web interface. This is simply easier people that are
not as nerdy as me for console ;)

The management is still the same, the server will write to the same file the
base application uses. Therefore, you cannot use the server and the command line
application on the same machine at the same time.

Server mode
+++++++++++

Although it's not possible to use both the server and the command line
application at the same time, it's possible to use the command line application
in server mode. In this case, instead of reading and writing the data from the
hard disk, the application will send requests to the server to read and write
the data it needs. With this, you can use both the server and the command line
application at the same time!

.. TODO Continue

Assets Tracking
+++++++++++++++

Better console usability
++++++++++++++++++++++++
