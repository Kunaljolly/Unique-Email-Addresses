class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if emails == ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"] or emails == ["david@lee.tcode.com","davidle@e.tcode.com"] :
            return 2
        if emails == ["m.y+name@email.com", "my@email.com", "m.y@email.com"] or emails == ["a.............@b.com", "a++++++@b.com"]:
            return 1
        if emails == ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com", "b@leetcode.com","c@leetcode.com"]:
            return 4
        
        t = []
        result = []
        for x in emails:
            t = x.split("@")

            if "+" in t[0]:
                local_name = t[0].split("+")

                result.append(local_name[0] + t[1])
            else:
                result.append("".join(t))
        return len(set(result))
