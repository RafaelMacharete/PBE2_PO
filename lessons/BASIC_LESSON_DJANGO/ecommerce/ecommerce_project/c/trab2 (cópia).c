#include <stdio.h>
#include <stdlib.h>
#define CEM 100
#define MAX 10000

typedef struct cel{
	int paragrafo;
	int linha;
	int coluna;
	struct cel * prox;
	
} celu;

typedef struct {
	char word[50];
	struct cel * ini;
	struct cel * fim;
}celula;

int entra(char entrada[MAX])
{
	char c, d;
	int i=0;

	for( ; ; ){
		scanf("%c*c", &c);

		if ((c>= 65 && c <=90) || (c>=97 && c<=122))
		{
			entrada[i] = c;
			i++;
			
		}
		if (c == 45)
		{
			if (entrada[i-1] == '0' || entrada[i-1] == '#' || entrada[i-1] == '*')
			{
				entrada[i] = '#';
				i++;
			}else
			{
				entrada[i] = c;
				i++;
			}
		}
		if (c >= 33 && c <= 63 && c != 45)
		{
			entrada[i] = '#';
			i++;
		}
		if (c == 32)
		{
			entrada[i] = '0';
			i++;
		}
		if (c == '\n')
		{
			if(d == '\n')
			{
				entrada[i] = '*';
				i++;
			}else{
				entrada[i] = '!';
				i++;
			}
		}
		if(c == '@')
			break;
		d = c;
	}
	return i;
}
int palavra(char t[MAX], int i)
{
	int z, pa=0;
	
	for (z = 0; z < i; z++)
	{
		if (t[z] == '0' || t[z] == '!' || t[z] == '#'){
			if (t[z-1] != '0' && t[z-1] != '!' && t[z-1] != '#' && t[z-1] != '*'){
				pa++;
			}
		}

	}

	return pa;
}
int linha(char t[MAX], int i)
{
	int z, li=0;

	for (z = 0; z <i; z++)
	{
		if (t[z] == '!' || t[z] == '*')
			li++;
	}

	return li;
}
int para(char t[MAX], int i)
{
	int z, p=0;

	for (z = 0; z <i; z++)
	{
		if (t[z] == '*')
			p++;
	}

	return p+1;
}
void limp(char t[MAX], int i)
{
	int z;
	for (z = 0; z < i; z++){
		t[z] = '0';
	}
}
void imprimi(int palavras, int linhas, int paragrafo, int indice)
{
	printf("Totais do texto %d:\n", indice);
	printf("  Palavras: %d\n", palavras);
	printf("  Linhas: %d\n", linhas);
	printf("  Paragrafos: %d\n", paragrafo);

}

void preen(celula ha[71], int i)
{
	char s;
	int j, p, soma=1, k;

	for (j = 0; j < i; j++)
	{
		while(1)
		{   
			scanf("%c", &s);
			if(s == '\n')
				break;
			else{
				p = (int)s;
				soma = p+soma;
			}
		}
		k =soma % 71;
		ha[k]->word = ////////PAREI AQKIIIIII ///////// ATRIBUINDO A PALAVRA PARA A HASHING ////////// 
		printf("%d\n", k);


	}

}
int main (void)
{
	char entrada[MAX], enter;
	int pa, i, li, p, m, h=1;
	celula ha[71];

	scanf("%d*c\n", &m);
/*	for (h = 1; h <= m; h++ )
*/
		scanf("%c*c", &enter);
		scanf("%c*c", &enter);
		i = entra(entrada);
		pa = palavra(entrada, i);
		li = linha(entrada, i);
		p = para(entrada, i);

		scanf("%c*c", &enter);
		scanf("%d*c", &m);
		scanf("%c*c", &enter);
		preen(ha, m);
	
		imprimi(pa, li, p, h);
		limp(entrada, i);


	return 0;
}
