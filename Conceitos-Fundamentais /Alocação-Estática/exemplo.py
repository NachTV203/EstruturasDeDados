#include <stdio.h>

int a = 0 ;  // variável global, aloc. estática

void incrementa(void)
{
          int b = 0 ; // variável local, aloc. automática
   static int c = 0 ; // variável local, aloc. estática
   
   printf ("a: %d, b: %d, c: %d\n", a, b, c) ;
   a++ ;
   b++ ;
   c++ ;
}

int main(void)
{
   int i ;
  
   for (i = 0; i < 5; i++)
      incrementa() ;

   return 0 ;
}
A execução desse código gera a seguinte saída:

  a: 0, b: 0, c: 0
  a: 1, b: 0, c: 1
  a: 2, b: 0, c: 2
  a: 3, b: 0, c: 3
  a: 4, b: 0, c: 4
