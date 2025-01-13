#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <omp.h>
#include <math.h>
#include <time.h>



#ifndef N
#define N 100000000 // table size
#endif

#ifndef NUM_THREAD
#define NUM_THREAD 1// number of threads
#endif

float f1(float x){
    return 2.17 * x;
} 

float f2(float x){
    return 2.17 * log(x) * cos(x);
} 

int main() {


    float *table = (float *)malloc(N * sizeof(float));

    srand(time(NULL));

    for(int i=0; i<N;i++){
        table[i] = (float)rand() / RAND_MAX;
    }  

    //omp_set_num_threads(NUM_THREAD);

    double time_total = 0;
    for(int i = 0; i<10;i++){
        double start_time = omp_get_wtime();
        
        //#pragma omp parallel for
        for (int i = 0; i < N; i++) {
            table[i]=f1(table[i]);
        }

        double stop_time = omp_get_wtime();
        time_total+= stop_time - start_time;
    }
    free(table);

    char msg[128];

    sprintf(msg,"N %d, num thread %d, exec time %fs, function f1, no openmp \n",N,NUM_THREAD, time_total/10);
    printf("%s", msg);

    return 0;
}



