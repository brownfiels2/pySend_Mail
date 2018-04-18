'''
Emailer class
Author: Steve Brownfield
Created: 4/15/2018
'''

import argparse
from wiki_emailer import Emailer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert markdown to pdf and email it')
    parser.add_argument('-f', '--from', help='Send from email address', required=True)
    parser.add_argument('-t', '--to', help='Send to email address', required=True)
    parser.add_argument('-b', '--subject', help='Subject of email', required=True)
    parser.add_argument('-m', '--message', help='Message body', required=True)
    parser.add_argument('-a', '--md_filename', help='markdown file to convert and send', required=True)
    parser.add_argument('-s', '--server', help='Server address(default:localhost)', required=True)
    parser.add_argument('-p', '--port', help='Server port number', required=True)
    parser.add_argument('-u', '--username', help='Server username', required=True)
    parser.add_argument('-n', '--password', help='Server password', required=True)
    parser.add_argument('-e', '--tls', help='Should we use tls(default:True)', required=True)

    args = vars(parser.parse_args())

    emailer = Emailer.Emailer();
    emailer.send_mail(args['from'], args['to'], args['subject'], args['message'], args['md_filename'],
              args['server'], args['port'], args['username'], args['password'], args['tls']);
