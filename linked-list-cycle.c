#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    struct ListNode *node = head;
    struct ListNode *pre = NULL;
    struct ListNode *nxt = NULL;

    if (NULL == head || NULL == head->next) {
        return false;
    }
    while (node) {
        nxt = node->next;
        node->next = pre;
        pre = node;
        node = nxt;
    }
    if (pre == head) {
        return true;
    }
    return false;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
