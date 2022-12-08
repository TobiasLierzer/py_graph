
import colorsys
import networkx as nx
from pyvis.network import Network

class connection:
  def __init__(self, source, dest):
    self.source = source
    self.dest = dest
  
  def __str__(self):
    return(f'source: {self.source}, destination: {self.dest}')

  def __eq__(self, other):
      return (isinstance(other, self.__class__) and
          getattr(other, 'source', None) == self.source and
          getattr(other, 'dest', None) == self.dest)

  def __hash__(self):
      return hash((self.source, self.dest))


#should be replace with a bit more dynamic evaluation of fortigate as the man in the middle.
def eval_sample_connections():
  sample_connections = set()
  sample_connections.add(connection("core", "bridge-g"))
  sample_connections.add(connection("core", "bridge-f"))
  sample_connections.add(connection("core", "bridge-d"))
  sample_connections.add(connection("core", "bridge-q"))
  sample_connections.add(connection("bridge-q", "final-branch"))
  sample_connections.add(connection("bridge-q", "final-branch2"))

  return sample_connections

def node_color_pick_environment(node):
  colorinterval = 1/6
  pick = 0

  if '-q-' in node or node.endswith('-q'):
    pick = 1
  elif '-d-' in node or node.endswith('-d'):
    pick =  2
  elif '-f-' in node or node.endswith('-f'):
    pick =  3
  elif '-p-' in node or node.endswith('-p'):
    pick =  4
  elif '-g-' in node or node.endswith('-g'):
    pick =  5
  elif node.startswith('itc-') or node.endswith('-aws') or 'azure' in node:
    pick =  6
  else:
    print(node)
    pick =  7

  colorcode = pick * colorinterval

  return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(colorcode,1.0,1.0))


def create_networkgram():

  print('#####create network diagram#####')
  Graph = nx.DiGraph()
  
  sample_connections_set = eval_sample_connections()
  for connection in sample_connections_set:
 #     Graph.add_node(connection.source, color=str(f'rgb{str(node_color_pick_environment(connection.source))}'))
      Graph.add_edge(connection.source, connection.dest, color="red")


  net = Network(notebook=True, height="1000px", width="100%")
  net.from_nx(Graph)
  html = net.generate_html()
  f = open(f'{file_path}{file_name}', "w")
  f.write(html)
  f.close()
  
if __name__ == '__main__':

    #1 Globale Variablen. Kannste auch in der Funktion definieren
    file_path = './'
    file_name = 'my_graph.html'

    #
    test_data = set()

    #2 Daten sammeln

    #3 visualize data
    create_networkgram()
  
else:
  print("not_main")
pass