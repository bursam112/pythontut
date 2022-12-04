import functions

# when a program is imported, it executes it fully first.
# this also includes print statements, or anything other than just def as well.

functions.hello()
functions.goodbye()

print(__name__)
print(functions.__name__)

