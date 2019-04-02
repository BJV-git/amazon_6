# POINT: u need to traverse, so check it, and again traverse
# time: O(N) - as we pass only once, space: O(1)

# use dfs - in any dfs write the base condition to reject it and later modify it

def flood_fill(image, sr, sc, newcolor):
    rows, cols, orig = len(image), len(image[0]), image[sr][sc]

    def traverse(r,c):
        if not(0<= r< rows and 0<= c< cols) or image[r][c] != orig:
            return
        image[r][c] = newcolor
        [traverse(r+i, c+j) for i,j in ((0,1),(1,0), (0,-1), (-1,0))]
    if orig != newcolor:
        traverse(sr,sc)

    return image