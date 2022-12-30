import json
import re
from IPython.display import HTML, Javascript, IFrame, clear_output

# Run these cells at the start of the lesson (i.e. to set up blockly)
lesson1cells = [8, 14, 19, 31] 
lesson2cells = [11, 23, 35, 41] 
lesson3cells = [10, 17, 19]
lesson4cells = [9, 11] 
lesson5cells = [12] 
lesson6cells = [13] 
lesson7cells = [] 
lesson8cells = [] 
lesson9cells = [3,7] 
lesson10cells = [44] 

def add_run_button(): 
    # set up run button for every cell
    display(HTML("<style>div.run_this_cell{display:block;}table {margin-left: 0 !important;}</style>"))
    
def run_cells(cells):
    for i in cells:
        js = 'Jupyter.notebook.execute_cell_range(' + str(i) + ',' + str(i+1) + ')'
        display(Javascript(js))

def setup_Lesson1(): 
    clear_output()
    add_run_button()
    run_cells( lesson1cells )
    
    
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

def setup_Lesson5(): 
    clear_output()
    add_run_button()
    run_cells( lesson5cells )

def setup_Lesson6(): 
    clear_output()
    add_run_button()
    run_cells( lesson6cells )

def setup_Lesson8(): 
    clear_output()
    add_run_button()
    run_cells( lesson8cells )

def setup_Lesson9(): 
    clear_output()
    add_run_button()
    run_cells( lesson9cells )

def setup_Lesson10(): 
    clear_output()
    add_run_button()
    run_cells( lesson10cells )

"""
def setup_blockly():
    # Ref : https://github.com/jupyter/notebook/issues/2660#issuecomment-354994932
    display(Javascript('Jupyter.notebook.get_cells'))
    
    display(Javascript('Jupyter.notebook.execute_cell_range(3,40)'))
    #Javascript(IPython.notebook.execute_cell_range(2,26))
"""
