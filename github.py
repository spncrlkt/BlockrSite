import urllib2
import simplejson as json

def open_url(url):
    open = urllib2.urlopen(url)
    return open

def create_repo_list(username):
    """
    takes a github username and returns a list of n repos owned by that username
    """
    url = "https://api.github.com/users/"+username+"/repos"
    reader = json.load(open_url(url))
    repo_list = []
    length = len(reader)
    n = 0
    while n < length:
        try:
            repo_list.append(reader[n]['name'])
            n+=1
        except:
            pass
    return repo_list

def check_commit_list(username, repo_name):
    """
    takes a github username and repo_name and returns a list of i commits for that repo
    """
    url = "https://api.github.com/repos/"+username+"/"+repo_name+"/commits"
    reader = json.load(open_url(url))
    repo_commit_list = []
    i = 0
    while i < 20:
        try:
            repo_commit_list.append({"message":reader[i]['commit']['message'], "date":reader[i]['commit']['committer']['date']})
        except:
            pass
        i+=1
    return repo_commit_list

def create_total_commit_list(username, repo_list):
    """
    takes a github username and a list of repos and creates a list of commits for all repos
    """
    total_commit_list = []
    for r in repo_list:
        print r
        total_commit_list.append(check_commit_list(username,r))
    return total_commit_list
        
import datetime
def clean_date(date_string):
    """
    takes a string from the gihub api and properly formats it for the python datetime module
    """
    list = date_string.split('-')
    year, month = int(list[0]), int(list[1])
    day_time = list[2].split('T')
    day = int(day_time[0])
    clean_date = datetime.datetime(year, month, day)
    time = day_time[1].split(':')
    minute, second = int(time[1]), int(time[2])
    if len(time[0]) > 1 and time[0][0] == "0":
        hour = int(time[0][1])
    else:
        hour = int(time[0])
    return datetime.datetime(year, month, day, hour, minute, second)

#clean_date("2012-05-23T0:21:52-07:00")

def check_for_recent_commits(time, total_commit_list):
    """
    takes a list of commit times and checks against a specified time and prints commits that have come since the specified time and prints the number of commits since the specified time
    """
    count = 0
    for repo in total_commit_list:
        for commit in repo:            
            if clean_date(commit['date']) > time:
                count += 1
    print str(count)+" commits since "+str(time)

#print create_total_commit_list(create_repo_list("jsmoxon"))[0][0]['date']
#check_for_recent_commits(datetime.datetime(2012,5,21), create_total_commit_list(create_repo_list("jsmoxon")))

def check_commits(time, username):
    """
    takes a time and a username and checks for commits by that user since that time
    """
    return check_for_recent_commits(time, create_total_commit_list(username, create_repo_list(username)))
