%#list of currents posts
%include shared/header.tpl header=page,logged=logged
<div id="main">
	%if logged and not himself:
		%if is_following:
		<form action="/unfollow/{{username}}" method="post" accept-charset="utf-8" class="unfollow-user">	
			<p><input type="submit" value="Unfollow {{username}}"></p>
		</form>
		%else:
		<form action="/follow/{{username}}" method="post" accept-charset="utf-8" class="follow-user">	
			<p><input type="submit" value="Follow {{username}}"></p>
		</form>
		%end
	%end
	<div class="tweets">
	%if posts:
  	%for tweet in posts:
  		<p><img src="/static/avatar.png" /> <strong><a href="/{{tweet.user.username}}">{{tweet.user.username}}</a></strong> {{tweet.content}}<span><a href="/{{username}}/statuses/{{tweet.id}}">permalink</a></span></p>
  	%end
  %else:
   <p>{{username}} has posted any tweet yet</p>
  %end
	</div>
</div>
%include shared/side.tpl username=username,counts=counts
	
%include shared/footer.tpl