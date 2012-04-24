module Main(main) where
import Data.List

takecoin value sofar = concat $ map (unfoldr (\x -> if x < 0 then Nothing else Just (x, x-value))) sofar

coins = [200,100,50,20,10,5,2] -- no need for one penny
takecoins = map takecoin coins
--ways = length $ foldl (flip ($)) [200] takecoins
ways = flip (foldl (flip ($))) takecoins

main = print $ length $ ways [200]
