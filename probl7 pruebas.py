import string
print string.punctuation

w= "DSS.?  adr, dg//23+ds soft's HAH gdg) ii"
e = w.lower().replace(string.punctuation, ' ')

print w.lower().replace(string.punctuation, ' ')

for i in range(len(string.punctuation)):
    e = e.replace(string.punctuation[i], ' ')
    
print e
print e.split(' ')
    
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

# TODO: WordTrigger
class wordTrigger(Trigger):
    def __init__(self, wordTrig):
        self.word = wordTrig        
    def isWordIn(self, text):
        textlower = str(text).lower()
        for i in range(len(string.punctuation)):
            textlower = textlower.replace(string.punctuation[i], ' ')
        textWords = textlower.split(' ')
        for tword in textWords:
            if self.word.lower() == tword:
                return True
        return False
     
# TODO: TitleTrigger
class TitleTrigger(wordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.nTitle)
            
# TODO: SubjectTrigger
class SubjectTrigger(wordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.nSubject)
            
# TODO: SummaryTrigger
class SummaryTrigger(wordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.nSummary)

class NotTrigger(Trigger):
    def __init__(self, otherTrig):
        self.otherTrig = otherTrig
    def getOtherTrig(self):
        return self.otherTrig
    def evaluate(self, story):
        return not self.otherTrig().evaluate()
             
koala = NewsStory('', '', '', 'Koala bears are soft and cuddly', '')
pillow = NewsStory('', '', '', 'I prefer pillows that are soft.', '')
soda = NewsStory('', '', '', 'Soft drinks are great', '')
pink = NewsStory('', '', '', "Soft's the new pink!", '')
football = NewsStory('', '', '', '"Soft!" he exclaimed as he threw the football', '')
microsoft = NewsStory('', '', '', 'Microsoft announced today that pillows are bad', '')
nothing = NewsStory('', '', '', 'Reuters reports something really boring', '')
caps = NewsStory('', '', '', 'soft things are soft', '')

s1 = SummaryTrigger('soft')
print s1.evaluate(pink)
