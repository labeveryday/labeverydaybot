import random
import tweepy
import time

__author__ = "Du'An Lightfoot"
__email__ = "duanl@labeveryday"

CONSUMER_KEY = ' '
CONSUMER_SECRET = ' '
ACCESS_KEY = ' ' 
ACCESS_SECRET = ' '

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()
print('The user is %s' % user.name)

# tweet_mentions = api.mentions_timeline()

FILE_NAME = 'last_seen_id.txt'
SECOND_FILE = 'last_reply'

reply1 = """
Hey thanks for the message! Here's an #inspirationalquote. 
'You miss 100% of the shots you don’t take. –Wayne Gretzky' #LabEveryday  
"""
reply2 = """
Whats up? Thanks for the message! Here's one of my favorite #inspirationalquotes.
'The mind is everything. What you think you become.  –Buddha' #LabEveryday
"""
reply3 = """
Hola! Thanks for the message! Here's one of my favorite #inspirationalquotes.
'The best time to plant a tree was 20 years ago. The second best time is now. –Chinese Proverb' #LabEveryday
"""
reply4 = """
Whats good? Thanks for the message! Here's a #inspirationalquote.
'Eighty percent of success is showing up. –Woody Allen' #LabEveryday
"""
reply5 = """
Hey thanks for the message! Here's a interesting #techfact.
'The first Apple logo was of Sir Isaac Newton sitting underneath a tree,
with an apple about to hit his head.' #LabEveryday
"""
reply6 = """
Hey! Thanks for the message! Here's a fun #techfact.
'Bill Gates was a college dropout. And so was Kanye West!' #LabEveryday
"""
reply7 = """
Hola! Thanks for the message! Here's a fun #techfact.
'Did you know Alaska is the only state that can be typed on one row of a traditional QWERTY keyboard.' #LabEveryday
"""
reply8 = """
Hey! Thanks for the message! Here's a #inspirationalquote.
'Go confidently in the direction of your dreams.  Live the life you have imagined. –Henry David Thoreau' #LabEveryday
"""
reply9 = """
Hey, how are you? Thanks for the message! Here's one awesome #inspirationalquote.
'Everything you’ve ever wanted is on the other side of fear. –George Addair' #LabEveryday
"""
reply10 = """
Happy Monday! Wait, is it Monday? Thanks for the message! Here's one awesome #inspirationalquote.
'You can’t fall if you don’t climb.  But there’s no joy in living your whole life on the ground.' #LabEveryday
"""
reply11 = """
Turn up Tuesday! Ummm... Is it Tuesday? Thanks for the message! Here's a #inspirationalquote.
'To learn and not do is really not to learn! - Stephan Covey' #LabEveryday
"""

reply12 = """
I love Fridays! Thanks for the message! Here's a truly #inspirationalquote.
'It does not matter how slowly you go as long as you do not stop. –Confucius' #LabEveryday
"""
reply13 = """
Hey whats up? Thanks for the message! Here's a super #techfact.
'Did you know 8 billion devices will be connected to the internet by 2020?
Great time to be a NetworkEngineer' #LabEveryday
"""
reply14 = """
Sunday Funday? I'm sure its not Sunday lol. Thanks for the message! Here's a interesting #techfact.
'Did you know that the company Cisco's name derived from San Francisco?' #LabEveryday
"""
reply15 = """
Sunday Funday? I'm sure its not Sunday lol. Thanks for the message! Here's a interesting #techfact.
'Did you know that the company Cisco's name derived from San Francisco?' #LabEveryday
"""
reply16 = """
Whats up fam? Thanks for the message! Here's a helpful #techfact.
'Last time I checked. Indeed listed 60,827 open Network Engineer positions in the US!' #LabEveryday
"""
reply17 = """
Hola! Thanks for the message! Here's a fun #techfact.
'Did you know Google receives over 63,000 searches per second on any given day?' #LabEveryday
"""
reply18 = """
Hola! Thanks for the message! Here's a interesting #techfact.
'According to CBTNuggets there are an estimated 59,737 CCIEs in the world!' #LabEveryday
"""
reply19 = """
What's! What day is it? If today is Wednesday I think I ran out of responses.......
.
.
.
.
.
.
.
.
.
.
 SYKE! 
 Here's a fun #techfact.
'Technophobia is the fear of technology!' #LabEveryday
"""
reply20 = """
What's! What day is it? If today is Thursday I am taking the day off.......
.
.
.
.
.
.
.
.
.
.
 SYKE! 
 Here's a fun #techfact.
'Did you know the last /22 block of ipv4 addresses were chopped and dished out and 2017?' #LabEveryday
"""
reply21 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
Which of these is not related to linux? 
A. Open platform
B. Open Source
C. Debian
D. Active Directory
#LabEveryday
"""
reply22 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
In Ubuntu how do execute Super User Privileges? 
A. sudo
B. pwd
C. loginas:
D. ssh -l 
#LabEveryday
"""
reply23 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
How do you navigate back to the home directory? 
A. cd ..
B. ls
C. cd - 
D. cd 
#LabEveryday
"""
reply24 = """
#YOUWIN #Python #QuizTime! Thanks for the message! 
Here's a Python related #techquestion.
Python is a interpreted language? 
A. True
B. False
#LabEveryday
"""
reply25 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
Which command is an improvement on the more command? 
A. cat
B. head
C. less
D. tail
#LabEveryday
"""
reply26 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
In which file is DNS information referenced? 
A. /etc/network/interfaces
B. host 
C. dns.txt
D. resolv.conf
#LabEveryday
"""
reply27 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
How do you display interface ip information in linux? 
A. ipconfig
B. ping
C. ifconfig
D. show ip route
#LabEveryday
"""
reply28 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
What is the name of the first process that the Linux kernel runs, aside from itself? 
A. who
B. init 
C. cron
D. bootp
#LabEveryday
"""
reply29 = """
#YOUWIN #Linux #QuizTime! Thanks for the message! 
Here's a Linux related #techquestion.
Which command changes a files group? 
A. groupmod
B. groupadd
C. chmod
D. chown
#LabEveryday
"""
reply30 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
What would you use to verify security controls are in place? 
A. ping
B. port analyzer 
C. penetration test
D. vulnerability scan
#LabEveryday
"""
reply31 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
On which port would you apply an ACL to block IMAP traffic? 
A. 143
B. 22
C. 443
D. 3389
#LabEveryday
"""
reply32 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
What would you use to verify security controls are in place? 
A. ping
B. port analyzer 
C. penetration test
D. vulnerability scan
#LabEveryday
"""
reply33 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
Which protocols utilize UDP ports 161 and 162? 
A. HTTPS
B. SNMP 
C. SSL
D. APPLETALK
#LabEveryday
"""
reply34 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
Full disk encryption prevents? 
A. Client side attacks
B. Theft
C. Viruses
D. Clear text access
#LabEveryday
"""
reply35 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
A buffer overflow can result in which attack type? 
A. ARP poisoning
B. Zero-day
C. DNS poisoning
D. Pivilege escalation
#LabEveryday
"""
reply36 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
Which of the following sets multiple flag fields in a TCP packet? 
A. ARP poisoning
B. Zero-day
C. XMAS
D. Pivilege escalation
#LabEveryday
"""
reply37 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
In regards to PKI which component MUST be trusted by all parties? 
A. Private Key
B. Door key
C. CA
D. Key to the city
#LabEveryday
"""
reply38 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
This is used to trick people in social engineer? 
A. Software scan
B. Human nature
C. Protocol violation
D. Applications issues 
#LabEveryday
"""
reply39 = """
#YOUWIN #Security #QuizTime! Thanks for the message! 
Here's a Security+ related #techquestion.
Which is related to Bitlocker? 
A. ping
B. TPM
C. ACL
D. ipconfig 
#LabEveryday
"""
reply40 = """
#YOUWIN #CCNA #QuizTime! Thanks for the message! 
Here's a CCNA related #techquestion.
A MAC address operates at what layer of the OSI model? 
A. 1
B. 4
C. 2
D. 7
#LabEveryday
"""
reply41 = """
#YOUWIN #CCNA #QuizTime! Thanks for the message! 
Here's a CCNA related #techquestion.
Which MAC address begins a frame? 
A. destination node
B. router
C. source node
D. firewall
#LabEveryday
"""

