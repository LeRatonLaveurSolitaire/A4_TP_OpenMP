for N in 1000 100000 10000000 100000000; do
    for thread in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do 
        echo "Executing exo2 with N ${N} num_thread ${thread} "
        gcc   exo2.c -O3 -DN="$N" -DNUM_THREAD="$thread" -fopenmp -lm -o exo2
        ./exo2 >> "./exo2_results/result_f2.txt"
    done
done