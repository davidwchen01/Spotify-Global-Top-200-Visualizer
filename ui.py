import graphs
import mplcursors
import matplotlib.pyplot as plt 
import webscraper


def ask_for_filter() -> int:
    num_of_streams = 0
    while True:
        num_of_streams = input("Please input the number of streams to filter for or type default: ")
        try:
            if num_of_streams == 'default':
                return 200
            num_of_streams = int(num_of_streams)
            if num_of_streams > 200:
                print("Number of streams to filter cannot be greater than 200")
            else:
                return num_of_streams
        except:
            print("Input was not convertible to an integer")

def ask_for_type_of_graph() -> str:
    valid_inputs = {1:"bar_graph",2:"scatterplot"}
    while True:
        try:
            num = int(input("Input 1 for a bar graph or 2 for a scatterplot: "))
            if num in valid_inputs.keys():
                return valid_inputs[num]
            else:
                print("Invalid input")
        except:
            print("Input was not convertible to an integer")
        
def get_graph(graph:str,filter:int):
    if graph == "bar_graph":
        graph = graphs.bar_graph(filter)
    elif graph == "scatterplot":
        graph = graphs.scatterplot(filter)
    return graph


def create_labels(filter:int):
    return webscraper.combine_results(webscraper.get_title_results(),webscraper.get_stream_results())[:filter]

def main():
    num_streams = ask_for_filter()
    graph_string = ask_for_type_of_graph()
    labels = create_labels(num_streams)
    graph = get_graph(graph_string,num_streams)
    mplcursors.cursor(graph,hover = True).connect("add",lambda sel: sel.annotation.set_text(labels[sel.target.index]))
    plt.show()



if __name__ == "__main__":
    main()

