import os
import webbrowser

path = (os.path.abspath(__file__))
path = path.strip('runwebsite.py') + 'raport.html'
webbrowser.open_new_tab(path) 
