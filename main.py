from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup

def click():
    ticker = e1.get()
    try:
        baseUrl = 'https://www.marketwatch.com/investing/fund/'
        url = baseUrl + ticker
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        price = soup.find("meta", {"name": "price"})['content']
        change = soup.find("meta", {"name": "priceChange"})['content']
        percent = soup.find("meta", {"name": "priceChangePercent"})['content']
        if "-" in change:
            newchange = f"The Price went down by {change}"
        else:
            newchange = f"The Price went up by {change}"
        ppr = Label(window, text=f'The Price is {price}                  ', background="blue", foreground="black", font="none 15 bold") .grid(row=6, column=0, sticky=W)
        ppc = Label(window, text=f'{newchange}, which is {percent}                ', background="blue", foreground="black", font="none 15 bold") .grid(row=7, column=0, sticky=W)
        print(price)
        print(change)
        print(percent)
    except:
        ppr = Label(window, text=f'Ticker not found.                   ', background="blue", foreground="red", font="none 15 bold") .grid(row=6, column=0, sticky=W)
        ppc = Label(window, text='                                                                            ', background="blue", foreground="black", font="none 15 bold") .grid(row=7, column=0, sticky=W)

window = Tk()
window.geometry("800x400")
window.title("Stock Lookup")
window.configure(background="blue")

Label (window, text="What Stock Do You Want to Look Up? - Enter the Ticker", background="blue", foreground="white", font="none 15 bold") .grid(row=1, column=0, sticky=W)

e1 = tk.Entry(window)


e1.grid(row=2, column=0)

def close():
    window.destroy()
    exit()

Button(window, text="SUBMIT", width=15, command=click) .grid(row=3, column=0, sticky=W)
Button(window, text="Quit", width=15, command=close) .grid(row=10, column=3, sticky=W)


window.mainloop()
