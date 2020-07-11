num = int(input("ENTER FRIENDS:  "))
words = int(input("ENTER RHYME:  "))
friends = [i for i in range(1, num+1)]
c = 0
while len(friends)>1:
    c += words-1
    c %= len(friends)
    friends.pop(c)
print(friends[0])

#Scores full marks or 30/30

"""Analysis:
This is an implementation challenge, following the instructions carefully should lead to a full credit result.
There is typically no need to think of the efficiency to Q1 problems, but it is wise to test your program with the largest input 
that it could be given in competition, in this case: 1000 friends, and any rhyme. It runs comfortably.

One thing to note with this problem in particular, is the -1 on line 6. Since a person does point to themselves 
in the rhyme we need to subtract one for this.

,
It is generally possible to solve these problems if you have a basic mathematical background, for example,
computing primes quickly, and if you know a language well.


"""