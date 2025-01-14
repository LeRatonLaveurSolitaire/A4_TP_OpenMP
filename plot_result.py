import matplotlib.pyplot as plt
import numpy as np

def pars_exo2(file_name:str =None)->list :
    
    outout_list = []
    with open(file_name,'r') as file:
        for line in file.readlines():
            words = line.split(" ")
            to_keep = []
            for word in words :
                if ',' in word:
                    if 's' in word:
                        to_keep.append(float(word[:-2]))
                    else:
                        to_keep.append(int(word[:-1]))
            outout_list.append(to_keep)
    
    return outout_list

def pars_exo3(file_name:str =None)->list :
    
    outout_list = []
    with open(file_name,'r') as file:
        for line in file.readlines():
            words = line.split(" ")
            to_keep = []
            for word in words :
                if ',' in word:
                    to_keep.append(int(word[:-1]))
                elif word[-1] == 's' :
                        to_keep.append(float(word[:-1]))
            to_keep.append(' '.join(words[9:-1]))
            outout_list.append(to_keep)
    
    return outout_list

def plot_time_N(input_list:list = None,title:str = None,exo3:bool = False) ->None:
    N = []
    dico_N = {}

    for element in input_list:
        if element[0] not in N:
            N.append(element[0])

    for i,n in enumerate(N):      
        dico_N[n] = i

    if exo3 ==False :

        time_threads = [[0 for i in range(len(N))] for j in range(len(input_list)//len(N))]
        for element in input_list:
            time_threads[element[1] - 1][dico_N[element[0]]] = element[2]

        threads_to_print = [1,2,4,8,12,16]
        plt.figure(figsize=(10, 6))

        for i in threads_to_print:
            plt.loglog(N, time_threads[i-1], marker='o', linestyle='-', label=f'{i} Threads')

        plt.title(title)
        plt.xlabel('N')
        plt.ylabel('Time')
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.legend()

        plt.tight_layout()
        plt.savefig(title.replace(' ', '_')+'.pdf')
        #plt.show()
    else:
        

        opti_name = []
        dico_opti_name ={}
        for element in input_list:
            if element[-1] not in opti_name:
                opti_name.append(element[-1])
                dico_opti_name[element[-1]] = opti_name.index(element[-1])

        time_opti = [[0 for i in range(len(N))] for j in range(len(opti_name))]

        for element in input_list:
            if element[1] == 8 :
                time_opti[dico_opti_name[element[-1]]][dico_N[element[0]]] = element[2]

        plt.figure(figsize=(10, 6))

        for i in range(len(time_opti)):
            plt.loglog(N, time_opti[i], marker='o', linestyle='-', label=f'{opti_name[i]}')

        plt.title(title)
        plt.xlabel('N')
        plt.ylabel('Time')
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.legend()

        plt.tight_layout()
        plt.savefig(title.replace(' ', '_')+'.pdf')
        #plt.show()



def plot_perf_N(input_list:list = None,title:str = None,n_in:int=None,exo3:bool = False) ->None:
    
    
    N = []
    dico_N = {}
    threads = []
    for element in input_list:
        if element[0] not in N:
            N.append(element[0])
        if element[1] not in threads:
            threads.append(element[1])

    for i,n in enumerate(N):      
        dico_N[n] = i

    if exo3 ==False :
        
        time_threads = [[0 for i in range(len(N))] for j in range(len(input_list)//len(N))]
        for element in input_list:
            time_threads[element[1] - 1][dico_N[element[0]]] = element[2]

        accel = [0 for i in threads]
        for element in input_list:
            if element[0] == n_in:
                accel[element[1] - 1] = element[2]
        t_0 = accel[0]
        for i in range(len(accel)):
            accel[i] = (t_0 - accel[i]) / t_0 * 100

        plt.figure(figsize=(10, 6))

        
        plt.bar(threads[1:],accel[1:])
        plt.title(title)
        plt.xlabel('Number of thread')
        plt.ylabel("Acceleration (%)")
        plt.grid(True, which="both", ls="-", alpha=0.2)


        plt.tight_layout()
        plt.savefig(title.replace(' ', '_')+'.pdf')
        plt.show()
    else:
        opti_name = []
        dico_opti_name ={}
        for element in input_list:
            if element[-1] not in opti_name:
                opti_name.append(element[-1])
                dico_opti_name[element[-1]] = opti_name.index(element[-1])

        opti_thread_time = [[0 for i in range(len(threads))] for j in range(len(opti_name))]
        for element in input_list:
            if element[0] == n_in:
                opti_idx = dico_opti_name[element[-1]]
                thread_idx = element[1] - 1
                opti_thread_time[opti_idx][thread_idx] = element[2]

        opti_thread_accel = [[0 for i in range(len(threads))] for j in range(len(opti_name))]
        
        for opti in range(len(opti_thread_time)):
            t_0 = opti_thread_time[opti][0]
            for i in range(len(threads)):
                opti_thread_accel[opti][i]= (t_0 - opti_thread_time[opti][i])/ t_0 * 100

        
        plt.figure(figsize=(10, 6))

        width = 1/(len(opti_name) + 1) 
        offset_opti = [i/len(opti_name) - 0.5 for i in range(len(opti_name))]
        for i in range(len(opti_name)):
            
            plt.bar(np.array(threads[1:]) + offset_opti[i],opti_thread_accel[i][1:],width=width,label=opti_name[i])
        plt.title(title)
        plt.xlabel('Number of thread')
        plt.ylabel("Acceleration (%)")
        plt.legend()
        plt.tight_layout()
        plt.savefig(title.replace(' ', '_')+'.pdf')
        #plt.show()



def main() -> None:
    results_f1 = pars_exo2("./exo2_results/result_f1.txt")
    results_f2 = pars_exo2("./exo2_results/result_f2.txt")
    results_exo3 = pars_exo3("./exo3_results/results.txt")
    # plot_time_N(results_f1,'Time vs N for f1')
    # plot_time_N(results_f2,'Time vs N for f2')
    # plot_time_N(results_exo3,title='Time vs N for 8 threads' ,exo3=True)

    # plot_perf_N(results_f1,'Acceleration exo2 f1 for N 1000',n_in=1000)
    # plot_perf_N(results_f1,'Acceleration exo2 f1 for N 10000000',n_in=100000)
    # plot_perf_N(results_f1,'Acceleration exo2 f1 for N 10000000',n_in=10000000)
    # plot_perf_N(results_f1,'Acceleration exo2 f1 for N 100000000',n_in=100000000)
    plot_perf_N(results_f2,'Acceleration exo2 f2 for N 1000',n_in=1000)
    # plot_perf_N(results_f2,'Acceleration exo2 f2 for N 10000000',n_in=100000)
    # plot_perf_N(results_f2,'Acceleration exo2 f2 for N 10000000',n_in=10000000)
    # plot_perf_N(results_f2,'Acceleration exo2 f2 for N 100000000',n_in=100000000)
    # plot_perf_N(results_exo3,'Acceleration exo3 for N 1000',n_in=1000,exo3=True)
    # plot_perf_N(results_exo3,'Acceleration exo3 for N 100000',n_in=100000,exo3=True)
    # plot_perf_N(results_exo3,'Acceleration exo3 for N 10000000',n_in=10000000,exo3=True)
    # plot_perf_N(results_exo3,'Acceleration exo3 for N 100000000',n_in=100000000,exo3=True)


if __name__ == "__main__":
    main()



