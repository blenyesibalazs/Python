from atlassian import Jira
import jira

for key in jira.results:
    print(key)
#import json #to access the dumps function

#jira = Jira(
#    url = 'https://jira.orcsoftware.com/',
#    username = 'bblenyesi',
#    password = 'Infront22222222!'
#)

#jql_request = 'project=FOBR and issuekey = FOBR-16143'
#ticket = jira.jql(jql_request)

#print(type(issues))

#conv_issues = json.dumps(ticket) #converts the returned dict type to string

#print(type(conv_issues))

#f = open("C:\PythonFiles\jiratest.txt","w+")
#f.write(conv_issues)
#f.close()

#print("Successfully written")

#just to check the file contents in the output window
#g = open("C:\PythonFiles\jiratest.txt","r")
#if g.mode == 'r':
#    contents = g.read()
#    print(contents)

#for key in issues:
#    print(key, '->', issues[key])
#    print('\n')
#i = "expand"

#for key in ticket:
#    print(key)
#
#del ticket[i] 
#
#for key in ticket:
#    print(key)
