''' birthday_text_1 = "I am "
age = 23
birthday_text_2 = " years old."
full_text = birthday_text_1 + str(age) + birthday_text_2
print(full_text) '''

'''
hike_caption = "What an amazing time to walk through nature!!"

#Almost forgot the hashtags:)
hike_caption += " #nofilter"
hike_caption += " #blessed"
print(hike_caption)
'''


'''
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory = sorted(inventory)
print(inventory)
'''
my_info = ('Ferhat', '23', 'programmer')
name, age, occupation = my_info
print(occupation)