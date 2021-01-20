import os

visited = open("visited.txt", "w")


with open("seed.txt") as seed:
    for link in seed:
        visited.write(link)
        links = open("link.txt", "w")
        links.write(link)
        links.close()
        execfile("links.py")
        execfile("cleanHtml.py")
        with open("selected.txt") as selected:
            for s in selected:
                visited.write(s)

            selected.close()
