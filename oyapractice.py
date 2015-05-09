# -*encoding:utf-8*-

def testa():
    s = "in test"
    print s

def testb(t):
    print t
    
if __name__ == '__main__':
    
    a = 20
    print a
    
    print 5 / 2
    print int(5 / 2)
    
    if a <= 20:
        print "a < 20"
        print a**2
    elif(a > 20):
        print "a > 20"        
    else:
        print"other"
    
    for i in range(10):
        print i
        
    tst = 10
    j = 0
    while j < tst:
        j += 1 
            
    a = []
    a.append(1)
    a.append("test")
    print a[0]
    print a[1]
    
    b = [1,2,3,4,5,6]
    print b[0:3]
    print b[0:2] + b[4:6]
    
    c = map(str, b)
    d = ", ".join(c)
    print c
    print d
    
    for e in range(10):
        print e
        #e.append(a)
    for f in range(0, 40, 2):
        print f
    g = b[::3]
    print g
    
    h = {'ishikawa': 10, 'isibashi' : 20, 'okumura': 30}
    print h
    
    h = {}
    h['okumura'] = 10
    print h
    
    l = [[1,2,3],[4,5,6],[7,8,9]]
    print l
    print l[1][2]
    for row in l:
        print len(l)
        for i in row:
            print i
    print l[0]
    
    m = [[1,2],[1,2,3,4,5,6,7,8],[1]]
    print m
    
    n = [i * 10 for i in range(10)]
    print n
    n = [i * 2 for i in n]
    print n
    
    o = [[i for i in range(10)] for i in range(5)]
    print o
    o = [[1 for i in range(10)] for i in range(5)]
    print o
    
    p = [1] * 100
    print p
    
    #caution!!
    q = [[0] * 5] * 3
    print q
    q[0][1] = 1
    print q
    
    r1 = b
    r2 = o
    r3 = p
    print r1
    print r2
    print r3
    
    astr = "hello world"
    print len(astr)
    
    print max(a,b)
    print min(b)
    print ord("A")
    print chr(66)
    print [chr(i) for i in range(ord("A"),ord("A") + 26)]
    print range(len(astr))
    
    print "input str"
    v = raw_input()
    print v
    print "input int"
    v = int(raw_input())
    print v
    
    u = set([1 ,2 ,3 ,4 ,5 ,6, 7, 8, 9, 10])
    print u
    
    file = open('text1.txt','r')
    w = {}
    for line in file:
        name, value = line.rstrip().split(',')
        w[name] = int(value)
    print w["ishikawa "]
    file.close()
    
    file1 = open("text2.txt","r")
    x = []
    for line in file1:
        x.append(map(int, line.split(",")))
    print x
    file.close()
    
    out = open('res.txt', 'w')
    for i in range(10000):
        out.write(i)
        out.write("\n")
        #out.write(str(i)+"\n")
    out.close()
    
    testa()
    testb(u)
    
    