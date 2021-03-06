# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, nTitle, nSubject, nSummary, nLink):
        self.guid = guid
        self.nTitle = nTitle
        self.nSubject = nSubject
        self.nSummary = nSummary
        self.nLink = nLink
        
    def getGuid(self):
        return self.guid
        
    def getSubject(self):
        return self.nSubject
        
    def getTitle(self):
        return self.nTitle
        
    def getSummary(self):
        return self.nSummary
        
    def getLink(self):
        return self.nLink     

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self, wordTrig):
        self.word = wordTrig
    def getWord(self):
      return self.word    
    def isWordIn(self, text):
        textlower = str(text).lower()
        for i in range(len(string.punctuation)):
            textlower = textlower.replace(string.punctuation[i], ' ')
        textWords = textlower.split(' ')
        for tword in textWords:
            if self.getWord().lower() == tword:
                return True
        return False
     
# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
            
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
            
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
       
# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, otherTrig):
        self.otherTrig = otherTrig
    def getOtherTrig(self):
        return self.otherTrig
    def evaluate(self, story):
        return not self.getOtherTrig().evaluate(story)
    
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, Trig1, Trig2):
        self.Trig1 = Trig1
        self.Trig2 = Trig2
    def getTrig1(self):
        return self.Trig1
    def getTrig2(self):
        return self.Trig2
    def evaluate(self, story):
        return self.getTrig1().evaluate(story) and self.getTrig2().evaluate(story)
    
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, Trig1, Trig2):
        self.Trig1 = Trig1
        self.Trig2 = Trig2
    def getTrig1(self):
        return self.Trig1
    def getTrig2(self):
        return self.Trig2
    def evaluate(self, story):
        return self.getTrig1().evaluate(story) or self.getTrig2().evaluate(story)

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def getPhrase(self):
        return self.phrase
    def evaluate(self, story):
        return (self.getPhrase() in story.getTitle()) or (self.getPhrase() in story.getSubject()) or (self.getPhrase() in story.getSummary())

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filteredStories = []
    for story in stories:
        for trigger in triggerlist:
            print trigger.evaluate(story)
            if trigger.evaluate(story) and not (story in filteredStories):
                filteredStories.append(story)
    return filteredStories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    #trigger = makeTrigger(triggerMap, linesplit[1], linesplit[2:], linesplit[0])
    
    #triggerMap[name].getWord() = params
    if name not in triggerMap.keys():
        if triggerType == "TITLE":
            trigger = TitleTrigger(params[0])
        elif triggerType == "SUBJECT":
            trigger = SubjectTrigger(params[0])
        elif triggerType == "SUMMARY":
            trigger = SummaryTrigger(params[0])
        elif triggerType == "NOT":
            trigger = NotTrigger(triggerMap[params[0]])
        elif triggerType == "AND":
            trigger = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
        elif triggerType == "OR":
            trigger = OrTrigger(triggerMap[params[0]], triggerMap[params[1]]) 
        elif triggerType == "PHRASE":
            trigger = PhraseTrigger(' '.join(params))
        triggerMap[name] = trigger
        return trigger


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("C:/Python34/ProblemSet7/triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

