directions = ['direction', ['north', 'south', 'east']]
verbs = ['verb', ['go', 'kill', 'eat']]
stops = ['stop', ['the', 'in', 'of']]
nouns = ['noun', ['bear', 'princess']]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

class Lexicon():
    def __init__(self, n):
        self.n = n
    def scan(self, n):
        a = n.split(' ')
        result = []
        l = [directions, verbs, stops, nouns]
        for s in a:
            found = False
            for i in l:
                if s in i[1]:
                    found = True
                    result.append((i[0], s))
            if found == False:
                t = convert_number(s)
                if t == None:
                    result.append(('error', s))
                else:
                    result.append(('number', t))
        return result



lexicon = Lexicon(['directions', 'verbs', 'stops', 'nouns'])
