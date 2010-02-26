/* playing nice with other kids */
(function(){
  
  /* bye bye old browsers */
  if(!document.getElementsByClassName){return;} 
  
  /* Look Ma', no jQuery! */
  var $ = function(id,scope){ s = scope||document;return s.getElementById(id);}
  var $$ = function(tag,scope){s = scope||document;return s.getElementsByTagName(tag);}
  var $$$ = function(cls,scope){s = scope||document;return s.getElementsByClassName(cls);}

  var regexp = {
    url :/((https?\:\/\/)|(www\.))(\S+)(\w{2,4})(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/gi,
    twitterUsername : /(@)(\w+)/g
  }
  
  var enhance = function()
  {
    //summary : replace url in text by url + link
    //dependencies : $$, $$$
    //params : null
    //returns : void
        
    
    var linkify = function(text){
      
      //Sometimes people have a problem, and decide to solve it with regular expressions. Now they have two problems. – Jamie Zawinski
      //Thx ricky : http://rickyrosario.com/blog/converting-a-url-into-a-link-in-javascript-linkify-function
        
      //summary : replace url in text by url + link
      //dependencies : regexp
      //params :
      //  (string) text
      //returns : (string) text
      
        if (text) {
            text = text.replace(regexp.url,
                function(url){
                    var full_url = url;
                    if (!full_url.match('^https?:\/\/')) {
                        full_url = 'http://' + full_url;
                    }
                    return '<a href="' + full_url + '">' + url + '</a>';
                });
        }
        return text;
    }
    
    var twitterify = function(text)
    {
      if(text){
        text = text.replace(regexp.twitterUsername,
            function(username){
              short_username = username.substring(1,username.length)
              return "<a href='/"+ short_username +"'>"+ username+"</a>";
        });
        return text;
      }
    }
  
    var results = $$$('tweets');
    var i = results.length;
    while(i--){
      //var n = results[i].getElementsByTagName('p')[0];
      var n = results[i];
      var p = $$('p',results[i])[0];
      if (n == null){break;} //defensive programming FTW !
      p.innerHTML = linkify(p.innerHTML);
      n.innerHTML = twitterify(n.innerHTML);
    }
    
    
    
  }
  
  enhance();
}());