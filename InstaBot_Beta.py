from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common import exceptions
import getpass
from datetime import datetime
from selenium.webdriver.common.by import By
from random import randint
from playsound import playsound

non_story_viewers=[]
new_list=[]

class Bot:
    def __init__(self):
        self.driver= webdriver.Chrome('chromedriver.exe')
        self.base_url = 'https://www.instagram.com/'
        self.driver.execute_script("alert('Please check your Application console window. Hit Ok before continuing or the Bot will not work.')")
        self.login()
    
    
    def open_chrome(self):
        self.driver= webdriver.Chrome('chromedriver.exe')
        self.base_url = 'https://www.instagram.com/'
        

    def login(self):
        ch= input("\nDo you have 2-Factor Authentication enabled on your account? [y/n]: ")
        if ch=='y':
            print('\nPlease keep your phone handy...The program will wait for 2-Factor Authentication after loggin in. Just type in the code and hit "Confirm"...')
            self.username = str(input("\nEnter your username: "))   
            self.password = getpass.getpass(prompt='Password (Hidden Entry): ')
            print("\nCheck your browser...")
            self.driver.get(self.base_url)
            time.sleep(4)
            self.driver.find_element_by_xpath('//input[@name= \"username\"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//input[@name= \"password\"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//button[@type= "submit"]').click()
            print("\nContinuing in 50...")
            for x in range(49 ,-1, -1):
                time.sleep(1)    
                print(x)    
            
        else:
            print('\nOkay cool...')
            self.username = str(input("\nEnter your username: "))   
            self.password = getpass.getpass(prompt='Password (Hidden Entry): ')
            print("\nCheck your browser...")
            self.driver.get(self.base_url)
            time.sleep(4)
            self.driver.find_element_by_xpath('//input[@name= \"username\"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//input[@name= \"password\"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//button[@type= "submit"]').click()
            time.sleep(4)
        
        try:
            self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        except Exception:
            self.go_to_my_profile()
            self.driver.execute_script('alert("Please keep an eye on your Application Console Window for progress...")')
            
        
    def go_to_my_profile(self):
        self.driver.get(self.base_url + self.username)
        time.sleep(4)

    def get_followers_list(self):
        self.go_to_my_profile()
        #Getting Followers list below
        print('\n***Getting Followers list***')
        time.sleep(4)
        self.driver.find_element_by_xpath('//a[@href= "/{}/followers/"]'.format(self.username)).click()
        time.sleep(2)
        scrollbox= self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_height, curr_height= 0, 1
        while last_height!= curr_height:
            last_height= curr_height
            time.sleep(1)
            curr_height= self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scrollbox
            )
            time.sleep(1)
        follower_links= scrollbox.find_elements_by_tag_name('a')
        followers_names= [name.text for name in follower_links]
        [followers_names.remove(x) for x in followers_names if x=='']
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click() #Click the [x] button for followers
        except Exception:
            self.driver.refresh()
            time.sleep(4)
        return followers_names


    def get_following_list(self):
        self.go_to_my_profile()
        #Getting Following list below
        print('***Getting Following list***')
        self.driver.find_element_by_xpath('//a[@href= "/{}/following/"]'.format(self.username)).click()
        time.sleep(1)
        scrollbox= self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_height, curr_height= 0, 1
        while last_height!= curr_height:
            last_height= curr_height
            time.sleep(1)
            curr_height= self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scrollbox
            )
            time.sleep(1)
        following_links= scrollbox.find_elements_by_tag_name('a')
        following_names= [name.text for name in following_links]
        [following_names.remove(x) for x in following_names if x=='']
        return following_names


    def get_unfollowers(self):
        followers_names= self.get_followers_list()  #Getting Followers list 
        following_names= self.get_following_list()  #Getting Following list 
  
        #Getting Non-followers
        for x in following_names:
            if not x in followers_names:
                new_list.append(x)                
                print(x)
        
        print('\nFollowers: ' + str(len(followers_names)), end='')
        print('    Following: ' + str(len(following_names)))
        print('\nNumber of Non-followers: ' + str(len(new_list)) + '\n')


    def start_follow(self):
        self.go_to_my_profile()
        time.sleep(4)
        keyword= input("Enter a profile username: ")
        print('\n***Starting Follow Procedure***\n')
        print('\nFollowing 35 Users every hour for 5 hours straight [Safe Following rate]')
        total_followed= 0
        hours= 5
        for z in range(1, hours+1):
            followed_this_hour= 0
            i=35
            self.driver.get(self.base_url + keyword) #In case input is a User
            time.sleep(4)
            try:
                self.driver.find_element_by_xpath('//button[contains(text(), "Follow")]').click()
            except:
                pass
            time.sleep(1)

            contents= self.driver.find_elements_by_xpath('//a[@href="/{}/followers/"]'.format(keyword))
            contents= [x.text for x in contents]
            contents= ''.join(contents)
            contents= contents.split(' ')
            if contents[0] == '0':
                print("\nSORRY! There are no users to Follow | Exiting\n")
                playsound('FaZe_Sway_ringtone.mp3')
                return
            
            time.sleep(3)
            self.driver.find_element_by_xpath('//a[@href="/{}/followers/"]'.format(keyword)).click()
            time.sleep(2)
        
            scrollbox= self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]') 
            for x in range(2):
                self.driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', scrollbox)
                time.sleep(1)
        
            to_follow_list= scrollbox.find_elements_by_tag_name('a')
            to_follow_list= [x.text for x in to_follow_list]
            [to_follow_list.remove(x) for x in to_follow_list if x=='']
            
            print('\n')
            print(to_follow_list)
            print('\n')

            follow_count=0
            for x in range(0,i):
                if i>len(to_follow_list):
                    i= len(to_follow_list)
                self.driver.get('https://instagram.com/' + to_follow_list[x])
                time.sleep(4)
                follow_button= self.driver.find_elements_by_xpath('//button[contains(text(), "Follow")]')
                if len(follow_button) > 0:
                    follow_button[0].click()
                    time.sleep(randint(2,3))
                    follow_count+=1
                    print('Followed ' + to_follow_list[x])
                else:
                    continue

            print("\nTotal followed this hour: " + str(follow_count) + " at " + datetime.now().strftime("%H:%M:%S"))
            print("\nTime remaining to completion: " + str(hours-z) + " hours")
            total_followed+= follow_count
            if z<5:
                playsound('FaZe_Sway_ringtone.mp3')
                time.sleep(3600)

        print("\nTotal Followed this session: " + str(total_followed) + "\nTime of completion: " + datetime.now().strftime("%H:%M:%S") + " CONGRATULATIONS!!")
        self.go_to_my_profile()
        playsound('FaZe_Sway_ringtone.mp3')


    def start_unfollow(self):
        exclude_list_decision= input("Do you want to create Exclusions list to prevent me from Unfollowing your friends?[y/n]: ")
        if exclude_list_decision.lower()=='y':
            self.create_exclusions_list()

        if len(new_list)==0:
            self.get_unfollowers()

        f= open('exclusions.txt', 'r')
        contents= f.read()
        contents= contents.split(' ')
        contents= [y for y in contents if y!='']
        f.close()
        
        total_unfollow=0
        for y in range(5):
            i=25
            unfollow_count=0
            print('***Starting Unfollow Procedure***\n')
            
            if len(new_list)== total_unfollow:
                print("\nThere are no users left to Unfollow | Exiting\n")
                return
            
            if len(new_list)< i:
                i= len(new_list)-total_unfollow
                
                print(total_unfollow)
                print(len(new_list))
                print(i)

            for x in range(total_unfollow, i + total_unfollow):
                self.driver.get(self.base_url + new_list[x])
                time.sleep(3)  

                ch= self.driver.find_element(By.XPATH, '//a[@href= "/{}/followers/"]'.format(new_list[x])).text
                ch= ch.split(" ")
                    
                if new_list[x] in contents:
                    continue

                if 'm' not in ch[0] and 'k' not in ch[0] and ',' not in ch[0]:
                    unfollow_button= self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
                    if len(unfollow_button) > 0:
                        unfollow_button[0].click()
                        self.driver.find_element_by_xpath('//button[contains(text(), "Unfollow")]').click()
                        print('Unfollowed ' + new_list[x])
                        unfollow_count+=1
                        time.sleep(1)
                    else:
                        unfollow_button= self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button')
                        if len(unfollow_button) > 0:
                            unfollow_button[0].click()
                            self.driver.find_element_by_xpath('//button[contains(text(), "Unfollow")]').click()
                            print('Unfollowed ' + new_list[x])
                            unfollow_count+=1
                            time.sleep(1)
                    
            total_unfollow+=unfollow_count

            print('\nTotal Unfollowed this hour: ' + str(unfollow_count))
            print(datetime.now().strftime("%d-%m-%Y - %H:%M:%S"))
            if y<4:
                print('Next wave starts in 1 hour')
                playsound('FaZe_Sway_ringtone.mp3')
                time.sleep(3600)
        print("\nTotal Unfollowed this session: " + str(total_unfollow) + "\nTime of completion: " + datetime.now().strftime("%H:%M:%S") + " CONGRATULATIONS!!\n")
        self.go_to_my_profile()
        playsound('FaZe_Sway_ringtone.mp3')


    def raw_unfollow(self):
        self.go_to_my_profile()
 
        #Getting following list
        print("\nLog:")
        print('\n***Getting Following list***')
        print("**Unfollowing 35 people every hour**")
        time.sleep(randint(1,2))
        
        try:
            contents= self.driver.find_elements_by_xpath('//a[@href="/{}/following/"]'.format(self.username))
        except Exception:
            self.go_to_my_profile()
            time.sleep(4)
            contents= self.driver.find_elements_by_xpath('//a[@href="/{}/following/"]'.format(self.username))
        contents= [x.text for x in contents]
        contents= ''.join(contents)
        contents= contents.split(' ')
        if contents[0] == '0':
            print("\nSORRY! There are no users to Unfollow | Exiting\n")
            playsound('FaZe_Sway_ringtone.mp3')
            return
        
        lower_lim= 0
        upper_lim= 7
        total_unfollowed=0
        hours= 5
        for z in range(1, hours+1):
            unfollow_count=0
            for y in range(5):
                try:
                    self.driver.find_element_by_xpath('//a[@href= "/{}/following/"]'.format(self.username)).click() #Click User's Following button
                except KeyboardInterrupt:
                    self.go_to_my_profile()
                    time.sleep(4)
                    self.logout()
                except Exception:
                    self.go_to_my_profile()
                    time.sleep(4)
                    self.driver.find_element_by_xpath('//a[@href= "/{}/following/"]'.format(self.username)).click() #Click User's Following button
                for x in range(lower_lim, upper_lim):
                    time.sleep(2)
                    
                    try:
                        self.driver.find_element_by_xpath('//button[contains(text(), "Following")]').click() #Click Following button
                    except KeyboardInterrupt:
                        self.go_to_my_profile()
                        time.sleep(4)
                        self.logout()
                    except Exception:
                        self.go_to_my_profile()
                        time.sleep(4)
                        self.driver.find_element_by_xpath('//a[@href= "/{}/following/"]'.format(self.username)).click() #Click User's Following button
                        time.sleep(2)
                        try:
                            self.driver.find_element_by_xpath('//button[contains(text(), "Following")]').click() #Click Following button
                        except exceptions.NoSuchElementException:
                            continue
                     
                    try:
                        self.driver.find_element_by_xpath('//button[contains(text(), "Unfollow")]').click() #Click Final Unfollow button
                    except KeyboardInterrupt:
                        self.go_to_my_profile()
                        time.sleep(4)
                        self.logout()
                    except Exception:
                        self.go_to_my_profile()
                        time.sleep(4)
                        self.driver.find_element_by_xpath('//a[@href= "/{}/following/"]'.format(self.username)).click() #Click User's Following button
                        time.sleep(2)                    
                        try:
                            self.driver.find_element_by_xpath('//button[contains(text(), "Following")]').click() #Click Following button
                        except KeyboardInterrupt:
                            self.go_to_my_profile()
                            time.sleep(4)
                            self.logout()
                        except Exception:
                            continue
                        try:
                            self.driver.find_element_by_xpath('//button[contains(text(), "Unfollow")]').click() #Click Final Unfollow button
                        except KeyboardInterrupt:
                            self.go_to_my_profile()
                            time.sleep(4)
                            self.logout()
                        except Exception:
                            continue    
                    
                    unfollow_count+=1
                    time.sleep(randint(1,3))
                    
                try:
                    self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click() #Click the [x] button for followers
                except exceptions.NoSuchElementException:
                    continue
                time.sleep(randint(1,2))
                self.driver.refresh()
                time.sleep(3)
            
            total_unfollowed+= unfollow_count
            
            if unfollow_count<1:
                print("\nNo more users left to Unfollow | Exiting")
                print("\nTotal Unfollowed this pass: " + str(unfollow_count) + " at " + datetime.now().strftime("%H:%M:%S"))
                print("\nTotal Unfollowed this session: " + str(total_unfollowed) + "\nTime of completion: " + datetime.now().strftime("%H:%M:%S") + " CONGRATULATIONS!!")
                playsound('FaZe_Sway_ringtone.mp3')
                return
            
            print("\nTotal Unfollowed this pass: " + str(unfollow_count) + " at " + datetime.now().strftime("%H:%M:%S"))
            print("\nTime remaining to completion: " + str(hours-z) + " hours")
            if z<5:
                playsound('FaZe_Sway_ringtone.mp3')
                time.sleep(3600)
        print("\nTotal Unfollowed this session: " + str(total_unfollowed) + "\nTime of completion: " + datetime.now().strftime("%H:%M:%S") + " CONGRATULATIONS!!")
        playsound('FaZe_Sway_ringtone.mp3')
        time.sleep(3)
        self.driver.refresh()

    def check_story_non_viewers(self):
        self.go_to_my_profile()
        self.driver.find_element_by_xpath('//img[@alt="{}\'s profile picture"]'.format(self.username)).click()
        time.sleep(2)
        seen_by= self.driver.find_element_by_xpath('//span[contains(text(), "Seen by")]')
        print('\nYour story is ' + seen_by.text)
        time.sleep(1)
        self.driver.find_element_by_xpath('//span[contains(text(), "Seen by")]').click()
        time.sleep(1)
        ###########################
        try:
            scrollbox= self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div') #/html/body/div[4]/div/div/div[2]/div
            last_height, curr_height= 0, 1
            while last_height!= curr_height:
                last_height= curr_height
                time.sleep(1)
                curr_height= self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scrollbox
                )
                time.sleep(1)
        except Exception:
            pass
        
        viewers= self.driver.find_elements_by_tag_name('a')
        viewers= [x.get_attribute('title') for x in viewers]
        viewers= [x for x in viewers if x!=self.username and x!='']
        print('\n')
        print(viewers)
        print('\n' + str(len(viewers)) + ' viewers')
        self.get_unfollowers_list()
        time.sleep(1)
        non_viewers= []
        [non_viewers.append(x) for x in non_story_viewers if x not in viewers]
        print('\n' + str(len(non_viewers)) + ' people from your followers didn\'t view your story')
        print('\nNon-viewers are :')
        [print(x) for x in non_viewers]


    def create_exclusions_list(self):
        print("\nKeep your Browser window besides this...")
        print('\nStarting...')
        if len(new_list)==0:
            self.get_unfollowers()

        f= open('exclusions.txt', 'a+')
        for x in new_list:
            self.driver.get(self.base_url + x)
            #time.sleep(4)
            choice= input("\nExclude {} ? [y/n]: ".format(x))
            if choice.lower()=='y':
                f.write(x + ' ')
        f.close()
        print('\nExclusions registered. Do not delete the "exclusions.txt file in this folder."... You may Unfollow safely now.')


    def logout(self):
        self.driver.get(self.base_url + self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[contains(text(), "Log Out")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[contains(text(), "Log Out")]').click()
    
    
    def close_browser(self):
        self.driver.close()
        

# Driver Code
try:
    obj = Bot()
    while(True):
        choice= input("\n\n1. Navigate to Your Profile\n2. Check who is not following you back\n3. Create Exclusions List\n4. Unfollow Non-followers\n5. Follow People\n6. Raw Unfollow\n7. Log Out\n0. Exit\n\nEnter numbers for the following features: ")
            
        if choice=='1':
            print('Please wait...1')
            obj.go_to_my_profile()  #Navigate to User Profile
        if choice=='2': 
            print('Please wait...1')
            obj.get_unfollowers()  #Self Explanatory
        if choice=='3': 
            print('Please wait...1')
            obj.create_exclusions_list()
        if choice=='4': 
            print('Please wait...1')
            obj.start_unfollow() #Haha! Again self explanatory
        if choice=='5': 
            print('Please wait...1')
            obj.start_follow()
        if choice=='6': 
            print('Please wait...1')
            obj.raw_unfollow()
        if choice=='7': 
            print('Please wait...1')
            obj.logout()
        if choice=='0':
            print("Thank You! | Exiting Now")
            try:
                obj.close_browser()
            except Exception:
                break
            break
except KeyboardInterrupt:
    print('\n\n****************Process Interrupted by User******************\n')