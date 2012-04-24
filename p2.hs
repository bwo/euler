module Main(main) where

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

evens = filter (\x -> x `mod` 2 == 0) 

lts = takeWhile (\x -> x < 4000000)

main = do 
  print (foldl (+) 0 ((evens . lts) fibs))
