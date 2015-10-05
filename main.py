__version__ = '0.1'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

def text_to_address(string):
    hund = int(string[0])
    tens = int(string[1])
    ones = int(string[2])
    return hund*100+tens*10+ones

def address_to_text(add):
    ones=add%10
    add=add-ones
    if add < 10 :
        tens = 0
        hund = 0
    else:
        tens=(add%100)/10
        add=add-tens
        if add < 100:
            hund = 0
        else:
            hund=add/100
    return str(hund)+str(tens)+str(ones)
    


class TogglesPanel(BoxLayout):
    pass

class MidPanel(BoxLayout):
    def all_up(self):
        stuff=self.ids['address']
        curr_add=text_to_address(stuff.text)
        if curr_add < 511:
            stuff.text = address_to_text(curr_add+1)
        else:
            stuff.text = '000'

    def all_down(self):
        stuff=self.ids['address']
        curr_add=text_to_address(stuff.text)
        if curr_add > 000 and curr_add < 512:
            stuff.text = address_to_text(curr_add-1)
        else:
            stuff.text = '511'

    def hund_up(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if hund != 5:
            hund+=1
        else:
            hund=0
        stuff.text = str(hund)+str(tens)+str(ones)

    def tens_up(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if tens != 9:
            tens+=1
        else:
            tens=0
        stuff.text = str(hund)+str(tens)+str(ones)

    def ones_up(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if ones != 9:
            ones+=1
        else:
            ones=0
        stuff.text = str(hund)+str(tens)+str(ones)

    def hund_down(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if hund != 0:
            hund-=1
        else:
            hund=5
        stuff.text = str(hund)+str(tens)+str(ones)

    def tens_down(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if tens != 0:
            tens-=1
        else:
            tens=9
        stuff.text = str(hund)+str(tens)+str(ones)

    def ones_down(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if ones != 0:
            ones-=1
        else:
            ones=9
        stuff.text = str(hund)+str(tens)+str(ones)



class UpButtons(BoxLayout):
    pass

class DownButtons(BoxLayout):
    pass

class ButtonRow(BoxLayout):
    pass



class MainView(BoxLayout):
    pass

    ###def input_to_binary(self):
###
        ###in_txt = self.ids['address']
###
        ###label = self.ids['binary']
        ###try:
            ###int_add=int(in_txt.text)
        ###except ValueError:
            ###int_add=0
            ###print "value error"
###
        ###print "int_add: %d" % int_add
        ####if int_add != 0 and isinstance(in_txt.text, int):
        ###if int_add != 0 and int(in_txt.text) == float(in_txt.text):
            ###print "int(in_txt.text) == float(in_txt.text)"
###
            ###if int(in_txt.text) < 512:
                ###label.text='{0:09b}'.format(int(in_txt.text))
            ###else:
                ###label.text='Bad Value'
        ###else:
            ###label.text='Bad Value'

class DipSwitch(App):
    def build(self):
        return MainView()

if __name__ == "__main__":
    DipSwitch().run()
