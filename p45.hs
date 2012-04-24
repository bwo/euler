module Main (main) where 

hexadds = 5 : map (+4) hexadds
pentadds = 4 : map (+3) pentadds
pents = 1 : zipWith (+) pentadds pents
hexes = 1 : zipWith (+) hexadds hexes
tris = 1 : zipWith (+) [2..] tris

joinstreams (x:xs) (y:ys) | x < y = joinstreams xs (y:ys)
                          | x > y = joinstreams (x:xs) ys
                          | otherwise = x:(joinstreams xs ys)

trihexpents = joinstreams tris (joinstreams hexes pents)

main = do
  print $ show (take 3 trihexpents)
