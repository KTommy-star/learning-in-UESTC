
#define MAXLEN 40
typedef struct {          /*串结构定义*/
    char ch[MAXLEN];
    int len;
}SString;

void createstring(SString *s)
{
	int i,j;
	char c;
	printf("请输入要建立的串的长度:");
	scanf("%d",&j);
	for(i=0; i<j; i++)
	{
		printf("请输入串的第%d个字符:",i+1);
		fflush(stdin);
		scanf("%c",&c);
		s->ch[i] = c;
	}
	s->len = j;
}

void output(SString *s)
{
	int i;
	for (i=0;i<s->len;i++)
		printf("%c   ",s->ch[i]);
	printf("\n");
}