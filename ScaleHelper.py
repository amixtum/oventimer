from NoteHelper import NoteHelper

class ScaleHelper(object):
    def __init__(self, start=0, frequency=220):
        self.start = start
        self.fromStart = 0
        self.notes = NoteHelper(self.frequency)
        self.notes.setCenter(frequency)
        self.scale = [2, 2, 1, 2, 2, 2, 1]
        t = 0
        if start > 0:
            for _ in range(start):
                t += self.scale[0]
                self.scale.append(self.scale.pop(0))
            self.notes.transpose(t)
        else:
            for _ in range(int(abs(start))):
                t += self.scale[0]
                self.scale.insert(0, self.scale.pop())
            self.notes.transpose(-t)

    def transpose(self, n):
        self.fromStart += n
        t = 0
        if n > 0:
            for _ in range(int(n)):
                t += self.scale[0]
                self.scale.append(self.scale.pop(0))
            self.notes.transpose(t)
        else:
            for _ in range(int(abs(n))):
                t += self.scale[0]
                self.scale.insert(0, self.scale.pop())
            self.notes.transpose(-t)
        return self.notes.frequency

    def frequency(self):
        return self.notes.frequency

    def reset(self):
        self.transpose(-self.fromStart)