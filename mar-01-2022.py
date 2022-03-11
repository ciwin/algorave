Clock.bpm=140
Scale.default="minor"

p1 >> pluck()

d1 >> play(P["x-o="].layer("add", "abcdef"), sample=5, pan=(-1,1))

a1 >> ambi([var([0,-1,-1,0]),4,[7,10],9], dur = 4, sus = 3, oct = 5, fmod = 4, pan = (-1,1))

a2 >> prophet([var([0,-1,-1,0]),4,[7,10],9], dur = 4, sus = 4, oct = 4, amp = 0.5, fmod = 1, pan = (-1,1))

b1 >> dirt(var([0,2,-1,3]), dur=PDur(3,8), bits=4, lpf=40, fmod=(0,1), amp=3)

b1.stop()

b2 >> bass([0, 0, 0, 0, -1, -1, -1, -1, -2, -2, -2, -2, -3, -3, -3, -3], dur = 1, sus = 1, oct = 5, amp = 0.8, pan = (-1, 1))

b1.stop()

d2 >> play(PZip("Vs", " n "), sample=4, hpf=var([0,4000],[28,4])).every(3,'stutter', dur=1)

d2.stop()

k1 >> karp(dur=1/4, oct=var([6,7]), sus=1, rate=P[:32]*(1,2),delay=(0,1/8), lpf=linvar([400,5000],12),pan=linvar([-1,1],8)) + var([0,-1,1,-7])

p1 >> blip([var([0,-1,-1,0]),4,[7,10],9], dur=1/2, sus=2, oct=(6,7))

k2 >> karp(P[var([0,1],8),7,6,4,2].layer("mirror"),
      delay=(0,0.25),
      sus=2,
      dur=PDur(5,8),
      chop=4,
      oct=7)

Clock.clear()

