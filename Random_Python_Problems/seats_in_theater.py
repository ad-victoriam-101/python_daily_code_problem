def solution(nCols, nRows, col, row):
    cols_moved = (nCols-col)+1
    rows_moved = nRows-row
    return cols_moved*rows_moved
