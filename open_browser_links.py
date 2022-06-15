import webbrowser

with open('./websites.txt') as reader:
  for link in reader:
    webbrowser.open(link.strip()) 
