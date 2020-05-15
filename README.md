<h1 align="center">Instagram Bot v1.6</h1>
<p align="center">
<img src="https://imgur.com/nu9qFI0.png" width='200'>
  <h3 align='center'>I am a robust, powerful and fully featured Instagram Bot that automates boring & tedious tasks on Instagram for you</h3>
</p>
  <p align="center">⭐️ Star it | 🔱 Fork it on GitHub </p>
  <p align="center">
    <a href="https://github.com/timgrossmann/InstaPy/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/license-GPLv3-blue.svg" />
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-blueviolet" />
    </a>
      <img src='https://img.shields.io/badge/118-Stars-brightgreen'>
  </p>
<p align='center'><a href='https://github.com/Harshp20'><img  src='https://img.shields.io/badge/Coded%20By-Harsh%20Pradhan-red'></a></p>

## Features:
- [x] 1. **Get Non-Followers -** See who's not following you back.
- [x] 2. **Unfollow People -** Unfollows people that are not following you back. *(25 people/hour for 5 hours)* **Note:-** *This feature will skip celebrities and famous/professional accounts. If you want the Bot to skip selected users, use "Create Exclude list feature". It will also pop-up by default when "Unfollow Non-followers" is chosen.*
- [x] 3. **Raw Unfollow -** Unfollows everybody regardless of them following you back or not. *(35 people/hour for 5 hours)*
- [x] 4. **Create Exclude List -** Create eclude list so that the Bot skips selected users. **Note :- You will have 4 seconds to either accept or reject the addition of each user to the exclusion list. If no decision is made before time out, the Bot will exclude that user from UNFOLLOW list by default. You can manage the exclusion list later.**
- [x] 5. **Follow People -** Follows people from the *followers* list of desired profile for growth. *(35 people/hour for 5 hours)*
- [x] 6. **Supports** wait time of *50 seconds* for accounts having 2-Factor Authentication enabled.
### Upcoming Features
- [ ] 7. **Analyze** and determine _Ghost_ followers, i.e. People who follow you but never have liked your posts.
- [ ] 8. **Analyze** and determine followers that never viewed your stories.

## IMPORTANT | Must Read Before Usage:
1. You can select "Create Exclusions List" feature and SHOULD add only those people to the "Exclusion List" whom you want to keep following even if they ever unfollowed you. You will have to press "Yes" for people you want to exclude from the Unfollow List. If no choice is made, the particular user will be automatically excluded. You can leave popular accounts alone. The Bot will detect and automatically exclude them so you don't have to press "Yes" for every single account.
2. If you are running "Unfollow Non-followers" feature for the first time, the Bot will go over to the account of every single person that doesn't *follow you back* and is not in your Exclusion list and learn whether they are a celebrity OR professional account. The Bot has the ability to learn about accounts. If they are, the Bot will not flag them as your *Non-follower* and also would not visit their account from the next time onwards. This will save a lot of time of yours. However, for the sake of learning, it is ***Important*** to visit all the accounts that don't follow you back and are not in your Exclusion List.
3. The Bot will prompt the user to enter their username and password. During password entry the user will not see any letters being typed but are input invisibly. This is just for security purposes so that the person next to you does not see your password :)

## Prerequistes for executing Source Code
1. Python 3 and above
Libraries Required:
1. Playsound
2. Selenium
3. Download chromedriver according to your chrome version and OS that you are using from https://chromedriver.chromium.org/downloads . Also, to check Chrome Browser version that you are using right now, search < chrome://version > in the google chrome search bar.

### For setting up Selenium & chromedriver on a Mac, follow the link below
http://jonathansoma.com/lede/foundations-2017/classes/more-scraping/selenium/

## Prerequistes for Executable(.exe)
1. Microsoft Windows Only
2. Use chromedriver according to your chrome version and OS that you are using. Download from here https://chromedriver.chromium.org/downloads . To check chrome version that you are using right now, search < chrome://version > in the google chrome search bar.

## Troubleshooting
1. If the Bot seems to be freezed, go to the Bot's console/terminal window and press any of the arrow keys.
2. If the executable doesn't work, the source .py file is available for you.
3. If you are facing any problems executing the source code then consider upgrading all your python packages. Upgrade your pip to the latest version using `python -m pip install --upgrade pip` and upgrade all your packages to latest versions using `pip install pip-upgrade-outdated`

## Development
If you want to contribute to this project and add more functionality to the Bot then feel free to _Fork_ this repository and submit your changes.