reply_list = [reply1, reply2, reply3, reply4, reply5, reply6, reply7, reply8, reply9, reply10,
              reply11, reply12, reply13, reply14, reply15, reply16, reply17, reply18, reply19, reply20, reply21,
              reply22, reply23, reply24, reply25, reply26, reply27, reply28, reply29, reply30, reply31, reply32,
              reply33, reply34, reply35, reply36, reply37, reply38, reply39, reply40, reply41]

general_reply = "Hi thanks for the message! I am just a BOT that will soon have super powers! #StayTuned"


def find_tweets():
    # Find 'new' tweets (under hashtags/search terms)
    term = "#labeveryday"
    # Change the amount of tweets being searched for 50-75
    search = tweepy.Cursor(api.search, q=term, result_type="recent", lang="en").items(35)
    print("Searching under term..." + term)
    # Like 'new' tweets (only if the user has more than 100 followers & less than 2500 tweets)
    for tweet in search:
        if tweet.user.followers_count < 25 and tweet.user.statuses_count < 500:
            print("Ignoring user " + tweet.user.screen_name)
            continue
        try:
            tweet.retweet()
            print("Retweeted " + tweet.user.screen_name)
            # Follow the user, and then mute them.
            time.sleep(6)
            api.create_friendship(id=tweet.user.id)
            time.sleep(3)
            api.create_mute(id=tweet.user.id)
        except tweepy.TweepError as e:
            # Catching errors
            if e.args[0][0]['code'] == 139:
                print("Error with tweet " + str(tweet.id) + ", already liked!")
                continue
            if e.args[0][0]['code'] == 88:
                print("Rate limited..")
                time.sleep(60*15)
                continue
        print("Error with tweet " + str(tweet.id))


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets(reply_list):
    timeout = 300
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        print('Retrieving and replying to tweets.')
        reply = random.choice(reply_list)
        reply = str(reply)
        last_seen_id = retrieve_last_seen_id(FILE_NAME)
        tweet_mentions = api.mentions_timeline(last_seen_id)
        try:
            for mention in reversed(tweet_mentions):
                print(str(mention.id) + ' - ' + mention.text)
                last_seen_id = mention.id
                store_last_seen_id(last_seen_id, FILE_NAME)
                api.create_favorite(mention.id)
                if '#labeveryday' in mention.text.lower():
                    print('found #labeveryday!')
                    print('responding back...')
                    api.update_status('@' + mention.user.screen_name + reply, mention.id)
                else:
                    print('New Message')
                    print('responding back...')
                    api.update_status('@' + mention.user.screen_name + general_reply, mention.id)
        except AttributeError:
            print('No new mentions')
        time.sleep(15)


if __name__ == '__main__':
    while True:
        reply_to_tweets(reply_list)
        find_tweets()
        time.sleep(15)
