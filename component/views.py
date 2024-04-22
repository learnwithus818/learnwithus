from django.shortcuts import render,redirect



import psycopg2

# PostgreSQL connection parameters
# db_config = {
#     'dbname': 'postgres',
#     'user': 'fx818',
#     'password': '@Anurag818@',
#     'host': 'learnwithus.postgres.database.azure.com',
#     'port': '5432'
# }

# db_config = psycopg2.connect(user="fx818", password="@Anurag818@", host="learnwithus.postgres.database.azure.com", port=5432, database="postgres")


db_config = {
    'user': 'fx818',
    'password': '@Anurag818@',
    'host': 'learnwithus.postgres.database.azure.com',
    'port': 5432,
    'database': 'postgres'
}

connection = psycopg2.connect(**db_config)




universal_username = None
name = None
data = ''

# import attr
# @attr.s(frozen=True)
# class ImmutableClass:
#     universal_username = attr.ib()

# obj = ImmutableClass("Test Name")




def logout(request):
    global universal_username
    universal_username = None
    user_data = {
        'username' : None,
        'name' : None
    }

    return render(request,'home.html',user_data)


def login(request):

    connection = psycopg2.connect(**db_config)
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        if len(username)==0 or len(password)==0:
            errormsg = {'error':'Username or password is empty !'}
            return render(request,'index.html',errormsg)

        sql_query = "SELECT * FROM \"user\" where username = %s;"
        cursor.execute(sql_query,(username,))

        rows = cursor.fetchall()
        res = rows

        global name
        name = res[0][0]

        if len(res)!=0 and res[0][-1] == password:

            global universal_username
            universal_username = (username,)

            # home(request)
            user_data = {
                'username' : universal_username[0],
                'name' : name
            }
            # data = username
            return render(request,'home.html',user_data)
            # return redirect('home')

        else:
            errormsg = {'error':'Username or password is incorrect !'}
            return render(request,'index.html',errormsg)

        # return redirect('index')

    else:
        return render(request,'index.html')


def register(request):
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        skills = request.POST['skills']
        gender = request.POST['gender']
        country = request.POST['country']
        linkedin = request.POST['linkedin']
        activitypoint = 0

        query = "select rank from \"profile\";"
        cursor.execute(query)

        res = cursor.fetchall()
        rank = int(res[-1][0])

        if password1 != password2:
            err_msg = {
                'error':'Password does not match !'
            }
            return render(request,'register.html',err_msg)

        command1 = "INSERT INTO \"user\" (name, username, email, password) VALUES (%s, %s, %s, %s)"
        command2 = "INSERT INTO \"profile\" (rank, username, skills, gender, country, linkedin, activitypoint) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(command1, (name, username, email, password1))
        connection.commit()
        cursor.execute(command2, (rank+1,username,skills,gender,country,linkedin,activitypoint))
        connection.commit()

        return redirect('home')

    else:
        return render(request,'register.html')


def home(request):
    if universal_username is None:
        return render(request,'home.html')

    user_data = {
        'username' : universal_username[0],
        'name' : name
    }
    return render(request,'home.html',user_data)


def techblog(request):
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    # global universal_username
    global universal_username
    username = universal_username

    sql_query = "SELECT content FROM \"blogs\";"

    id_query = "select id from \"blogs\";"
    cursor.execute(id_query)
    id = cursor.fetchall()
    nid = id[-1][0]

    cursor.execute(sql_query)


    rows = cursor.fetchall()
    # result = rows[-1:-4:-1]
    result = rows[::-1]


    value = {
            'data':result,
            'username':universal_username
    }

    if request.method == 'POST':
        content = request.POST['content']
        link = request.POST['reflink']

        sql_query = "SELECT content FROM \"blogs\";"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        result = rows[::-1]


        if len(content)==0 or content == "Start writing your blog here....(Please remove this text)" or content=='nill':
            
            errmsg={
                'username':universal_username,
                'error':'Please write some of your content !',
                'data':result,
                'username':universal_username

            }

            if content=='nill':


                errmsg['error']  = ''

                return render(request,'techblog.html',errmsg)

        query = 'insert into blogs values(%s,%s,%s,%s)'
        values = (nid+1,username,content,link)
        cursor.execute(query,values)
        connection.commit()  
        sql_query = "SELECT content FROM \"blogs\";"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        result = rows[::-1]

        content = 'nill'

        value = {
                'data':result,
                'username':universal_username
        }

        return render(request,'techblog.html',value)

    else:
        return render(request,'techblog.html',value)

