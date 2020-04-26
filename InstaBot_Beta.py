from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common import exceptions
import getpass
from datetime import datetime
from selenium.webdriver.common.by import By
from random import randint
#from PIL import ImageTk, Image
#from tkinter import *
from playsound import playsound


'''root= Tk()
root.title("InstaBot")
root.geometry("500x500+450+200")

my_img= ImageTk.PhotoImage(Image.open('landscape_window_BLur.jpg'))
label1= Label(root, image=my_img)
label1.place( relwidth=1, relheight=1)

root.iconbitmap('Icon.ico') ##ICON'''

new_list=[]
class Bot:
    def __init__(self):
        self.driver= webdriver.Chrome('chromedriver.exe')
        self.base_url = 'https://www.instagram.com/'
        self.driver.execute_script("alert('Please check your Application console window')")
    
    def open_chrome(self):
        self.driver= webdriver.Chrome('chromedriver.exe')
        self.base_url = 'https://www.instagram.com/'
        
    def login(self):
        ch= input("\nDo you have 2-Factor Authentication enabled on you account? [y/n]: ")
        if ch=='y':
            print('\nPlease keep your phone handy...The program will wait for 2-Factor Authentication after loggin in. Just type in the code and hit "Confirm"...')
            self.username = str(input("\nEnter your username: "))    # usernameEntry.get()
            self.password = getpass.getpass()    # passwordEntry.get()
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
            self.username = str(input("\nEnter your username: "))    # usernameEntry.get()
            self.password = getpass.getpass()    # passwordEntry.get()
            print("\nCheck your browser...")
            self.driver.get(self.base_url)
            time.sleep(4)
            self.driver.find_element_by_xpath('//input[@name= \"username\"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//input[@name= \"password\"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//button[@type= "submit"]').click()
        
        try:
            self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        except Exception:
            self.go_to_my_profile()
            self.driver.execute_script('alert("Please keep an eye on your Application Console Window for progress...")')
            
        
    def go_to_my_profile(self):
        self.driver.get(self.base_url + self.username)
        time.sleep(4)

    def get_unfollowers_list(self):
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

        #Compare Followers list with Following list
        for x in following_names:
            if not x in followers_names:
                new_list.append(x)                
                print(x)
        
        print('Followers: ' + str(len(followers_names)), end='')
        print('    Following: ' + str(len(following_names)))
        print('Number of Non-followers: ' + str(len(new_list)) + '\n')


    def start_follow(self):
        self.go_to_my_profile()
        time.sleep(4)
        keyword= 'nahichahiyeji'#input("Enter a profile username: ")
        print('\n***Starting Follow Procedure***\n')
        print('\nFollowing 35 Users every hour for 5 hours straight [Safe Following rate]')
        total_followed= 0
        hours= 5
        for z in range(1, hours+1):
            followed_this_hour= 0
            for y in range(5):
                i= 7
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
                scrollbox= self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]') #/html/body/div[4]/div/div[2]
                to_follow_list= scrollbox.find_elements_by_tag_name('a')
                to_follow_list= [x.text for x in to_follow_list]
                [to_follow_list.remove(x) for x in to_follow_list if x=='']
                
                print("\n")
                print(to_follow_list)
                print("\n" + str(len(to_follow_list)))

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
                followed_this_hour+= follow_count
            print("\nTotal followed this hour: " + str(followed_this_hour) + " at " + datetime.now().strftime("%H:%M:%S"))
            print("\nTime remaining to completion: " + str(hours-z) + " hours")
            total_followed+= followed_this_hour
            if z<5:
                playsound('FaZe_Sway_ringtone.mp3')
                time.sleep(4) #3600

        print("\nTotal Unfollowed this session: " + str(total_followed) + "\nTime of completion: " + datetime.now().strftime("%H:%M:%S") + " CONGRATULATIONS!!")
        self.go_to_my_profile()
        playsound('FaZe_Sway_ringtone.mp3')


    def start_unfollow(self):
        if len(new_list)==0:
            print("There are no users to Unfollow | Exiting\n")
            return

        total_unfollow=0
        for y in range(5):
            i=25
            unfollow_count=0
            print('***Starting Unfollow Procedure***\n')
            
            if len(new_list)== total_unfollow:
                print("There are no users left to Unfollow | Exiting\n")
                return
            
            if len(new_list)< i:
                i= len(new_list)-total_unfollow
                
                print(total_unfollow)
                print(len(new_list))
                print(i)

            for x in range(total_unfollow, i + total_unfollow):
                self.driver.get('https://instagram.com/' + new_list[x])
                time.sleep(3)  
                
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
            time.sleep(3600)
        print("\nTotal Unfollowed this session: " + str(total_unfollow) + "\nTime of completion: " + datetime.now().strftime("%H:%M:%S") + " CONGRATULATIONS!!\n")
        self.go_to_my_profile()


    def raw_unfollow(self):
        self.go_to_my_profile()
        
        #Getting following list
        print("\nLog:")
        print('\n***Getting Following list***')
        print("**Unfollowing 35 people every hour**")
        time.sleep(randint(1,2))
        #scrollbox= self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        
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
                    #self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(x)).click()
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
                    #time.sleep(randint(1,2))    
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
                        
                    # FIX THIS!!print( "Unfollowed " + self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]'.format(x)).text)
                    unfollow_count+=1
                    time.sleep(randint(1,3))
                    

                try:
                    self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click() #Click the [x] button for followers
                except exceptions.NoSuchElementException:
                    continue
                time.sleep(randint(1,2))
                self.driver.refresh()
                time.sleep(3)
                #self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollbox)# [WORKED]
            
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


    def logout(self):
        self.driver.get(self.base_url + self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(), "Log Out")]').click()
        time.sleep(4)
    
    
    def close_browser(self):
        self.driver.close()
        
