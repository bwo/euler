module Main(main) 
where
ispent n = floor s == ceiling s
    where
      s = (1 + (sqrt (1 + 24 * (fromInteger n))))/6
pents = 1 : zipWith (+) (map (\x -> 3*x + 1) [1..]) pents
ps = [(a,b) | a <- pents, b <- (takeWhile (<a) pents), ispent (a+b), ispent (a-b)]

main = do
  (a,b) <- return $ head ps
  print (a-b)
