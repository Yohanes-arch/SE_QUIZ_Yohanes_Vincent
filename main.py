import StudiKasus

db = StudiKasus.StudiKasus2('localhost', '3306', 'root', '')
df = db.import_csv('sample1.csv')
print(db.create_db('sample3'))
print(db.create_table('sample3', 'sample_data', df))
print(db.load_data('sample3', 'sample_data'))

