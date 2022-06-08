def authorization(login):
    def check_authentication(*args, **kwargs):
        print('Check authentication')
        msg=''
        if login(*args, **kwargs):
            print('logged in')
            msg='You are Logged in'
            msg+='Redirect to page.html'
            return msg
        else:
            print('logged out')
            msg='you are not LOGGED In'
            msg+=' Redirect to errroPage.html'
            return msg
            
    return  check_authentication()


@authorization
def login(username="", password=""):
    if not len(username+password):
        return False
    return True

print(login('ja'))


