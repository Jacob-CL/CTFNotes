# Chapter 2: Introduction to Number Theory
Number theory is everywhere in cryptographic alogrithms and are fundamental to asymmetric (public-key) cryptographic algorithms.

## 2.1 Divisibility and the Division Alogrithm

---

Divisbility:
When we say "`b` divides `a`" (written as `b|a`), we mean: You can divide `a` by `b` and get a whole number with no leftover.
- 3 divides 12 because `12|3 = 4` (no remainder)
- 5 divides 30 because `30|5 = 6` (no remainder)
- ` does NOT divide 15 because `15|4 = 3` remainder 3

If you wanted to find all divisors for the number `24`:
- 1 goes into 24 (24 times)
- 2 goes into 24 (12 times)
- 3 goes into 24 (8 times)
- 4 goes into 24 (6 times)
- 5 does not go in to 24 
- etc

So we have some simple rules of divisibility:
- If something divides 1, it must be 1 or -1 because only they can divide 1 evenly.
- If `a` divides `b` AND `b` divides `a`, then they're basically the same size. Like saying 6 divides 12 AND 12 divides 6 - this only works if they're euqal (or opposites)
- Any number divides 0: `0|anything = 0` so there's never a remainder
- `Chain rule`: if `a` divides `b`, and `b` divides `c` then `a` divides `c`: e.g `11(a)|66(b)` --> `66(b)|198(c)` --> then 11(a) MUST | by 198(c)
- `Combination Rule`: If `b|g` AND `b|h`, then `b|ANY combination of them` e.g If `7|14` and `7|63`, then 7 will also divide things like (3×14 + 2×63). Think of it like: if you can share 14 apples and 63 oranges equally among 7 people, you can also share any combination of those fruits equally.

To explain the combination rule more:
`7| both 14 AND 63` so we can say that the total of (ANY arbitrary number x 14 + ANY arbitrary number x 63) will be divisable by 7. e.g
```
(1×14 + 1×63) = 77 ✓ (77 ÷ 7 = 11)
(5×14 + 3×63) = 259 ✓ (259 ÷ 7 = 37)
(10×14 - 4×63) = -112 ✓ (-112 ÷ 7 = -16)
```
The coefficents can be any integer you want

---

The Division Algorithm:
