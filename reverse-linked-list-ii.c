#include <stdio.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head);
struct ListNode* reverseBetween(struct ListNode* head, int m, int n);

struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
    struct ListNode *subHead, *subTail, *pre = NULL, *nxt = NULL;
    int i = m;

    subHead = head;
    while (--i && subHead) {
        pre = subHead;
        subHead = subHead->next;
    }
    if (pre) pre->next = NULL;

    i = n - m;
    subTail = subHead;
    while (i-- && subTail) {
        subTail = subTail->next;
    }
    if (subTail) {
        nxt = subTail->next;
        subTail->next = NULL;
    }

    reverseList(subHead);
    if (pre) pre->next = subTail;
    if (nxt) subHead->next = nxt;

    if (1 == m) return subTail;
    else        return head;
}

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

int main(int argc, char *argv[])
{
    
    return 0;
}
