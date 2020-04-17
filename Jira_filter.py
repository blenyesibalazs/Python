from atlassian import Jira

jira = Jira(
    url = 'https://jira.orcsoftware.com/',
    username = 'bblenyesi',
    password = 'Infront22222222!'
)

jql_request = 'project=FOBR and issuekey = FOBR-16143'
ticket = jira.jql(jql_request)