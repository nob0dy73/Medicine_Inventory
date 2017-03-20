import datetime
import json
import sys
        
def create_list_meds():
    print("CAUTION THIS WILL OVERRIDE ANY CURRENT LIST!")
    print("Please input your medication list")
    list_of_meds = []
    while True:
        med = get_current_med()
        list_of_meds.append(med)
        list_complete = input('Is there more meds? yes or no: ')
        if list_complete == 'no':
            break
    while True:
        for med in list_of_meds:
            print(med)
        sanity_check_list = input('Is the list correct? yes or no: ')
        if sanity_check_list != 'yes':
            list_of_meds = create_list_meds()
        else:
            break
        list_of_meds,  sanity_check_list = create_list_meds()
    return list_of_meds
    
def get_current_med():
        today = datetime.date.today()
        pill_name = (input("Enter the medicine's name and dosage: "))
        pill_per_day = int(input("Enter how many taken per day: "))
        pill_inv = int(input("How many pills on hand: "))
        med = {pill_name : {"Pill's per day":pill_per_day, "On hand":pill_inv, "Last_modified": str(today)}}
        while True:
            print(med)
            sanity_check_current = input("Is the medicine correct? yes or no: ")
            if sanity_check_current != 'yes':
                med = get_current_med()
            else: 
                break
        return med
        
def add_med(list_of_meds):
    med = get_current_med()
    list_of_meds.append(med)
    return list_of_meds
    
def remove_med(list_of_meds):
    for index,  med in enumerate(list_of_meds):
        print(index,  ''.join(med.keys()))
    pill_number = int(input("Enter the medicine's number: "))
    pill_name = None
    for index,  med in enumerate(list_of_meds):
        if pill_number == index:
            print(index,  str(med.keys()))
            pill_name = ''.join(med.keys())
    while True:
        print(pill_name)
        sanity_check_remove = input("Do you want to remove this medicine? yes or no: ")
        if sanity_check_remove == 'yes':
            for med in list_of_meds:
                if pill_name in med.keys():
                    list_of_meds.remove(med)
            return list_of_meds
        else:
            print('exiting')
            break

def update_med(list_of_meds):
    today = datetime.date.today()
    for index,  med in enumerate(list_of_meds):
        print(index,  ''.join(med.keys()))
    pill_number = int(input("Enter the medicine's number you wish to update: "))
    pill_name = None
    for index,  med in enumerate(list_of_meds):
        if pill_number == index:
            print(index,  str(med.keys()))
            pill_name = ''.join(med.keys())
            print(pill_name)
    while True:
        for meds in list_of_meds:
            for name,  attributes in meds.items():
                if pill_name == name:
                    attr_have = input("How many pills on hand: ")
                    attr_per_day = input("Enter how many taken per day: ")
                    print(name, ",",  (attr_have + " on hand,"), (attr_per_day + " per day"))
                    sanity_check_update = input("Is this correct? yes or no: ")
                    if sanity_check_update == 'yes':
                        attributes['On hand'] = int(attr_have)
                        attributes["Pill's per day"] = int(attr_per_day)
                        attributes['Last_modified'] = str(today)
                        return list_of_meds
                    else:
                        print('exiting')
                        break
                        
def print_current_list(list_of_meds):
    for meds in list_of_meds:
        for name, attributes in meds.items():
            print(name,  "Number on Hand:", attributes['On hand'], ", Pills per day: ", attributes["Pill's per day"], ", Last Updated: ",  attributes['Last_modified'])
    print("Number of Medicines: " + str(len(list_of_meds)))
        
def main():
    while True:
        print("create\nadd\nremove\nupdate\nlist\n")
        arugument = input("What do you want to do?: ")
        if arugument == 'create':
            list_of_meds = create_list_meds()
            json.dump(list_of_meds,  open("Med_list.json", 'w'))
            break
        elif arugument == 'add':
            with open('Med_list.json') as json_data:
                list_of_meds = json.load(json_data)
                add_med(list_of_meds)
                json.dump(list_of_meds,  open("Med_list.json", 'w'))
            break
        elif arugument == 'remove':
            with open('Med_list.json') as json_data:
                list_of_meds = json.load(json_data)
                remove_med(list_of_meds)
                json.dump(list_of_meds,  open("Med_list.json", 'w'))
            break
        elif arugument == 'update':
            with open('Med_list.json') as json_data:
                list_of_meds = json.load(json_data)
                update_med(list_of_meds)
                json.dump(list_of_meds,  open("Med_list.json", 'w'))
            break
        elif arugument == 'list':
            with open('Med_list.json') as json_data:
                list_of_meds = json.load(json_data)
                print_current_list(list_of_meds)
            break
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting application\n')
    sys.exit(0)

    
