import json
from random import choice, randrange
from pprint import pprint

inputs = ['SnP500', 'GDPgr', 'HousingGrowth', 'Unemployment', 'Fed30Yr']

outputs = ['Revenues', 'Losses', 'Capital']

modelGroups = ['OpRisk', 'Retail Credit', 'Wholesale Credit', 'Market Risk',
                'PPNR', 'Capital']

nodes = []

edges = []

maxnodes = 15
maxedges = 60
maxvalue = 10
inpmodels = 4

for i in range (1, maxnodes + 1):
    group = choice(modelGroups)
    nodes.append({
        'id': i,
        'group': group,
        'title': group,
        'shape': 'dot',
    })

for j in range (1, maxedges + 1):
    edges.append({
        'from': randrange(maxnodes) + 1,
        'to': randrange(maxnodes) + 1,
        'value': randrange(maxvalue) + 1
    })

for inp in inputs:
    nodes.append({
        'id' : inp,
        'group': 'Inputs',
        'title': inp,
        'shape': 'square'
    })

    for edge in range(randrange(maxnodes/3)):
        edges.append({
            'from': inp,
            'to': randrange(maxnodes) + 1
        })

for op in outputs:
    nodes.append({
        'id' : op,
        'group': 'Outputs',
        'title': op,
        'shape': 'hexagon'
    })

    for edge in range(randrange(maxnodes/3)):
        edges.append({
            'to': op,
            'from': randrange(maxnodes) + 1
        })

fh = open('generatedGraph.html', 'w')

fh.write (
'''
<html>
<head>
    <script type="text/javascript" src="https://visjs.org/dist/vis.js"></script>
    <link href="https://visjs.org/dist/vis.css" rel="stylesheet" type="text/css" />

    <style type="text/css">
        #mynetwork {
            width: 100%;
            height: 100%;
            border: 1px solid lightgray;
        }
    </style>
</head>
<body>
<div id="mynetwork"></div>

<script type="text/javascript">
    // create an array with nodes
'''
)

fh.write ('\n\nvar nodes = ' + json.dumps(nodes))
fh.write ('\n\nvar edges = ' + json.dumps(edges))

fh.write (
'''
    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
        edges: edges
    };

    var options = {
      edges:{
        arrows: {
          to:     {enabled: true, scaleFactor:1, type:'arrow'},
          }
        }
    }


    // initialize your network!
    var network = new vis.Network(container, data, options);
</script>
</body>
</html>
'''
)

fh.close()
