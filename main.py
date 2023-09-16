import requests
import pprint as pp
import tkinter
from tkinter import END, Text
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

def button_task():
    text_box.delete('1.0', END)
    itemappended = random.choice(itemlist)
    text_box.insert(END, itemappended)



my_label = tkinter.Label(text="Poke Names:" ,font=font)
my_label.pack()
text_box = tkinter.Text(window, height=10, width=50)
text_box.pack()
get_button = tkinter.Button(window, text="Get Poke", command=button_task)
get_button.pack()
#my_label2 = tkinter.Label(text=itemappended, font=font2)
#my_label2.pack()



window.mainloop()