for N in 1000 100000 10000000 100000000; do
    for thread in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do 
        echo "Executing exo3 with N ${N} num_thread ${thread} "
        gcc   exo3.c -O3 -DN="$N" -DNUM_THREAD="$thread" -fopenmp -lm -o exo3
        ./exo3 >> "./exo3_results/results.txt"
    done
done