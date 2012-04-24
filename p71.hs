module Main(main) where
import Data.List

fracs x = [(n,d) |          
           d <- [1..x], 
           n <- ns d,
           gcd n d == 1]

ns d = [lower .. upper - 1] 
    where
      lower = (d * 428571) `div` 1000000
      upper =  (3 * d) `div`  7

fc (a,b) (x,y) = compare (b*y) (a*x)

main = do
  fs <- return $ fracs 1000000
  putStrLn.show.fst.head.(sortBy fc) $ fs
