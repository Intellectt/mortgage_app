from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDLabel:
        text: "Hello APK"
        halign: "center"
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()