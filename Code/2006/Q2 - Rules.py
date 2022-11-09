

class Rule:


    lets = ["x", "u", "d"]

    def __init__(self, inp):
        self.valid = []

        self.rule = inp
        self.gen(0)


    def gen(self, pos, stem="", group = [], groupactive=False):

        if pos >= len(self.rule):

            self.valid.append(stem)
            #print(stem, len(stem))
            return

        ### A few cases
        ### First deal with it just being a letter

        if self.rule[pos] in Rule.lets:
            ### Add to stem and recurse

            if groupactive:
                group += self.rule[pos]
                self.gen(pos + 1, stem, group[:], groupactive)

            else:
                self.gen(pos + 1, stem + self.rule[pos], group[:], groupactive)


        else:

            if self.rule[pos] == "?":

                if group:
                    self.gen(pos+1, stem+"".join(group), [], False)

                else:
                    ### Take previous letter
                    self.gen(pos+1, stem[:-1], [], False)
                self.gen(pos + 1, stem, [], False)



            elif self.rule[pos] == "*":
                if group:

                    sgroup = "".join(group)

                    c = 0
                    while len(stem) <= 12-(c*len(sgroup)):
                        self.gen(pos+1, stem+(c*sgroup), [], False)
                        c += 1


                else:
                    ### Take previous letter
                    ### Account for case where letter is zero
                    self.gen(pos+1, stem[:-1], [], False)


                    for rep in range(13-len(stem)):
                        self.gen(pos+1, stem+(self.rule[pos-1]*rep), [], False)


            elif self.rule[pos] == ")":

                self.gen(pos+1, stem, group, False)

            else:

                self.gen(pos+1, stem, [], True)

                ### Open bracket


    def match(self, string, rule):

        if len(string) != len(rule):
            return False
        last = -1

        for ind in range(len(string)):
            ne = int(string[ind])
            #print(last, ne, rule[ind])
            if rule[ind] == "x":
                pass
            elif rule[ind] == "d":

                if last <= ne:
                    return False
            else:

                ### ne > last for True
                if last >= ne:
                    return False
            last = int(ne)
        return True



    def matchany(self, string):

        for r in self.valid:
            if self.match(string, r):
                return True
        return False


r = Rule(input())


for i in range(2):
    rep = r.matchany(input())
    if rep:
        print("Yes")
    else:
        print("No")





"""
B)

Four different rules:
x - 10
xxx - 10^3
xxd - Count carefully (10 * 45) = 450
xxdxx = 450*100
= 45000+1000+450+10
= 46460


BUT all passwords accepted by xxd will also be accepted by xxd(xx)?
so -450
46010

C) x(ud)*u?


D) No, because there are only 10 digits that may be used in the password, For a rule to match only one password
there must only be one option at the end of the 11 digit rule. This means that the rule cannot end in x, so the rule must end
in either u / d. If the rule ends in a U and only has one option, this must mean that the last letter must be a 9, and
and then for there only to be one option, the second last letter must be a u. So the second last letter in the password
must be an 8. This similarly holds for the D letters. Since there are only 10 digits, we have one too many characters in the rule
therefore there must be at least two xs at the start of the rule, which can encode multiple passwords.
eg.
xxuuuuuuuuu
xxddddddddd




"""

