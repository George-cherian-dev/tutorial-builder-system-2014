import urllib2

def noHTML(definition):
    command = False

    while command is False:
        lessOpen = definition.find('<')
        greatClose = definition.find('>')
        if lessOpen > -1 and greatClose > -1:
            definition = definition[0:lessOpen] + definition[greatClose+1:]
        else:
            command = True

    return definition



def main():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for letter in letters:
        response = urllib2.urlopen("http://dictionary.reference.com/browse/"+letter)
        page_source = response.read()

        beginDef = page_source.find('<div class="def-content">')

        if beginDef > -1:
            endDef = page_source[beginDef:beginDef+3000].find('</div>')
            print letter+":",noHTML(page_source[beginDef:beginDef+endDef])

        else:
            beginDef = page_source.find('</span> <div class="luna-Ent">')

            if beginDef > -1:
                endDef = page_source[beginDef:beginDef+3000].find('</div>')
                print letter+":",noHTML(page_source[beginDef+30:beginDef+endDef])

            else:
                print letter, "has no definition"

    for firstletter in letters:
        for letter in letters:
            response = urllib2.urlopen("http://dictionary.reference.com/browse/"+firstletter+letter)
            page_source = response.read()

            beginDef = page_source.find('<div class="def-content">')

            if beginDef > -1:
                endDef = page_source[beginDef:beginDef+3000].find('</div>')
                print firstletter+letter+":",noHTML(page_source[beginDef+20:beginDef+endDef])

            else:
                beginDef = page_source.find('</span> <div class="luna-Ent">')

                if beginDef > -1:
                    endDef = page_source[beginDef:beginDef+3000].find('</div>')
                    print firstletter+letter+":",noHTML(page_source[beginDef+30:beginDef+endDef])

                else:
                    print firstletter+letter, "has no definition"

main()
