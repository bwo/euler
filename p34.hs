import Char
fac :: Int -> Int
fac n = f n 1
    where
      f 0 a = a
      f n a = f (n - 1) (n * a)
sumfacs :: Int -> Int
sumfacs = foldl1 (+) . map (\c -> fac $ Char.digitToInt c) . show 

