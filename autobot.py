"""
Autobot v0.01 alpha

COPYRIGHT -> (c) 2020 by Muhammad Fakhri Putra Supriyadi.
LICENSE   -> MIT, see LICENSE for more details.
"""

from subprocess import check_output
from subprocess import call
from bs4 import BeautifulSoup
import stdiomask
import requests
import json
import os
import re


def hello():
    clear()

    TEMPLATE = """
    \r===================================================================
    \r                     ___                ___                ___      
    \r                    (   )              (   )              (   )     
    \r  .---.   ___  ___   | |_       .--.    | |.-.     .--.    | |_     
    \r / .-, \ (   )(   ) (   __)    /0010\   | /   \   /    \  (   __)   
    \r(__) ; |  | |  | |   | |      |10.-.1;  |  .-. | |  .-. ;  | |      
    \r  .'`  |  | |  | |   | | ___  |0|  |1|  | |  | | | |  | |  | | ___  
    \r / .'| |  | |  | |   | |(   ) |0|  |0|  | |  | | | |  | |  | |(   ) 
    \r| /  | |  | |  | |   | | | |  |1|  |1|  | |  | | | |  | |  | | | |  
    \r; |  ; |  | |  ; '   | ' | |  |1'  |0|  | '  | | | '  | |  | ' | |  
    \r' `-'  |  ' `-'  /   ' `-' ;  ' 1`-'0/  ' `-' ;  '  `-' /  ' `-' ;  
    \r`.__.'_.   '.__.'     `.__.    `.01.'    `.__.    `.__.'    `.__.   
    \r
    \r===================================================================
    \r|   Welcome to AUTOBOT, a slightly better version of TEL-U LMS    |
    \r|               created with inner peace by f4r4w4y               |
    \r===================================================================
    """
    print(TEMPLATE, end='')


def menu(what='default'):

    TEMPLATE = """
    \r===================================================================
    \r| [1] All my courses                                              |
    \r| [2] Access course                                               |
    \r| [3] All my messages                                             |
    \r| [4] All events in this month                                    |
    \r| [5] Logout from current account                                 |
    \r| [6] Exit the app                                                |
    \r===================================================================
    """
    print(TEMPLATE, end='')

    try:
        inp = int(input('\r[+] Choose menu (1-6) = '))
        return inp
    except:
        return 0


def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')


def pause():
    input("[#] Press Enter to continue...")


def welcome(fullname, sessionCookie):
    clear()

    TEMPLATE = """
    \r===================================================================
    \r Welcome, {}
    \r Current session = {}
    \r===================================================================
    """
    print(TEMPLATE.format(fullname, sessionCookie), end='')


def show(what):
    if what == 'hello':
        hello()
    elif what == 'menu':
        ret_code = menu()
        return ret_code


