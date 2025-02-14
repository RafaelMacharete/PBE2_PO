/*
 ============================================================================
 Name        : ArvBinBusca.c
 Author      : Ronaldo Fiorilo
 Version     :
 Copyright   : 
 Description : Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Abb.h"

int main(void)
{

    char comando[10];
    int chave, i;
    No *tree, *resp;
    srand( (unsigned)time(NULL) );

    /* arvore inicialmente vazia */
    tree = NULL;


    scanf("%s", comando);

    /* inicio do laco principal*/
    while(strcmp(comando, "sair")!=0)
    {

        if(strcmp(comando, "imprimir")==0)
        {
            mostrarArvore(tree);
        }
        else
        {
            scanf("%d", &chave);
            if(strcmp(comando, "inserir")==0)
            {


                    for ( i = 1; i <= 100; i++)
                    {
                    inserir(&tree, rand()%1000);}
                
            }
            else
            {
                if(strcmp(comando, "remover")==0)
                {
                    for ( i = 1; i <= 100; i++)
                    {
                    remover(&tree, rand()%1000);}
                }
                else
                {
                    if(strcmp(comando, "buscar")==0)
                    {
                        resp = buscar(tree, chave);

                        /* verifica se a busca retornou um no valido */
                        if(resp == NULL)
                            printf("Chave nao encontrada!\n");
                        else
                            printf("Chave encontrada!\n");
                    }
                    else
                    {
                        if(strcmp(comando, "visitar")==0)
                        {
                            visitar(tree, chave);
                        }
                    }
                }
            }
        }
        scanf("%s", comando);
    }

    return EXIT_SUCCESS;
}
