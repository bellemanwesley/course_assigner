course_assigner
========

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

course_assigner is a Python library for assigning students to courses based on a preference list. The documentation below should help you understand the parameters passed to the course_assigner functions and what they return, but I recommend starting with examples. Check out the examples in the [samples folder](/samples)

Installation instructions
-------------------------

    python3 -m pip install --upgrade pip
	python3 -m pip install course_assigner

## Classes
The course_assigner library has one method:
   - `assign`: assigns 

# assign

*import course_assigner.assign*

```python
	from statebasedml import bitfold
```

*request syntax*

```python

    folded_value = bitfold.fold(
        value = string,
        new_size = 123,
        mapping = [1, 2, 3],
        ops = [1, 2, 3]
    )

```

*parameters*
   - `size` *(integer)*: The number of bits of the largest sized string that you want to fold. You can determine the bit size of a string with `8*len(string)`

*response syntax*

```python

    {
        "mapping":mapping,
        "ops":ops
    }

```