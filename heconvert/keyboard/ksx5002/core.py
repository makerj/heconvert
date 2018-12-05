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
from enum import Enum

from heconvert.core import select_keyboard, Converter
from heconvert.keyboard.ksx5002.mapping import JA_LEAD, MO, JA_TAIL, JA, H2E_MAPPING, E2H_MAPPING, JAMO_COMPOSE_TABLE


def h2e(string):
    """
    Convert hangul to english. ('한영타' -> 'gksdudxk')
    :param string: hangul that actually represent english string
    :return: converted english string
    """
    result = []
    for c in string:
        ccode = ord(c)  # Character code

        if 0x3131 <= ccode <= 0x3163:  # Hangul Compatibility Jamo
            result.append(H2E_MAPPING[c])
        elif 0xAC00 <= ccode <= 0xD7A3:  # Hangul Syllables
            ccode -= 0xAC00
            # decompose hangul
            lead = JA_LEAD[ccode // 588]
            medi = MO[(ccode % 588) // 28]
            tail = JA_TAIL[(ccode % 588) % 28]
            result.append(H2E_MAPPING[lead])
            result.append(H2E_MAPPING[medi])
            result.append(H2E_MAPPING[tail])
        else:  # Rest of all characters
            result.append(c)
    return ''.join(result)


def e2h(string):
    """
    Convert english to hangul. ('gksdudxk' -> '한영타')
    During processing, state interleaves INIT, LEAD_GIVEN, MEDI_GIVEN and TAIL_GIVEN

    :param string: english that actually represent hangul string
    :return: converted hangul string
    """
    ctx = Context(string)
    for char in ctx.input:
        hchar = E2H_MAPPING.get(char)

        if not char.isalpha() or not hchar:
            ctx.do_final()
            ctx.output.append(char)
            ctx.state = State.INIT
            continue

        if ctx.state is State.INIT:
            if hchar not in JA_LEAD:
                ctx.output.append(hchar)
            else:
                ctx.state = State.LEAD_GIVEN
                ctx.pending.append(hchar)

        elif ctx.state is State.LEAD_GIVEN:
            if hchar in MO:  # ㅇ + ㅏ
                ctx.state = State.MEDI_GIVEN
                ctx.pending.append(hchar)
            else:  # ㅇ + ㅇ
                ctx.state = State.INIT
                ctx.pending.append(hchar)
                ctx.flush()

        elif ctx.state is State.MEDI_GIVEN:
            if hchar in JA:  # ㅇ + ㅏ + ㅇ
                ctx.state = State.TAIL_GIVEN
                ctx.pending.append(hchar)
            else:
                compose_waiter = ctx.pending[-1]
                compose_tuple = JAMO_COMPOSE_TABLE.get(compose_waiter)

                if compose_tuple and hchar in compose_tuple:  # (ㅇ + ㅗ + ㅏ)
                    ctx.pending[-1] = chr((ord(compose_waiter) + compose_tuple.index(hchar) + 1))
                else:  # (ㅇ + ㅏ + ㅏ)
                    ctx.do_final()
                    ctx.state = State.INIT
                    ctx.output.append(hchar)

        elif ctx.state is State.TAIL_GIVEN:
            if hchar in MO:
                if len(ctx.composing_tails) == 2:  # (ㅇ + ㅓ + ㄵ + ㅔ ==> 언제)
                    ctx.pending.pop()  # drop 'ㄵ'
                    ctx.do_final(ctx.composing_tails.pop(0))  # (ㅇ + ㅓ + ㄴ)
                    ctx.pending.append(ctx.composing_tails.pop())  # (ㅈ)
                    ctx.pending.append(hchar)  # (ㅈ + ㅔ)
                    ctx.state = State.MEDI_GIVEN
                else:  # ㄱ,ㅏ,ㅅ  + ㅏ ==> 가,사
                    last_hchar = ctx.pending.pop()
                    ctx.do_final()
                    ctx.pending.append(last_hchar)
                    ctx.pending.append(hchar)
                    ctx.state = State.MEDI_GIVEN
            else:
                compose_waiter = ctx.pending[-1]
                compose_tuple = JAMO_COMPOSE_TABLE.get(compose_waiter)

                if compose_tuple and hchar in compose_tuple:  # (ㄷ + ㅏ + ㄹ + ㄱ)
                    ctx.pending[-1] = chr((ord(compose_waiter) + compose_tuple.index(hchar) + 1))

                    ctx.composing_tails.clear()
                    ctx.composing_tails.append(compose_waiter)
                    ctx.composing_tails.append(hchar)

                else:  # (ㄷ + ㅏ + ㅂ + ㄱ) or (ㄷ + ㅏ + ㄹ + ㄱ + ㄱ)
                    ctx.do_final()
                    ctx.state = State.LEAD_GIVEN
                    ctx.pending.append(hchar)
                    ctx.composing_tails.clear()

    ctx.do_final()  # finalize remain character if any
    return ''.join(ctx.output)


def compose(lead, medi, tail=0):
    """
    Compose hangul using given consonant and vowel
    :param lead:  lead consonant
    :param medi:  medial vowel
    :param tail: tail consonant if any
    :return: composed hangul character
    """
    tail_remainder = None

    lead = JA_LEAD.index(lead) * 588
    medi = MO.index(medi) * 28
    if tail:
        try:
            tail = JA_TAIL.index(tail)
        except ValueError:
            tail_remainder = tail
            tail = 0

    ccode = lead + medi + tail + 0xAC00
    return [chr(ccode)] if not tail_remainder else [chr(ccode), tail_remainder]


class State(Enum):
    INIT = 1
    LEAD_GIVEN = 2  # Lead consonant given
    MEDI_GIVEN = 3  # Medial vowel given
    TAIL_GIVEN = 4  # Tail consonant given


class Context(object):
    def __init__(self, string):
        self.input = list(string)
        self.output = []
        self.state = State.INIT
        self.pending = []
        self.composing_tails = []

    def flush(self):
        self.output += self.pending
        self.pending.clear()

    def do_final(self, hchar=None):
        if hchar:
            self.pending.append(hchar)
        if len(self.pending) < 2:
            return self.flush()

        self.output += compose(*self.pending)
        self.pending.clear()
