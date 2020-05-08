#include <stdio.h>

void cubicSpline(int n, double xi[], double fxi[]);
double Newton(int n, double x[], double diffTable[][10]);
void splitDiffTable(int n, double x[], double fx[], double diffTable[][10]);
void printDiffTable(int n, double x[], double diffTable[][10]);

int main() {
    int option, nPoints;
    double xb[] = {-4,-2.667,-1.333,0,1.333,2.667,4};
    double fxb[] = {0.943,0.884,0.698,0.368,0.698,0.884,0.943};
    double xd[] = {-4,-2.857,-1.714,-0.571,0.571,1.714,2.857,4};
    double fxd[] = {0.943,0.897,0.776,0.470,0.470,0.776,0.897,0.943};
    double diffTable[10][10];

    printf("Exercise to be solved:\n1) Exercise 2.b) [nPoints = 7]\n2) Exercise 2.d) [nPoints = 8]\n");
    scanf("%d", &option);
    if (option == 1) {      // Exercise 2.b)
        int nPoints = 7;
        splitDiffTable(nPoints, xb, fxb, diffTable);
        printDiffTable(nPoints, xb, diffTable);
        Newton(nPoints, xb, diffTable);
        cubicSpline(nPoints, xb, fxb);
        }
    else if (option == 2) { // Exercise 2.d)
        int nPoints = 8;
        splitDiffTable(nPoints, xd, fxd, diffTable);
        printDiffTable(nPoints, xd, diffTable);
        Newton(nPoints, xd, diffTable);
        cubicSpline(nPoints, xd, fxd);
    }
    return 0;
}

void cubicSpline(int n, double xi[], double fxi[]) {
    n--;
    double h[n], A[n], l[n+1], u[n+1], z[n+1], c[n+1], b[n], d[n];

    for(int i = 0; i < n; i++)
        h[i] = xi[i+1] - xi[i];
    
    for(int i = 1; i < n; i++)
        A[i] = 3 * (fxi[i+1] - fxi[i]) / h[i] - 3 * (fxi[i] - fxi[i-1]) / h[i-1];
    
    l[0] = 1;
    u[0] = 0;
    z[0] = 0;

    for (int i = 1; i < n; i++) {
        l[i] = 2 * (xi[i+1] - xi[i-1]) - h[i-1] * u[i-1];
        u[i] = h[i] / l[i];
        z[i] = (A[i] - h[i-1] * z[i-1]) / l[i];
    }

    l[n] = 1;
    z[n] = 0;
    c[n] = 0;

    for (int j = n - 1; j >= 0; j--) {
        c[j] = z[j] - u[j] * c[j+1];
        b[j] = (fxi[j+1] - fxi[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3;
        d[j] = (c[j+1] - c[j]) / (3 * h[j]);
    }

    printf("\nCubic Spline:\n");
    printf("%2s %8s %8s %8s %8s\n", "i", "x^3", "x^2", "x", "fxi");
    for (int i = 0; i < n; i++){
        printf("%2d %8.3f %8.3f %8.3f %8.3f\n", i, d[i], c[i], b[i], fxi[i]);
    }
}

double Newton(int n, double x[], double diffTable[][10]){
    printf("P%d(x) = %f + ", n-1, diffTable[0][0]);
    for(int i = 1; i < n; i++) {
        printf("%f * ", diffTable[0][i]);
        for(int j = 0; j < i; j++) {
            if(j != i - 1)
                printf("(x - %f) * ", x[j]);
            else
                printf("(x - %f) ", x[j]);
        }
        if(i != n - 1)
            printf("+ ");
        printf("\n\t");
    }
    printf("\n");
}

void splitDiffTable(int n, double x[], double fx[], double diffTable[][10]) {
    for(int i = 0; i < n; i++) {
        diffTable[i][0] = fx[i];
    }
    for(int i = 1; i < n; i++) {
        for(int j = 0; j < n - i; j++) {
            diffTable[j][i] = (diffTable[j][i-1] - diffTable[j+1][i-1]) / (x[j] - x[i+j]);
        }
    }
}

void printDiffTable(int n, double x[], double diffTable[][10]) {
    printf("\nPolinomial Interpolation:\n");
    for(int i = 0; i < n; i++) {
        printf("%8.3f", x[i]);
        for(int j = 0; j < n - i; j++) {
            printf("%8.3f", diffTable[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}