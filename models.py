from sqlalchemy.sql import func
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from config import db

Base = declarative_base()

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  f_name = db.Column(String(45))
  l_name = db.Column(String(45))
  email = db.Column(String(45))
  pw = db.Column(String(45))
  is_admin = db.Column(Boolean, unique=False, default=False)
  created_at = db.Column(DateTime, server_default=func.now())
  updated_at = db.Column(DateTime, server_default=func.now(), onupdate=func.now())