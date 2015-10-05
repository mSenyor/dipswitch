__version__ = '0.1'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

int_address=1
bin_address='{0:09b}'.format(int_address)

def update_address(num):
    global int_address
    global bin_address
    print "old address: %d" % int_address
    print "old dipswitch: %s" % bin_address
    int_address=num
    if int_address >= 1 and int_address <= 511:
        bin_address='{0:09b}'.format(int_address)
    elif int_address == 0 or int_address >= 512:
        bin_address='{0:09b}'.format(0)

    print "new address: %d" % int_address
    print "new dipswitch: %s" % bin_address
 
def text_to_address(string):
    if int(string)>= 512:
        return 0

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
    out = str(hund)+str(tens)+str(ones)
    if int(out) >= 512 or int(out) == 0:
        return '512'
    return out
    


class TogglesPanel(BoxLayout):
    pass

class MidPanel(BoxLayout):
    def all_up(self):
        stuff=self.ids['address']
        curr_add=text_to_address(stuff.text)
        if curr_add < 511:
            curr_add+=1
            stuff.text = address_to_text(curr_add)
        else:
            curr_add=0
            stuff.text = '512'
        print curr_add
        update_address(curr_add)


    def all_down(self):
        stuff=self.ids['address']
        curr_add=text_to_address(stuff.text)
        if curr_add > 0 and curr_add < 512:
            curr_add-=1
            stuff.text = address_to_text(curr_add)
        else:
            curr_add=511
            stuff.text = '511'
        print curr_add
        update_address(curr_add)


    def hund_up(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if hund != 5:
            hund+=1
        else:
            hund=0
        
        add_str = str(hund)+str(tens)+str(ones)
        curr_add = text_to_address(add_str)
        update_address(curr_add)
        if curr_add >= 1 and curr_add <= 511:
            stuff.text = add_str
        else:
            stuff.text = '512'

    def tens_up(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if hund != 5:
            if tens != 9:
                tens+=1
            else:
                tens=0
        else:
            if tens > 0:
                tens=0
            else:
                tens=1
        add_str = str(hund)+str(tens)+str(ones)
        curr_add = text_to_address(add_str)
        update_address(curr_add)

        if curr_add >= 1 and curr_add <= 511:
            stuff.text = add_str
        else:
            stuff.text = '512'



    def ones_up(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if hund != 5:
            if ones != 9:
                ones+=1
            else:
                ones=0
        else:
            if tens == 0:
                if ones != 9:
                    ones+=1
                else:
                    ones=0
            else:
                if ones <= 1:
                    ones += 1
                else:
                    ones=0
        add_str = str(hund)+str(tens)+str(ones)
        curr_add = text_to_address(add_str)
        update_address(curr_add)

        if curr_add >= 1 and curr_add <= 511:
            stuff.text = add_str
        else:
            stuff.text = '512'



    def hund_down(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if hund != 0:
            hund-=1
        else:
            hund=5
        add_str = str(hund)+str(tens)+str(ones)
        curr_add = text_to_address(add_str)
        update_address(curr_add)

        if curr_add >= 1 and curr_add <= 511:
            stuff.text = add_str
        else:
            stuff.text = '512'



    def tens_down(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if tens != 0:
            tens-=1
        else:
            tens=9
        add_str = str(hund)+str(tens)+str(ones)
        curr_add = text_to_address(add_str)
        update_address(curr_add)

        if curr_add >= 1 and curr_add <= 511:
            stuff.text = add_str
        else:
            stuff.text = '512'



    def ones_down(self):
        stuff=self.ids['address']
        hund=int(stuff.text[0])
        tens=int(stuff.text[1])
        ones=int(stuff.text[2])
        if ones != 0:
            ones-=1
        else:
            ones=9
        add_str = str(hund)+str(tens)+str(ones)
        curr_add = text_to_address(add_str)
        update_address(curr_add)

        if curr_add >= 1 and curr_add <= 511:
            stuff.text = add_str
        else:
            stuff.text = '512'





class UpButtons(BoxLayout):
    pass

class DownButtons(BoxLayout):
    pass

class ButtonRow(BoxLayout):
    pass

class DipSwitchPanel(BoxLayout):
    pass
    #switch_1=0
    #switch_2=0
    #switch_4=0
    #switch_8=0
    #switch_16=0
    #switch_32=0
    #switch_64=0
    #switch_128=0

class SingleSwitch(BoxLayout):
    pass

class MainView(BoxLayout):
    add_panel = TogglesPanel()
    bin_panel = DipSwitchPanel()

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
