# bottle_session.py - based on :
# gmemsess.py - memcache-backed session Class for Google Appengine
# Version 1.2
#	Copyright 2008 Greg Fawcett <greg@vig.co.nz>

#substituting memcache for redis
# Version 0.1
#	Copyright 2010 Tim Bart

#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
import pickle
import settings

r = settings.r

_sidChars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
_defaultTimeout=30*60 # 30 min
_defaultCookieName='gsid'

#----------------------------------------------------------------------
class Session(dict):
	"""A secure lightweight memcache-backed session Class for Google Appengine."""

	#----------------------------------------------------------
	def __init__(self,request,response,name=_defaultCookieName,timeout=_defaultTimeout):
		"""Create a session object.

		Keyword arguments:
		rh -- the parent's request handler (usually self)
		name -- the cookie name (defaults to "gsid")
		timeout -- the number of seconds the session will last between
		           requests (defaults to 1800 secs - 30 minutes)
		"""
		self.request=request
		self.response = response
		self._timeout=timeout
		self._name=name
		self._new=True
		self._invalid=False
		dict.__init__(self)
		
		_name = request.COOKIES.get(self._name, None)
		if _name:
			self._sid= _name
			data = r.get(self._sid)
			if data:
				self.update(pickle.loads(data))
				# memcache timeout is absolute, so we need to reset it on each access
				r.set(self._sid,data)
				r.expire(self._name,self._timeout)
				self._new=False
				return

		# Create a new session ID
		# There are about 10^14 combinations, so guessing won't work
		self._sid=random.choice(_sidChars)+random.choice(_sidChars)+\
						random.choice(_sidChars)+random.choice(_sidChars)+\
						random.choice(_sidChars)+random.choice(_sidChars)+\
						random.choice(_sidChars)+random.choice(_sidChars)
		self.response.set_cookie(self._name,self._sid, path='/')

	#----------------------------------------------------------
	def save(self):
		"""Save session data."""
		if not self._invalid:
			r.set(self._sid,pickle.dumps(self.copy()))
			r.expire(self._name,self._timeout)

	#----------------------------------------------------------
	def is_new(self):
		"""Returns True if session was created during this request."""
		return self._new

	#----------------------------------------------------------
	def invalidate(self):
		"""Delete session data and cookie."""
		self.response.set_cookie(self._name,'',expires=-100)
		r.delete(self._sid)
		self.clear()
		self._invalid=True
