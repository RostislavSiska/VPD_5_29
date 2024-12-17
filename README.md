# VPD_5_29

![э](https://psv4.userapi.com/s/v1/d/__GfMLJOQLVr1hvHY-jaXBtcfa-qHVsru0P685odvCJ0nAvJ5S68yJYHQ9418J6VGrtIvUR2DIPF62iG9C1cVpAIrc_c0xXVtHiBmcmrU_xzDPE_-bAdmA/ba9a1041-aedf-4322-b8bf-39c3c46a9e7e.jpg)

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
    result = 0
    for i in range(end):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
    return result
```

![smex](https://sun9-21.userapi.com/impg/0I6dJOR3TLsBhPP0NKUUis7nFM2DqN1CFzJjmA/_-cz5X9pqNc.jpg?size=735x716&quality=95&sign=82246d7f06b2963f10ddf510ed58e360&type=album)

# [_Счастье_ __НЕ__ _за горами_](https://youtu.be/UZB-klaKXII?si=81QckuRa_3ImRyf2)
![smex](https://sun9-55.userapi.com/impg/H6IGeV57A4Y4039Xa4F-FJz0tF2lC1GIJL1SfQ/TFW6wt4dMsI.jpg?size=620x310&quality=96&sign=ab69e4d9fa775bf72d64c329a76a643b&type=album)
