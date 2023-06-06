# this is for all the functions
# corresponding to key and button

import settings as st
# from one to 0 is simply adding the designated number
# to the entry array entry

# this function refreshes the label 
# whenever an element is appended to entry or 
# something is clicked
def refresh(func):
    def wrapper(*args):
        func()
        # make it untypable if entry longer than 30
        if len(st.entry) >= 33:
            # if more than 29, keep popping the
            # entry so that no more values are added
            # and =, C, backspace are the only ones
            # that can make it move out
            del st.entry[32]
        if len(st.entry) % 11 == 0:
            st.entry.append('\n')
        crr = ''.join(str(e) for e in st.entry)
        st.answer.config(text=crr[1: len(crr)])
    return wrapper


@refresh
def one_is_pressed(*args):
    st.entry.append('1')

# 이렇게 따로따로 버튼을 지정하지 않고
# 그냥 event.char을 받아서 특정 버튼 제외 나머지를
# 다 받게 할 수도 있으나 그러면 특정 버튼에 대한
# 기능 개발이 덜해질 수 있음?
@refresh
def two_is_pressed(*args):
    st.entry.append('2')


@refresh
def three_is_pressed(*args):
    st.entry.append('3')


@refresh
def four_is_pressed(*args):
    st.entry.append('4')


@refresh
def five_is_pressed(*args):
    st.entry.append('5')


@refresh
def six_is_pressed(*args):
    st.entry.append('6')


@refresh
def seven_is_pressed(*args):
    st.entry.append('7')


@refresh
def eight_is_pressed(*args):
    st.entry.append('8')


@refresh
def nine_is_pressed(*args):
    st.entry.append('9')


@refresh
def zero_is_pressed(*args):
    st.entry.append('0')


@refresh
def C_is_pressed(*args):
    st.entry.clear()
    # reset the whole thing


@refresh
def mod_is_pressed(*args):
    st.entry.append(' % ')


@refresh
def division_is_pressed(*args):
    st.entry.append(' / ')


@refresh
def multiplication_is_pressed(*args):
    st.entry.append(' X ')


@refresh
def addition_is_pressed(*args):
    st.entry.append(' + ')


@refresh
def subtraction_is_pressed(*args):
    st.entry.append(' - ')


@refresh
def point_is_pressed(*args):
    st.entry.append('.')


@refresh
def delete_is_pressed(*args):
    del st.entry[len(st.entry) - 1]


@refresh
def left_bracket_is_pressed(*args):
    st.entry.append('(')


@refresh
def right_bracket_is_pressed(*args):
    st.entry.append(')')


@refresh
def equal_is_pressed(*args):
    # return the result of the calculation
    pass
