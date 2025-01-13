#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <omp.h>

int main(){

    int num_proc = omp_get_num_procs();
    int max_threads = omp_get_max_threads();

    char msg[128];

    sprintf(msg,"This computer has %d cores.\n", num_proc);
    printf(msg);
    sprintf(msg,"OpenMP can execute a maximum of %d treads.\n", max_threads);
    printf(msg);

    return 0;
}