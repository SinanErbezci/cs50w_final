get_object_or_404 -> gets the objects. If three is no object it raises 404.

Always return an HttpResponseRedirect after successfully dealing
with POST data. This prevents data from being posted twice if a
user hits the Back button.

# Query expressions.
F() expressions. Directly doing database manupilations. No loading data to python and make changes etc.
getting the database, rather than Python, to do work
reducing the number of queries some operations require
reporter = Reporters.objects.get(name="Tintin")
reporter.stories_filed = F("stories_filed") + 1
reporter.save()

# Generic views
These views represent a common case of basic web development: getting data from the database according to a parameter passed in the URL, loading a template and returning the rendered template. Because this is so common, Django provides a shortcut, called the “generic views” system.

path("<int:pk>") -> pk necessary for generic views

