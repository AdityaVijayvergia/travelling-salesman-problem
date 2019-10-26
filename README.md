# travelling-salesman-problem
Implemented using genetic algorithm.

I tried to decrease randomness in the mutation function. I selected the first city c1 randomly from any parent. For next city c2, I selected a city from the cities that the 2 parents had after c1 based on which had lesser distance. 
Say parent 1 had c3 and parent 2 had c4. I selected c3 if dist(c1, c3) < dist(c1, c4). And then applied some random swaps. 
This resulted in a lot of speed up and more accurate solutions even for less population size.

The results are shown below.
step 1:
![1](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/1.PNG)
step 2:
![2](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/2.PNG)
step 3:
![3](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/3.PNG)
step 4:
![4](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/4.PNG)
step 5:
![5](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/5.PNG)
step 6:
![6](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/6.PNG)
step 7:
![7](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/7.PNG)
step 8:
![8](https://github.com/AdityaVijayvergia/travelling-salesman-problem/blob/master/tsp%20images/8.PNG)





