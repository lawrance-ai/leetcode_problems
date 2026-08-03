
int compare(const void *a, const void *b) {
    int *interval1 = *(int **)a;
    int *interval2 = *(int **)b;

    return interval1[0] - interval2[0];
}

int** merge(int** intervals, int intervalsSize, int* intervalsColSize,
            int* returnSize, int** returnColumnSizes) {

    if (intervalsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    // Sort intervals based on start time
    qsort(intervals, intervalsSize, sizeof(int *), compare);

    int **result = (int **)malloc(intervalsSize * sizeof(int *));
    *returnColumnSizes = (int *)malloc(intervalsSize * sizeof(int));

    int index = 0;

    // Store first interval
    result[index] = (int *)malloc(2 * sizeof(int));
    result[index][0] = intervals[0][0];
    result[index][1] = intervals[0][1];
    (*returnColumnSizes)[index] = 2;

    for (int i = 1; i < intervalsSize; i++) {

        // If overlapping intervals
        if (intervals[i][0] <= result[index][1]) {

            // Update end if needed
            if (intervals[i][1] > result[index][1]) {
                result[index][1] = intervals[i][1];
            }
        }
        else {
            // Add new interval
            index++;
            result[index] = (int *)malloc(2 * sizeof(int));
            result[index][0] = intervals[i][0];
            result[index][1] = intervals[i][1];
            (*returnColumnSizes)[index] = 2;
        }
    }

    *returnSize = index + 1;

    return result;
}