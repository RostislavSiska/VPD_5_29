# VPD_5_29

- Функция 2 sin(x)
- Функция 5 ch(x)
- Функция 8 arctg(x) 

# Реализация функций

- [ ] 1. e^x
- [x] 2. sin(x)
- [ ] 3. cos(x)
- [ ] 4. sh(x)
- [x] 5. ch(x)
- [ ] 6. ln(1 + x)
- [ ] 7. ln(1 - x)
- [x] 8. arctg(x)
- [ ] 9. (1 + x)^m
- [ ] 10. (1 - x)^m

## Функция sin(x)

sin(x) = $\displaystyle\sum_{i=0}^n\(-1)^{i}\frac{x^{2i+1}}{(2i+1)!}\$,   $-\infty\$ < x < $+\infty\$

``` python
    summ = 0
    for i in range(end):
        summ = summ + (((-1)**i) * ((x**(2*i + 1))/(factorial(2*i + 1))))
    return summ
```

## Функция ch(x)

ch(x) = $\displaystyle\sum_{i=0}^n\frac{x^{2i}}{(2i)!}\$,   $-\infty\$ < x < $+\infty\$

``` python
    summ = 0
    for i in range(end):
        summ = summ + ((x**(2*i))/(factorial(2*i)))
    return summ
```

## Функция arctg(x)

arctg(x) = $\displaystyle\sum_{i=0}^n\(-1)^{i}\frac{x^{2i+1}}{2i+1}\$,   -1 < x < 1

``` python
    Здесь будет код
```
