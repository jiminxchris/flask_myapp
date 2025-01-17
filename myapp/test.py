from myapp import db
from myapp.models import User

anonymous_user  = User(username='Anonymous', 
                        password = '9999',
                        email='anonymous@example.com')
db.session.add(anonymous_user)
db.session.commit()