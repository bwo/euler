module Main(main) where

fracs = [(n,d) | d <- [1..10000], n <- [(d `div` 3) .. (d `div` 2)], gcd n d == 1, 2*n < d, 3*n > d]

main = do
  print $ length fracs
