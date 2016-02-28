# Nothing for you here (yet)

This repo holds (sub-optimal) implementations of a few data structures in `python`. The aim is to provide a boilerplate package that can be built upon by others studying DS.

##Features

* **Complete documentation using [Sphinx](sphinx-doc.org)**, the best automated doc generator for Python.
* **Include rigorous testing**, so that development happens on a tight leash of reliabilty, correctness. `unittests` can also be used as **autograders**.
* Platform to discuss issues, post solutions/questions (via [gists](gist.github.com))
* Can publish a website (free, cool layout, written in `reST` or `md`) thru [`gh-pages`](pages.github.com)
* Easy collaborative development, versioning and code reviews.
* Automated build, testing systems ([travisCI](travis-ci.org))
* Documentation can be hosted (free) on readthedocs.com or readme.io

##Contributing, Setting it all up

Clone the project into your local directory using CLI `git`. You don't really need `git` but it's strongly recommended that you use this powerful tool. In that cas download the `.zip` (top right).

This package supports `python 2.7+`. So your local machine must have `2.7` and `3.4+` installed.
Once the repo-code is on your local machine, 

 - [ ] Install Sphinx, and any other dependencies. You can do that via `git` (bleeding edge) or `pip` (pretty recent, suggested) or the system package manager. Get for both python versions.
 - [ ] Run the following command. There should be no errors.
 ```
 cd docs/
 make html
 ```
 - [ ] open `build/html/index.html` in the browser.

**Congrats!** You've setup the environment. Use `array_stack.py` as a reference and modify other DS implementations.

##Sphinx and `autodocs`

Sphinx is a powerful tool and I redirect you to the following resources for now. I might write a `this-repo-specific` guide later.

- https://sphinx-docs.org
- [Example Documentation](https://sphinxcontrib-napoleon.readthedocs.org/en/latest/), servers as a reference for all keywords that can be used for *in-file* documentation.

###Sphinx workings
Sphinx uses the files in `docs/source/*.rst` and *in-file* documentation *(as content source)* to generate the docs.
`docs/conf.py` and `Makefile` help *building* the `source/*` into actual documentation.
The best thing about these systems is that **you'll have to** document your source properly. With no extra effort, you get beautiful `html`, `latex` and `pdf` documentation, complete with examples and `tests`.

##Agenda

Issues and Milestones drive this project.
