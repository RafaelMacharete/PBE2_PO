/*
 * Abb.h
 *
 *      Author: ronaldo
 */

#ifndef ABB_H_
#define ABB_H_

#define NULL ((void *)0)

struct node{
	int chave;
	struct node *esq;
	struct node *dir;
};

typedef struct node No;



/*==============================================
 * prototipacao das funcoes que implementam uma
 * arvore binaria de busca
 *==============================================*/

/*busca o elemento x na arvore de raiz pt*/
No* buscar(No *pt, int x);

/*insere o elemento x na arvore de raiz pt*/
void inserir(No **pt, int x);

/*remove o elemento x da arvore de raiz pt*/
void remover(No **pt, int x);

/*realiza um percurso na arvore de raiz pt
 * de acordo com o parametro p*/
void visitar(No *pt, int p);


/*imprime a arvore utilizando uma
 * representacao hierarquica*/
void mostrarArvore(No *pt);


#endif /* ABB_H_ */
