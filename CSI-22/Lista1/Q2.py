import turtle

def draw_poly(t, n, sz):
    """Make turtle t draw a regular polygon whith n sides of size sz."""
    for i in range(n):
        t.forward(sz)
        t.left(180-180*(n-2)/n)