def hackathon(request):

    if request.method == 'POST':
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        # Collecting the data from the form
        team = request.POST['team']
        college = request.POST['college']
        lead = request.POST['lead']
        leadmobile = request.POST['leadmobile']
        leadmail = request.POST['leadmail']
        mem2 = request.POST['mem2']
        m2mobile = request.POST['m2mobile']
        mem3 = request.POST['mem3']
        m3mobile = request.POST['m3mobile']
        year = request.POST['year']
        branch = request.POST['branch']

        values = (team,college,lead,leadmobile,leadmail,mem2,m2mobile,mem3,m3mobile,year,branch)

        try:
            query = "insert into hackathon24 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(query,values)
            connection.commit()
        except:
            err = {
                'error':"Something went wrong please check again or try again later"
            }
            return render(request,'hackathon.html',err)



        return render(request,'msg.html')
    global universal_username
    user_data = {
        'username' : universal_username[0]
    }
    return render(request,'hackathon.html',user_data)

def opportunities(request):
    return render(request,'opportunities.html')

def githubblog(request):
    return render(request,'allblogs/explore-github.html')

def msg(request):
    return render(request,'msg.html')


def courses(request):
    return render(request,'courses.html')


def linux(request):
    return render(request,'linux.html')

def python(request):
    return render(request,'python-course.html')


def book(request):
    return render(request,'book.html')


def about(request):
    return render(request,'about.html')


def copyright(request):
    return render(request,'copyright.html')

def contact(request):
    if request.method == 'POST':

        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()

        name = request.POST['name']
        college = request.POST['college']
        mobile = request.POST['mobile']
        email = request.POST['email']
        question = request.POST['question']
        values = (name,college,mobile,email,question)

        if len(name)==0 or len(mobile)==0 or len(email)==0:
            err_msg = {
                'error':'Sorry could not submit the data. Some error occured ! Please fill the form correctly !'
            }
            return render(request,'contact.html',err_msg)

        try:
            # if len(name)==0 or len(mobile)==0 or len(email)==0 or len(question)==0:
            query = "insert into query values(%s,%s,%s,%s,%s);"
            cursor.execute(query,values)
            connection.commit()

        except:
            err_msg = {
                'error':'Sorry could not submit the data. Some error occured !'
            }
            return render(request,'contact.html',err_msg)

        return render(request,'msg.html')


    return render(request,'contact.html')

def profile_page(request):

    if universal_username is None:
        return render(request,'loginerror.html')

    user_data = {
        'username' : universal_username[0]
    }

    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()


    sql_query = "SELECT * FROM \"profile\" where username=%s;"
    cursor.execute(sql_query,(universal_username,))

    retrieved_data = cursor.fetchall()
    retrieved_data = retrieved_data[0]

    res = retrieved_data


    rank = res[0]
    user_name = user_data['username']

    skills = res[2].split(',')

    skill_1 = skills[0]
    skill_2 = skills[1]
    skill_3 = skills[2]
    activity_1 ='Operating System Notes'
    activity_2 ='Software Engineering'
    activity_3 ='Principles Of Programming Language'
    gender= res[3]
    country = res[4]
    linkedin = res[5]
    activity_points = res[6]
    context = {'username':user_name,
               'rank': rank,
               'skill_1':skill_1,
               'skill_2':skill_2,
               'skill_3':skill_3,
               'activity_1':activity_1,
               'activity_2':activity_2,
               'activity_3':activity_3,
               'gender':gender,
               'country':country,
               'linkedin':linkedin,
               'activity_points':activity_points
               }

    return render(request,'profile_page.html' ,context )

def notespedia(request):
    opportunities_for_fresher= ['Web Developer', 'App Developer' , 'Software Engineer', 'iOS Engineer', 'AI Developer', 'NLP Engineer', 'Data Scientist','Data Analyst', 'Data Engineer', 'Course Engineer']
    referance_books=['Sebesta, "Concept of Programming Language", Addison Wesley, 4th Edition, 2019',
                     ' Deitel & Deitel, “Internet and World Wide Web – How to Program”, Goldberg,Pearson Education. 3rd Edition 2003',
                     'Petersons, "Operating Systems", Addison Wesley, 9th Edition, 2012',
                     'Forouzan, B. A., Data Communications and Networking, McGraw-Hill Higher Education,3rd Edition, 2004.',
                     'A.S. Tannenbaum, “Computer Networks”, 3rd Edition, Prentice Hall India, 1997.']
    context= {
        'opportunities_for_fresher':opportunities_for_fresher,
        'referance_books':referance_books
    }
    return render(request,'notespedia.html',context)



def cse(request):
    return render(request,'cse.html')



def et(request):
    return render(request,'et.html')


def loginerror(request):
    return render(request,'loginerror.html')

def team(request):
    return render(request,'team.html')




# connection = psycopg2.connect(**db_config)
# cursor = connection.cursor()
# query = "select rank from \"profile\";"
# cursor.execute(query)

# sql_query = "SELECT * FROM \"user\" where username = 'edith27401';"
# cursor.execute(sql_query)

# rows = cursor.fetchall()
# res = rows
# print(res[0][0])


# random