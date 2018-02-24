from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
	username = StringField('用户名', validators=[InputRequired(message='姓名不能为空')], 
		render_kw={"placeholder":"请输入您的用户名"})
	password = PasswordField('密码', validators=[InputRequired(message='密码不能为空')], 
		render_kw={"placeholder":"请输入您的密码"})
	submit = SubmitField('确定')
