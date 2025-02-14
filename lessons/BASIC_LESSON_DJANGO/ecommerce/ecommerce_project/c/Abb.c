/***************************************************
*                                                  *
* Nome completo Mariany Morais Silva               *
* RGA 2014.0743.017 - 3                            *
* Implementação 1                                  *
* Disciplina: Estruturas de Dados e Programação I  *
* Professor: Ronaldo Fiorilo                       *
*                                                  *
***************************************************/

#include "Abb.h"
#include <malloc.h>
#include <string.h>

/*==============================================
 * implementacao das funcoes prototipadas no
 * arquivo Abb.h e de funcoes auxiliares para
 * a manutencao de uma arvore binaria de busca
 *==============================================*/


/* prototipacao das funcoes auxiliares */
void mostraSubArvore(No *pt, char *separator, No* raiz);
void pre_ordem(No *p);
void pos_ordem(No *p);
void em_ordem(No *p);
No *MaiorChaveEsq(No **tree);

/**
 * busca a chave x na arvore de raiz pt
 *  - devolve um ponteiro para o no que possui a chave
 * ou NULL caso a chave nao exista
 */
No* buscar(No *pt, int x)
{
	if(x == pt->chave)
    return pt;
  if((pt->chave) < x)
    buscar(pt->esq, x);
  if((pt->chave) > x)
    buscar(pt->dir, x);
	return NULL;
}



/**
 * insere a chave x na arvore de raiz pt
 */
void inserir(No **pt, int x)
{
  printf("%d\n", x);
  if (*pt == NULL)
  {
	 *pt = (No*) malloc(sizeof(No));
    (*pt)->chave = x;
    (*pt)->dir = NULL;
    (*pt)->esq = NULL;
                
	}
  else
  {
    if((*pt)->chave < x)
    {
      inserir(&(*pt)->dir, x);

    }
    if((*pt)->chave > x)
    {
      inserir(&(*pt)->esq, x);
                
    } 
  }   
}


/**
 * remove a chave x da arvore de raiz pt
 */
void remover(No **pt, int x)
{
  printf("%d\n", x);
  No *aux = *pt;
  if(*pt == NULL)
  {
    return;
  }
  if( x < (*pt)->chave){
    remover(&(*pt)->esq, x);
  }
  else
  {
    if(x > (*pt)-> chave){
      remover(&(*pt)->dir, x);
    }
    else
    {
      if (((*pt)->esq == NULL) && ((*pt)->dir == NULL))
      {
        free(aux);
        (*pt) = NULL;
      }
      else
      {
        if ((*pt)->esq == NULL)
        {
          (*pt) = (*pt)->dir;
          aux->dir = NULL;
          free(aux);
          pt = NULL;
        }
        else
        {
          aux = MaiorChaveEsq(&(*pt)->esq);
          aux->esq = (*pt)->esq;
          aux->dir = (*pt)->dir;
          (*pt)->esq = NULL;
          (*pt)->dir = NULL;
          free((*pt));
          *pt = aux;
          aux = NULL;
        }
      }
    }
  }
}


/**
 * realiza um percurso na arvore. O percurso
 * a ser realizado é passado por parâmetro:
 * -1 = pre-ordem
 *  0 = ordem simetrica
 *  1 = pos-ordem
 * Visitar um no, nesses metodos, equivale a imprimir
 * o valor de sua chave. Faca a impressao de todas as
 * chaves em uma mesma linha, passando para uma nova
 * linha somente apos imprimir todas as chaves.
 */
void visitar(No *pt, int p)
{

  if (p == -1)
    pre_ordem(pt);
  else if (p == 0)
    em_ordem(pt);
  else if (p == 1)
    pos_ordem(pt);
  printf("\n");
}


/**
 * Mostra o estado atual da arvore
 *
 * método baseado no codigo de Leonardo Zandoná - 2006/2
 */

void mostrarArvore(No *pt) {
   if (pt == NULL)
   {
      printf("Árvore vazia!\n");
   }
   else
   {
       char separator[] = "  |__";
       printf("%d(RAIZ)\n", pt->chave);
       mostraSubArvore(pt->esq,  separator, pt);
       mostraSubArvore(pt->dir, separator, pt);
   }
}



/**
 * Metodos auxiliares:
 * aqui voce pode criar metodos para auxiliar nas
 * operacoes acima.
 */


void mostraSubArvore(No *pt, char *separator, No* pai) {
    if (pt != NULL) {
    	char newsep[1000] = "     ";
        if (pt == pai->esq) {
            printf("%s%d (ESQ)\n", separator, pt->chave);
        }else{
            printf("%s%d (DIR)\n", separator, pt->chave);
        }
        /*concatena no final*/
        strcat(newsep, separator);
        mostraSubArvore(pt->esq, newsep, pt);
        mostraSubArvore(pt->dir, newsep, pt);
    }
}

void pre_ordem(No *p)
{
  if(p != NULL)
  {
    printf("%d  ", p->chave);
    pre_ordem(p->esq);
    pre_ordem(p->dir);
  }
 
}

void pos_ordem (No *p)
{
  if(p != NULL)
  {
    pos_ordem(p->esq);
    pos_ordem(p->dir);
    printf("%d  ", p->chave);
  }

}

void em_ordem (No *p)
{
  if(p != NULL)
  {
    em_ordem(p->esq);
    printf("%d  ", p->chave);
    em_ordem(p->dir);
  }
}

No *MaiorChaveEsq(No **tree)
{
  No *aux = *tree;

  if((*tree)->dir == NULL)
  {
      *tree = (*tree)->esq;
    return aux;
  }
  else if((*tree)->dir->dir = NULL)
  {
    aux = (*tree)->dir;
    printf("%d\n", aux->chave);
    (*tree)->dir = aux->esq;
    return aux;
  }else
    return MaiorChaveEsq(&(*tree)->dir);
}