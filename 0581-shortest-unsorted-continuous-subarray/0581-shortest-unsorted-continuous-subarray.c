int findUnsortedSubarray(int* nums, int numsSize) {
    if (numsSize <= 1) {
        return 0;
    }

    int max_val = INT_MIN;
    int min_val = INT_MAX;
    int start = -1;
    int end = -2; 

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > max_val) {
            max_val = nums[i];
        }
        if (nums[i] < max_val) {
            end = i;
        }
    }

    for (int i = numsSize - 1; i >= 0; i--) {
        if (nums[i] < min_val) {
            min_val = nums[i];
        }
        if (nums[i] > min_val) {
            start = i;
        }
    }

    return end - start + 1;
}