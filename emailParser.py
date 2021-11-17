# -*- coding: utf-8 -*-

import poplib, os
from email.parser import Parser

# pop3 server domain.



# pop3 server connection object.
pop3_server_conn = None

'''
This method will connect to the global pop3 server 
and login with the provided user email and password.
'''
def connect_pop3_server(user_email, user_password):
    # use global pop3_server_conn variable in this function.
    global pop3_server_conn
    
    # if pop3 server connection object is null then create it.
    if(pop3_server_conn is None):
        print('********************************* start connect_pop3_server *********************************')
        # create pop3 server connection object.
        pop3_server_conn = poplib.POP3_SSL('pop.gmail.com', '995')
        pop3_server_conn.set_debuglevel(1)
        
        # get pop3 server welcome message and print on console.
        welcome_message = pop3_server_conn.getwelcome()
        print('Below is pop3 server welcome messages : ')
        print(welcome_message)
        
        # send user email and password to pop3 server.
        pop3_server_conn.user(user_email)
        pop3_server_conn.pass_(user_password)
    
    return pop3_server_conn

'''
Close the pop3 server connection and release the connection object.
'''
def close_pop3_server_connection():
    global pop3_server_conn
    if pop3_server_conn != None:
        pop3_server_conn.quit()
        pop3_server_conn = None

'''
Get email messages status of the given user.
'''
def get_user_email_status(user_email, user_password):
    
    # connect to pop3 server with the user account.
    connect_pop3_server(user_email, user_password)

    print('********************************* start get_user_email_status *********************************')
    
    # get user total email message count and email file size. 
    (messageCount, totalMessageSize) = pop3_server_conn.stat()
    print('Email message numbers : ' + str(messageCount))
    print('Total message size : ' + str(totalMessageSize) + ' bytes.')
    

'''
Get user email index info。
'''
def get_user_email_index(user_email, user_password):
    
    connect_pop3_server(user_email, user_password)
    print('********************************* start get_user_email_index *********************************')
    
    # get all user email list info from pop3 server.
    (resp_message, mails_list, octets) = pop3_server_conn.list()
    # print server response message.
    print('Server response message : ' + str(resp_message))
    # loop in the mail list.
    for mail in mails_list:
        # print each mail object info.
        print('Mail : ' + str(mail))
    
    print('Octets number : ' + str(octets))
    msgCount, mailboxSize = pop3_server_conn.stat()
    return msgCount
    

'''
Get user account email by the provided email account and email index number.
'''
def get_email_by_index(user_email, user_password, email_index):
    
    connect_pop3_server(user_email, user_password)
    print('********************************* start get_email_by_index *********************************')

    # retrieve user email by email index. 
    (resp_message, lines, octets) = pop3_server_conn.retr(email_index)
    print('Server response message : ' + str(resp_message))
    print('Octets number : ' + str(octets))
   
    # join each line of email message content to create the email content and decode the data with utf-8 charset encoding.  
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # print out the email content string.
    # print('Mail content : ' + msg_content)
    
    # parse the email string to a MIMEMessage object.
    msg = Parser().parsestr(msg_content)
    
    header, val = parse_email_msg(msg)
    return header, val
    
 
# Parse email message.   
def parse_email_msg(msg):
    
    print('********************************* start parse_email_msg *********************************')
    
    header = parse_email_header(msg)
     
    val = parse_email_body(msg)    
    return header, val
    
# Delete user email by index.   
def delete_email_from_pop3_server(user_email, user_password, email_index):
    connect_pop3_server(user_email, user_password)   
    print('********************************* start delete_email_from_pop3_server *********************************')
    
    pop3_server_conn.dele(email_index)
    print('Delete email at index : ' + email_index)
    
    
# Parse email header data.    
def parse_email_header(msg):
    print('********************************* start parse_email_header *********************************')
    # just parse from, to, subject header value.
    header_list = ('From', 'To', 'Subject')
    total = ""
    # loop in the header list
    for header in header_list:
        # get each header value.
        header_value = msg.get(header, ' ')
        total = total + ' ' + header + ' ' + header_value
    return total
      
# Parse email body data.      
def parse_email_body(msg):
    print('********************************* start parse_email_body *********************************')
    val = ' '
    # if the email contains multiple part.
    if (msg.is_multipart()):
        # get all email message parts.
        parts = msg.get_payload()
        # loop in above parts.
        for n, part in enumerate(parts):
            # get part content type.
            content_type = part.get_content_type()
            print('---------------------------Part ' + str(n) + ' content type : ' + content_type + '---------------------------------------')
            val = val + parse_email_content(msg)                
    else:
       val = val + parse_email_content(msg) 
    return val

# Parse email message part data.            
def parse_email_content(msg):
    # get message content type.
    content = " "
    content_type = msg.get_content_type().lower()
    
    print('---------------------------------' + content_type + '------------------------------------------')
    # if the message part is text part.
    if content_type=='text/plain' or content_type=='text/html':
        # get text content.
        content = msg.get_payload(decode=True)
        # get text charset.
        charset = msg.get_charset()
        # if can not get charset. 
        if charset is None:
            # get message 'Content-Type' header value.
            content_type = msg.get('Content-Type', '').lower()
            # parse the charset value from 'Content-Type' header value.
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
                pos = charset.find(';')
                if pos>=0:
                    charset = charset[0:pos]           

        if charset:
            content = content.decode(charset)
                
        print(content)
    # if this message part is still multipart such as 'multipart/mixed','multipart/alternative','multipart/related'
    elif content_type.startswith('multipart'):
        # get multiple part list.
        body_msg_list = msg.get_payload()
        # loop in the multiple part list.
        for body_msg in body_msg_list:
            # parse each message part.
            content = content + parse_email_content(body_msg)
    # if this message part is an attachment part that means it is a attached file.        
    elif content_type.startswith('image') or content_type.startswith('application'):
        # get message header 'Content-Disposition''s value and parse out attached file name.
        attach_file_info_string = msg.get('Content-Disposition')
        prefix = 'filename="'
        pos = attach_file_info_string.find(prefix)
        attach_file_name = attach_file_info_string[pos + len(prefix): len(attach_file_info_string) - 1]
        
        # get attached file content.
        attach_file_data = msg.get_payload(decode=True)
        # get current script execution directory path. 
        current_path = os.path.dirname(os.path.abspath(__file__))
        # get the attached file full path.
        attach_file_path = current_path + '/' + attach_file_name
        # write attached file content to the file.
        with open(attach_file_path,'wb') as f:
            f.write(attach_file_data)
            
        print('attached file is saved in path ' + attach_file_path)    
                
    else:
        content = content + msg.as_string()
        print(content)    
        
    return content
    
