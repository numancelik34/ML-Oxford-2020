import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy


def V(s, t, eta, tau):
    return 1./(16.*s*t**3) * (1 + (4*(1+4*s+4*s**2))*np.exp(-2*s) + (100*(1+4*np.pi*t+4./3.*np.pi**2*t**2))*np.exp(-2*np.pi*t) - 4*(1+2*s)*np.exp(-s)*np.cos(eta) - 20*(1+2*np.pi*t)*np.exp(-np.pi*t)*np.cos(np.pi*tau) + 40*(1+2*s+2*np.pi*t)*np.exp(-s-np.pi*t)*np.cos(eta-tau))


########################################################################################################################
# (a) Make contour plots
########################################################################################################################
# implement this here


########################################################################################################################
# (b) Implement tournament selection
########################################################################################################################
def fitness(individual):
    # implement this here


def binary_tournament_select(e1, e2):
    # implement this here


########################################################################################################################
# (c) Implement mutation routine
########################################################################################################################
def mutate(individual, mutation_rate=0.05):
    # implement this here


########################################################################################################################
# (d) Implement crossover routine
########################################################################################################################
def crossover(parent1, parent2):
    # implement this here


########################################################################################################################
# (e) Implement survival routine
########################################################################################################################
def survival_selection(parents, children):
    # implement this here


########################################################################################################################
# (f) Run the GA
########################################################################################################################
NUM_GENERATIONS = 300
NUM_INDIVIDUALS = 100
MUTATION_RATE = 0.05

# randomly in initialized first generation

# iterate over generations
for g in range(NUM_GENERATIONS):
    # tournament select
    # crossover
    # mutate
    # survival