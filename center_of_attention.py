# code: utf-8


class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h

    def idx2sub(self, j):
        return (j // self.width, j % self.width)

    def sub2idx(self, s):
        return s[0]*self.width + s[1]

    def where_pixels(self, colour):
        pixels = dict()
        for j, p in enumerate(self.pixels):
            if p == colour:
                pixels[self.idx2sub(j)] = 99999999999999999999
        return pixels

    def central_pixels(self, colour):
        pixels = self.where_pixels(colour)
        # print(pixels)

        def neighbors(s):
            return [(s[0]-1, s[1]), (s[0]+1, s[1]), (s[0], s[1]-1), (s[0], s[1]+1)]

        for k in pixels.keys():
            if any(pixels.get(e, -1) == -1 for e in neighbors(k)):
                pixels[k] = 1
        # print(pixels)

        # for j in range(1):
        while 99999999999999999999 in pixels.values():
            for s in [e[0] for e in pixels.items() if e[1] == min(pixels.values())]:
                for n in neighbors(s):
                    if n in pixels.keys():
                        pixels[n] = min(pixels[n], pixels[s]+1)
            for s in [e[0] for e in pixels.items() if e[1] == min(pixels.values())]:
                pixels.pop(s)
        # print(pixels)

        return [self.sub2idx(s) for s in pixels.keys()]

    def central_pixels_fast(self, colour):
        size = self.width * self.height
        depths = [0] * size
        internal = []
        for position, pcolour in enumerate(self.pixels):
            if pcolour == colour:
                depths[position] = 1
                if (position > self.width and
                    position < size - self.width and
                    position % self.width and
                        (position + 1) % self.width):
                    internal.append(position)
                    depths[position] += min(depths[position - 1],
                                            depths[position - self.width])
        max_depth = 1
        for position in internal[::-1]:
            depths[position] = min(depths[position],
                                   depths[position + 1] + 1,
                                   depths[position + self.width] + 1)
            max_depth = max(depths[position], max_depth)
        return [position for position, depth in enumerate(depths) if depth == max_depth]


image = Image([1, 1, 4, 4, 4, 4, 2, 2, 2, 2,
               1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
               1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
               1, 1, 1, 1, 1, 3, 2, 2, 2, 2,
               1, 1, 1, 1, 1, 3, 3, 3, 2, 2,
               1, 1, 1, 1, 1, 1, 3, 3, 3, 3], 10, 6)


print(image.central_pixels(1))
print(image.central_pixels(2))
print(image.central_pixels(3))
