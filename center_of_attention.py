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
        pixels = set()
        for j, p in enumerate(self.pixels):
            if p == colour:
                pixels.add(self.idx2sub(j))
        return pixels

    def central_pixels(self, colour):
        pixels = self.where_pixels(colour)

        def shrink(pixels, edges=None):
            new_pixels = set()
            new_edges = set()
            if edges is None:
                for p in pixels:
                    if (p[0]-1, p[1]) in pixels and (p[0]+1, p[1]) in pixels and (p[0], p[1]-1) in pixels and (p[0], p[1]+1) in pixels:
                        new_pixels.add(p)
                    else:
                        new_edges.add(p)
            else:
                new_pixels = pixels.copy()
                for e in edges:
                    for ee in [(e[0]-1, e[1]), (e[0]+1, e[1]), (e[0], e[1]-1), (e[0], e[1]+1)]:
                        if ee in pixels:
                            new_edges.add(ee)
                            if ee in new_pixels:
                                new_pixels.remove(ee)
            return new_pixels, new_edges

        edges = None
        while pixels:
            new_pixels, new_edges = shrink(pixels, edges)
            if not new_pixels:
                break
            pixels, edges = new_pixels, new_edges

        return [self.sub2idx(s) for s in pixels]
        return 0


image = Image([1, 1, 4, 4, 4, 4, 2, 2, 2, 2,
               1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
               1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
               1, 1, 1, 1, 1, 3, 2, 2, 2, 2,
               1, 1, 1, 1, 1, 3, 3, 3, 2, 2,
               1, 1, 1, 1, 1, 1, 3, 3, 3, 3], 10, 6)


print(image.central_pixels(1))
print(image.central_pixels(2))
print(image.central_pixels(3))