class User:
    """
    User class for saving and generating user profiles
    and all the meta.

    Parameters
    ----------
    username : str
        Username of the user
    password : str
        Password of the user
    """
    __username = ''
    __password = ''
    __cookie = ''

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def getSessionCookie(self):
        """Get session cookie based on username and password."""
        return self.__cookie

    def generateSessionCookie(self):
        """
        Generate session cookie based on username and password.

        Returns
        -------
        Str : If Succeed
            Cookie string
        None : Else
        """
        print('[+] Logging in... (Please wait, this will take a while).')
        result = check_output([
            'node',
            'sleepynightnight.js',
            self.__username,
            self.__password,
        ])

        if b'Cookie:' in result:
            result = result.split(b'Cookie: ')[1]

            try:
                resJson = json.loads(result)
                cookie = resJson['value']
                self.__cookie = cookie
                return cookie
            except ValueError:
                print('[!] Failed to decode the resulted json.')

        print('[!] Login failed, there are three possible reasons for this :')
        print('    - username and password not found,')
        print('    - you are not connected to the internet,')
        print('    - https://lms.telkomuniversity.ac.id is currently down.')

        return None

    def addCourse(self, course):
        """
        Add course to current all courses array.

        Parameters
        ----------
        course : dict
            Course to be added

        Returns
        -------
        Boolean
            True if succeed, otherwise False
        """
        if self.__courses:
            self.__courses.append(course)
            return True
        else:
            return False

    def printAllCourses(self):
        """Fancy print all the courses."""
        TEMPLATE = """
        \r {}. Course fullname = {}
        \r    Course shortname = {}
        \r    Category = {}
        """

        print('\r===================================================================')
        if len(self.__courses) <= 0:
            print('[+] Sadly, you\'re not currently enrolled to any course :(')
        else:
            for i, data in enumerate(self.__courses):
                print(TEMPLATE.format(
                    i+1, data['fullname'], data['shortname'], data['coursecategory']), end='')
        print('\r\n===================================================================')

    def printCourseDetail(self, course_id):
        """Fancy print detail of selected course."""
        TEMPLATE = """
        \r {}. Title = {}
        \r    Deskripsi =
        \r{}
        \r 
        \r    Contents =
        \r{}
        """

        selected_course = self.__courses[course_id]

        print('\n\rCourse Fullname = {}'.format(selected_course['fullname']))

        print('\r-------------------------------------------------------------------')
        if len(selected_course['details']) <= 0:
            print('[+] This course doesn\'t has any detail')
        else:
            for i, data in enumerate(selected_course['details']):
                content_str = ''
                summary_str = ''

                if data['contents'] != None and data['contents'] != '' and len(data['contents']) > 0:
                    for content in data['contents']:
                        content_str += f"    | >> {content['text']} [ {content['link']} ] ({content['category']})"
                        if content['mandatory']:
                            content_str += f" |{'COMPLETED' if content['isCompleted'] else 'NOT COMPLETED' }|\n"
                        else:
                            content_str += '\n'

                    if data['summary'] != None and data['summary'] != '' and len(data['summary'].split('\n')) > 0:
                        for summ in data['summary'].split('\n'):
                            summary_str += f"    | {summ}\n"
                    else:
                        summary_str = '    | No description for this topic'

                    print(TEMPLATE.format(
                        i+1, data['topic'], summary_str, content_str), end='')
        print('\r\n-------------------------------------------------------------------')

    def setAllCourses(self, courses):
        self.__courses = courses

    def updateCourses(self, course_id, details):
        self.__courses[course_id].update(details)

    def getAllCourses(self):
        try:
            return self.__courses
        except:
            return None


