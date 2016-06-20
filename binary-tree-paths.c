#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};



struct Stack {
    struct TreeNode **nodeList;
    int depth;
};

struct Stack * StackCreate(int size) {
    struct Stack *stack = malloc(sizeof(struct Stack));
    struct TreeNode **nodeList = malloc(sizeof(struct TreeNode *) * size);
    stack->nodeList = nodeList;
    stack->depth = 0;
    return stack;
}

void StackFree(struct Stack *stack) {
    free(stack->nodeList);
    free(stack);
}

void pushNode(struct TreeNode *node, struct Stack *stack) {
    stack->nodeList[stack->depth] = node;
    stack->depth++;
}

struct TreeNode * popNode(struct TreeNode *node, struct Stack *stack) {
    stack->depth--;
    return stack->nodeList[stack->depth];
}



void binaryTreePathsCountHelper(struct TreeNode* node, int* returnSize) {
    if (NULL == node->left && NULL == node->right) {
        ++*returnSize;
        return;
    }
    if (node->left)
        binaryTreePathsCountHelper(node->left, returnSize);
    if (node->right)
        binaryTreePathsCountHelper(node->right, returnSize);
}

// TODO: realloc, strlen, strnlen, strncpy, strncat, snprintf, str[MAX_SIZE]
// 
char** binaryTreePathsHelper(struct TreeNode* node, int* returnSize, char** stringList, char *pathString) {
    char newPathString[MAX_SIZE];
    int len;
    char *finalString = NULL;

    if (NULL == node) return stringList;

    len = strnlen(pathString, MAX_SIZE);
    strncpy(newPathString, pathString, MAX_SIZE);
    newPathString[sizeof(newPathString) - 1] = '\0';

    if (NULL == node->left && NULL == node->right) {
        ++*returnSize;
        snprintf(newPathString + len, MAX_SIZE - len, "%d", node->val);
        stringList = realloc(stringList, sizeof(char *) * (*returnSize));
        finalString = malloc(sizeof(char) * (strnlen(newPathString, MAX_SIZE - 1) + 1));
        /* strncpy(finalString, newPathString, strnlen(newPathString, MAX_SIZE)); */
        /* strncpy(finalString, newPathString, sizeof(finalString)); */
        strncpy(finalString, newPathString, strnlen(newPathString, MAX_SIZE - 1) + 1);
        finalString[strnlen(newPathString, MAX_SIZE)] = '\0';
        stringList[*returnSize - 1] = finalString;
        return stringList;
    }
    if (node->left) {
        snprintf(newPathString + len, MAX_SIZE - len, "%d->", node->val);
        stringList = binaryTreePathsHelper(node->left, returnSize, stringList, newPathString);
    }
    if (node->right) {
        snprintf(newPathString + len, MAX_SIZE - len, "%d->", node->val);
        stringList = binaryTreePathsHelper(node->right, returnSize, stringList, newPathString);
    }
    return stringList;
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    char ** stringList = malloc(0);
    return binaryTreePathsHelper(root, returnSize, stringList, "");
}



/**
 *                  37
 *          -34             -48
 *       null -100     -100         48
 *         null null null null  -54     null
 *                          -72     -22
 *                       null null null 8
 *                  
 * -------------------------------------------
 * [6,1,null,null,3,2,5,null,null,4]
 *                   6
 *                 1   null
 *             null 3
 *                2     5
 *          null null  4
 */
int main(int argc, char *argv[])
{
    char ** stringList = malloc(0);
    int returnSize = 0;
    int i;

    printf("%p\n", stringList);
    struct Stack *stack = StackCreate(100);
    StackFree(stack);

    /* struct TreeNode node_l_r = {10, NULL, NULL}; */
    /* struct TreeNode node_r = {9, NULL, NULL}; */
    /* struct TreeNode node_l = {8, NULL, &node_l_r}; */
    /* struct TreeNode node = {7, &node_l, &node_r}; */

    struct TreeNode node_6_1 = {8, NULL, NULL};
    struct TreeNode node_5_2 = {-22, NULL, &node_6_1};
    struct TreeNode node_5_1 = {-72, NULL, NULL};
    struct TreeNode node_4_1 = {-54, &node_5_1, &node_5_2};
    struct TreeNode node_3_3 = {48, &node_4_1, NULL};
    struct TreeNode node_3_2 = {-100, NULL, NULL};
    struct TreeNode node_3_1 = {-100, NULL, NULL};
    struct TreeNode node_2_2 = {-48, &node_3_2, &node_3_3};
    struct TreeNode node_2_1 = {-34, NULL, &node_3_1};
    struct TreeNode node = {37, &node_2_1, &node_2_2};
    /* binaryTreePathsHelper(&node, &returnSize, stringList, ""); */
    stringList = binaryTreePaths(&node, &returnSize);
    printf("------------\n");
    printf("%d\n", returnSize);
    for (i = 0; i < returnSize; i++) {
        printf("%s\n", stringList[i]);
    }

    return 0;
}
