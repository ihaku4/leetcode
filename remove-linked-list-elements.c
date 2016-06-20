#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* node;

    while (head && val == head->val) {
        head = head->next;
    }

    node = head;
    while (node && node->next) {
        while (node->next && val == node->next->val) {
            node->next = node->next->next;
        }
        node = node->next;
    }
    return head;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
