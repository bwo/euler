module Main(main,digits) where 
flip (x,y) =  (y,2*y+x)
contfracsparts = (1,2) : (map Main.flip contfracsparts)
addone = map (\(x,y) -> ((x+y),y)) 
--- digits misses thirty, for some reason?
digits x = truncate ((1+) $ logBase 10 x)
morenumeratordigits = filter (\(x,y) -> (digits x > digits y))
morenumeratordigits2 = filter (\(x,y) -> (length $ show x) > (length $ show y))
main = do
  print . length $ morenumeratordigits2 (take 1000 $ addone contfracsparts)
