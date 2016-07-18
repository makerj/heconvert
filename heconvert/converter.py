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

import heconvert.core

KEYBOARD = heconvert.core.select_keyboard()


def h2e(string):
    """
    Convert hangul to english. ('한영타' -> 'gksdudxk')
    :param string: hangul that actually represent english string
    :return: converted english string
    """
    return KEYBOARD.h2e(string)


def e2h(string):
    """
    Convert english to hangul. ('gksdudxk' -> '한영타')
    FSM used for implementing the e2h

    :param string: english that actually represent hangul string
    :return: converted hangul string
    """
    return KEYBOARD.e2h(string)


class HangulToEnglishConverter(heconvert.core.Converter):
    """
    Stateful convert builder (Hangul -> English)
    """

    def __init__(self, initial_value=None, keyboard='ksx5002'):
        keyboard = heconvert.core.select_keyboard(keyboard)
        super().__init__(keyboard.h2e, initial_value)


class EnglishToHangulConverter(heconvert.core.Converter):
    """
    Stateful convert builder (English -> Hangul)
    """

    def __init__(self, initial_value=None, keyboard='ksx5002'):
        keyboard = heconvert.core.select_keyboard(keyboard)
        super().__init__(keyboard.e2h, initial_value)
