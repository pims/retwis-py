%#login page
%include shared/header.tpl header=page,logged=logged

<form method="POST" action="/login" id="login">
	<h2>Login</h2>
	%if error_login:
		<p>wrong username/password</p>
	%end
	<p><label for="login-name">username:</label><input type="text" name="name" id="login-username"/></p>
	<p><label for="login-password">password:</label><input type="password" name="password" id="login-password"/></p>
<p><input type="submit" value="login!" /></p>
</form>

<form method="POST" action="/signup" id="signup">
		<h2>Sign up</h2>
	%if error_signup:
		<p>username already exists</p>
	%end
<p><label for="signup-name">username:</label><input type="text" name="name" id="signup-username"/></p>
<p><label for="signup-password">password:</label><input type="password" name="password" id="signup-password"/></p>
<p><input type="submit" value="signup!" /></p>
</form>
%include shared/footer.tpl