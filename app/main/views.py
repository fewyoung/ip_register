from . import main
from .forms import AddForm, SearchForm, EditForm
from flask import render_template, session, flash, redirect, url_for
from flask_login import logout_user, login_required
from ..models import db, Registration_Lan, Registration_Wan


def add_reg(add_form, Reg):
	new_reg	= Reg(name = add_form.add_name.data,
				  department = add_form.add_department.data,
				  office = add_form.add_office.data,
				  ip = add_form.add_ip.data,
				  vlan = add_form.add_vlan.data,
				  port = add_form.add_port.data,
				  remark = add_form.add_remark.data)
	for field in add_form:
		field.data = None
	db.session.add(new_reg)
	db.session.commit()
	flash('完成：添加记录')
	
			
def edit_reg(edit_form, Reg):
	edit_reg = Reg.query.filter(
		Reg.id == edit_form.edit_id.data).first()
	edit_reg.name = edit_form.edit_name.data
	edit_reg.department = edit_form.edit_department.data
	edit_reg.office = edit_form.edit_office.data
	edit_reg.ip = edit_form.edit_ip.data
	edit_reg.vlan = edit_form.edit_vlan.data
	edit_reg.port = edit_form.edit_port.data
	edit_reg.remark = edit_form.edit_remark.data
	db.session.commit()	
	flash('完成：修改记录')
	
	
def del_reg(edit_form, Reg):
	del_reg = Reg.query.filter(
		Reg.id == edit_form.edit_id.data).first()
	db.session.delete(del_reg)
	db.session.commit()	
	flash('完成：删除记录')			
	
	
def search_reg(search_form, edit_forms, Reg):
	key_dict = {'1':Reg.name, '2':Reg.department, '3':Reg.office,
		'4':Reg.ip, '5':Reg.vlan, '6':Reg.port, '7':Reg.remark}
		
	if search_form.selectfield.data == str(None):
		search_field = search_form.selectfield.data = session.get('selectfield')
		search_key = search_form.keyword.data = session.get('keyword')
	else:
		search_field = search_form.selectfield.data
		search_key = search_form.keyword.data

	if search_field is not None:
		if search_field == '0':
			regs = Reg.query.order_by(Reg.id.desc())
			search_form.keyword.data = ''
		else:
			regs = Reg.query.filter(
				key_dict[search_field].like(
					'%s%s%s' % ('%',search_key,'%'))).order_by(
						key_dict[search_field])												
		for reg in regs:
			edit_form = EditForm(Reg)
			edit_form.edit_id.data = reg.id
			edit_form.edit_name.data = reg.name
			edit_form.edit_department.data = reg.department
			edit_form.edit_office.data = reg.office
			edit_form.edit_ip.data = reg.ip
			edit_form.edit_vlan.data = reg.vlan
			edit_form.edit_port.data = reg.port
			edit_form.edit_remark.data = reg.remark
			edit_forms.append(edit_form)	


def segment_index(add_form, search_form, edit_forms, segment):
	edit_form = EditForm(segment)
	
	if add_form.add_submit.data and add_form.validate_on_submit():
		add_reg(add_form, segment)
		return True
						
	if edit_form.edit_submit.data and edit_form.validate_on_submit():
		edit_reg(edit_form, segment)
		return True
				
	if edit_form.del_submit.data and edit_form.validate_on_submit():
		del_reg(edit_form, segment)
		return True
		
	if search_form.search_submit.data and search_form.validate_on_submit():
		session['selectfield'] = search_form.selectfield.data
		session['keyword'] = search_form.keyword.data	
		return True
				
				
@main.route('/lan', methods=['GET', 'POST'])
@login_required
def lan_index():
	add_form = AddForm(Registration_Lan)
	search_form = SearchForm()
	edit_forms = []
		
	if segment_index(add_form, search_form, edit_forms, Registration_Lan):
		return redirect(url_for('main.lan_index'))
		
	search_reg(search_form, edit_forms, Registration_Lan)
	
	return render_template('main.html', 
		add_form=add_form,
		search_form=search_form, 
		edit_forms=edit_forms)


@main.route('/wan', methods=['GET', 'POST'])
@login_required
def wan_index():	
	add_form = AddForm(Registration_Wan)
	search_form = SearchForm()
	edit_forms = []
		
	if segment_index(add_form, search_form, edit_forms, Registration_Wan):
		return redirect(url_for('main.wan_index'))
		
	search_reg(search_form, edit_forms, Registration_Lan)
	
	return render_template('main.html', 
		add_form=add_form,
		search_form=search_form, 
		edit_forms=edit_forms)



