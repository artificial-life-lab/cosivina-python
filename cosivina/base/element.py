#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Abstract base class for architecture elements.
'''

class Element():
    def __init__(self, parameters):
        '''
        INPUT:
        parameters : List of strings as parameter names.
        '''
        self.num_inputs = 0
        self.input_elements = []
        self.input_components = []
        self.paramaters = parameters

    def _delete_elements(self):
        self.input_elements = []
    
    def _close_connections(self):
        NotImplemented
    
    def _add_input(self, input_handle, input_component):
        self.num_inputs += 1
        self.input_elements.append(input_handle)
        self.input_components.append(input_component)

    def _parameter_exists(self, parameter_name):
        '''
        parameter_name : str
        Returns True if parameter_name string exists in self.parameters
        '''
        return any(item == parameter_name for item in self.paramaters)
        
    def _component_exists(self, component):
        '''
        component : str
        Returns True if component string exists in self.input_components
        '''
        return any(item == component for item in self.input_components)
    
    def _get_parameter_change_status(self, parameter_name):
        if self._parameter_exists(parameter_name):
            return parameter_name
        else:
            KeyError('No parameter {} found in element.'.format(parameter_name))
