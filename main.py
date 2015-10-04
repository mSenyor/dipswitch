__version__ = '0.1'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainView(BoxLayout):
    def input_to_binary(self):

        in_txt = self.ids['address']

        label = self.ids['binary']
        try:
            int_add=int(in_txt.text)
        except ValueError:
            int_add=0
            print "value error"

        print "int_add: %d" % int_add
        #if int_add != 0 and isinstance(in_txt.text, int):
        if int_add != 0 and int(in_txt.text) == float(in_txt.text):
            print "int(in_txt.text) == float(in_txt.text)"

            if int(in_txt.text) < 512:
                label.text='{0:09b}'.format(int(in_txt.text))
            else:
                label.text='Bad Value'
        else:
            label.text='Bad Value'

class DipSwitch(App):
    def build(self):
        return MainView()

if __name__ == "__main__":
    DipSwitch().run()
