        l=[]
        m=[]
        l.append(expressions)
        for s in l:
            c=0
            l1=[]
            ans=""
            for i in s:
                c+=1
                if i=="+":
                    pos=c
                    break
            s1=""
            s2=""
            s1=s[0:pos-1]
            s2=s[pos:]
            from fractions import Fraction
            a=Fraction(s1).numerator
            b=Fraction(s1).denominator
            c=Fraction(s2).numerator
            d=Fraction(s2).denominator
            import math
            den3 = math.gcd(b,d);
            den3 = (b*d) / den3;
            num3 = (a)*(den3/b) + (c)*(den3/d);
            ans=str(Fraction((int(num3)),int(den3)).numerator)+"/"+str(Fraction((int(num3)),int(den3)).denominator)
            l1.append(ans)