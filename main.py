import requests
import pprint as pp
import tkinter
import random
font = ('Arial', 30, "normal")
font2 = ('Arial', 25, "bold")

window = tkinter.Tk()
window.title("poke names from poke api")
window.minsize(width=300, height=200)

itemlist = []


url = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}



for offset in range(0, 1000, 100):
    params['offset'] = offset  # add new value to dict with `limit`
    response = requests.get(url, params=params)

    if response.status_code != 200:
            print(response.text)
    else:
        data = response.json()
        # pp.pprint(data)
        for item in data['results']:
            itemlist.append(item['name'])



itemappended = random.choice(itemlist)

my_label = tkinter.Label(text="Poke Names:" ,font=font)
my_label.pack()
my_label2 = tkinter.Label(text=itemappended, font=font2)
my_label2.pack()
window.mainloop()