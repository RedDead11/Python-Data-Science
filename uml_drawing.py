import graphviz

# Create a new graph
graph = graphviz.Digraph(format='png')

# Define the steps and add nodes to the graph
steps = [
    'Start',
    'Login',
    'Validate Credentials',
    'Authenticate User',
    'Browse Products',
    'Add to Cart',
    'View Cart',
    'Modify Cart',
    'Proceed to Checkout',
    'Enter Shipping Details',
    'Select Payment Method',
    'Process Payment',
    'Place Order',
    'Generate Order Confirmation',
    'Complete'
]

for step in steps:
    graph.node(step)

# Define the relationships between steps
relationships = [
    ('Start', 'Login'),
    ('Login', 'Validate Credentials'),
    ('Validate Credentials', 'Authenticate User'),
    ('Authenticate User', 'Browse Products'),
    ('Browse Products', 'Add to Cart'),
    ('Add to Cart', 'View Cart'),
    ('View Cart', 'Modify Cart'),
    ('Modify Cart', 'Proceed to Checkout'),
    ('Proceed to Checkout', 'Enter Shipping Details'),
    ('Enter Shipping Details', 'Select Payment Method'),
    ('Select Payment Method', 'Process Payment'),
    ('Process Payment', 'Place Order'),
    ('Place Order', 'Generate Order Confirmation'),
    ('Generate Order Confirmation', 'Complete')
]

for relationship in relationships:
    graph.edge(*relationship)

# Save the graph to a file and render it
graph.render('activity_diagram', view=True)
