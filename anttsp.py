from antcolony import AntColony
from antgraph import AntGraph

import pickle
import sys
import traceback

def main(argv):
    #default
    num_nodes = 10

    if len(argv) >= 3 and argv[0]:
        num_nodes = int(argv[0])

    if num_nodes <= 10:
        num_ants = 20
        num_iterations = 12
        num_repetitions = 1
    else:
        num_ants = 28
        num_iterations = 20
        num_repetitions = 1

    stuff = pickle.load(open(argv[1], "r"))
    cities = stuff[0]
    cost_mat = stuff[1]

    if num_nodes < len(cost_mat):
        cost_mat = cost_mat[0:num_nodes]
        for i in range(0, num_nodes):
            cost_mat[i] = cost_mat[i][0:num_nodes]

    #print cost_mat

    try:
        graph = AntGraph(num_nodes, cost_mat)
        best_path_vec = None
        best_path_cost = sys.maxint
        for i in range(0, num_repetitions):
            print "Repetition %s" % i
            graph.reset_tau()
            ant_colony = AntColony(graph, num_ants, num_iterations)
            print "Colony Started"
            ant_colony.start()
            if ant_colony.best_path_cost < best_path_cost:
                print "Colony Path"
                best_path_vec = ant_colony.best_path_vec
                best_path_cost = ant_colony.best_path_cost

        print "\n------------------------------------------------------------"
        print "                     Results                                "
        print "------------------------------------------------------------"
        print "\nBest path = %s" % (best_path_vec,)
        city_vec = []
        for node in best_path_vec:
            print cities[node] + " ",
            city_vec.append(cities[node])
        print "\nBest path cost = %s\n" % (best_path_cost,)
        results=[best_path_vec,city_vec,best_path_cost]
        pickle.dump(results,open(argv[2],'w+'))
    except Exception, e:
        print "exception: " + str(e)
        traceback.print_exc()


if __name__ == "__main__":
    main(sys.argv[1:])
