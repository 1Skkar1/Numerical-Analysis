#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double f(float x){
  return sin(cos(sin(cos(pow(x,2)))));
}

double rectangle_rule(float a, float b, float n){
  int j = b - a;
  float h = j / n;
  float s_1 = 0.0;
  for(int i = 1; i < n; i++){
    s_1 += f(i - 1);
  }
  return s_1 * h;
}

int main(){
  clock_t start = clock();
  printf("Com 5 Casas decimais:  %.5f\n",rectangle_rule(0.0, 3.0, 123570.0));
  clock_t end = clock();
  float seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);

  start = clock();
  printf("Com 7 Casas decimais:  %.7f\n",rectangle_rule(0.0, 3.0, 12500000.0));
  end = clock();
  seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);

  start = clock();
  printf("Com 9 Casas decimais:  %.9f\n",rectangle_rule(0.0, 3.0, 1250000000.0));
  end = clock();
  seconds = (float)(end - start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);
}