import random
import numpy as np

class GeneticOptimizer:
    def __init__(self, population_size=100, mutation_rate=0.01, generations=100, elitism=True):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.elitism = elitism
        self.population = []

    def initialize_population(self, chromosome_length):
        """
        Initialize the population with random chromosomes.
        :param chromosome_length: The length of each chromosome.
        :return: A list of chromosomes (population).
        """
        self.population = []
        for _ in range(self.population_size):
            chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
            self.population.append(chromosome)

    def fitness_function(self, chromosome):
        """
        Define the fitness function that evaluates the quality of a chromosome.
        In this case, we’ll assume we're optimizing for a target sum of 50 (example problem).
        :param chromosome: The individual chromosome.
        :return: Fitness score (higher is better).
        """
        # Example: We want to find the chromosome that has the most 1's (maximize the number of 1's).
        return sum(chromosome)

    def selection(self):
        """
        Select individuals for mating based on their fitness.
        :return: Two selected parents.
        """
        weighted_population = [(self.fitness_function(chromosome), chromosome) for chromosome in self.population]
        total_fitness = sum([fitness for fitness, _ in weighted_population])

        # Selecting two individuals based on their fitness.
        selected_parents = random.choices(self.population, weights=[fitness / total_fitness for fitness, _ in weighted_population], k=2)
        return selected_parents

    def crossover(self, parent1, parent2):
        """
        Perform crossover (recombination) between two parents to create two offspring.
        :param parent1: First parent chromosome.
        :param parent2: Second parent chromosome.
        :return: Two offspring chromosomes.
        """
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        return offspring1, offspring2

    def mutate(self, chromosome):
        """
        Perform mutation on a chromosome with a certain mutation rate.
        :param chromosome: The chromosome to mutate.
        :return: Mutated chromosome.
        """
        return [gene if random.random() > self.mutation_rate else 1 - gene for gene in chromosome]

    def evolve(self):
        """
        Evolve the population over multiple generations.
        :return: The best solution found.
        """
        for generation in range(self.generations):
            new_population = []

            # Elitism: Carry the best individuals to the next generation unchanged
            if self.elitism:
                best_individual = max(self.population, key=self.fitness_function)
                new_population.append(best_individual)

            # Create new population by selecting parents and performing crossover and mutation
            while len(new_population) < self.population_size:
                parent1, parent2 = self.selection()
                offspring1, offspring2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(offspring1))
                if len(new_population) < self.population_size:
                    new_population.append(self.mutate(offspring2))

            self.population = new_population

            # Print the best fitness in each generation for monitoring
            best_fitness = self.fitness_function(max(self.population, key=self.fitness_function))
            print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

        # Return the best individual found after all generations
        best_chromosome = max(self.population, key=self.fitness_function)
        return best_chromosome, self.fitness_function(best_chromosome)
