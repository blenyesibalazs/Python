from atlassian import Jira
import json #to access the dumps function

jira = Jira(
    url = 'https://jira.orcsoftware.com/',
    username = 'bblenyesi',
    password = 'Infront22222222!'
)

jql_request = 'project=FOBR and issuekey = FOBR-16143'
ticket = jira.jql(jql_request)

#conv_issues = json.dumps(ticket) #converts the returned dict type to string
#print(type(conv_issues))

#f = open("C:\PythonFiles\jiratest.txt","w+")
#f.write(conv_issues)
#f.close()

print("Successfully written to the file")

#just to check the file contents in the output window
#g = open("C:\PythonFiles\jiratest.txt","r")
#if g.mode == 'r':
#    contents = g.read()
#    print(contents)

#for key in ticket:
#    print(key, '->', ticket[key])
#    print('\n')

#delete miscellaneous keys, needs optimization
notNeededKeys = ["expand", "startAt", "maxResults", "total"]

print("Deleting keys: ")
for i in range(len(notNeededKeys)):
    del ticket[notNeededKeys[i]]
    print(notNeededKeys[i])

print('\n\n')
#the types vary depending on depth, there's a ton of nesting ongoing
#print(type(ticket))
#print(type(ticket["issues"]))
#print(type(ticket["issues"][0]))
#print(type(print(ticket["issues"][0]["fields"]))) #this finally contains all custom fields

parameters = ticket["issues"][0]["fields"] #new dictionary to house parameters

#for key in parameters:
#    print(key, parameters[key])

execution_desk = ticket["issues"][0]["fields"]["customfield_104814"]["value"]