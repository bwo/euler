import Data.Monoid
import Data.Function
import Data.List
-- same weird strategy as p72
import Primes

limit = 100000

data Factored a = F {v :: !a, f :: ![(a,a)] }

instance Ord a => Ord (Factored a) where
    compare (F v _) (F w _) = compare v w
instance Eq a => Eq (Factored a) where
    F v _ == F w _ = v == w
instance Num a => Monoid (Factored a) where
    mempty = F 1 mempty
    (F v exps) `mappend` (F w exps2) = F (v*w) (exps `mappend` exps2)

--mkf v e = F v (Cons e Nil)
mkf v e = F v [e]

powers n = scanl (\f c -> mkf ((v f) *n) (n,c)) (mkf n (n,1)) [2..]
primepows = [takeWhile ((<=limit).v) $ powers p | p <- takeWhile (<=limit) primes]

merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys) 
    | x <= y = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

merge3 [] [] [] = []
merge3 as [] [] = as
merge3 [] bs [] = bs
merge3 [] [] cs = cs
merge3 as bs [] = merge as bs
merge3 as [] cs = merge cs as
merge3 [] bs cs = merge bs cs
merge3 all@(a:as) ball@(b:bs) call@(c:cs) 
    | ab == EQ = case bc of 
                   LT -> a : merge3 as bs call
                   EQ -> a : merge3 as bs cs
                   GT -> c : merge3 all bs cs
    | ab == LT = case ac of
                   LT -> a : merge3 as ball call
                   EQ -> a : merge3 as ball cs
                   GT -> c : merge3 all ball cs
    | ab == GT = case bc of 
                   GT -> c : merge3 all ball cs
                   EQ -> c : merge3 all bs cs
                   LT -> b : merge3 all bs call
    where
      ab = compare a b
      bc = compare b c
      ac = compare a c

mergeseq (xs) = go (sortBy (compare `on` length)  xs) []
    where
      go [] lasts = go (reverse lasts) []
      go [x] [] = x
      go [x] lasts = go (reverse (x:lasts)) []
      go (a:b:xs) lasts = let m = merge a b in go xs $ m:lasts

mergeprimepowers [] = []
mergeprimepowers [s1] = s1
mergeprimepowers (s:ss) = foldl' mergepp s ss
    where
      mergepp pp rr = merge3 pp (mergeacc pp $ reverse rr) rr
      mergeacc sofar newprimes = mergeseq acc
          where acc = foldl' (\a r -> let w = takeWhile ((<=limit).v) $ map (mappend r) sofar in w:a) [] newprimes

rad :: Num a => Factored a -> a
rad (F _ f) = foldr (\(prime, pow) acc -> prime * acc) 1 f

main = do
  let rads = (1,1):(map (\f -> (v f, rad f)) $ mergeprimepowers $ reverse primepows)
      sorted = sortBy (compare `on` snd) rads
  print $ fst $ sorted !! 9999
