module Main(main) where
pal n = (show n) == (reverse $ show n)
flip :: (Read a, Show a) => a -> a
flip = read . reverse . show
step n = n + (Main.flip n)
islychrel n = isl (step n) 1
    where
      isl n 50 = True
      isl n sofar = if pal n then False else isl (step n) (sofar + 1)
main = do
  print . length $ filter islychrel [1..10000]
