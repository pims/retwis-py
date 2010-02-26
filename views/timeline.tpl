%#list of currents posts
%include shared/header.tpl header=page,logged=logged
<div id="main">
%include shared/form.tpl tweet=last_tweet
	
	<div class="tweets">
	%for tweet in timeline:
		<p><img src="/static/avatar.png" /> <strong><a href="/{{tweet.user.username}}">{{tweet.user.username}}</a></strong> {{tweet.content}}<span><a href="/{{tweet.user.username}}/statuses/{{tweet.id}}">permalink</a></span></p>
	%end
	</div>
</div>
%include shared/side.tpl username=username,counts=counts
	
%include shared/footer.tpl