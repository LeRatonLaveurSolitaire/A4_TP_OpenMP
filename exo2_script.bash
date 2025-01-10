for N in 1000 100000 10000000 100000000; do
    for thread in 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do 
        echo "Executing exo2 with N ${N} num_thread ${thread}"
        gcc -O3 -DN="$N" -DNUM_THREAD="$thread" exo2.c -o exo2
        ./exo2 >> "result_N${N}_num_thread${thread}.txt"
    done
done