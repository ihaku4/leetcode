struct Stack {
    struct StackElement *list;
    int depth;
};

struct StackElement {
    struct TreeNode* node;
    int step;
};

// TODO
Stack *CreateStack();
void FreeStack(Stack *stack);
StackElement PopStack();
void PushStack(StackElement se);
