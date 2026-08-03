int compare(const void *a, const void *b) {
    int *i1 = *(int **)a;
    int *i2 = *(int **)b;

    if (i1[0] != i2[0])
        return i1[0] - i2[0];

    return i2[1] - i1[1];
}

int removeCoveredIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {

    qsort(intervals, intervalsSize, sizeof(int *), compare);

    int count = 0;
    int end = 0;

    for (int i = 0; i < intervalsSize; i++) {

        // Current interval is not covered
        if (intervals[i][1] > end) {
            count++;
            end = intervals[i][1];
        }
    }

    return count;
}