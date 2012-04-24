module Main(main) where
import Char 
digits = map Char.digitToInt (concatMap show [1..])

main = do
  print $ foldl1 (*) (map (\d -> digits !! ((truncate $ 10 ^^ d) - 1)) [0..6])
