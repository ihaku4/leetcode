#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void invertTreeHelper(struct TreeNode* root) {
    if (NULL == root)
        return;

    root->left ^= root->right;
    root->right ^= root->left;
    root->left ^= root->right;

    invertTreeHelper(root->left);
    invertTreeHelper(root->right);
}

struct TreeNode* invertTree(struct TreeNode* root) {
    invertTreeHelper(root);
    return root;
}

int main(int argc, char *argv[])
{
    
    return 0;
}