class Web:
    """
    Web class for saving session and all the state.

    Parameters
    ----------
    cookie : str
        Cookie of corresponding credential
    """
    BASE_DOMAIN = 'https://lms.telkomuniversity.ac.id{}'

    GET_URL = {
        'home': '/my',
        'logout': '/login/logout.php?sesskey={apikey}',
        'course': {
            'participants': '/user/index.php?id={course_id}&page={iteration}',
            'categories': ['resource', 'url', 'forum', 'chat', 'discussion', 'assign', 'quiz']
        }
    }

    POST_URL = {
        'events': '/lib/ajax/service.php?sesskey={apikey}&info=core_calendar_get_action_events_by_timesort',
        'courses': '/lib/ajax/service.php?sesskey={apikey}&info=core_course_get_enrolled_courses_by_timeline_classification'
    }

    POST_DATA = {
        'events': '[{\
            "index": 0,\
            "methodname": "core_calendar_get_action_events_by_timesort",\
            "args": {\
                "limitnum": 20,\
                "timesortfrom": {from_time},\
                "timesortto": {to_time},\
                "limittononsuspendedevents": true\
            }\
        }]',
        'courses': '[{\
            "index": 0,\
            "methodname": "core_course_get_enrolled_courses_by_timeline_classification",\
            "args": {\
                "offset": 0,\
                "limit": 0,\
                "classification": "all",\
                "sort": "fullname",\
                "customfieldname": "",\
                "customfieldvalue": ""\
            }\
        }]'
    }

    __session = ''
    __apikey = ''

    def __init__(self, cookie):
        self.__session = requests.Session()
        cookie_obj = requests.cookies.create_cookie(
            domain='lms.telkomuniversity.ac.id',
            name='MoodleSession',
            value=cookie
        )
        self.__session.cookies.set_cookie(cookie_obj)

    def logout(self):
        """
        Log current user out.

        Returns
        -------
        Boolean
            True if succeed, otherwise False
        """
        res = self.__session.get(
            self.BASE_DOMAIN.format(self.GET_URL['logout']))
        if self.BASE_DOMAIN.format(self.GET_URL['home']) in res.text:
            self.__session = ''
            self.__apikey = ''
            return True
        else:
            return False

    def parseApiKey(self):
        """
        Parse api key (or in this case session key) from homepage html.

        Returns
        -------
        Boolean
            True if succeed, otherwise False
        """
        res = self.__session.get(self.BASE_DOMAIN.format(self.GET_URL['home']))
        soup = BeautifulSoup(res.text, 'html.parser')
        hidden_inp = soup.find_all(attrs={"name": "sesskey"})
        if len(hidden_inp) > 0:
            try:
                chosen_inp = hidden_inp[0]
                self.__apikey = chosen_inp.attrs['value']
                return True
            except:
                print('[!] Error parsing API key')
                return False
        else:
            print('[!] Error parsing API key')
            return False

    def parseCourse(self, user, course_id):
        """
        Parse all data for corresonding course

        Parameters
        ----------
        user: User
            current user class object
        course_id: int
            id of the course that want to be parsed        
        """
        courses = user.getAllCourses()
        selected_course = courses[course_id]

        res = self.__session.get(selected_course['view_url'])
        soup = BeautifulSoup(res.text, 'html.parser')

        all_details = []

        topics = soup.find_all(attrs={"class": "topics"})[0]
        sections = topics.find_all('li', recursive=False)

        for section in sections:
            details = {}

            # Add topic text if any
            try:
                details['topic'] = section.find_all(
                    attrs={'class': 'wdm-sectionname'})[0].a.string
            except:
                pass

            # Parse summary if any
            try:
                summary = section.find_all(
                    attrs={'class': 'summary'})[0]
                summ_text = str(summary.text)

                result = ''
                temp = ''

                found = False
                for pos, char in enumerate(summ_text):
                    temp += char

                    if summary.find(text=temp) != None:
                        found = True
                        if pos == len(summ_text)-1:
                            result += temp

                            try:
                                parent = summary.find(text=temp).parent
                                elements = re.findall(
                                    r'<[^>]+>$', str(re.sub(temp + '.*', '', parent)))
                                if '<a' in elements[-1]:
                                    for element in elements[::-1]:
                                        if 'href' in element:
                                            soup = BeautifulSoup(
                                                element, 'html.parser')
                                            result += '[ ' + \
                                                soup.a['href'] + ' ]'
                                            break
                            except:
                                pass

                    else:
                        if found:
                            result += temp[:-1] + '\n'

                            try:
                                parent = summary.find(text=temp[:-1]).parent
                                elements = re.findall(
                                    r'<[^>]+>$', str(re.sub(temp + '.*', '', parent)))
                                if '<a' in elements[-1]:
                                    for element in elements[::-1]:
                                        if 'href' in element:
                                            soup = BeautifulSoup(
                                                element, 'html.parser')
                                            result += '[ ' + \
                                                soup.a['href'] + ' ]'
                                            break
                            except:
                                pass

                            temp = temp[len(temp)-1:]
                            found = False

                details['summary'] = result
            except:
                pass

            # Add contents if any
            contents = []
            links = section.find_all(attrs={"class": "activityinstance"})
            for link in links:
                for category in self.GET_URL['course']['categories']:
                    href = link.a['href']
                    text = link.a.span.contents[0]
                    sibling = link.find_next_sibling(
                        attrs={"class": "actions"})
                    if category in href:
                        content = {
                            'text': text,
                            'link': href,
                            'category': category,
                            'mandatory': True if sibling != None else False,
                        }

                        try:
                            content['isCompleted'] = False if 'Not completed:' in sibling.img['alt'] else True
                        except:
                            pass

                        contents.append(content)

            details['contents'] = contents
            all_details.append(details)

        # Update user courses with parsed details
        course_details = {'details': all_details}
        user.updateCourses(course_id, course_details)

    def parseCourses(self, user):
        """
        Parse all user courses.

        Parameters
        ----------
        user: User
            current user class object
        """
        course_url = self.POST_URL['courses'].format(apikey=self.__apikey)
        course_data = self.POST_DATA['courses']
        res = self.__session.post(
            self.BASE_DOMAIN.format(course_url), data=course_data)

        try:
            resJson = json.loads(res.text)

            result = resJson[0]
            isError = result['error']

            if not isError:
                # Filter out only important data
                data = result['data']
                courses = data['courses']
                courses = [{
                    'fullname': x['fullname'].replace('\n', ' '),
                    'shortname': x['shortname'],
                    'course_id': x['id'],
                    'view_url': x['viewurl'],
                    'coursecategory': x['coursecategory']
                } for x in courses]

                user.setAllCourses(courses)
            else:
                print('[!] Error fetching courses data.')
        except ValueError:
            print('[!] Failed to decode the resulted json.')

    def parseEvents(self, user, from_time, to_time):
        """
        Parse all user events with range
        of 2 timestamps.

        Parameters
        ----------
        user: User
            current user class object
        from_time: int
            timestamp of starting date
        to_time: int
            timestamp of ending date
        """
        event_url = self.POST_URL['events'].format(apikey=self.__apikey)
        event_data = self.POST_DATA['events'].format(
            from_time=from_time, to_time=to_time)
        res = self.__session.post(
            self.BASE_DOMAIN.format(event_url), data=event_data)

        try:
            resJson = json.loads(res.text)

            result = resJson[0]
            isError = result['error']

            if not isError:
                # Filter out only important data
                data = result['data']
                events = data['events']
                events = [{
                    'id': x['id'],
                    'name': x['name'],
                    'course_id': x['course']['id'],
                    'view_url': x['viewurl'],
                } for x in events]
            else:
                print('[!] Error fetching events data.')
        except ValueError:
            print('[!] Failed to decode the resulted json.')


