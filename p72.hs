{-# OPTIONS_GHC -XBangPatterns -O2 -funbox-strict-fields #-}
--silly implementation, but it works
import Primes
import Data.Monoid
import Data.List
import Control.DeepSeq 
import Data.Function

limit = 1000000

data Factored a = F { v :: !a, f :: ![(a, a)]} deriving Show

instance Ord a => Ord (Factored a) where
    compare (F v _) (F w _) = compare v w

instance Eq a => Eq (Factored a) where
    (F v _) == (F w _) = v == w

instance Num a => Monoid (Factored a) where
    mempty = F 1 []
    -- here we assume that v and w are relatively prime, which, here,
    -- they always are.
    (F v exps) `mappend` (F w exps2) = F (v*w) (exps++exps2)

instance (NFData a) => NFData (Factored a) where
    rnf (F v exps) = (rnf v) `deepseq` (rnf exps) `deepseq` ()

powers n = scanl (\f c -> F ((v f) * n) [(n,c)]) (F n [(n,1)]) [2..]

primepows = [takeWhile ((<=limit).v) $ powers p | p <- takeWhile (<=limit) primes]
numfracs (F {f = f}) = foldl' (\acc (base,exp) -> 
                                   acc * (fracs base exp)) 1 f
    where
      fracs base 1 = base - 1
      fracs base e = base * fracs base (e - 1)

merge [] as = as
merge as [] = as
merge (a:as) (b:bs) 
    | a == b = a : merge as bs
    | a <  b = a : merge as (b:bs)
    | otherwise = b : merge (a:as) bs
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

-- given a sequence of sequences to merge, try to merge the shorter
-- sequences together first (proceeding pairwise: merge (merge s1 s2),
-- (merge s3 s4)).  It is not obvious to me whether this actually
-- gives an advantage over foldl' merge [] in practice, but it seems
-- that it should; merging is proportional to the lengths of the inputs. 
mergeseq (xs) = go (sortBy (compare `on` length)  xs) []
    where
      go [] lasts = go (reverse lasts) []
      go [x] [] = x
      go [x] lasts = go (reverse (x:lasts)) []
      go (a:b:xs) lasts = let !m = merge a b in go xs $ m:lasts

mergepps [s1] = s1
mergepps (s:ss) = foldl' mergepp s ss
    where
     mergepp pp rr = merge3 pp (mergeacc pp $ reverse rr)  rr
     mergeacc sofar !newprimes = mergeseq acc
          where
            acc = foldl' (\a r -> let w = takeWhile ((<=limit).v) $ map (mappend r) sofar in (w:a)) [] newprimes

main = do
  putStrLn $ show $ sum . map numfracs $ 
           mergepps $ reverse primepows
