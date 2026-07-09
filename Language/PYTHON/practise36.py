def func(name, *fav_Games):
    print("\n", name, "likes to  play ")
    for Games in fav_Games:
        print(Games)
func("navaneeth", "BGMI","Uncharted","GTA")
func("Rajiva", "GTA", "BGMI")
func("Manohar", "FreeFire")