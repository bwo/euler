module Main(main) where
    
ispal n = (show n) == (reverse (show n))

threedigits = [100..999]
threepairs = [(x,y) | x <- threedigits, y <- threedigits]

best [] m = m
best ((x,y):rest) m 
          | ispal prod && prod > m = best rest prod
          | otherwise = best rest m
          where
            prod = x*y

main = do
  print (best threepairs 0)
