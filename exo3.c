#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <omp.h>
#include <math.h>


#define table_type float32

#ifndef N
#define N 1000 // table size
#endif

#ifndef NUM_THREAD
#define NUM_THREAD 1// number of threads
#endif

int main() {

    table_type *table = (table_type)malloc(N * sizeof(table_type));

    srand(time(NULL));

    for(int i=0; i<N;i++){
        table[i] = (table_type)rand() / RAND_MAX;
    }  
    table_type sum = 0;

    omp_set_num_threads(NUM_THREAD);

    double start_time = omp_get_wtime();
    
    #pragma omp parallel for
    for (int i = 0; i < SIZE; i++) {
        sum+=table[i];
    }

    double stop_time = omp_get_wtime();

    free(table);

    char msg[128];

    sprintf(msg,"N %d, num thread %d, exec time %fs",N,NUM_THREAD, stop_time - start_time);
    printf(msg);

    return 0;
}
