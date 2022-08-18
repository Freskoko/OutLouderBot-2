
def AddToTxt(songtoadd):
    with open("GoodSongs.txt", "a") as CoolSongFile: 
        CoolSongFile.writelines(f"{songtoadd}\n")
    CoolSongFile.close()

if __name__ == "__main__":
    AddToTxt("coolsong")