# Driver Code
obj = Bot()
while(True):
    choice= input("\n\n1. Log In\n2. Navigate to Your Profile\n3. Check who is not following you back\n4. Unfollow Non-followers\n5. Follow People\n6. Raw Unfollow\n7. Log Out\n8. Open Browser\n0. Exit\n\nEnter numbers for the following features: ")
    
    if choice=='1':
        print('Please wait...1')
        obj.login()
    if choice=='2':
        print('Please wait...1')
        obj.go_to_my_profile()  #Navigate to User Profile
    if choice=='3': 
        print('Please wait...1')
        obj.get_unfollowers_list()  #Self Explanatory
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
    if choice=='8': 
        print('Please wait...1')
        obj.close_browser()
    if choice=='9': 
        print('Please wait...1')
        obj.open_chrome()
    if choice=='0':
        print("Thank You! | Exiting Now")
        obj.close_browser()
        break

'''frame= Frame(root, bg='blue', bd='10')
frame.place(relx=0.150, rely=0.150, relwidth=0.7, relheight=0.7)

my_img2= ImageTk.PhotoImage(Image.open('landscape_window.jpg'))
label2= Label(frame, image=my_img2)
label2.place( relwidth=1, relheight=1)

loginButton= Button(frame, text="Log In", padx='20', pady="5", fg='white', bg="red", command=obj.login)
loginButton.place(anchor=CENTER, rely=0.22, relx=0.5)

label1= Label(root, text=" ")
label1.grid(row=3, columnspan=2)

usernameEntry= Entry(frame, width=30, borderwidth=2)
usernameEntry.place(anchor=CENTER, relx=0.5, rely=0.04)
usernameEntry.insert(0, "Username")

passwordEntry= Entry(frame, width=30, borderwidth=2, show='*')
passwordEntry.place(anchor=CENTER, relx=0.5, rely=0.12)
passwordEntry.insert(0, "Password")

############### LEFT SIDE BUTTONS
myProfile= Button(frame, text="My Profile", padx='15', pady="5",  fg='white', bg="red", command=obj.go_to_my_profile)
myProfile.place(anchor=W, rely=0.4, relx=0.03)

startUnfollowButton= Button(frame, text="Unfollow", padx='18', pady="5",  fg='white', bg="red", command=obj.start_unfollow)
startUnfollowButton.place(anchor=W, rely=0.51, relx=0.03)
###################################

############### RIGHT SIDE BUTTONS
getListButton= Button(frame, text="Get Nonfollowers", padx='10', pady="5",  fg='white', bg="red", command=obj.get_unfollowers_list)
getListButton.place(anchor=E, rely=0.4, relx=0.97)

openBrowserButton= Button(frame, text="Open Chrome", padx='18', pady="5",  fg='white', bg="red", command=obj.open_chrome)
openBrowserButton.place(anchor=E, rely=0.51, relx=0.97)


####### CENTER BUTTONS
logoutButton= Button(frame, text="Log Out", padx='34', pady="5", fg='white', bg="red", command=obj.logout)
logoutButton.place(anchor=CENTER, rely=0.79, relx=0.5)

exitButton= Button(frame, text="Exit", padx='15', pady="5",  fg='white', bg="red", command=obj.close_browser)
exitButton.place(anchor=CENTER, rely=0.9, relx=0.5)


###################################


label1= Label(frame, text="")
label1.grid(row=9, columnspan=2)


########### AUTHOR NAME
label2= Label(root, text="Author: Harsh Pradhan")
label2.place(relx=0.5, rely=0.92, anchor=CENTER)

########### Status Bar
status_bar= Label(root, text='Declare Variables, Not War', bd=1.5, relief=SUNKEN, anchor=E)
status_bar.place(relx=0.5, rely=0.975, anchor=CENTER)

root.mainloop()'''