import datetime
import json
import time
import os
from tkinter import *

def medicine_counter(list_of_meds):
    today = datetime.date.today()
    for meds in list_of_meds:
        for attributes in list(meds.values()):
            string_date = attributes['Last_modified']
            attr_date = datetime.datetime.strptime(string_date, '%Y-%m-%d').date()
            attr_per_day = attributes["Pill's per day"]
            attr_have = attributes['On hand']
            if today > attr_date:
                diff_day = abs((today - attr_date).days)
                number_used = int(attr_per_day) * int(diff_day)
                attributes['On hand'] = int(attr_have) - number_used
                attributes['Last_modified'] = str(today)
    json.dump(list_of_meds,  open('Med_list.json', 'w'))
    return list_of_meds
                
def warning(list_of_meds, root):
    list_of_messages = []
    for meds in list_of_meds:
        for name,  attributes in meds.items():
            attr_have = attributes['On hand']
            attr_per_day = attributes["Pill's per day"]
            num_of_use = (int(attr_have)/ int(attr_per_day))
            if num_of_use <= 5:
                message = name + " needs refilled now"
                list_of_messages.append(message)
    for message in list_of_messages:            
        w = Label(root, text=message)
        w.pack()
    return
            
def main():
    while 1:
        os.chdir("/home/nob0dy/Python_Projects/")
        root = Tk()
        with open('Med_list.json',  'r+') as json_data:
            list_of_meds = json.load(json_data)
            print(list_of_meds)
            new_list = medicine_counter(list_of_meds)
            warning(new_list, root)
        root.mainloop()
        time.sleep(86400)
        #86400
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting application\n')



