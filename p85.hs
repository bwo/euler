{-# OPTIONS_GHC -fvia-C -O3 #-}
rectangles (x,y) = sum [(x-n+1)*(y-m+1) | n <- [1..x], m <- [1..y]]
tm = 2000000

lowestover x y = last$takeWhile ((>tm).snd) [(p, rectangles p) | p <- pairs x y]

is = dropWhile ((<tm).rectangles)$concat [[(x-1,x),(x,x)] | x<-[1..70]]
   
pairs x y = map (\a -> (x-a,y+a)) [1..x-1]
closest (x,y) = if v - tm < tm - v2 then (v-tm,lox*loy) else (tm-v2,nx*ny)
    where
      ((lox,loy),v) = lowestover x y
      (nx,ny) = (lox-1, loy+1)
      v2 = rectangles (nx,ny)


main = print  $ minimum $ map closest is
