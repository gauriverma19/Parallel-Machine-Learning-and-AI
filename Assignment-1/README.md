# Assignment-1 

1. Show the node list, time limit, state, and CPU numbers of the “debug” partition.             

2. Tell the TA the meaning of the following code of the job states and what you should do if it happens: PD, R, S, CG               

3. Show all pending jobs on the “debug” partition.          

4. Show how to use srun to request one node and 4 tasks for 30 minutes with 16GB memory on the “express” partition.       

5. Use squeue to show the job information in the question 4, including the job_id and the node name which the job is working, and the job state.   

6. Show how to cancel the job in the question 4.            

7. In your $HOME, create a new directory: tmp7105; then create a sub-directory: homework1                                                    

8. Show how to transfer (any) one file in your local machine to the cluster to your subdirectory you created in question 7.      

9. Check available modules and loaded modules.             

10. Load modules of anaconda3/3.7 and openmpi/3.1.2                   

11. On this compute node, implement the following operations:        

Compile omp_hello.c with gcc compiler with OpenMP flag.
OpenMP parallel run the executable on 4 threads
12. On this compute node, implement the following operations:         

Compile mpi_hello.c with MPI compiler wrapper.
MPI parallel run the executable on 4 processors.

13. Copy the tarball hpl-2.3.tar.gz from /scratch/flyingsky2007 to your home directory; then extract the tarball using the command tar and flags.       

14. Write a sbatch script according to the following requirements:      

Note: write this script when the TA interviews you. You can write it in the cluster in vi or in your local machine then transfer it to the cluster. 

* define the names of the job, output file and error file as hw1, hw1.out and hw1.err.
* request one compute node from the “express” partition;
* request 8 tasks per node;
* request 16GB memory;
* define your work directory, and go to this work directory;
* set the number of threads to 4
* command to run your compiled OpenMP executable omp_hello.
* load anaconda3/3.7 module;
* command to run a python file (any).
