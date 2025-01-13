#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <omp.h>
#include <math.h>
#include <time.h>


#ifndef N
#define N 1000 // table size
#endif

#ifndef NUM_THREAD
#define NUM_THREAD 1// number of threads
#endif

int main() {

    /*
    // Création du tableau de taille N avec des valeurs aléatoires
    */


    float *table = (float *)malloc(N * sizeof(float));

    srand(time(NULL));

    for(int i=0; i<N;i++){
        table[i] = (float)rand() / RAND_MAX;
    }  

    // Initialisation variables
    float sum = 0;
    double time_total = 0;

    // Définition du nombre de threads
    omp_set_num_threads(NUM_THREAD);

    /*
    // Somme avec réduction classique
    */

   double start_time = 0;
   double stop_time = 0;

    for (int i = 0; i < 10; i++) {

        start_time = omp_get_wtime();
        

        #pragma omp parallel for reduction(+:sum)
        for (int i = 0; i < N; i++) {
            sum+=table[i];
        }

        stop_time = omp_get_wtime();
        time_total += stop_time - start_time;

    }

    char msg[128];

    sprintf(msg,"N %d, num thread %d, exec time %fs with reduction \n",N,NUM_THREAD, time_total/10);
    printf("%s", msg);


    /*
    // Somme avec atomicité
    */

    for (int i = 0; i < 10; i++) {

        sum = 0;

        start_time = omp_get_wtime();
        
        #pragma omp parallel for 
        for (int i = 0; i < N; i++) {
            #pragma omp atomic
            sum+=table[i];
        }

        stop_time = omp_get_wtime();
        time_total += stop_time - start_time;

    }

    sprintf(msg,"N %d, num thread %d, exec time %fs with atomicity \n",N,NUM_THREAD, time_total/10);
    printf("%s", msg);

    /*
    // Somme avec section critique
    */

    for (int i = 0; i < 10; i++) {

        sum = 0;

        start_time = omp_get_wtime();
        
        #pragma omp parallel for 
        for (int i = 0; i < N; i++) {
            #pragma omp critical
            sum+=table[i];
        }

        stop_time = omp_get_wtime();
        time_total += stop_time - start_time;

    }

    sprintf(msg,"N %d, num thread %d, exec time %fs with critical section \n",N,NUM_THREAD, time_total/10);
    printf("%s", msg);

    /*
    // Somme avec réduction et séquenceur statique
    */

    for (int i = 0; i < 10; i++) {

        sum = 0;

        start_time = omp_get_wtime();
        
        #pragma omp parallel for reduction(+:sum) schedule(static)
        for (int i = 0; i < N; i++) {
            sum+=table[i];
        }

        stop_time = omp_get_wtime();
        time_total += stop_time - start_time;

    }

    sprintf(msg,"N %d, num thread %d, exec time %fs with scheduler static \n",N,NUM_THREAD, time_total/10);
    printf("%s", msg);

    /*
    // Somme avec réduction et séquenceur dynamique
    */

    for (int i = 0; i < 10; i++) {

        sum = 0;

        start_time = omp_get_wtime();
        
        #pragma omp parallel for reduction(+:sum) schedule(dynamic)
        for (int i = 0; i < N; i++) {
            sum+=table[i];
        }

        stop_time = omp_get_wtime();
        time_total += stop_time - start_time;

    }

    sprintf(msg,"N %d, num thread %d, exec time %fs with scheduler dynamic \n",N,NUM_THREAD, time_total/10);
    printf("%s", msg);

    /*
    // Somme avec réduction et séquenceur "guidé"
    */

    for (int i = 0; i < 10; i++) {

        sum = 0;

        start_time = omp_get_wtime();
        
        #pragma omp parallel for reduction(+:sum) schedule(guided)
        for (int i = 0; i < N; i++) {
            sum+=table[i];
        }

        stop_time = omp_get_wtime();
        time_total += stop_time - start_time;

    }

    sprintf(msg,"N %d, num thread %d, exec time %fs with scheduler guided \n",N,NUM_THREAD, time_total/10);
    printf("%s", msg);

    free(table);

    return 0;
}
