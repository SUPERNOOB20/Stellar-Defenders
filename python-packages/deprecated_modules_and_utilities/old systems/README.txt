-- "Old Saving System" is when the saving system was in a txt file (nexus.txt) as opposed to the newer JSON (.json) saving system.

-- "Old Physics System" is when the system was "scattered around" (list-based) as opposed to the newer physics system (array-based)

!! Note that both system changes improve performance by a LOT (O(n) to O(1) for the saving system, and O(n/2) to O(1) for the new physics system)


If you don't understand how these improvements work, make sure to hit me up, and maybe I'll cover it in a blog post :3)/