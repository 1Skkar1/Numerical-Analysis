#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double f(float x){
  return sin(cos(sin(cos(pow(x,2)))));
}

double trapezoidal_rule(float a, float b, int n){
  float h = (b - a) / n;
  float s = (h / 2) * (f(a) + f(b));
  for(int i = 1; i < n; i++)
    s += f(i);
  return h * s;
}

int main(){
  clock_t start = clock();
  printf("Com 5 Casas decimais:  %.5f\n",trapezoidal_rule(0.0, 3.0, 883.0));
  clock_t end = clock();
  float seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);

  start = clock();
  printf("Com 7 Casas decimais:  %.7f\n",trapezoidal_rule(0.0, 3.0, 8824.0));
  end = clock();
  seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);
  
  start = clock();
  printf("Com 9 Casas decimais:  %.9f\n",trapezoidal_rule(0.0, 3.0, 88236.0));
  end = clock();
  seconds = (float)(end-start)/CLOCKS_PER_SEC;
  printf("Time: %f\n",seconds);
}