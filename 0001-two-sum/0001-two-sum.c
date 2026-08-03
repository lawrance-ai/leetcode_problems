typedef struct {
    int value;
    int index;
} NumPair;
int compare(const void* a, const void* b) {
    int val_a = ((NumPair*)a)->value;
    int val_b = ((NumPair*)b)->value;
    return (val_a > val_b) - (val_a < val_b);
}
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    NumPair* pairs = (NumPair*)malloc(numsSize * sizeof(NumPair));
    for (int i = 0; i < numsSize; i++) {
        pairs[i].value = nums[i];
        pairs[i].index = i;
    }
    qsort(pairs, numsSize, sizeof(NumPair), compare);
    int* result = (int*)malloc(2 * sizeof(int));
    if (result == NULL) {
        *returnSize = 0;
        free(pairs);
        return NULL;
    }
    int left = 0;
    int right = numsSize - 1;
    while (left < right) {
        int current_sum = pairs[left].value + pairs[right].value;
        if (current_sum == target) {
            result[0] = pairs[left].index;
            result[1] = pairs[right].index;
            *returnSize = 2;
            free(pairs);
            return result;
        } 
        else if (current_sum < target) {
            left++;
        } 
        else {
            right--; 
        }
    }
    *returnSize = 0;
    free(pairs);
    free(result);
    return NULL;
}
