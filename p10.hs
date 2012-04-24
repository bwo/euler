module Main(main) where
import Primes

main = do
  print $ sum (takeWhile (<2000000) primes)
