import json,string,codecs
model={}

with codecs.open("sentiment_json.txt","r") as f:
	model = json.load(f)

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content


def tag(s):
	seq=''
	score=[]
	words=s.split()
	for word in words:
		word = unicode(word, "utf-8")		
		if word in model:
			print word,': ',model[word]
		else:
			print word,': neu'		
	return

content=fileRead('test.txt')

for s in content:
	tag(s)
	
	
	
