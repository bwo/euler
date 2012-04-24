module Main(main) where

import List

threes = 3 : map (+3) threes
fives = 5 : map (+5) fives
lts = takeWhile (< 1000)


main = do 
  print (sum (List.union (lts threes) (lts fives)))
