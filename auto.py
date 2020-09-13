import mechanize

br = mechanize.Browser()
br.set_handler_robots(False)
br.addheaders = [('User-agent','Firefox')]
br.open("https://www.facebook.com/login.php")
br.select_form(nr=0)
br.from['email'] = 'femasakbar79'
br.from['pass'] = 'femasgans'
sub = br.submit()
print sub.geturl()
