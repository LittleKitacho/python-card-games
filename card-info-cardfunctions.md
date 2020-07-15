# Card Information

This document details how the information is handled and provided in the `card`
object.

## data.suit

`suit` is an `int` that represents the suit of the card.  Below is how this
variable is read:

| ID  | Suit    |
| --- | ------- |
| 0   | N/A     |
| 1   | Spade   |
| 2   | Clubs   |
| 3   | Heart   |
| 4   | Diamond |

## data.colored

`colored` is a `bool` that details whether or not the card is colored.
Below is how this variable is read:

| State   | Color |
| ------- | ----- |
| `true`  | Red   |
| `false` | Black |

## data.number

`number` is an `int` that details the numerical value of the card.  Below is
how this variable is read:
