# Changelog

## Unreleased (asians-cloud django-5 fork)

* Support Django 5.x / Python 3.12 and the **psycopg v3** driver.
* The PostgreSQL and PostGIS metrics backends now detect the active driver
  (`psycopg` v3 or `psycopg2`) and wrap the right cursor class. On psycopg v3
  the metrics cursor is layered onto Django's own `connection.cursor_factory`
  after connect (Django sets it while opening the connection), so full
  per-query metrics work on both drivers.
* Bump dependencies: psycopg2 → `psycopg[binary]>=3.2`, `prometheus-client>=0.20`,
  `django-redis>=5.4`, `pytest>=8.2`, `pytest-django>=4.8`, black/flake8/isort
  to current; tox matrix → Django 4.2–5.2 on Python 3.9–3.12.
* Update trove classifiers (Django 3.2–5.2, Python 3.8–3.12).

## v2.2.0 - December 19, 2021

* Switch to Github Actions CI, remove travis-ci.
* Add support for Django 3.2 & 4.0 and Python 3.9 & 3.10

## v2.1.0 - August 22, 2020

* Remove support for older django and python versions
* Add support for Django 3.0 and Django 3.1
* Add support for [PostGIS](https://github.com/korfuri/django-prometheus/pull/221), Thanks [@EverWinter23](https://github.com/EverWinter23)

## v2.0.0 - Jan 20, 2020

* Added support for newer Django and Python versions
* Added an extensibility that applications to add their own labels to middleware (request/response) metrics
* Allow overriding and setting custom bucket values for request/response latency histogram metric
* Internal improvements:
  * use tox
  * Use pytest
  * use Black
  * Automate pre-releases on every commit ot master
  * Fix flaky tests.

## v1.1.0 -  Sep 28, 2019

* maintenance release that updates this library to support recent and supported version of python & Django