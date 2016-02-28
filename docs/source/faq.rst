Stupid, yet common mysteries demystefied
========================================

Does ``python`` have access specifiers?
----------------------------------------

Short Answer: *No, it does not*. The top answer on StackOverflow_ is perfect. The philosophy behind access specifiers is,
	
	*It's not about forbidding access or hiding something, it's about implicit API documentation. Developers as well as compilers/interpreter/code-checker easily see which members are recommended to be used and which ones shouldn't get touched (or at least with care). In most cases it would be a horrible mess if all members of a class or module were public. Consider the distinction of private/protected/public members as a service, saying: "Hey, these members are important while those are used internally and probably not useful for you."*

	– Oben Sonne

Then why is the book littered with class names, method names that start with ``_<name>``?

That's a convention followed by all Python Developers, and you should (understand and) follow it too. How is this convention *useful* and who *implements* it? As noted above, most IDEs and other dev-services understand this convention.

The proof_ shows you the configuration of a docstring_ parser called **Napolean**. **Napolean** is used by Sphinx_, an automated documentation generator. You can see that the parser can be told not to ``auto-document`` the *"private"* functions, methods and attributes.

What is ``self``? Is it same as ``this->``?
--------------------------------------------

See what Guido_ has said on "`why explicit self has to stay`_".

.. _StackOverflow: http://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes#answer-1641236
.. _why explicit self has to stay: http://neopythonic.blogspot.in/2008/10/why-explicit-self-has-to-stay.html
.. _Guido: https://www.python.org/~guido/
.. _proof: https://sphinxcontrib-napoleon.readthedocs.org/en/latest/index.html#Config.napoleon_include_private_with_doc
.. _docstring: https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring
.. _Sphinx: http://sphinx-doc.org/