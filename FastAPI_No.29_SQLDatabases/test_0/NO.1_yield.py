"""yield"""

def fun():
    try:
        print ('1')
        db = 'SessionLocal()' # db
        yield db
    finally:
        print ('3')

for i in fun():
    print(i)
    print('2')

# fun()