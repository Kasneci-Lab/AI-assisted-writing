import streamlit as st


class BasePage:
    def __init__(self,*,name:str):
        self.__widgets__ = []
        self.__key__ = name



    def __post_process__(self,session):
        if self.__key__ not in st.session_state.page_widgets.keys():
            st.session_state.page_widgets[self.__key__] = self


    def clear(self):
        for i in self.__widgets__:
            i.empty()


    def append(self, *, empty):
        self.__widgets__.append(empty)

    def extend(self,*,li:list):
        for i in li:
            self.append(empty=i)
