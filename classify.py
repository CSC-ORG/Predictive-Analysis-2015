import sys
import re
import nltk.classify
    
    #start classify
def classify(self):
        #load positive keywords file          
        inpfile = open("data/pos_mod.txt", "r")            
        line = inpfile.readline()
        positive_words = []
        while line:
            positive_words.append(line.strip())
            line = inpfile.readline()
            
        #load negative keywords file    
        inpfile = open("data/neg_mod.txt", "r")            
        line = inpfile.readline()
        negative_words = []
        while line:
            negative_words.append(line.strip())
            line = inpfile.readline()
        #start processing each tweet 
        fp = open('processeddata.txt', 'r')
        line = fp.readline()       
        for i in line:
            tw = line[i]
            count = 0
            res = {}
            for t in tw:
                neg_words = [word for word in negative_words if(self.string_found(word, t))]
                pos_words = [word for word in positive_words if(self.string_found(word, t))]
                if(len(pos_words) > len(neg_words)):
                    label = 'positive'
                    self.pos_count[i] += 1
                elif(len(pos_words) < len(neg_words)):
                    label = 'negative'
                    self.neg_count[i] += 1
                else:
                    if(len(pos_words) > 0 and len(neg_words) > 0):
                        label = 'positive'
                        self.pos_count[i] += 1
                    else:
                        label = 'neutral'
                        self.neut_count[i] += 1
                result = {'text': t, 'tweet': self.origTweets[i][count], 'label': label}
                res[count] = result                
                count += 1         
            #end inner loop
            self.results[i] = res
        #end outer loop   
        
        

    
        #start writeOutput
        fp = open('input.txt', 'w')
        for i in self.results:
            res = self.results[i]
            for j in res:
                item = res[j]
                text = item['text'].strip()
                label = item['label']
                writeStr = text+" | "+label+"\n"
                fp.write(writeStr)
            #end inner loop
        #end outer loop      
    #end writeOutput
     
