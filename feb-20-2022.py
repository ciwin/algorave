Clock.bpm=140
Scale.default="minor"

p1 >> pluck()

d1 >> play(P["x-o="].layer("add", "abcdef"), sample=5, pan=(-1,1))

a1 >> ambi([0, -1, -2, -3], dur = 4, sus = 4, oct = 4, fmod = 2, pan = (-1,1))

a2 >> prophet([0, -1, -2, -3], dur = 4, sus = 4, oct = 4, amp = 0.5, fmod = 1, pan = (-1,1))

b1 >> bass([0, 0, 0, 0, -1, -1, -1, -1, -2, -2, -2, -2, -3, -3, -3, -3], dur = 1, sus = 1, oct = 5, amp = 0.8, pan = (-1, 1))

b1.stop()

Clock.clear()
