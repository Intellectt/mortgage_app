from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:
    MDBottomNavigation:
        panel_color: "#eeeaea"

        MDBottomNavigationItem:
            name: "python"
            text: "Python"
            icon: "language-python"

            MDLabel:
                text: "Tab Python"
                halign: "center"

        MDBottomNavigationItem:
            name: "js"
            text: "JavaScript"
            icon: "language-javascript"

            MDLabel:
                text: "Tab JavaScript"
                halign: "center"

        MDBottomNavigationItem:
            name: "cpp"
            text: "C++"
            icon: "language-cpp"

            MDLabel:
                text: "Tab C++"
                halign: "center"
"""


class BottomNavigationDemo(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    BottomNavigationDemo().run()
