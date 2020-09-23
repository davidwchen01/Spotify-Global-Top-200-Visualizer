import matplotlib.pyplot as plt
import webscraper
import numpy
import math

NUMBER_OF_STREAMS = 200



def bar_graph():
    "Returns a graph object resembling a bar graph"
    indices = numpy.arange(NUMBER_OF_STREAMS)
    width = 0.50
    stream_results = webscraper.get_stream_results()
    graph = plt.figure(figsize = (20,8), dpi = 100)
    graph = plt.bar(indices,stream_results,width)
    plt.ylabel('Number of Streams')
    plt.title('Spotify\'s Global Top 200')
    plt.yticks(numpy.arange(0,math.ceil((stream_results[0])),1000000))
    return graph


def pie_graph():
    "Returns a pie_graph"
    stream_results = webscraper.get_stream_results()
    fig1,ax1 = plt.subplots()
    ax1.pie(stream_results,startangle = 0)
    ax1.axis('equal')
    return ax1

def scatterplot():
    "Returns a scatterplot"
    indices = numpy.arange(NUMBER_OF_STREAMS)
    stream_results = webscraper.get_stream_results()
    plt.scatter(indices,stream_results)




main()