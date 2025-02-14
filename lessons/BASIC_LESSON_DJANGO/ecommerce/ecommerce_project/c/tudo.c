#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct cel {
	int chave;
	struct cel * prox;
//	struct cel * ant; //lista linear, encadeada simplesmente;
	}celula;


void insere_C(int y, celula *p)
{
	celula *nova;
	nova = (celula*) malloc(sizeof(celula));
	nova->chave = y;
	nova->prox = p->prox;
	p->prox = nova;
}

celula *busca_C(int x, celula *lst)
{
	celula *p;
	p = lst->prox;
	while (p != NULL && p->chave != x)
		p = p->prox;
	return p;
}

void remove_C(celula *p)// proximo nó depois de p;
{
	celula *lixo;
	lixo = p->prox;
	p->prox = lixo->prox;
	free(lixo);
}

void busca_remove_C(int x, celula *lst)
{
	celula *p, *q;
	
	p = lst;
	q = lst->prox;
	while(q != NULL && q->chave != x)
	{
		p = q;
		q = q->prox;
	}
	if (q != NULL)
	{
		p->prox = q->prox;
		free(q);
	}
}
 void busca_remove_outros(int x, celula *lst)
 {
 	celula *aux;
	aux = busca_C(x, lst);
	remove_C(aux);
	
 }

void busca_insere_C(int y, int x, celula *lst)
{
	celula *p, *q, *nova;	
	nova = (celula*) malloc(sizeof (celula));
	nova->chave = y;
	p = lst;
	q = lst->prox;
	while(q != NULL && q->chave != x)
	{
		p = q;
		q = q->prox;
	}
	nova->prox = q;
	p->prox = nova;
}

void busca_insere_outros(int y, int x, celula *lst)
{
	celula *aux;
	aux = busca_C(x, lst);
	insere_C(y, aux);
	
}

celula *busca_S(int x, celula *lst)
{
	celula *p;
	
	p=lst;
	while(p != NULL && p->chave != x)
		p = p->prox;
	
	return p;
}

void busca_remove_S(int x, celula **lst)
{
	celula *p, *q;

	p = NULL;
	q = *lst;
	while(q != NULL && q->chave != x)
	{
		p = q;
		q = q->prox;
	}	
	if (q != NULL)
		if (p != NULL)
		{
			p->prox = q->prox;
			free(q);
		}else
		{
			*lst = q->prox;
			free(q);
		}
}

void busca_insere_S(int y, int x, celula **lst)
{
	celula *p, *q, *nova;
	
	nova = (celula*) malloc(sizeof (celula));
	nova->chave = y;
	p = NULL;
	q = *lst;
	while(q != NULL && q->chave != x)
	{
		p = q;
		q = q->prox;
	}
	nova->prox = q;
	if(p != NULL)
		p->prox = nova;
	else
		*lst = nova;
}

void imprimi(celula *lst)
{
	celula *p;
	for (p = lst; p != NULL; p = p->prox)
		printf("%d\n", p->chave);
}

void enfileira_seq(int *f, int F[MAX], int y)
{
	if (*f != MAX)
	{
		F[*f] = y;
		(*f)++;
	}
	else
		printf("FILA CHEIA\n");
}

int desenfilera_seq(int *i, int f, int F[MAX])
{
	int x;
	
	if(*i != f)
	{
		x = F[*i];
		(*i)++;
	}else
	{
		x = 0;
		printf("FILA VAZIA\n");
	}
	
	return x;
}

void enfileira_seq_2(int *i, int *f, int F[MAX], int y)
{
	if(*f != *i){
		if(*f == MAX){
			*i = 0;
			*f = 0;
		}
		F[*f] = y;
		*f = (*f+1) % MAX;
	}else
		printf("FILA CHEIA\n");
}

int desenfileira_seq_2(int *i, int *f, int F[MAX])
{
	int r;
	
	r = 0;
	if(*i != 0)
	{
		r = F[*f];
		*i = (*i + 1) % MAX;
		if(*i == *f)
		{
			*i = 0;
			*f = MAX;
		}
	}else
		printf("FILA VAZIA\n");
	
	return r;
}

 void impri(int i, int f, int F[MAX])
 {
  	for( ; i < f; i++)
 		printf("%d\n", F[i]);
 }
 
 void enfileira_enc_C(celula *i, celula **f, int y)
 {
 	celula *nova;
 	
 	nova = (celula *) malloc (sizeof (celula));
 	nova->chave = y;
 	nova->prox = NULL;
 	(*f)->prox = nova;
 	*f = nova;
 }
 
 int desenfileira_enc_C(celula *i, celula **f)
 {
 	int x;
 	celula *p;
 	
 	x = 0;
 	p = i->prox;
 	if(p != NULL)
 	{
 		x = p->chave;
 		i->prox = p->prox;
 		free(p);
 		if(i->prox == NULL)
 			*f = i;
 	}
 	else
 		printf("FILA VAZIA\n");
 	return x;
 }


int main (void) // MAIN DE UMA FILA
{
	/*int i, f, F[MAX], y;
	
	i = 0;
	f = 0;
	y = 13;
	enfileira_seq(&f, F, y);
	y = 23;
	enfileira_seq(&f, F, y);
	desenfilera_seq(&i, f, F);
	impri(i, f, F);*/
	
	celula *i, *f;
	int y;
	
	i = (celula *) malloc (sizeof (celula));
	f = i;
	y=13;
	enfileira_enc_C(i, &f, y);
	y=23;
	enfileira_enc_C(i, &f, y);
	imprimi(i->prox);
	
	
}


/*int main (void) //MAIN DE UMA LISTA
{
	celula *t, *c;
	int n, x, y;
//	t = (celula*) malloc(sizeof (celula));
//	c = (celula*) malloc(sizeof (celula));
//	t->prox = c;
//	t->ant = NULL;
//	c->ant = t;
//	c->prox = NULL;
//	t->prox = NULL;
	t = NULL;
	n = 13;
//	/*insere_C(n, &t);
//	n = 78;
//	insere_C(n, &t);
//	n = 45;
//	insere_C(n, t);
//	n = 23;
//	insere_C(n, t);
//	scanf("%d", &n);
//	while (n != 0)
//	{
//		depois(n, t);
//		scanf("%d", &n);
//	}
	x = 45;
//	busca_remove_S(x, &t);
//	busca_remove_C(x, t);
//	busca_remove_outros(x, t);
	y = 67;
//	busca_insere_S(y, x, &t);
//	busca_insere_outros(y, x, t);
//	busca_insere_C(y, x, t);
//	busca_insere_antes(y,x,c);
	imprimi(t);



	
	return 0;
}*/
