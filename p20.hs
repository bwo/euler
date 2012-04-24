module Main(main)
    where
      import Char
      fac n = fac' n 1 
          where
            fac' 1 acc = acc
            fac' 0 acc = acc
            fac' n acc = fac' (n - 1) (n * acc)
      sumdigits n = foldl1 (+) . map Char.digitToInt $ show n
      main = do
        print . sumdigits $ fac 100
