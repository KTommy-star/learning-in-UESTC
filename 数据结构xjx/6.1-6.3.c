#include <stdio.h>
#include <stdlib.h>  // malloc 和 free 的标准头文件

typedef char DataType;

typedef struct Node {
    DataType data;
    struct Node *LChild;
    struct Node *RChild;
} BiTNode, *BiTree;

void Visit(const char ch) {
    printf("%c  ", ch);
}

//6.1 先序遍历二叉树
void PreOrder(BiTree root) {
    if (root != NULL) {
        Visit(root->data);
        PreOrder(root->LChild);
        PreOrder(root->RChild);
    }
}

//6.2 中序遍历二叉树
void InOrder(BiTree root) {
    if (root != NULL) {
        InOrder(root->LChild);
        Visit(root->data);
        InOrder(root->RChild);
    }
}

//6.3 后序遍历二叉树
void PostOrder(BiTree root) {
    if (root != NULL) {
        PostOrder(root->LChild);
        PostOrder(root->RChild);
        Visit(root->data);
    }
}

//创建二叉树
void CreateBiTree(BiTree *bt) {
    char ch = getchar();
    if (ch == '.' || ch == '\n') {
        *bt = NULL;
    } else {
        *bt = (BiTree)malloc(sizeof(BiTNode));
        if (!*bt) {
            fprintf(stderr, "Memory allocation failed.\n");
            exit(EXIT_FAILURE);
        }
        (*bt)->data = ch;
        CreateBiTree(&((*bt)->LChild));
        CreateBiTree(&((*bt)->RChild));
    }
}

int main(void) {
    BiTree T = NULL;

    printf("请输入先序序列创建二叉树（空节点用.表示）：\n");
    CreateBiTree(&T);

    printf("先序遍历序列为: ");
    PreOrder(T);

    printf("\n中序遍历序列为: ");
    InOrder(T);

    printf("\n后序遍历序列为: ");
    PostOrder(T);

    printf("\n");
    return 0;
}

