#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

void deleteNode(struct ListNode* node) {
    if (NULL == node || NULL == node->next)
        return;
    node->val = node->next->val;
    node->next = node->next->next;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
