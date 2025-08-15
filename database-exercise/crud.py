import os 
from database import con,cur
def create_user():
    os.system('clear')
    new_data='''
    INSERT INTO users (firstname, lastname, ide_number, email)
    Values('Sofia', 'Chirveches', '1234', 'sofiachirvechesdelgado@gmail.com'),
    '''
    con.exacute(new_data)
    con.comit()
    print(':::User has been created sucessfully!:::')
create_user()
