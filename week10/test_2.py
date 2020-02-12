class Triathlete(object):

    def __init__(self, name, tid=0):
        self.name = name
        self.tid = tid
        self.times = {}
        self.race_times = 0

    def __str__(self):
        return 'Name: {:s}\nID: {:d}\nRace time: {:d}'.format(self.name, self.tid, self.race_times)

    def add_time(self, sport, t):
        self.times[sport] = t
        self.race_times += t

    def get_time(self, sport):
        return self.times[sport]

    def __eq__(self, other):
        return self.race_times == other.race_times


    def __lt__(self, other):
        return self.race_times < other.race_times

    def __gt__(self, other):
        return self.race_times > other.race_times

class Triathlon(object):

    def __init__(self):
        self.mapping = {}

    def add(self, triathlete):
        self.mapping[triathlete.tid] = triathlete

    def remove(self, tid):
        del self.mapping[tid]

    def lookup(self, tid):
        if tid in self.mapping:
            return self.mapping[tid]
        return None

    def __str__(self):
        l = []
        for e in sorted(self.mapping.values(), key=lambda x: x.name):
            l.append('Name: {:s}'.format(e.name))
            l.append('ID: {:d}'.format(e.tid))
        return '\n'.join(l)

    def best(self):
        return min(self.mapping.values(), key=lambda x: x.race_times)

    def worst(self):
        return max(self.mapping.values(), key=lambda x: x.race_times)
