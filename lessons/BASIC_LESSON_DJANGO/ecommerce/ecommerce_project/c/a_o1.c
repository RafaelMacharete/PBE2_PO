#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 1pt

int _soma = 0;

typedef struct ar {
	int chave;
        int indic;
	struct ar * esq;
	struct ar * dir; //folha da árvore;
	}arvore;

void insereFolha(int y, arvore **tree)
{
        if (*tree == NULL){
		*tree = (arvore*) malloc(sizeof(arvore));
		(*tree)->chave = y;
                (*tree)->dir = NULL;
                (*tree)->esq = NULL;
                
	}
        else
        {
            if((*tree)->chave < y)
            {
                insereFolha(y, &(*tree)->dir);
            }
            if((*tree)->chave > y)
            {
                insereFolha(y, &(*tree)->esq);
                
                
            } 
        }
}
void pre_ordem(arvore *lst)
{
	arvore *p;
        p = lst;
	if (p != NULL)
        {
            printf("%d  ", p->chave);
            pre_ordem(p->esq);
            pre_ordem(p->dir);
        }
}

int quantidadeFolhas(arvore *p)
{
	if(p == NULL)
		return 0;
	if(p->esq == NULL && p->dir == NULL)
		return 1;
	return quantidadeFolhas(p->esq) + quantidadeFolhas(p->dir);
}

void pos_ordem (arvore *lst)
{
	arvore *p;
	p = lst;
	if(p != NULL)
	{
		pos_ordem(p->esq);
		pos_ordem(p->dir);
		printf("%d  ", p->chave);
	}

}

void em_ordem (arvore *lst)
{
	arvore *p;
	p = lst;
	if(p != NULL)
	{
		em_ordem(p->esq);
		printf("%d  ", p->chave);
		em_ordem(p->dir);
	}
}

int somaFolhas(arvore *s){
    arvore *p;
    p = s;
    if (p != NULL)
    {
        _soma = _soma + p->chave;
        somaFolhas(p->esq);
        somaFolhas(p->dir);
    }
    return _soma;
}

int quntasArv(arvore *p)
{
	if (p == NULL)
		return 0;
	else
		return 1 + quntasArv(p->esq) + quntasArv(p->dir);
}


int main (void) // MAIN DE UMA ÁRVORE
{
	arvore *bin;
        bin = NULL;
        
	int y, i;

	/*srand( (unsigned)time(NULL) );

	for ( i = 1; i <= 10; i++)
	{
		insereFolha(rand(), &bin);
	}*/


        insereFolha(7, &bin);
        insereFolha(3, &bin);
        insereFolha(10, &bin);
        insereFolha(1, &bin);
        insereFolha(6, &bin);
        insereFolha(14, &bin);
        insereFolha(4, &bin);
        //insereFolha(7, &bin);
        insereFolha(13, &bin);

        pre_ordem(bin);
        printf("\n");
        em_ordem(bin);
        printf("\n");
        pos_ordem(bin);
        //y = somaFolhas(bin);
        printf("\n");
        //printf("%d\n", quantidadeFolhas(bin));
        //printf("%d\n", quntasArv(bin));
        free(bin);
        return;



        /* -------------- REMOVER ------------
   */
        
}