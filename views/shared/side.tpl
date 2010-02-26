<div id="side">
	<p class="bio">
		<img src="/static/avatar-small.png" />{{username}}
		<span><a href="/{{username}}">{{counts[2]}} tweets</a></span>
	</p>
	<div>
	<ul class="follow">
		<li><a href="#">Following<span>{{counts[0]}}</span></a></li>
		<li><a href="#">Followers<span>{{counts[1]}}</span></a></li>
		<li><a href="/mentions">@{{username}}</a></li>
	</ul>
</div>