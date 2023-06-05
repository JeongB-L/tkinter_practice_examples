# this is for all the functions
# corresponding to key and button

import settings as st

# from one to 0 is simply adding the designated number
# to the entry array entry
def refresh():
    st.answer.config(text=st.entry)
    
def one_is_pressed(*args):
    st.entry.append('1')
    st.answer.config(text=st.entry)
    
def two_is_pressed(*args):
    st.entry.append('2')
    st.answer.config(text=st.entry)
    
def three_is_pressed(*args):
    st.entry.append('3')
    st.answer.config(text=st.entry)
    
def four_is_pressed(*args):
    st.entry.append('4')
    st.answer.config(text=st.entry)
    
def five_is_pressed(*args):
    st.entry.append('5')
    st.answer.config(text=st.entry)
    
def six_is_pressed(*args):
    st.entry.append('6')
    st.answer.config(text=st.entry)
    
def seven_is_pressed(*args):
    st.entry.append('7')
    st.answer.config(text=st.entry)
    
def eight_is_pressed(*args):
    st.entry.append('8')
    st.answer.config(text=st.entry)
    
def nine_is_pressed(*args):
    st.entry.append('9')
    st.answer.config(text=st.entry)
    
def zero_is_pressed(*args):
    st.entry.append('0')
    st.answer.config(text=st.entry)
    
def C_is_pressed(*args):
    st.entry = []
    st.answer.config(text=st.entry)
    # reset the whole thing

def mod_is_pressed(*args):
    pass
    st.answer.config(text=st.entry)

def division_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def multiplication_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def addition_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def subtraction_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def point_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def delete_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def left_bracket_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def right_bracket_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass

def equal_is_pressed(*args):
    st.answer.config(text=st.entry)
    pass