def ask_retry():
    retry = str(input('\r[#] Retry ? (y/n)'))
    if retry == 'y':
        main()
    elif retry == 'n':
        return
    else:
        ask_retry()


def main():
    show('hello')

    username = str(input('\r[+] Input your username = '))
    password = stdiomask.getpass(
        prompt='\r[+] Input your password = ', mask='●')

    currentUser = User(username, password)
    sessionCookie = currentUser.generateSessionCookie()

    if sessionCookie:
        process = Web(sessionCookie)

        print('[+] Parsing api key...')

        if process.parseApiKey():
            logout = False
            while not logout:
                welcome(username, sessionCookie)

                inp = show('menu')
                if inp == 1:
                    # Parse all courses
                    print('[+] Parsing all courses...')
                    process.parseCourses(currentUser)

                    if currentUser.getAllCourses() != None:
                        currentUser.printAllCourses()

                elif inp == 2:
                    # Access one of the course
                    if currentUser.getAllCourses() == None:
                        print('[+] Parsing all courses...')
                        process.parseCourses(currentUser)

                    courses = currentUser.getAllCourses()
                    currentUser.printAllCourses()

                    try:
                        course_id = int(
                            input('\r[+] Choose course to parse (1 - {}) = '.format(len(courses)))) - 1
                    except:
                        print('[!] Wrong input...')
                        print('    Choose only between 1 - {}'.format(len(courses)))
                        pass

                    process.parseCourse(currentUser, course_id)
                    currentUser.printCourseDetail(course_id)

                elif inp == 3:
                    # Parse all my messages
                    print(
                        '[+] This feature have not created yet (might even won\'t :v)')

                elif inp == 4:
                    # Parse all event in this month
                    print(
                        '[+] This feature have not created yet [i still dont have the sample to parse :(]')

                elif inp == 5:
                    # Logout current account
                    if process.logout():
                        logout = True
                        print('[+] Logout successfully')
                    else:
                        print('[!] Logout failed...')

                elif inp == 6:
                    # Exit the app
                    print('[#] Thanks for using this app :D')
                    break

                else:
                    # Input is out of range
                    print('[!] Wrong input...')

                pause()
            else:
                main()  # User logout, back to login screen
        else:
            # Couldn't parse the api key, terminate app
            print('[!] Try running the script again.')
            print('    If the problem persist, contact the creator.')
    else:
        # Couldn't log the user in, ask for retry
        ask_retry()


if __name__ == "__main__":
    main()
