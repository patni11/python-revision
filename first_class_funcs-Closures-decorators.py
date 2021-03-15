# Example of a first class and a closure
def html(tag):
    def printer(message):
        print("<{0}> {1} </{0}>".format(tag, message))

    return printer


h1 = html("H1")
p = html("p")

h1('Makes a H1 Heading')
p('makes a paragraph')

# A decorator is the same thing, excpet the outer fucniton takes in a fucntion as a argument
