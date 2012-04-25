modexp b e m = modexp' b e m 1
    where 
      modexp' b 0 m a = a
      modexp' b e m a 
          | e `rem` 2 == 0 = modexp' (b*b) (e `quot` 2) m a
          | otherwise = modexp' b (e - 1) m ((a * b) `rem` m)
p = 1 + 28433 * (modexp 2 7830457 100000000000)
main = print $ p `rem` 10000000000
