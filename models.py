from sqlalchemy.sql import func
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from config import db

Base = declarative_base()

class User(db.Model):
  __tablename__ = "users"
  id  = db.Column(Integer, primary_key=True)
  f_name  = db.Column(String(45))
  l_name  = db.Column(String(45))
  email  = db.Column(String(45))
  pw  = db.Column(String(45))
  is_admin  = db.Column(Boolean, unique=False, default=False)
  blogs = relationship("Blog", backref="users")
  comments = relationship("Comment", backref="users")
  blog_likes = relationship("Blog_Like", backref="users")
  comment_likes = relationship("Comment_Like", backref="users")
  created_at  = db.Column(DateTime, server_default=func.now())
  updated_at  = db.Column(DateTime, server_default=func.now(), onupdate=func.now())

class Blog(db.Model):
  __tablename__ = "blogs"
  id  = db.Column(Integer, primary_key=True)
  author_id  = db.Column(Integer, ForeignKey('users.id'))
  title  = db.Column(String(255))
  content  = db.Column(String(65535))
  comments = relationship("Comment",backref="blogs")
  likes = relationship("Blog_Like", backref="blogs")
  created_at  = db.Column(DateTime, server_default=func.now())
  updated_at  = db.Column(DateTime, server_default=func.now(), onupdate=func.now())

class Comment(db.Model):
  __tablename__ = "comments"
  id = db.Column(Integer, primary_key=True)
  author_id = db.Column(Integer, ForeignKey('users.id'))
  blog_id = db.Column(Integer, ForeignKey('blogs.id'))
  likes = relationship("Comment_Like", backref="comments")
  content = db.Column(String(65535))
  created_at = db.Column(DateTime, server_default=func.now())
  updated_at  = db.Column(DateTime, server_default=func.now(), onupdate=func.now())

class Blog_Like(db.Model):
  __tablename__ = "blog_likes"
  id = db.Column(Integer, primary_key=True)
  author_id = db.Column(Integer, ForeignKey('users.id'))
  blog_id = db.Column(Integer, ForeignKey('blogs.id'))
  created_at = db.Column(DateTime, server_default=func.now())
  updated_at  = db.Column(DateTime, server_default=func.now(), onupdate=func.now())

class Comment_Like(db.Model):
  __tablename__ = "comment_likes"
  id = db.Column(Integer, primary_key=True)
  author_id = db.Column(Integer, ForeignKey('users.id'))
  comment_id = db.Column(Integer, ForeignKey('comments.id'))
  created_at = db.Column(DateTime, server_default=func.now())
  updated_at  = db.Column(DateTime, server_default=func.now(), onupdate=func.now())

# class Attachment(db.Model):
#   __tablename__ = "attachments"
#   id = db.Column(Integer, primary_key=True)
#   table_reference = db.Column(String(45)) #(users,blogs, comments)
#   table_record_id = db.Column(Integer)
#   created_at = db.Column(DateTime, server_default=func.now())
#   updated_at  = db.Column(DateTime, server_default=func.now(), onupdate=func.now())


#likes table
# like_id
# blog_id
# user_id
# Date/Time Created
# Date/Time Updated

#attachments table
# attachment id
#type (1=blog attachment, 2=comment attachment, 3=user photo)
# attachment filepath
# Date/Time Created
# Date/Time Updated

#blog post table
# blog_id
# Author
# Title
# Content
# Date/Time Created
# Date/time updated

#blog comment table
# comment_id
# Author
# Content
# Date/Time Created
# Date/Time Updated
# blog_id reference
