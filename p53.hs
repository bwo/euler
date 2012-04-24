module Main(main) where
fac n = f n 1
    where
      f 0 a = a
      f 1 a = a
      f n a = f (n - 1) (a * n)
facupto n m = f n m 1 
    where
      f n m a 
          | n == m = a
          | otherwise = f (n - 1) m (a * n)
-- only call this with 2*r <= c for great justice.
c n r = (facupto n (n - r)) `div` (fac r)

ccount n r 
    | cnr && (r*2 == n) = 1
    | cnr = 2 
    | otherwise = 0
    where
      cnr = (c n r) > 1000000
main = do
  print $ sum [ccount n r | n <- [23..100], r <- [1..n `div` 2]]
