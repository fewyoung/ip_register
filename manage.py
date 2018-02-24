import os
from app import create_app, db
from app.models import User, Registration_Lan, Registration_Wan
from flask_script import Manager, Shell


app = create_app(os.getenv('IP_REGISTER_CONFIG') or 'development')

def make_shell_context():
	return dict(app=app, db=db, User=User, 
		Registration_Lan=Registration_Lan,
		Registration_Wan=Registration_Wan)

manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()
