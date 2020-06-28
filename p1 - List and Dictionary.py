# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 5

#netacad email cth: 'abcd@gmail.com'
email='apriliaerlitalisna@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini
#no 1

def letter_catalog(items,letter='A'):
    pass

    fruit = []
    for element in items:
        if element[0] == letter:
              fruit.append(element)
    return fruit

#print(letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],letter='A'))


#no 2

def counter_item(items):
    pass

    fruit=[]
    for item in items:
        item.count('Apple' and 'Blueberries')
        return

fruit = ['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries']
counter_item = fruit.count('Apple'and 'Blueberries')

dictionary = {'Apple':counter_item,'Blueberries':counter_item}
#print(dictionary)


#no 3

fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']
daftar = {}

def counter_item(items):
    
    for i in items:
        daftar[i] = items.count(i)
        #print(daftar)
    return daftar

chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

counter_item(chart)

dictionary = {'Blueberries':counter_item,'Grapes':counter_item,'Apple':counter_item,'Guava':counter_item,'Jackfruit':counter_item}
#print(dictionary)

fruit_price = dict(zip(fruits,prices))
frequency = {}

def total_price(dcounter,fprice):
    total = 0
    for i in dcounter.keys():
        price = dcounter[i] * fprice[i]
        total = total + price
        #print(total)
    return total

total_price(counter_item(chart),fruit_price)


#no 4

def discounted_price(total,discount,minprice=100):
    if total >= minprice:
        tdiskon = total - (discount / 100) * total
        #print(tdiskon)
    else:
        tdiskon = total
        #print(tdiskon)
    return tdiskon
        
discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100)

total = total_price(counter_item(chart),fruit_price)
tdiskon = discounted_price(total, 10, minprice=100)

#no 5

frequency_list = counter_item(chart)

def print_summary(items, fprice):
    item1 = frequency_list
    item2 = total
    item3 = tdiskon

    # for word in items:
    for words in sorted(daftar):
        #print(daftar)
        p = fruit_price[words] * daftar[words]
        print(daftar[words]," ", words," : ",p)
    print("Total : ", total)
    print("Harga Diskon : ", tdiskon)

print_summary(chart,fruit_price)