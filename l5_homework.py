score = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]
fail = []
for i in score :
    if i < 10 :
        fail.append(i)
#----------------------------------------------------
students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida'] 
scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]
snc = list(zip(students , scores))
rank = 1
while snc :
    bishtarin = -1
    for students , scores in snc:
        if scores > bishtarin :   
            bishtarin = scores          
    for students, scores in snc :           
        if scores == bishtarin :
            if scores >= 10:
                print(rank, students, scores)
                rank += 1
            snc.remove((students,scores))
            break
#----------------------------------------------------
products = []
while True :
    product = input('nam-e mahsol-e mored-d nazar ra vared konid :')
    if product == 'exit' :
        break
    products.append(product)
print(products)
#----------------------------------------------------
while True :
    print('---MENUE---')
    print('   mojoodi   ')
    print('  bardasht   ')
    print('   variz   ')
    amaliat = input('amaliat-e khod ra vared konid : ') 
    print(f'amaliat-e {amaliat} entekhab shod.')
    amaliat2 = input ('amaliat-e digar / khoroj ? ')
    if amaliat2 == 'amaliat-e digar' :
        continue
    if amaliat2 == 'khorooj' :
        print('khorooj ba mavafaghiat anjam shod!')
        break                       
#----------------------------------------------------
while True :
    user_name = input('Nam-e karbari-e khod ra vared konid : ')
    password = float(input('ramz-e oboor-e khod ra vared konid : '))
    if user_name == 'admin' and  password == 1234 :
        print('shoma ba movafaghiat vared shodid!')
        break
    else :
        print('nam-e karbari ya ramz-e oboor eshtabah ast!')
#----------------------------------------------------
for i in range (3) :
    user_name = input('Nam-e karbari-e khod ra vared konid : ')
    password = float(input('ramz-e oboor-e khod ra vared konid : '))
    if user_name == 'admin' and  password == 1234 :
        print('shoma ba movafaghiat vared shodid.')
        break
    elif i == 2 :
        print('account-e shoma ghofl shod!')
        break
    else :
        print('nam-e karbari ya ramz-e oboor eshtabah ast.')
#----------------------------------------------------
orders = []
while True :
    print('--- FOODS ---')
    foods = ['Pizza','Pasta','Stake','Salasd','Burger',
             'French Frize','Chiken Sandwich','Soda']
    print(foods)
    order = input('Sefaresh-e khod ra vared kond : ')
    if order == 'order' : 
        break
    else :
        orders.append(order)
print('---- FACTOR ----')
for rank, food in enumerate(orders, 1):
    print(rank, food)
#----------------------------------------------------
print('salam')
while True :
    user = input()
    if user == 'bye' :
        print('Goodbye')
        break
    else :
        print('[javabe chatbot]')




























