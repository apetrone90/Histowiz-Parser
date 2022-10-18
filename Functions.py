def number_parser(num,vendor):
    if len(num) < 3:
        print(f'This number {num} should not have been passed to parser.. review code!')
    if vendor == 'Histowiz':
        num = num[-3:]
        num = num.lstrip("0")
        return num
    elif vendor == 'Crownbio':
        return num
    else:
        print('Unrecognized Vendor!')

def imagetagParser(data):
    print(data['Image Tag'][0])
    ini_cut = input('Select Symbol to make initial cut')
    print(data['Image Tag'][0].split(ini_cut))
    ini_idx = int(input('Select Index to keep:'))
    print(data['Image Tag'][0].split(ini_cut)[ini_idx])
    data['Animal Number Raw'] = data['Image Tag'].apply(lambda x: x.split(ini_cut)[ini_idx])
    cont = input("Does this need further splitting? (Y/N)")
    while cont == "Y":
        print(data['Animal Number Raw'][0])
        add_cut = input('Select Symbol to make additional cut')
        print(data['Animal Number Raw'][0].split(add_cut))
        add_idx = input('Select Index to keep:')
        print(data['Animal Number Raw'][0].split(add_cut)[add_idx])
        data['Animal Number Raw'] = data['Animal Number Raw'].apply(lambda x: x.split(add_cut)[add_idx])
        print('===================================================')
        print(data['Animal Number Raw'][0])
        cont = input('Is this ok to move on to number parser? (Y/N)')