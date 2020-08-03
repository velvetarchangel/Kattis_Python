#das blinkenlights

p, q, s = [int(x) for x in input().split()]

blink_p = set()
blink_q = set()

i = 1

while(i <= s):
    if i % p == 0:
        blink_p.add(i)
    if i % q == 0:
        blink_q.add(i)
    i += 1

final = blink_p.intersection(blink_q)

if(len(final) > 0):
    print("yes")
else:
    print("no")
