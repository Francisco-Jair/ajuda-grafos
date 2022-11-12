from Graph import Graph, Edge, Vertex
from ChinesePostman import ChinesePostmanAlgorithm
import GraphGenerator
import csv
import datetime

BENCH_TIMES = 3

if __name__ == "__main__":
    vertexes_num = [5, 10, 25, 50, 100, 250, 500]

    with open('complete_graph.csv', 'w', newline='') as csvfile:
        completegraphwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        times = [str(i) for i in vertexes_num]
        print(times)
        headerrow = ['Vertexes Num']
        for t in times:
            headerrow.append(t)
        completegraphwriter.writerow(headerrow)

        # Executa o teste 3 vezes para as X quantidade de vertices
        results = []
        for x in vertexes_num:
            print(f"COMPLETE GRAPH : {x} vertexes")
            average = 0
            for i in range(BENCH_TIMES):
                graph = GraphGenerator.generate_complete_graph(x)
                algorithm = ChinesePostmanAlgorithm(graph)
                initial_time = datetime.datetime.now()
                result = algorithm.solve()
                final_time = datetime.datetime.now()
                average += (final_time - initial_time).total_seconds()
            average = average / BENCH_TIMES
            results.append(average)
        results = [f"{i:.2f}s" for i in results]
        results_list = ["Time (s)"]
        for r in results:
            results_list.append(r)
        completegraphwriter.writerow(results_list)

    with open('incomplete_graph.csv', 'w', newline='') as csvfile:
        incompletegraphwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        times = [str(i) for i in vertexes_num]
        print(times)
        headerrow = ['Vertexes Num']
        for t in times:
            headerrow.append(t)
        incompletegraphwriter.writerow(headerrow)

        # Executa o teste 3 vezes para as X quantidade de vertices
        results = []
        for x in vertexes_num:
            print(f"INCOMPLETE GRAPH : {x} vertexes")
            average = 0
            for i in range(BENCH_TIMES):
                graph = GraphGenerator.generate_incomplete_graph(x)
                algorithm = ChinesePostmanAlgorithm(graph)
                initial_time = datetime.datetime.now()
                result = algorithm.solve()
                final_time = datetime.datetime.now()
                average += (final_time - initial_time).total_seconds()
            average = average / BENCH_TIMES
            results.append(average)
        results = [f"{i:.2f}s" for i in results]
        results_list = ["Time (s)"]
        for r in results:
            results_list.append(r)
        incompletegraphwriter.writerow(results_list)