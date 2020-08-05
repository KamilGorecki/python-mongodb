from create import create_doc
from read import read_all
from delete import delete_one

print('C reate one')
create_doc({"name": "test", "pass": "test"}, 'users')

print('R ead all')
read_all('users')

print('D elete one')
delete_one({"name": "test"}, 'users')
