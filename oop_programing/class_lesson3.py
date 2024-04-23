from datetime import datetime, timedelta

import time

print(
    "-----------------------------OOP sprendimai-----------------------------------------"
)

print(
    "-----------------------------Destytojo uzdavinys:------------------------------------"
)

"""Kaip zinote, while ciklas dazniausiai naudojamas su laiku. 
Ir siuo metu projekte naudojame toki koda:
    import time
    from datetime import datetime, timedelta
    current_time = datetime.now()
    while current_time + timedelta(seconds=5) >= datetime.now():
        print('vienas')
        time.sleep(1)
Kas karta reikia daryti importus, prisiminti kaip cia rasyti ir panasiai. 
Todel galima parasyti klase ir ja naudoti taip:
    import time
    timer = Timer()
    while timer.fired(5):
        print('vienas')
        time.sleep(1)
Paraškite metodą, kuris leistų naudoti klase auksciau aprasytu budu."""
# def print_one_for_five_seconds():
#     current_time = datetime.now()
#     while current_time + timedelta(seconds=5) >= datetime.now():
#         print('vienas')
#         time.sleep(1)
#
# print(print_one_for_five_seconds())


class Timer:
    """representing time"""
    def __init__(self):
        self.start_time = datetime.now()

    def fired(self, seconds):
        """representing time changes"""
        return datetime.now() >= self.start_time + timedelta(seconds=seconds)


timer = Timer()
while timer.fired(5):
    print("vienas")
    time.sleep(1)
# print(timer.fired(5))
