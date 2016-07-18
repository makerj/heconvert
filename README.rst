heconvert
#########

.. _description:

**heconvert** is simple converter that convert hangul to english and vise-versa

.. contents::

.. _requirements:

Requirements
============

- python 3


.. _installation:

Installation
============

**heconvert** should be installed using pip3: ::

    pip3 install heconvert

Use heconvert
=============
#) Hangul --> English: ::

    from heconv.converter import h2e

    h2e('사랑합니다')  # return 'tkfkdgkqslek'

#) English --> Hangul: ::

    from heconv.converter import h2e

    e2h('tkfkdgkqslek')  # return '사랑합니다'

# Continuous Converting: ::

    from heconv.converter import HangulToEnglishConverter, EnglishToHangulConverter

    # Hangul --> English
    h2e_builder = HangulToEnglishConverter()
    h2e_builder.update('한영타')  # just update internal state
    h2e_builder.convert()  # return 'gksdudxk'
    h2e_builder.update('변환기', convert=True)  # return 'gksdudxkqusghksrl'

    # English --> Hangul
    e2h_builder = EnglishToHangulConverter()
    e2h_builder.update('gksdudxk')  # just update internal state
    e2h_builder.convert()  # return '한영타'
    e2h_builder.update('qusghksrl', convert=True)  # return '한영타변환기'

Bug tracker
===========

If you have any suggestions or bug reports, please report them to the issue tracker
at https://github.com/makerj/heconvert/issues


Contributing
============

Contribution of heconvert available at github: https://github.com/makerj/heconvert
To start a support for a new keyboard layout, use manage.py to create a new module directory structure (for more information, run manage.py with '--help' argument)


License
=======

Licensed under The Apache License (Apache).


Copyright
=========

Copyright (c) 2016 Junhui Lee (ohenwkgdj@gmail.com)

.. _github: https://github.com/makerj/heconvert
