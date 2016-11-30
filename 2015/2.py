import sys

class Box:
    def __init__(self, l, w, h):
        self.l = int(l)
        self.w = int(w)
        self.h = int(h)

    def calc_surface(self):
        return 2 * self.l * self.w + \
               2 * self.w * self.h + \
               2 * self.h * self.l

    def calc_volume(self):
        return self.l * self.w * self.h

    def calc_extra(self):
        s1 = self.l * self.w
        s2 = self.w * self.h
        s3 = self.h * self.l
        return min(s1, s2, s3)

    def calc_ribbon(self):
        ret = self.calc_volume()
        ret += int(map(lambda x: 2*x[0] + 2*x[1], [sorted([self.l, self.w, self.h])[:2]])[0])
        return ret

total_area = 0
total_ribbon = 0

boxes = sys.stdin.readlines()
for box in boxes:
    box = box.rstrip('\n')
    cur_box = Box(*box.split('x'))
    total_area += cur_box.calc_surface()
    total_area += cur_box.calc_extra()
    total_ribbon += cur_box.calc_ribbon()

print "Paper: " + str(total_area)
print "Ribbon: " + str(total_ribbon)
