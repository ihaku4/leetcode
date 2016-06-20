#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *list;
    int depth;
} Stack;

/* Create a stack */
void stackCreate(Stack *stack, int maxSize) {
    stack->list = malloc(sizeof(int) * maxSize);
    stack->depth = 0;
}

/* Push element x onto stack */
void stackPush(Stack *stack, int element) {
    stack->list[stack->depth] = element;
    ++stack->depth;
}

/* Removes the element on top of the stack */
void stackPop(Stack *stack) {
    --stack->depth;
}

/* Get the top element */
int stackTop(Stack *stack) {
    return stack->list[stack->depth - 1];
}

/* Return whether the stack is empty */
bool stackEmpty(Stack *stack) {
    return 0 == stack->depth;
}

/* Destroy the stack */
void stackDestroy(Stack *stack) {
    free(stack->list);
}
