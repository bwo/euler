module Main(main) where
pairs = [(x,y) | x <- [1..9], y <- [1..9]]

pairsofpairs = [((x1,y1),(x2,y2)) | (x1,y1) <- pairs, (x2,y2) <- pairs, x1 == y2 || x1 == x2 || y1 == y2 || y1 == x2]

nontrivial ((x1,y1),(x2,y2)) 
    | x1 == x2 && y1 == y2 = False
    | otherwise = True

lessthanone ((x1,y1),(x2,y2)) = (x1*10+y1) < (x2*10+y2)

interesting ((x1,y1),(x2,y2))
    | x1 == x2 = (x1*10+y1)*y2 == (x2*10+y2)*y1
    | x1 == y2 = (x1*10+y1)*x2 == (x2*10+y2)*y1
    | y1 == x2 = (x1*10+y1)*y2 == (x2*10+y2)*x1
    | y1 == y2 = (x1*10+y1)*x2 == (x2*10+y2)*x1

reduced ((x1,y1),(x2,y2))
    | x1 == x2 = (y1,y2)
    | x1 == y2 = (y1,x2)
    | y1 == y2 = (x1,x2)
    | y1 == x2 = (x1,y2)

gcdized (x,y) = (x `div` g, y `div` g)
    where 
      g = gcd x y

fracmul (x1,y1) (x2,y2) = gcdized (x2*x1,y1*y2)

main = do
  print . snd . foldr1 fracmul . map reduced . filter interesting . filter lessthanone $ filter nontrivial pairsofpairs
