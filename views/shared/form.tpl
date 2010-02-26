<h1>What's happening?</h1>
<form method="POST" action="/post" class="update">
	<textarea name="content"></textarea>
	<fieldset>
	%if tweet:
	<p>{{tweet.content}}</p>
	%else:
	<p>really ? nothing's happening ?</p>
	%end
	<input type="submit" value="update!" />
	</fieldset>
</form>