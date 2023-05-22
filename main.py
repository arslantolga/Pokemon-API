import tkinter
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
import requests

# url = "https://pokeapi.co/api/v2/pokemon-species/"
# count = 1
# response = requests.get(url)
# icerik = response.json()
#
# for i in icerik["results"]:
#     url = f"https://pokeapi.co/api/v2/pokemon-species/{count}"
#     print(f"Pokemon's name : {i['name']}")
#     response = requests.get(url)
#     print(f"{i['name'].capitalize()}'s growth rate : ",response.json()['growth_rate']["name"])
#     print(f"{i['name'].capitalize()}'s habitat : ", response.json()['habitat']["name"])
#     print(f"{i['name'].capitalize()} is baby? : ", response.json()['is_baby'])
#     print(f"{i['name'].capitalize()} is legendary? : ", response.json()['is_legendary'])
#     print(f"{i['name'].capitalize()} is mythical? : ", response.json()['is_mythical'])
#     print(f"{i['name'].capitalize()}'s shape : ", response.json()['shape']["name"])
#     print("-----------------------------------------------------------")
#     count += 1


def getir():
    deger = poke_entry.get()
    url = "https://pokeapi.co/api/v2/pokemon-species/"
    response = requests.get(url)
    icerik = response.json()

    for i in enumerate(icerik["results"]):
        if deger.lower() in i[1]['name']:
            url = f"https://pokeapi.co/api/v2/pokemon-species/{i[0]+1}"
            print(f"Pokemon's name : {i[1]['name']}")
            response = requests.get(url)
            my_text = f"""
            Pokemon's name : {i[1]['name'].capitalize()}
            {i[1]['name'].capitalize()}'s growth rate : {response.json()['growth_rate']["name"]}
            {i[1]['name'].capitalize()}'s habitat : {response.json()['habitat']["name"]}
            {i[1]['name'].capitalize()} is baby? : {response.json()['is_baby']}
            {i[1]['name'].capitalize()} is legendary? : {response.json()['is_legendary']}
            {i[1]['name'].capitalize()} is mythical? : {response.json()['is_mythical']}
            {i[1]['name'].capitalize()}'s shape : {response.json()['shape']["name"]}
            """
            pokemon_label = tkinter.Label(text=my_text,font=FONT,padx=0.1,justify="left",foreground="green")

            pokemon_label.pack()



            print(f"{i[1]['name'].capitalize()}'s growth rate : ", response.json()['growth_rate']["name"])
            print(f"{i[1]['name'].capitalize()}'s habitat : ", response.json()['habitat']["name"])
            print(f"{i[1]['name'].capitalize()} is baby? : ", response.json()['is_baby'])
            print(f"{i[1]['name'].capitalize()} is legendary? : ", response.json()['is_legendary'])
            print(f"{i[1]['name'].capitalize()} is mythical? : ", response.json()['is_mythical'])
            print(f"{i[1]['name'].capitalize()}'s shape : ", response.json()['shape']["name"])
            print("-----------------------------------------------------------")











window = tkinter.Tk()
window.title("Pokemon")
window.geometry("380x680")

my_image = ImageTk.PhotoImage(Image.open("pokemon.png"))

FONT = ("Arial", 13,"bold")

empty_image = tkinter.Label(text="",pady=1)
empty_image.pack()

image_label = tkinter.Label(image=my_image)
image_label.pack()

empty_image = tkinter.Label(text="",pady=1)
empty_image.pack()

title_label = tkinter.Label(text="Enter Your Pokemon",font=FONT)
title_label.pack()

empty_image = tkinter.Label(text="",pady=1)
empty_image.pack()

poke_entry = tkinter.Entry()
poke_entry.pack()

empty_image = tkinter.Label(text="",pady=1)
empty_image.pack()

button = tkinter.Button(text="Get",command=getir,padx=10,pady=5,font=("Arial",10,"bold"))
button.pack()













window.mainloop()