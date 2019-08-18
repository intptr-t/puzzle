
# 組み合わせの合計が一致する式の導出

```
ans:
    24
input:
    [5, 5, 5, 1]
output:
    (5 - (1 / 5)) * 5 = 24
    5 * (5 - (1 / 5)) = 24
```

# Case a b c

(0, 1): (a b) c
(1, 0): a (b c)

# Case a b c d

(0, 1, 2): (((a b) c) d)
(0, 2, 1): ((a b) (c d)) [*1]
(1, 0, 2): ((a (b c)) d)
(1, 2, 0): ((a b) (c d)) [*1]
(2, 0, 1): (a ((b c) d))
(2, 1, 0): (a (b (c d)))

# Case a b c d e

(0, 1, 2, 3) : ((((a b) c) d) e)
(0, 1, 3, 2) : (((a b) c) (d e)) [*1]
(0, 2, 1, 3) : (((a b) (c d)) e) [*2]
(0, 2, 3, 1) : (((a b) c) (d e)) [*1]
(0, 3, 1, 2) : ((a b) ((c d) e)) [*3]
(0, 3, 2, 1) : ((a b) (c (d e))) [*4]
(1, 0, 2, 3) : (((a (b c)) d) e)
(1, 0, 3, 2) : ((a (b c)) (d e)) [*5]
(1, 2, 0, 3) : (((a b) (c d)) e) [*2]
(1, 2, 3, 0) : (((a b) c) (d e)) [*1]
(1, 3, 0, 2) : ((a b) ((c d) e)) [*3]
(1, 3, 2, 0) : ((a b) (c (d e))) [*4]
(2, 0, 1, 3) : ((a ((b c) d)) e)
(2, 0, 3, 1) : ((a (b c)) (d e)) [*5]
(2, 1, 0, 3) : ((a (b (c d))) e)
(2, 1, 3, 0) : ((a (b c)) (d e)) [*5]
(2, 3, 0, 1) : ((a b) ((c d) e)) [*3]
(2, 3, 1, 0) : ((a b) (c (d e))) [*4]
(3, 0, 1, 2) : (a (((b c) d) e))
(3, 0, 2, 1) : (a ((b c) (d e))) [*6]
(3, 1, 0, 2) : (a ((b (c d)) e)) 
(3, 1, 2, 0) : (a ((b c) (d e))) [*6]
(3, 2, 0, 1) : (a (b ((c d) e)))
(3, 2, 1, 0) : (a (b (c (d e))))