import json
import re
from IPython.display import HTML, Javascript, IFrame, clear_output

lesson1cells = [8, 14, 19, 31] 
lesson2cells = [11, 23, 35, 41] 
lesson3cells = [9, 16, 18, 26, 28] 
lesson4cells = [21] 

def add_run_button(): 
    # set up run button for every cell
    display(HTML("<style>div.run_this_cell{display:block;}table {margin-left: 0 !important;}</style>"))
    
def run_blockly_Lesson1():
    display(Javascript('Jupyter.notebook.execute_cell_range(9,11)'))
    display(Javascript('Jupyter.notebook.execute_cell_range(14,16)'))
    display(Javascript('Jupyter.notebook.execute_cell_range(19,21)'))
    display(Javascript('Jupyter.notebook.execute_cell_range(26,28)'))
    display(Javascript('Jupyter.notebook.execute_cell_range(33,35)'))

def run_cells(cells):
    for i in cells:
        js = 'Jupyter.notebook.execute_cell_range(' + str(i) + ',' + str(i+1) + ')'
        display(Javascript(js))

def setup_Lesson1(): 
    """ 
    Sets up: 
        run button
        blockly code blocks
    """ 
    clear_output()
    add_run_button()
    run_cells( lesson1cells )
    #run_blockly_Lesson1()
    
    
def setup_Lesson2(): 
    clear_output()
    add_run_button()
    run_cells( lesson2cells )
    
def setup_Lesson3(): 
    clear_output()
    add_run_button()
    run_cells( lesson3cells )

def setup_Lesson4(): 
    clear_output()
    add_run_button()
    run_cells( lesson4cells )

"""
def setup_blockly():
    # Ref : https://github.com/jupyter/notebook/issues/2660#issuecomment-354994932
    display(Javascript('Jupyter.notebook.get_cells'))
    
    display(Javascript('Jupyter.notebook.execute_cell_range(3,40)'))
    #Javascript(IPython.notebook.execute_cell_range(2,26))
"""
