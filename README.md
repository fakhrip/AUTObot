# Story

So this all started when someday in the morning (iirc) i just told by one of my lecturers that i have to open this site [LMS Telkom University](https://lms.telkomuniversity.ac.id) in order for me to access all my lectures in my university (you guess it). 

But when i enter the site, i realize one thing immediately, why a big organization like this just created a site for online course using [moodle](https://moodle.com/), i mean yeah sure thing that its a "kinda" good LMS, but for a big organization like this why dont they just create an LMS by themselves, i mean its a college level (world class university) bruh...

And i kinda sad about all this and moreover the site looks ugly for sure, there are no notifications whatsoever, it kinda lag, and also i found self xss inside the chat feature (but its not a big deal tho).

# Workaround

And because of all these things that have broken my inner peace, then i will not just sit on my chair and do nothing, i mean ofc i still need to sit on my chair to create the script :v, so **let me bring the justice for all of us** (crickets sound).

# Critics

Wait, why would i even want to criticize myself ? :thonkang:.

----

#### Shhh

While developing this, i got a good idea so i named my script `autobot` that defeat this silly moodle thingy (`decepticon`) wkwkwk.

----

# Technicality

Alright, for all of you who read this and does really care about the technical stuff in this project, then im gonna spit it out here :

### Technology

- [NightmareJS](http://www.nightmarejs.org/)
  > I use this for browser automation part, and in this case, i used it for logging you guys in to the silly moodle thingy and grab the cookie for use throughout the whole system

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  > This one is for the web scraping part where i scrape the resulted html content and grab all the data you guys might need

- [PyInstaller](https://www.pyinstaller.org/)
  > Inspired by one of the CTF challenge i got when i play COMPFEST12 CTF competition (many thanks to the problem setter)  

  > Its a python packer, so i kinda be able to "compile" my python script so everyone without technical ability can still use the script without ever doing some cumbersome stuff

- [Python](https://www.python.org/download/releases/3.0/)
  > Do i even have to explain this one ?

### Requirement

- NodeJS
- Npm
- Python3 (with all the required modules)
- Terminal (cause i really lazy to create the frontend for this, **in case anyone reading this want to contribute by creating the frontend, feel free to contact [me](https://fakhrip.github.io)**, and maybe together we can defeat decepticon :D)
- Brain

### Project Tree

telkom-u lms automation  
 ┣ [README.md](#)  
 ┣ [autobot.py](./autobot.py) (Main Script)  
 ┣ [install.sh](./install.sh) (Installation Script)  
 ┗ [sleepynightnight.js](./sleepynightnight.js) (LMS Login Script)


### Misc

Why did i call the login script as sleepynightnight.js (referenced from spies in disguise) ?, cause its nightmare, you got it ? nvm.

----

# How To Use

Okay im gonna straight to giving you step by step of how to install and use this thing

- Open terminal / command prompt / whatever you call it
- Move to the directory of the project (`cd wherever/you/put/this/thing`)
- Run the install.sh script (`./install.sh`)
- Run the application (`./autobot`)

### Error

In case of any error persisted in the app or installation process, create issue in this repository (in case you know how to do it), and if you dont, then just contact me.

And also make sure you know how to reproduce the error, because otherwise i cant help to fix the bug.

----

# Future work

This is some of my plan for the future work (urgency level goes down the list) : 

- [ ] Complete all the features (chat not included)  
- [ ] Add local DB system to remember user account, manage all data, and provide some fancy statistics stuff  
- [ ] Add notification system  
- [ ] Add logging system so its easier to trace if someone else using this got a bug  
- [ ] Change all the frontend to a website instead of simple terminal stuff

----

# WARNING

Please use my version only if you dont really understand coding stuff as its safe, and **i promise that i never dump all your username nor password**.

**Otherwise, I will take no responsibility and any guarantee of security** if you use other version of the app rather than this one that i provide.