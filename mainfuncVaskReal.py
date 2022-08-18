import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import csv
from selenium.webdriver import ActionChains


def get_name():
    # csv format is: name, percentage of gender
    # data from https://www.ssb.no/statbank/table/10467/
    #
    # name column consists of first names.
    # percentage column refers to the percentage of
    # people the same gender that were given that name from 1996 to 2001.
    #
    # For example, the name Thea was given to 1.152% of girls.
    # TODO: Use this percentage info to give more realistic, weighted choices in the future.
    csv_path = 'data/navn.csv'
    with open(csv_path, newline="") as csv_file:
        names = [i[0] for i in csv.reader(csv_file)]
    
    names += ["Jan","Per","Bjørn","Ole","Lars",
    "Kjell","Natalie","Katrine","jakob","jens","tommy","celine",
    "Nora","hahaha","lise","kultnavn","danseløven","kris","djtommy","sarah","pddpdd",
    "yousef","mustafa","hansegutten","kiannn","andrew","gggggg","lollolol","xDDDD","zooom"]
    
    # Choose the holy name to post with
    name = random.choice(names)

    # Add randomness/humanize how the name is typed (this was overkill but v fun)
    # First, check for hyphens in names. Almost nobody will bother writing the hyphen,
    # and will prolly opt for a space or just nothing
    if name.find("-") != -1:
        if random.randrange(0, 20) != 0:
            hyphen_replacement = " "
            if random.choice((True, False)) == True:
                hyphen_replacement = ""
            name = name.replace("-", hyphen_replacement)

    # Drunkmode: Use the first letter of the name, plus a
    # random selection of the characters from the whole name
    if random.randrange(0, 5) == 0:
        name = name[0]+"".join([random.choice(name) for i in name]).lower()

    # name.lower(): The csv is capitalized, some people don't capitalize
    if random.randrange(0, 5) == 0:
        name = name.lower()

    # For the extra stylish kidz: Repeat the last letter a few times
    if random.randrange(0, 9) == 0:
        name += name[-1]*random.randint(1, 3)

    # Some might mistap, lets remove/add one character
    if random.randrange(0, 9) == 0:
        i = random.randrange(1, len(name)+1)
        name = name[:i-1]+name[i:]
    if random.randrange(0, 9) == 0:
        i = random.randrange(1, len(name)+1)
        char = random.choice(name).lower()
        name = name[:i]+char+name[i:]
    
    # Finally, our perfect fake name is ready >:) muahahaha
    return name

def UpvoteSong(url, votes,DownVoting):

    songsToUpvote = [] #make a list to add sonsg we want to upvote

    with open("GoodSongs.txt", "r") as CoolSongFile: 
        lines = CoolSongFile.readlines()

    for line in lines:
        songsToUpvote.append(line.replace("\n","")) 
        #we have added all our cool songs from a txt file to this list

    print(songsToUpvote) # print to make sure 

    # Loop the process for the amount of votes
    for i in range(votes):
        if i != 0:
            time.sleep(1)
        print(f'Vote attempt {i+1}...')
        
        # TODO: Assign the driver variable in a separate file
        # and gitignore it so we can seamlessly work with our own drivers
        PATH = "C:\Program Files (x86)\chromedriver.exe"

        driver = webdriver.Chrome(PATH)
        driver.get(url)
        
        time.sleep(3)
        
        #click join via web app

        search = driver.find_element_by_class_name("join-web")
        search.click()

        time.sleep(2)

        # Name enter
        search = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/p[2]/input')
        nameChoice = get_name()
        time.sleep(0.2)
        # Realistic typing simulation because it looks cool :P
        for char in nameChoice:
            search.send_keys(char)
            time.sleep(0.19 + random.randrange(-10, 7)/100)
        time.sleep(0.3)
        search.send_keys(Keys.RETURN)

        # Click next
        time.sleep(1.3)

        nextbutton = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/p[3]/a')
        nextbutton.click()

        ##--------------------------------- HERE WE HAVE LOGGED IN ---------------------------------

        time.sleep(2)

        #scroll page to load stuff 
        driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0,0);")

        time.sleep(1)

        #find elements by class title  // Here we are finding all songs aviable (titles)
        classtitles = driver.find_elements(by=By.CLASS_NAME, value="title")

        #find all upvote buttons on the screen 
        UpvoteButtons = driver.find_elements(by=By.CLASS_NAME, value="votes")

        #make a list where we will put all the RIGHT buttons to click on 
        buttonIndexList = []

        for index,PlayableSong in enumerate(classtitles):
            if PlayableSong.text in songsToUpvote: 
                #check all possible songs, if they are in songs we want: put button index in list
                print(PlayableSong.text)
                buttonIndexList.append(index-1) 
                # we have to minus one because it counts the currently playign song as one classtitle
                # and that class title does not have an index clickable button:

        time.sleep(1)

        for buttonindex,button in enumerate(UpvoteButtons):
            
            #buttonsVoting = button.find_elements_by_tag_name("a")

            if buttonindex in buttonIndexList: #if the button index is CORRECT, click it!
                button.find_element_by_tag_name("a").click()
                #buttonsVoting[0].click()
                time.sleep(0.2)

            #if DownVoting == True: #not yet implimented
                #if buttonindex in buttonIndexList: #if the button index is INCORRECT, click it!
                    #buttonsVoting[1].click()
                    #time.sleep(0.2)

        time.sleep(random.randint(5,10))
        driver.quit()

    # We're done voting now, quit the driver ALL VOTES FOR ALL PEOPLE COMPLETED
    time.sleep(1)
    
    print("Quit driver.")
    driver.quit()


if __name__ == "__main__":
    UpvoteSong("https://outloud.dj/5n4p8", 2, DownVoting  = False)


#https://outloud.dj/5n4p8
#https://outloud.dj/vbmzb