from django.shortcuts import render,redirect



import psycopg2

# PostgreSQL connection parameters
db_config = {
    'dbname': 'railway',
    'user': 'postgres',
    'password': 'UinbkcXWLRHOEiTRXhjTkJumhgqRvjCh',
    'host': 'viaduct.proxy.rlwy.net',
    'port': '34452'
}



universal_username = None

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

    # Fetch all rows from the result set
        rows = cursor.fetchall()

        # command = 'select * from user where username = %s'
        # mycursor.execute(command,(username,))

        res = rows

        if len(res)!=0 and res[0][-1] == password:
            universal_username = username

            # home(request)
            user_data = {
                'username' : universal_username
            }
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

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            err_msg = {
                'error':'Password does not match !'
            }
            return render(request,'register.html',err_msg)


        command = "INSERT INTO \"user\" (name, username, email, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(command, (name, username, email, password1))
        connection.commit()

        return redirect('home')

    else:
        return render(request,'register.html')


def home(request):
    login(request)
    # universal_username = getuser()
    user_data = {
        'username' : universal_username
    }


    return render(request,'home.html',user_data)
def techblog(request):
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    link = 'null'
    username = 'fx818'

    sql_query = "SELECT content FROM \"blogs\";"

    id_query = "select id from \"blogs\";"
    cursor.execute(id_query)
    id = cursor.fetchall()
    nid = id[-1][0]

    cursor.execute(sql_query)


    rows = cursor.fetchall()
    # result = rows[-1:-4:-1]
    result = rows

    value = {
            'data':result
    }

    if request.method == 'POST':
        content = request.POST['content']
        query = 'insert into blogs values(%s,%s,%s,%s)'
        values = (nid+1,username,content,link)
        cursor.execute(query,values)
        connection.commit()

        sql_query = "SELECT content FROM \"blogs\";"
        cursor.execute(sql_query)


        rows = cursor.fetchall()
        result = rows[-1:-4:-1]

        value = {
                'data':result
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

    return render(request,'hackathon.html')

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
    rank = 1
    user_name = 'Yash Chaudhary'
    skill_1 = 'C++'
    skill_2 = 'Python'
    skill_3 = 'Database'
    activity_1 ='Operating System Notes'
    activity_2 ='Software Engineering'
    activity_3 ='Principles Of Programming Language'
    gender= 'Male'
    country = 'India'
    linkedin = 'xyz@gmail.com'
    activity_points = int(30210)
    context = {'user_name':user_name,
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
    return render(request,'notespedia.html')
# random

