
from graphviz import Digraph

dot = Digraph(comment='Sign Language Recognition System')

# Define nodes
dot.node('A', 'Capture Frame')
dot.node('B', 'Extract ROI')
dot.node('C', 'Apply Gaussian Blur')
dot.node('D', 'Apply Threshold')
dot.node('E', 'Pass to CNN Model')
dot.node('F', 'Classify Symbols')
dot.node('G', 'Autocorrect')

# Define edges
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'])

# Output the diagram to a file
dot.render('sign-language-recognition-system', view=True)
