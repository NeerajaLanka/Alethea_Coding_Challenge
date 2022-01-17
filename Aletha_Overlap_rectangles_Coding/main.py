### Problem Statement
"""Consider the following is a list of numbers:

3 5 8 9 5 6 10 11

Each pair of numbers is an (x, y) coordinate (e.g., 3, 5 is (3, 5), and
8, 9 is (8, 9), but 5, 8 is not a pair).  In this manner, the entire list
can be parsed into a list of (x, y) points as follows:

(3, 5), (8, 9), (5, 6), (10, 11)

Now, consider each pair of these ordered pairs of coordinates:  the first describes
the lower-left corner of a rectangle on the cartesian plane and the second describes
an upper-right corner of a rectangle on the cartesian plane.  For example, one rectangle
is described by ((3, 5), (8, 9)) and another by ((5, 6), (10, 11)).

The task is:  determine the area of the intersection of all rectangles for an arbitrary
input list of positive integers, which may be odd or even.  Note that this is the area
of the intersection of all rectangles, not the total area of all intersections.
As an example, if there are three rectangles and only two overlap, then the area of
intersection is 0 because there's a rectangle in the set of input rectangles not overlapping
the rest.  It would be a plus if your program could read the list from STDIN and process it as
values appear, rather than requiring the entire list up front as input.

### Other requirements
- Must target Linux x86_64, macOS x86_64, or WSL 2.
- Must be coded in any of the following languages:  JavaScript, TypeScript, Python, Rust, C or C++
- Programs must not assume that the input fits in memory!

### Some considerations
- Comment your code in a helpful way that balances clarity over verbosity.
- Consider supplying a separate manifest for depedencies (e.g., if you write python, consider supplying a requirements file).  The
user should have minimum friction executing your code."""
L1 = [3, 5, 8, 9, 5, 6, 10, 11]
L=[]
for i in range(0,len(L1),2):
    L.append((L1[i],L1[i+1]))

l1=L[0]
r1=L[1]
l2=L[2]
r2=L[3]


def overlappingArea(l1,r1,l2,r2):
    x = 0
    y = 1

    # Area of 1st Rectangle
    area1 = abs(l1[x] - r1[x]) * abs(l1[y] - r1[y])

    # Area of 2nd Rectangle
    area2 = abs(l2[x] - r2[x]) * abs(l2[y] - r2[y])

    x_dist = (min(r1[x], r2[x]) -
              max(l1[x], l2[x]))

    y_dist = (min(r1[y], r2[y]) -
              max(l1[y], l2[y]))
    areaI = 0
    if x_dist > 0 and y_dist > 0:
        areaI = x_dist * y_dist

    return (area1 + area2 - areaI)

ans=overlappingArea(l1, r1, l2, r2)
print(ans)
