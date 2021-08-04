import pyshorteners
link = input("Enter a link : ")
shortener=pyshorteners.Shortener()
x = shortener.tinyurl.short(link)
print("\nHere is your shorterned link \t\n")
print(x)



