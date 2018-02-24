from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, HiddenField
from wtforms.validators import InputRequired, ValidationError, Length
from flask import flash


class AddForm(FlaskForm):
	def __init__(self, segment):
		super().__init__()
		self.segment = segment
		
	add_id = HiddenField('id')
	add_name = StringField('姓名', description="* 必填项",
		validators=[Length(max=10, message="超过最大10个字符")],
		render_kw={"placeholder":"请输入用户的姓名"})
	add_department = StringField('部门',
		validators=[Length(max=10, message="超过最大10个字符")])
	add_office = StringField('办公室',
		validators=[Length(max=10, message="超过最大10个字符")])
	add_ip = StringField('IP', description="* 必填项",
		validators=[Length(max=20, message="超过最大20个字符")],
		render_kw={"placeholder":"请输入用户的IP地址"})
	add_vlan = StringField('Vlan',
		validators=[Length(max=10, message="超过最大10个字符")])
	add_port = StringField('交换机端口',
		validators=[Length(max=10, message="超过最大10个字符")])
	add_remark = StringField('备注',
		validators=[Length(max=20, message="超过最大20个字符")])
	add_submit = SubmitField('确定')
	
	def validate_add_name(self, field):
		if field.data == '':
			flash('姓名 不能为空')
			raise ValidationError('错误：姓名 不能为空')
		segment = self.segment
		if segment.query.filter_by(name = field.data).first():	
			flash('错误：姓名 已存在')		
			raise ValidationError('错误：姓名 已存在')
						
	def validate_add_ip(self, field):
		if field.data == '':
			flash('IP 不能为空')
			raise ValidationError('错误：IP 不能为空')
		segment = self.segment
		if segment.query.filter_by(name = field.data).first():
			flash('错误：IP 已存在')
			raise ValidationError('错误：IP 已存在')
		

class SearchForm(FlaskForm):	
	search_id = HiddenField('id')
	keywords = [('0','全部记录'), ('1','姓名'), ('2','部门'), ('3','办公室'),
		('4','IP'), ('5','Vlan'), ('6','交换机端口'), ('7','备注')]
	selectfield = SelectField('按类型查询' ,
		validators=[InputRequired()] ,
		choices=keywords)
	keyword = StringField('关键词',
		render_kw={"placeholder":"请输入搜索关键词"})
	search_submit = SubmitField('查询')

class EditForm(FlaskForm):
	def __init__(self, segment):
		super().__init__()
		self.segment = segment
		 
	edit_id = HiddenField('id')
	edit_name = StringField('姓名', description="* 必填项",
		validators=[Length(max=10, message="超过最大10个字符")])
	edit_department = StringField('部门',
		validators=[Length(max=10, message="超过最大10个字符")])
	edit_office = StringField('办公室',
		validators=[Length(max=10, message="超过最大10个字符")])
	edit_ip = StringField('IP', description="* 必填项",
		validators=[Length(max=20, message="超过最大20个字符")])
	edit_vlan = StringField('Vlan',
		validators=[Length(max=10, message="超过最大10个字符")])
	edit_port = StringField('交换机端口',
		validators=[Length(max=10, message="超过最大10个字符")])
	edit_remark = StringField('备注',
		validators=[Length(max=20, message="超过最大20个字符")])
	edit_submit = SubmitField('确定')
	del_submit = SubmitField('删除')
	
	def validate_edit_name(self, field):
		if field.data == '':
			flash('姓名 不能为空')
			raise ValidationError('错误：姓名 不能为空')
		segment = self.segment
		ser = segment.query.filter_by(name = field.data).first()	
		if ser is not None and str(ser.id) != self.edit_id.data:
			flash('错误：姓名 已存在')
			raise ValidationError('错误：姓名 已存在')

	def validate_edit_ip(self, field):
		if field.data == '':
			flash('IP 不能为空')
			raise ValidationError('错误：IP 不能为空')
		segment =self.segment
		ser = segment.query.filter_by(ip = field.data).first()
		if ser is not None and str(ser.id) != self.edit_id.data:
			flash('错误：IP 已存在')
			raise ValidationError('错误：IP 已存在')

