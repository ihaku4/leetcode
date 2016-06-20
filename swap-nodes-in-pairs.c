#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *node1, *node2, *pre;

    if (NULL == head || NULL == head->next)
        return head;

    node1 = head;
    head = head->next;
    pre = NULL;
    while (node1 && node1->next) {
        node2 = node1->next;

        node1->next = node2->next;
        node2->next = node1;
        if (pre) pre->next = node2;

        pre = node1;
        node1 = node1->next;
    }

    return head;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
