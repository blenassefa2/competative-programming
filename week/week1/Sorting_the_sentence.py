class Solution:
    def sortSentence(self, s: str) -> str:
        li= s.split()
        final =[""]*(len(li))
        for a in li:
            place = int(a[len(a)-1])-1
            final[place] = a[:-1]
    
        result = ' '.join([i for i in final if not i.isdigit()])
    

       
        return result