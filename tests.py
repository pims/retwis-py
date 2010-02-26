#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Created by tim bart on 2010-02-25.
Copyright (c) 2010 Pims. All rights reserved.
"""

import unittest
import redis
import settings
#make sure it's different from 'production' settings since db will be flushed
settings.r = redis.Redis(host='localhost', port=6379, db=9)
from domain import User,Post

class tests(unittest.TestCase):
  def setUp(self):
    self.r = settings.r
    self.r.flushdb()
    self.params = dict(username='pims',password='password',post='hello world')

  def tearDown(self):
    self.r.flushdb()

  def test_create_user(self):
    user = User.create(self.params['username'],self.params['password'])
    self.assertEqual(self.params['username'], user.username)
    self.assertEqual(settings.SALT + self.params['password'], user.password)
    self.assertEqual(1,user.id)
    self.assertEqual(0,len(user.followees))
    self.assertEqual(0,len(user.followers))
    self.assertEqual(0,len(user.posts()))
    self.assertEqual(0,len(user.mentions()))
    self.assertEqual(0,len(user.timeline()))
    
    user = User.create(self.params['username'],self.params['password'])
    self.assertEqual(None,user)
  
  def test_follow(self):
    user_to_follow = User.create('anonymous','password')
    me = User.create(self.params['username'],self.params['password'])
    me.follow(user_to_follow)
    self.assertEqual(1,len(me.followees))
    self.assertEqual(1,len(user_to_follow.followers))
    self.assertEqual(0,len(me.followers))
    self.assertEqual(0,len(user_to_follow.followees))
    
    self.assertEqual(True,me.following(user_to_follow))
    
    me.stop_following(user_to_follow)
    self.assertEqual(0,len(me.followees))
    self.assertEqual(0,len(user_to_follow.followers))
    self.assertEqual(False,me.following(user_to_follow))
    
  def test_user_find_by_name(self):
    user = User.create(self.params['username'],self.params['password'])
    user_found = User.find_by_username(self.params['username'])
    self.assertEqual(user.id,user_found.id)
    self.assertEqual(self.params['username'],user_found.username)
    user_not_found = User.find_by_username('not_found')
    self.assertEqual(None,user_not_found)
    
  def test_user_find_by_id(self):
    user = User.create(self.params['username'],self.params['password'])
    user_found = User.find_by_id(user.id)
    self.assertEqual(user.username,user_found.username)
    user_not_found = User.find_by_id(2)
    self.assertEqual(None,user_not_found)
  
  def test_create_post(self):
    user = User.create(self.params['username'],self.params['password'])
    Post.create(user,self.params['post'])
    self.assertEqual(1,len(user.posts()))
    self.assertEqual(1,user.posts()[0].id)
    self.assertEqual(self.params['post'],user.posts()[0].content)
  
  def test_post_find_by_id(self):
    user = User.create(self.params['username'],self.params['password'])
    Post.create(user,self.params['post'])
    post_found = Post.find_by_id(1)
    self.assertEqual(1,post_found.id)
    self.assertEqual(user.id,int(post_found.user_id)) #shouldn't need int()
    self.assertEqual(self.params['username'],post_found.user.username)
    
    
  def test_create_post_with_mention(self):
    user = User.create(self.params['username'],self.params['password'])
    content_with_mention = self.params['post'] + '@' + self.params['username']
    Post.create(user,content_with_mention)
    self.assertEqual(1,len(user.mentions()))
    
  def test_dispatch_post_to_followers(self):
    user_to_follow = User.create('anonymous','password')
    me = User.create(self.params['username'],self.params['password'])
    me.follow(user_to_follow)
    Post.create(user_to_follow,self.params['post'])
    self.assertEqual(1,len(me.timeline()))
    self.assertEqual(1,len(me.timeline()))
    
if __name__ == '__main__':
  unittest.main()