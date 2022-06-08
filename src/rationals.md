# Rationals

A revisit of [Xavier Noria, "I See Your 127.32+. A Tale of Rationals"](https://github.com/euruko2013/site/blob/master/build/speakers/presentations/i_see_your_127_32_a_tale_of_rationals-noria.pdf)

## Unsigned integer in python

```
>>> import ctypes
>>> ctypes.c_ulong(-1).value
18446744073709551615
>>> ctypes.c_uint(-1).value
4294967295
>>>
```
## Numbers in python

> The `numbers` module (PEP 3141) defines a hierarchy of numeric abstract base classes which progressively define more operations.
> ..
> Class `numbers.Rational` subtypes `Real` and adds `numerator` and `denominator` properties...

Implementation of abstract `numbers.Rational` can be found in python module `fractions`.

> The `fractions` module provides support for rational number arithmetic.
>
> A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string.

```
>>> one
Decimal('1')
>>> three
Decimal('3')
>>> assert three * ( one / three ) == one, 'Thank you Python!'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Thank you Python!
```

### Resources

- [Xavier Noria, "I See Your 127.32+. A Tale of Rationals"](https://github.com/euruko2013/site/blob/master/build/speakers/presentations/i_see_your_127_32_a_tale_of_rationals-noria.pdf)
- [Unsigned integers and Python](https://kristrev.github.io/programming/2013/06/28/unsigned-integeres-and-python)
- [StackOverflow: How to convert signed to unsigned integer in python](https://stackoverflow.com/questions/20766813/how-to-convert-signed-to-unsigned-integer-in-python#20768199)
- [numbers - Numeric abstract base classes](https://docs.python.org/3.10/library/numbers.html?highlight=rational#numbers.Rational)
- [Lib/fractions.py](https://github.com/python/cpython/blob/3.10/Lib/fractions.py#L93) implements `numbers.Rational`

### Appendix

> Complements are used in digital computers in order to simply the subtraction operation and for the logical manipulations. For the Binary number (base-2) system, there are two types of complements: 1’s complement and 2’s complement.

