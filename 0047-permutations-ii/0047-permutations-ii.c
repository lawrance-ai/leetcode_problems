int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void backtrack(int* nums, int numsSize, int* current, int currentSize, int* visited, int*** result, int* returnSize, int* capacity, int** returnColumnSizes) {
    if (currentSize == numsSize) {
        if (*returnSize >= *capacity) {
            *capacity *= 2;
            *result = (int**)realloc(*result, (*capacity) * sizeof(int*));
            *returnColumnSizes = (int*)realloc(*returnColumnSizes, (*capacity) * sizeof(int));
        }
        (*result)[*returnSize] = (int*)malloc(numsSize * sizeof(int));
        for (int i = 0; i < numsSize; i++) {
            (*result)[*returnSize][i] = current[i];
        }
        (*returnColumnSizes)[*returnSize] = numsSize;
        (*returnSize)++;
        return;
    }

    for (int i = 0; i < numsSize; i++) {
        if (visited[i]) continue;
        if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) continue;

        visited[i] = 1;
        current[currentSize] = nums[i];
        backtrack(nums, numsSize, current, currentSize + 1, visited, result, returnSize, capacity, returnColumnSizes);
        visited[i] = 0;
    }
}

int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), compare);

    int capacity = 10;
    *returnSize = 0;
    int** result = (int**)malloc(capacity * sizeof(int*));
    *returnColumnSizes = (int*)malloc(capacity * sizeof(int));

    int* current = (int*)malloc(numsSize * sizeof(int));
    int* visited = (int*)calloc(numsSize, sizeof(int));

    backtrack(nums, numsSize, current, 0, visited, &result, returnSize, &capacity, returnColumnSizes);

    free(current);
    free(visited);

    return result;
}
