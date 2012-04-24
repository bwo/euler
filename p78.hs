import Data.Array

partitions :: Array Int Integer
partitions = array (0,1000000)  $
             (0,1):
             [(n, sum 
                    [s * partitions ! p | (s,p) <- zip signs $ parts n])
              | n <- [1..1000000]]
                 where
                   signs = cycle [1,1,(-1),(-1)]
                   genpents = map pentize $ concat [[n,(-n)] | n <- [1..]]
                   pentize n = n*(3*n-1) `quot` 2
                   parts k = takeWhile (>=0) [k-x | x <- genpents]

main = do
  let (x:_) = dropWhile (\x -> partitions ! x `rem` 1000000 /= 0) [1..]
  print (x,partitions ! x)
