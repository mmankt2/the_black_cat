from flask import render_template, redirect, request, session, flash, jsonify	# we now need fewer imports because we're not doing everything in this file!
# if we need to work with the database, we'll need those imports:    
from config import db, bcrypt
from models import User, Blog, Comment, Blog_Like, Comment_Like
import json, os

def landing():
  return render_template('index.html')

def blog():
  return render_template('blog.html')
  
def clear_session():
  session.clear()
  return redirect('/')

def logout():
  session.clear()
  return redirect('/')

def login_register(flag=0): #flag = 1 if the user is trying to place an order. otherwise flag is 0
  print(flag)
  if flag == '1':
    flash('Please login to continue')

  return render_template('/registration.html',flag=flag)

def login(flag=0):#flag = 1 if the user is trying to place an order. otherwise flag is 0
  print(flag) #flag = 1 if the user is trying to place an order. otherwise flag is 0
  is_valid=True
  #get form info
  form_email = request.form['email'].lower()

  if len(request.form['password'])<1:
    flash('Password cannot be blank.')
    is_valid = False
  if len(form_email)<1:
    flash('Email cannot be blank.')
    is_valid = False
  if is_valid == True:
    #see if user is already registered
    instance_of_user = User.query.filter_by(email=form_email).first()
    
    if instance_of_user is None:
      flash('Email does not match a registered user')
      return redirect('/login_register/'+str(flag))
    else:#check if password matches
      if bcrypt.check_password_hash(instance_of_user.pw,request.form['password']) == True:
        print('password matched')
        session['user_email'] = form_email
        session['first_name'] = instance_of_user.f_name
        session['id'] = instance_of_user.id
        return redirect('/my_account')
      else:
        flash('Password or email is incorrect.')
        return redirect('/login_register/'+str(flag))
  return redirect('/')

def register(flag=0): #flag = 1 if the user is trying to place an order. otherwise flag is 0
  print(flag)
  is_valid=True
  #get form info
  fn = request.form['first_name']
  ln = request.form['last_name']
  pw = request.form['password']
  cpw = request.form['confirm_password']
  form_email = request.form['email'].lower()

  if len(fn)<1:
    flash('First Name must be filled in.')
    is_valid = False
  if len(ln)<1:
    flash('Last Name must be filled in.')
    is_valid = False
  if is_valid == True:
    #check if email is registered
    instance_of_user = User.query.filter_by(email=form_email).first()
    print(instance_of_user)
    
    if instance_of_user is not None:
      flash('Email already registered. Please login.')
      return redirect('/login_register/'+str(flag))
    
    #if email not registered, add the user to the db
    pw_hash = bcrypt.generate_password_hash(pw)
    flash('Successfully added new user!')

    new_instance_of_a_user = User(f_name=fn, l_name=ln, email=form_email, pw=pw_hash)
    db.session.add(new_instance_of_a_user)
    db.session.commit()
    session['user_email'] = form_email
    session['first_name'] = fn
    instance_of_user = User.query.filter_by(email=form_email).first()
    session['id'] = instance_of_user.id
    if flag=='1':
      return redirect('/place_order')
  return redirect('/')

def my_account():
  instance_of_user = User.query.get(session['id'])
  return render_template('myaccount.html', user=instance_of_user)