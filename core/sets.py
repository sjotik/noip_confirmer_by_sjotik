import logging


USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 '
              'Yowser/2.5 Safari/537.36')

LOGLEVEL = logging.INFO
LOGFORMAT = '%(asctime)s %(filename)s [%(levelname)s] > %(message)s'
WSIZE = '900,1200'

# BAD_LOGIN = ' Username / Password combination is incorrect. Please try again. '
BAD_LOGIN = 'Sign In To Your Account'

# f'//div[@class="alert alert-error row"'
#                     f'and contains(text(), "{BAD_LOGIN}")]'