# import the necessary libraries
import tkinter as tk
from forex_python.converter import CurrencyRates


# define a function for what is to be performed when the convertButton is clicked
def convertCurrency():
    currencyRates = CurrencyRates()
    try:
        currencyFrom = currencyFromList.get(currencyFromList.curselection())
        currencyTo = currencyToList.get(currencyToList.curselection())
    except:
        messageLabel.config(text="No Selection Made!", fg="red")
        amountTo.set("")
        return

    try:
        amount = currencyRates.convert(currencyFrom[0:3], currencyTo[0:3], float(amountFrom.get()))
        amountTo.set(str(round(amount, 4)))
        messageLabel.config(text="Conversion Complete", fg="green")
    except ValueError:
        messageLabel.config(text="Invalid Amount!", fg="red")
        amountTo.set("")
        return

# Make a currency list
currencyList = ["USD - US dollar",
                "JPY - Japanese yen",
                "BGN - Bulgarian lev",
                "CZK - Czech koruna",
                "DKK - Danish krone",
                "GBP - Pound sterling",
                "HUF - Hungarian forint	",
                "PLN - Polish zloty",
                "RON - Romanian leu",
                "SEK - Swedish krona",
                "CHF - Swiss franc",
                "ISK - Icelandic krona",
                "NOK - Norwegian krone",
                "HRK - Croatian kuna",
                "RUB - Russian rouble",
                "TRY - Turkish lira",
                "AUD - Australian dollar",
                "BRL - Brazilian real",
                "CAD - Canadian dollar",
                "CNY - Chinese yuan renminbi",
                "HKD - Hong Kong dollar",
                "IDR - Indonesian rupiah",
                "ILS - Israeli shekel",
                "INR - Indian rupee",
                "KRW - South Korean won",
                "MXN - Mexican peso",
                "MYR - Malaysian ringgit",
                "NZD - New Zealand dollar",
                "PHP - Philippine peso",
                "SGD - Singapore dollar",
                "THB - Thai baht",
                "ZAR - South African rand"]

# Make a root node
root = tk.Tk()
root.geometry("490x480")
root.title("Currency Convertor")

# Make a heading Label and add it to root node
currencyConvertorHeading = tk.Label(root, text="Currency Convertor", bg="blue", fg="white",
                                    font="Helvetica 30 bold italic")
currencyConvertorHeading.pack(fill=tk.X)

# Make two variables to store amount from and amount to
amountFrom = tk.StringVar()
amountTo = tk.StringVar()

# Make a listbox label frame
listboxLabelFrame = tk.Label(root)
listboxLabelFrame.pack(fill=tk.X, pady=(30, 0))

# Make a listbox frame
listboxFrame = tk.Frame(root)
listboxFrame.pack(fill=tk.X, pady=(0, 0))

# Make a amount label frame
amountLabelFrame = tk.Label(root)
amountLabelFrame.pack(fill=tk.X, pady=(5, 0))

# Make a amount Frame
amountFrame = tk.Frame(root)
amountFrame.pack(fill=tk.X, pady=(0, 0))

# Make a button frame
buttonFrame = tk.Frame(root)
buttonFrame.pack(fill=tk.X, pady=(20, 0))

# Make a messageLabel frame
# messageLabelFrame = tk.Frame(root)
# messageLabelFrame.pack(fill=tk.X, pady=(20, 0))

# Make two label and add them to listbox label frame
fromLabel = tk.Label(listboxLabelFrame, text="From ", font="Helvetica 15 bold", fg="brown")
fromLabel.pack(side=tk.LEFT, padx=(40, 55))

toLabel = tk.Label(listboxLabelFrame, text="To ", font="Helvetica 15 bold", fg="brown")
toLabel.pack(side=tk.RIGHT, padx=(0, 47))

# Make two listbox with scrollbar and add them to listbox frame
currencyFromList = tk.Listbox(listboxFrame, width=27, exportselection=False)
currencyFromList.pack(side=tk.LEFT, padx=(44, 0))
scrollbarCurrencyFromList = tk.Scrollbar(listboxFrame)
scrollbarCurrencyFromList.config(command=currencyFromList.yview)
currencyFromList.config(yscrollcommand=scrollbarCurrencyFromList.set)
scrollbarCurrencyFromList.pack(side=tk.LEFT, padx=(0, 39), fill=tk.Y)

currencyToList = tk.Listbox(listboxFrame, width=27, exportselection=False)
currencyToList.pack(side=tk.LEFT, padx=5)
scrollbarCurrencyToList = tk.Scrollbar(listboxFrame)
scrollbarCurrencyToList.config(command=currencyToList.yview)
currencyToList.config(yscrollcommand=scrollbarCurrencyToList.set)
scrollbarCurrencyToList.pack(side=tk.LEFT, padx=(0, 0), fill=tk.Y)

# Make two label and add them to amount label frame
amountFromLabel = tk.Label(amountLabelFrame, text="Amount: ", font="Helvetica 11 italic")
amountFromLabel.pack(side=tk.LEFT, padx=(40, 55))

amountToLabel = tk.Label(amountLabelFrame, text="Amount: ", font="Helvetica 11 italic")
amountToLabel.pack(side=tk.RIGHT, padx=(0, 48))

# Make two entry widgets for inputting amount and add them to amountFrame
amountFromEntry = tk.Entry(amountFrame, textvariable=amountFrom, font=('calibre', 10, 'normal'), width=15)
amountFromEntry.pack(side=tk.LEFT, padx=(44, 0))

amountToEntry = tk.Entry(amountFrame, textvariable=amountTo, font=('calibre', 10, 'normal'), width=15)
amountToEntry.pack(side=tk.RIGHT, padx=(0, 55))

# Make a convert button and add it to buttonFrame
convertButton = tk.Button(buttonFrame, text="Convert", bd="5", command=convertCurrency)
convertButton.pack(side=tk.LEFT, padx=(210, 0))

# Make a message label and add it to messageLabelFrame
messageLabel = tk.Label(root, text="Provide Input to Begin", font="Helvetica 25 bold", fg="green")
messageLabel.pack(pady=(25, 0))

for currency in currencyList:
    currencyFromList.insert(tk.END, currency)
for currency in currencyList:
    currencyToList.insert(tk.END, currency)

root.mainloop()
