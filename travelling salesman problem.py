import turtle
import numpy as np
import random
import time


def draw_pts(ttl, city_loc):
	ttl.speed(0)
	ttl.penup()
	for i,j in city_loc:
		ttl.goto(i,j)
		ttl.dot()

def draw(ttl,order, city_loc):
	ttl.clear()
	order = order.astype(int)
	draw_pts(ttl, city_loc)
	ttl.penup()
	ttl.goto(city_loc[int(order[0])])
	ttl.pendown()
	for i in order:
		x, y = city_loc[i]
		ttl.goto(x,y)
	time.sleep(2)


def dist_fun(a, b):
	return (a[0]-b[0])**2 + (a[1]-b[1])**2

def init_parent(population, cities):
	parents = np.zeros((population, cities))
	for i in range(population):
		for _ in range(cities):
			a = np.arange(cities)
			p1 = random.randint(0,cities-1)
			p2 = random.randint(0,cities-1)
			a[p1], a[p2] = a[p2], a[p1]
		parents[i] = a
	return parents.astype(int)


def compute_fitness(parents, dist_matrix):
	fitness = np.zeros((parents.shape[0],1))
	for i in range(parents.shape[0]):
		for j in range(parents.shape[1]-1):
			fitness[i] = fitness[i] + dist_matrix[int(parents[i, j]), int(parents[i, j+1])]
	return fitness


def get_parent_idx(fitness, no_of_parents):
	fitness = (np.sum(fitness) / fitness).astype(int)
	fitness = (fitness / np.sum(fitness)) * 100
	new_parents_idx = []
	i=0
	while i < no_of_parents:
		x = random.randint(0, 99)
		idx = 0
		while x>0:
			x = x - fitness[idx]
			idx = idx + 1
		idx = idx - 1
		if idx in new_parents_idx:
			continue
		new_parents_idx.append(idx)
		i = i + 1
	new_parents_idx = np.asarray(new_parents_idx)
	return new_parents_idx


def generate_children_f1(parents, fitness, no_of_parents, dist_matrix):
	children = []
	#print('parents ={}'.format(parents))
	for _ in range(parents.shape[0]):
		a, b = get_parent_idx(fitness, no_of_parents)
		p = []
		p.append(parents[a])
		p.append(parents[b])
		p = np.asarray(p)
		child = np.zeros((parents.shape[1]), dtype =int) - 1 

		first = random.randint(0,1)
		child[0] = p[first,0]
		
		m0 = {}
		m1 = {}
		for i in range(p.shape[1]):
			m0[p[0,i]] = i
			m1[p[1,i]] = i
		
		i = 0
		l=child.shape[0]
		taken = [0]*l
		taken[child[0]] = 1
		while(i<l-1):
			n=-1
			
			n0 = p[0,(m0[child[i]]+1)%l]
			n1 = p[1,(m1[child[i]]+1)%l]
			
			if taken[n0]==0 and taken[n1]==0:				
				d0 = dist_matrix[child[i],n0]
				d1 = dist_matrix[child[i],n1]
				if d0 < d1:
					n = n0
				else:
					n = n1

			if taken[n0]:
				n = n1
			if taken[n1]:
				n = n0
			if taken[n0] and taken[n1]:
				n = taken.index(0)
			taken[n] = 1
			child[i+1] = n
			i = i + 1
		children.append(child)
	#print('children={},{}'.format(len(children), children))
	return np.array(children)


def mutate(children, cities):
	for i in range(children.shape[0]):
		no = random.randint(0,cities//4)
		for _ in range(no):
			p1 = random.randint(0,3)
			p2 = random.randint(0,3)

			children[i,p1], children[i,p2] = children[i,p2], children[i,p1]

	return children

if __name__ == '__main__':
	
	ttl = turtle.Turtle()
	ttl.speed(1)
	cities = 20
	no_of_parents = 2
	population_size = 80

	city_loc = (np.random.rand(cities, 2)*600 - 300).astype(int)

	dists = np.zeros((cities, cities))
	for i in range(cities):
		for j in range(cities):
			dists[i, j] = dist_fun(city_loc[i], city_loc[j])
			dists[j, i] = dists[i, j]
	parents = init_parent(population_size, cities)
	fitness = compute_fitness(parents, dists)

	best_idx = np.argmin(fitness)
	best_fitness = [fitness[best_idx]]
	record = {0:best_fitness[0][0]}
	order = parents[best_idx]
	orders_drawn = []
	orders_drawn.append(order)

	draw(ttl, parents[best_idx], city_loc)

	for i in range(500):
		print('-------------------------------------------------------------------------------------------------')
		print(i)

		fitness = compute_fitness(parents, dists)
		#print([(x,y) for x,y in zip(parents , fitness)])

		new_best_idx = np.argmin(fitness)
		new_best_fitness = fitness[new_best_idx]

		if new_best_fitness < best_fitness[-1]:
			print(new_best_fitness[0])
			best_fitness.append(new_best_fitness)
			order = parents[new_best_idx]
			record[i] = new_best_fitness[0]
			draw(ttl, order, city_loc)
			orders_drawn.append(order)


		children = generate_children_f1(parents, fitness, no_of_parents, dists)
		children = mutate(children, cities)
		parents = children

	
	draw(ttl, order, city_loc)
	time.sleep(4)
	#print(best_fitness)
	#print(orders_drawn)
	print(record)
	print('found in {} iterations'.format(list(record.keys())[-1]))
	print('end')
