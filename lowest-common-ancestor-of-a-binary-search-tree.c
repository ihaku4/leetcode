#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    struct TreeNode *node;
    struct TreeNode *larger, *less;

    if (p->val == q->val) return p;
    larger = (p->val > q->val) ? p : q;
    less   = (p->val > q->val) ? q : p;

    node = root;
    while (node) {
        if      (node->val < less->val)   node = node->right;
        else if (node->val > larger->val) node = node->left;
        else return node;  // if (less->val <= node->val && larger->val >= node->val)
    }
    return NULL;
}

int main(int argc, char *argv[])
{
    return 0;
}
