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

struct ResultList {
  int *list;
  int capacity;
  int length;
};

struct TreeNode *constructBinaryTreeFromList(int *arr, int len);
struct TreeNode *constructBinaryTreeFromList_Helper(int *arr, int len, struct TreeNode ***nodePList);

struct ResultList *CreateResultList() {
  struct ResultList *result = malloc(sizeof(struct ResultList));
  result->capacity = 1;
  result->length = 0;
  result->list = malloc(sizeof(int) * result->capacity);
  return result;
}

void AppendResultList(struct ResultList *result, int val) {
  while (result->capacity <= result->length) {
    result->capacity += result->capacity;
    result->list = realloc(result->list, sizeof(int) * result->capacity);
  }
  result->list[result->length++] = val;
}

void traverse() {
    int list[] = {37,-34,-48,0,-100,-100,48,0,0,0,0,-54,0,-71,-22,0,0,0,8};
    struct TreeNode *node = constructBinaryTreeFromList(list, 19);
    struct ResultList *resultList = CreateResultList();
    int i;
    struct TreeNode *current;

    while (node) {
      if (node->left) {
	current = node->left;
	while (current->right && current->right != node)
	  current = current->right;
	if (current->right == node) {
	  AppendResultList(resultList, node->val);	// visit node (inorder)
	  current->right = NULL;
	  node = node->right;
	}
	else {
	  /* AppendResultList(resultList, node->val);	// visit node (preorder) */
	  current->right = node;
	  node = node->left;
	}
      }
      else {
	AppendResultList(resultList, node->val); // visit node
	node = node->right;
      }
    }
    
    for (i = 0; i < resultList->length; i++) {
      printf("%d ", resultList->list[i]);
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
  /* WithStack(traverse); */
  traverse();
  return 0;
}
