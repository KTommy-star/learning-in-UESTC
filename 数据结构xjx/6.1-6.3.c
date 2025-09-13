#include <stdio.h>
#include <stdlib.h>  // malloc �� free �ı�׼ͷ�ļ�

typedef char DataType;

typedef struct Node {
    DataType data;
    struct Node *LChild;
    struct Node *RChild;
} BiTNode, *BiTree;

void Visit(const char ch) {
    printf("%c  ", ch);
}

//6.1 �������������
void PreOrder(BiTree root) {
    if (root != NULL) {
        Visit(root->data);
        PreOrder(root->LChild);
        PreOrder(root->RChild);
    }
}

//6.2 �������������
void InOrder(BiTree root) {
    if (root != NULL) {
        InOrder(root->LChild);
        Visit(root->data);
        InOrder(root->RChild);
    }
}

//6.3 �������������
void PostOrder(BiTree root) {
    if (root != NULL) {
        PostOrder(root->LChild);
        PostOrder(root->RChild);
        Visit(root->data);
    }
}

//����������
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

    printf("�������������д������������սڵ���.��ʾ����\n");
    CreateBiTree(&T);

    printf("�����������Ϊ: ");
    PreOrder(T);

    printf("\n�����������Ϊ: ");
    InOrder(T);

    printf("\n�����������Ϊ: ");
    PostOrder(T);

    printf("\n");
    return 0;
}

