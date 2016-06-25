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
    struct TreeNode *list;
    int capacity;
    int depth;
};
struct StackElement {
    struct TreeNode* node;
    int step;
};

struct Stack *CreateStack();
void FreeStack(struct Stack *stack);
int PopStack(struct Stack* stack, struct TreeNode **output);
void PushStack(struct Stack* stack, struct TreeNode se);
int EmptyStack(struct Stack *stack);

struct TreeNode *constructBinaryTreeFromList(int *arr, int len);
struct TreeNode *constructBinaryTreeFromList_Helper(int *arr, int len, struct TreeNode ***nodePList);

struct Stack *CreateStack() {
    struct Stack *stack = malloc(sizeof(struct Stack));
    stack->depth = 0;
    stack->capacity = 1;
    stack->list = malloc(sizeof(struct TreeNode) * stack->capacity);
    return stack;
}
void FreeStack(struct Stack *stack) {
    free(stack->list);
    free(stack);
}
int PopStack(struct Stack* stack, struct TreeNode **output) {
    if (0 == stack->depth) {
        *output = NULL;
        return 0;
    }

    --stack->depth;
    *output = &stack->list[stack->depth];
    return 1;
}
void PushStack(struct Stack *stack, struct TreeNode se) {
    while (stack->capacity <= stack->depth) {
        stack->capacity *= 2;
        stack->list = realloc(stack->list, sizeof(struct TreeNode) * stack->capacity);
    }
    stack->list[stack->depth] = se;
    ++stack->depth;
}
int EmptyStack(struct Stack *stack) {
    return 0 == stack->depth;
}

/**
 * Auto create and free Stack.
 */
void WithStack(void (*func)(struct Stack *)) {
    struct Stack *stack = CreateStack();
    func(stack);
    FreeStack(stack);
}

void traverse(struct Stack *stack) {
    int list[] = {37,-34,-48,0,-100,-100,48,0,0,0,0,-54,0,-71,-22,0,0,0,8};
    struct TreeNode *node = constructBinaryTreeFromList(list, 19);
    int capacity = 1;
    int length = 0;
    int *resultList = malloc(sizeof(int) * capacity);
    int i;

    /* PushStack(stack, *node); */
    /* node = NULL; */
    while (!EmptyStack(stack) || node) {
        if (node) {
	  PushStack(stack, *node);
	  node = node->left;
	}
	else {
	  PopStack(stack, &node);
	  while (capacity <= length) {
	    capacity += capacity;
	    resultList = realloc(resultList, sizeof(int) * capacity);
	  }
	  resultList[length++] = node->val;

	  node = node->right;
	}
    }
    for (i = 0; i < length; i++) {
      printf("%d\n", resultList[i]);
    }
    return;
}

struct TreeNode *constructBinaryTreeFromList(int *arr, int len) {
    struct TreeNode ***nodePList = malloc(sizeof(struct TreeNode **) * len * 2);
    struct TreeNode ***tofree = nodePList;
    struct TreeNode *root;

    root = constructBinaryTreeFromList_Helper(arr, len, nodePList);

    free(tofree);
    return root;
}

/**
 * eg:
 *   int list[] = { 1, 0, 2, 3 };
 *   int list[] = { 37,-34,-48,0,-100,-100,48,0,0,0,0,-54,0,-71,-22,0,0,0,8 };  // len = 19
 *
 * 0 indicates 'NULL'
 */
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
  WithStack(traverse);
  return 0;
}
