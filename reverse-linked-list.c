#include <stdio.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseListHelper(struct ListNode* head, struct ListNode* pre);
struct ListNode* reverseListRec(struct ListNode* head);
struct ListNode* reverseList(struct ListNode* head);

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *cur, *pre, *nxt;

    if (NULL == head) return NULL;

    pre = head;
    cur = pre->next;
    pre->next = NULL;
    while (cur) {
        nxt = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nxt;
    }
    return pre;
}

struct ListNode* reverseListRec(struct ListNode* head) {
    return reverseListHelper(head, NULL);
}

struct ListNode* reverseListHelper(struct ListNode* head, struct ListNode* pre) {
    struct ListNode *nxt;

    if (NULL == head) return NULL;
    nxt = head->next;
    head->next = pre;
    if (NULL == nxt) return head;
    return reverseListHelper(nxt, head);
}

int main(int argc, char *argv[])
{
    
    return 0;
}
