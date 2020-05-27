#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double f(float x){
  return sin(cos(sin(cos(pow(x,2)))));
}

double simpson_rule(float a, float b, int n){
  if(a > b){
    printf("Incorrect bounds.");
    return -1;
  }
  if(n % 2 != 0){
    printf("n must be an even integer.");
    return -1;
  }
  float h = (b - a) / n;
  float s_1 = 0.0;
  for(int i = 1; i < n; i += 2)
    s_1 += 4 * f(i);
  float s_2 = 0.0;
  for(int i = 2; i < n; i += 2)
    s_2 += 2 * f(i);
  return (h / 3) * (f(a) + f(b) + s_1 + s_2);
}

int main(){
  clock_t start = clock();
  printf("Com 5 Casas decimais:  %.5f\n",simpson_rule(0.0, 3.0, 96.0));
  clock_t end = clock();
  float seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);

  start = clock();
  printf("Com 7 Casas decimais:  %.7f\n",simpson_rule(0.0, 3.0, 310.0));
  end = clock();
  seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);

  start = clock();
  printf("Com 9 Casas decimais:  %.9f\n",simpson_rule(0.0, 3.0, 968.0));
  end = clock();
  seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);
}