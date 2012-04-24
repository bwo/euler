import Primes
bs = takeWhile (< 1000) primes
as = [-999, -997..1000]
isprime n = isp n primes
    where
      isp n (p:pt) 
          | n < 0 = False
          | n < p*p = True
          | n `mod` p == 0 = False
          | otherwise = isp n pt
cmptrip (a,b,c) (x,y,z) = compare c z
maxtrip t1 t2 = case cmptrip t1 t2 of 
                  GT -> t1
                  otherwise -> t2
primecount a b = pc a b 0
    where
      pc a b n = if isprime (n*n + a*n + b) then pc a b (n + 1) else n
vals a b = lst
    where
      lst = b : zipWith (\last n -> last + a + n*2-1) lst [1..]
main = do
  results <- return  $ do
               b <- bs
               a <- as
               return (a, b, length $ takeWhile isprime (vals a b))
  print $ foldl1 maxtrip results
