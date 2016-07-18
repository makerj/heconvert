"""
Copyright 2016 Junhui Lee (ohenwkgdj@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import importlib


def select_keyboard(keyboard_layout_name='ksx5002'):
    keyboard_interface = importlib.import_module('heconvert.keyboard.{}.interface'.format(keyboard_layout_name))
    return keyboard_interface.KEYBOARD


class Converter(object):
    def __init__(self, convert_func, initial_value=None):
        if initial_value and not isinstance(initial_value, str):
            raise TypeError('type of initial_value is must be str')
        self.value = list(initial_value) if initial_value else []
        self.convert_func = convert_func

    def update(self, val, convert=True):
        self.value.append(val)
        if convert:
            return self.convert()

    def convert(self):
        return self.convert_func(''.join(self.value))

    def reset(self):
        self.value.clear()
