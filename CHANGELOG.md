# Changelog

## Unreleased (asians-cloud django-5 fork)

* Support Django 5.x / Python 3.12 and the psycopg v3 driver.
* The PostgreSQL and PostGIS metrics backends now import `psycopg2` lazily:
  when only psycopg v3 is installed (the Django 5 default), the per-cursor
  `cursor_factory` wiring is skipped and connection-level metrics still work.
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