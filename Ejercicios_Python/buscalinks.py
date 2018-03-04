principio='a href="'
final='"'
print("intoduce codigo html")
page=str(input())

def buscasiguiente(html):
    pr=html.find(principio,0)
    if pr==-1:
        return None,0
    else:
        print(pr)
        fn=html.find(final,pr+8)
        print(fn)
        url=html[pr+8:fn]
        print (url)
        html=html[fn:]
        return url, html


todos=[]


def AllLinks(html,lista):
    
    while True:
        url,html= buscasiguiente(html)
        if url:
            lista.append(url)
            
        else:
            break
    return html,lista

page,todos=AllLinks(page,todos)

for i in todos:
    print(i+" \n")

print(page)
