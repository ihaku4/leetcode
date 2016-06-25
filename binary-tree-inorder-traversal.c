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

struct Stack {
    struct StackElement *list;
    int capacity;
    int depth;
};

struct StackElement {
    struct TreeNode* node;
    int step;
};

// TODO
struct Stack *CreateStack();
void FreeStack(struct Stack *stack);
int PopStack(struct Stack* stack, struct StackElement *output);
void PushStack(struct Stack* stack, struct StackElement se);

int* inorderTraversal(struct TreeNode* root, int* returnSize);
int* inorderTraversal_Helper(struct TreeNode* root, int* returnSize, int* returnArray, int *length);
struct TreeNode *constructBinaryTreeFromList_Helper(int *arr, int len, struct TreeNode ***nodePList);
struct TreeNode *constructBinaryTreeFromList(int *arr, int len);

struct Stack *CreateStack() {
    struct Stack *stack = malloc(sizeof(struct Stack));
    stack->depth = 0;
    stack->capacity = 1;
    stack->list = malloc(sizeof(struct StackElement) * stack->capacity);
    return stack;
}
void FreeStack(struct Stack *stack) {
    free(stack->list);
    free(stack);
}
int PopStack(struct Stack* stack, struct StackElement *output) {
    if (0 == stack->depth)
        return 0;

    --stack->depth;
    *output = stack->list[stack->depth];
    return 1;
}
void PushStack(struct Stack *stack, struct StackElement se) {
    while (stack->capacity <= stack->depth) {
        /* printf("Extending Capacity From %d to %d\n", stack->capacity, stack->capacity * 2); */
        stack->capacity *= 2;
        stack->list = realloc(stack->list, sizeof(struct StackElement) * stack->capacity);
        /* printf("Success Extending Capacity From %d to %d\n", stack->capacity, stack->capacity * 2); */
    }
    /* printf("------ capacity: %d\n", stack->capacity); */
    /* printf("------ depth: %d\n", stack->depth); */
    stack->list[stack->depth] = se;
    ++stack->depth;
    /* printf("------ Push Success, depth: %d\n", stack->depth); */
}

struct StackElement CreateStackElement(struct TreeNode *node, int step) {
    struct StackElement se;

    se.node = node;
    se.step = step;
    return se;
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    struct Stack *stack = CreateStack();
    struct StackElement se;

    int *returnArray;
    int length = 1;

    returnArray = malloc(sizeof(int) * length);
    *returnSize = 0;

    if (NULL == root) return NULL;

    se = CreateStackElement(root, 1);
    PushStack(stack, se);

    while (PopStack(stack, &se)) {
        /* printf("----------\n"); */
        if (1 == se.step) {
            PushStack(stack, CreateStackElement(se.node, 2));
            if (se.node->left)
                PushStack(stack, CreateStackElement(se.node->left, 1));
        }
        else {
            // visite
            while (*returnSize >= length) {
                length += length;
                returnArray = realloc(returnArray, sizeof(int) * length);
            }
            returnArray[*returnSize] = se.node->val;
            ++*returnSize;
            // ------

            if (se.node->right)
                PushStack(stack, CreateStackElement(se.node->right, 1));
        }
    }

    FreeStack(stack);
    return returnArray;
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inorderTraversal_Recursive(struct TreeNode* root, int* returnSize) {
    int *returnArray;
    int length = 1;

    returnArray = malloc(sizeof(int) * length);
    *returnSize = 0;

    return inorderTraversal_Helper(root, returnSize, returnArray, &length);
}

int* inorderTraversal_Helper(struct TreeNode* root, int* returnSize, int* returnArray, int *length) {
    if (NULL == root) return NULL;

    inorderTraversal_Helper(root->left, returnSize, returnArray, length);

    // visit
    while (*returnSize >= *length) {
        *length += *length;
        returnArray = realloc(returnArray, sizeof(int) * *length);
    }
    returnArray[*returnSize] = root->val;
    ++*returnSize;
    // -----

    inorderTraversal_Helper(root->right, returnSize, returnArray, length);

    return returnArray;
}

// free binary tree
void freeTree() {}

// create binary tree node
struct TreeNode *createNode(int val) {
    return NULL;
}

struct TreeNode *constructBinaryTreeFromList(int *arr, int len) {
    struct TreeNode ***nodePList = malloc(sizeof(struct TreeNode **) * len * 2);
    struct TreeNode ***tofree = nodePList;
    struct TreeNode *root;

    root = constructBinaryTreeFromList_Helper(arr, len, nodePList);

    free(tofree);
    return root;
}

struct TreeNode *constructBinaryTreeFromList_Helper(int *arr, int len, struct TreeNode ***nodePList) {
    int i;
    struct TreeNode *root, *newNode;
    struct TreeNode **nodeP;
    /* struct TreeNode **nodePList[1000]; */
    int nodeListStart = 0;
    int nodeListEnd = 0;

    if (3 > len) return NULL;
    if (0 == arr[0]) return NULL;

    root = malloc(sizeof(struct TreeNode));
    root->val = arr[0];
    root->left = root->right = NULL;

    nodePList[nodeListEnd++] = &root->left;
    nodePList[nodeListEnd++] = &root->right;

    for (i = 1; i < len; i++) {
        nodeP = nodePList[nodeListStart++];
        if (0 == arr[i]) // XXX NULL == 0 ... "null" ?
            *nodeP = NULL;
        else {
            newNode = malloc(sizeof(struct TreeNode));
            newNode->val = arr[i];
            newNode->left = newNode->right = NULL;

            *nodeP = newNode;
            nodePList[nodeListEnd++] = &newNode->left;
            nodePList[nodeListEnd++] = &newNode->right;
        }
    }
    return root;
}

int main(int argc, char *argv[])
{
    /* struct TreeNode node3 = { 3, NULL, NULL }; */
    /* struct TreeNode node2 = { 2, &node3, NULL }; */
    /* struct TreeNode node1 = { 1, NULL, &node2 }; */
    int *arr = NULL, *tofree = NULL;
    int len;
    int i;
    /* int list[] = { 1, 0, 2, 3 }; */
    int list[] = {37,-34,-48,0,-100,-100,48,0,0,0,0,-54,0,-71,-22,0,0,0,8};
    struct TreeNode *root = constructBinaryTreeFromList(list, 19);

    /* tofree = arr = inorderTraversal(&node1, &len); */
    /* tofree = arr = inorderTraversal(root, &len); */
    tofree = arr = inorderTraversal_Recursive(root, &len);
    for (i = 0; i < len; i++)
        printf("%d ", arr[i]);

    free(tofree);
    return 0;
}
