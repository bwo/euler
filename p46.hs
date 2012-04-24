module Main(main) where
import Primes
-- in Primes, "nonprimes" is actually odd nonprimes, for obvious reasons

-- problem def'n implicitly takes one to be a prime
tsq = map (\x -> 2*x*x) [1..]

nongoldbachian = nong
    where
      nong = findnongoldbach nonprimes (sprimes nonprimes)
      sprimes (c:ct) = takeWhile (< c) primes
      findnongoldbach (c:ct) []  = c
      findnongoldbach (c:ct) (p:ps) 
          | match c p tsq = findnongoldbach ct (sprimes ct)
          | otherwise = findnongoldbach (c:ct) ps
      match c p (ps:pss) 
          | ps+p > c = False
          | ps+p == c = True
          | otherwise = match c p pss

main = do
  print nongoldbachian
