#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *list0;
    int *list1;
    int len0;
    int len1;
} Queue;

/* Create a queue */
void queueCreate(Queue *queue, int maxSize) {
    queue->list0 = malloc(sizeof(int) * maxSize);
    queue->len0 = 0;
    queue->list1 = malloc(sizeof(int) * maxSize);
    queue->len1 = 0;
}

/* Push element x to the back of queue */
void queuePush(Queue *queue, int element) {
    while (queue->len1) {
        // pop list1, and push list0. (Reverse elements order)
        queue->list0[queue->len0] = queue->list1[queue->len1 - 1];
        ++queue->len0;
        --queue->len1;
    }
    // push list0
    queue->list0[queue->len0] = element;
    ++queue->len0;
    // pop list0, and push list1
    while (queue->len0) {
        queue->list1[queue->len1] = queue->list0[queue->len0 - 1];
        ++queue->len1;
        --queue->len0;
    }
}

/* Removes the element from front of queue */
void queuePop(Queue *queue) {
    --queue->len1;
}

/* Get the front element */
int queuePeek(Queue *queue) {
    return queue->list1[queue->len1 - 1];
}

/* Return whether the queue is empty */
bool queueEmpty(Queue *queue) {
    return (0 == queue->len1);
}

/* Destroy the queue */
void queueDestroy(Queue *queue) {
    free(queue->list0);
    free(queue->list1);
}

int main(int argc, char *argv[])
{
    
    return 0;
}
