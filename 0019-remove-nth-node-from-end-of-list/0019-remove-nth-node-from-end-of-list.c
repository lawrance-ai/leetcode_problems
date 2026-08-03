/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* current = head;
    int m=0;
    
    while (current != NULL && current->next != NULL) {
            current = current->next;
            m++;
    }
    if (m<n)
    {
        head=head->next;
        return head;
    }
    n=m-n;
    current = head;
    while(n>0)
    {
        current=current->next;
        n--;
    }
    current->next=current->next->next;
    printf("%d",m);
    return head;
}