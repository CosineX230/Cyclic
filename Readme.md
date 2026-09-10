
# Cyclic

Generating recursive sequence terms and related statistics.

## About

Cyclic is a webpage interface that allows users to generate terms of piecewise functions by parity, like the one used in the *Collatz Conjecture* or *3x+1 problem*. It also allows cases for m(mod n) for 2 <= n <= 5. For each run with a starting seed, the program will display the terms (if it converges) as well as the sequence length, max term, and cycle length.

## Usage

For those unfamiliar with the math behind the program, I recommend using what I call the "simplest ruleset". Leave the number of rules at 2, set the first rule, for even numbers, to x / 2 and the second rule, for odd numbers, to x + 1. Enter any whole number as the starting value, and investigate the results.

## Project Structure

Cyclic/
   ├─ backend/
   │  ├─ eval.py
   │  └─ main.py
   └─ frontend/
      ├─ index.html
      ├─ ruleset.js
      ├─ script.js
      └─ style.css

## Notes

This was made during my time as an undergrad student studying math and computer science. Feel free to send me any suggestions, but be aware that this was made as part of a research project and was my first experience with software integration.