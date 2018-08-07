#!/usr/bin/python3
# shebang line

################################################################################
        # FILE INFORMATION
################################################################################
# Grant Gregory
# ggregory@bu.edu
# GWGpage.py
# Website: http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py
#
#
# This is an application that serves as a website for GWG
#
#

###############################################################################
        # NOTES
################################################################################ 

################################################################################
        # HTML HEADERS AND IMPORT FUNCTIONS
################################################################################

# create html headers
print("Content-Type: text/html")
print() # blank line

import MySQLdb as db    # the mysql database API 
import time
import cgi  
import cgitb; cgitb.enable()# web debugging package; always import it into web apps

################################################################################
        # FUNCTIONS
################################################################################
# Function 1: Establish database connection
# TO DO: N/A
def getConnectionAndCursor():
    """
    This function will connect to the database and return the
    Connection and Cursor objects.
    """   
 
    # establish connection to database
    conn = db.connect(host="localhost",
                  user="ggregory", 
                  passwd="9421",
                  db="cs108_ggregory_project")

    cursor = conn.cursor()
    return conn, cursor

################################################################################
# Function 2: Administrative - HTML head - styling and javascript
# TO DO: N/A
def DoHTMLHead(title):
    '''
    This function creates the HTML head for the webpage -
    Incorporates styling to format the webpage in an appealing manner.
    Adds javascript functions to validate form entry.
    '''

    ### print out all the head information:

    # establish overall styling
    print("""
    <html>
    <head>
    <title>%s</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#00477e" />
    <!-- Import fonts and CSS from w3 and Google -->
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css">
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-highway.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato"> 
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Import Tracker for Google Analytics -->
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-121701024-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-121701024-1');
    </script>
    <!-- HTML Styling -->
    <style>
    h1,h2 {font-family: "Lato", sans-serif;}
    html,body,h3,h4,h5,h6 {"Roboto", sans-serif;}
    .w3-bar,h1,button {font-family: "Montserrat", sans-serif;}
    </style>
    """  % title)

    # print navbar
    print("""
    <body>
        <!-- Navbar -->
        <div class="w3-top">
          <div class="w3-bar w3-highway-blue w3-card w3-left-align w3-large">
            <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-left w3-animate-left w3-padding-large w3-hover-black w3-large" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>             
            <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py" class="w3-bar-item w3-button w3-hover-white w3-animate-left">Home</a>
            <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py?ResumePage=Resume" class="w3-bar-item w3-button w3-hide-small w3-hover-black w3-animate-left">Resume</a>
            <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py?PortfolioPage=Portfolio" class="w3-bar-item w3-button w3-hide-small w3-hover-black w3-animate-left">Portfolio</a>
            <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py?ContactPage=Contact" class="w3-bar-item w3-button w3-hide-small w3-hover-black w3-animate-left">Contact Me</a>
          </div>

          <!-- Navbar on small screens -->
          <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">
            <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py?ResumePage=Resume" class="w3-bar-item w3-button w3-padding-large w3-animate-left">Resume</a>
            <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py?PortfolioPage=Portfolio" class="w3-bar-item w3-button w3-padding-large w3-animate-left">Portfolio</a>
            <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py?ContactPage=Contact" class="w3-bar-item w3-button w3-padding-large w3-animate-left">Contact Me</a>
          </div>
        </div>

    """)

################################################################################
# Function 3: Administrative - HTML footer
# TO DO: N/A
def DoHTMLTail():
    '''
    This function creates the HTML tail for the webpage.
    '''

    # close off the body div tags and create the footer with a link to get back to the homepage
    print("""
    </div>
    </div>
   
    <!-- Footer -->
    <footer id="myFooter">
    <div class="w3-container w3-highway-blue w3-padding-32">
        <h4><hr>This page was generated at %s.<br>
        <a href="./GWGpage.py"> Return to home page.</a></h4>
            <!-- LINK TO DANIEL'S Website -->
        <a href="./GWGpage.py?ContactPage=Contact+Me"> Contact Me.</a>
    <!-- href="https://danielc3511.wixsite.com/abcd">Daniel's Website -->
    </div>

    <div class="w3-container w3-theme-l1">
        <p>Coded by Grant Gregory</p>
    </div>
    </footer>

<script>
// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else { 
        x.className = x.className.replace(" w3-show", "");
    }
}
</script>
    </body>
    </html>

    """ % time.ctime())

################################################################################
# Function 4: Administrative - Debugging the web application
def DebugFormData(form):
    """
    A helper function which will show us all of the form data that was
    sent to the server in the HTTP form.
    """

    # match styling of website and print out table of form values
    print("""
        <hr>
        <h2 class="w3-text-teal">DEBUGGING INFORMATION:</h2>
    <p>
    Here are the HTTP form fields:

    <table border=1>
        <tr>
            <th>key name</th>
            <th>value</th>
        </tr>
    </div>
    </div>
    """)
    
    # form behaves like a python dict
    keyNames = form.keys()
    # note that there is no .values() method -- this is not an actual dict

    ## use a for loop to iterate all keys/values
    for key in keyNames:

        ## discover: do we have a list or a single MiniFieldStorage element?
        if type(form[key]) == list:

            # print out a list of values
            values = form.getlist(key)
            print("""
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, str(values)))

        else:
            # print the MiniFieldStorage object's value
            value = form[key].value
            print("""
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, value))
        
    print("""
    </table>
    <h3>End of HTTP form data.</h3>
    <hr>
    """)

################################################################################
def WelcomePage():
    '''
    this is a comment
    '''
    
    # print header to have banner with logo and three buttons
    print("""
    <!-- Main Page -->
    <!-- Header -->
    <header class="w3-container w3-highway-blue w3-center" style="padding-top:50px; padding-bottom:10px;">
        <!-- text blue: style="padding:50px 16px; color:#000099" -->
      <h1 class="w3-margin w3-jumbo w3-animate-opacity">Grant W. Gregory</h1>
      
      <p class="w3-large w3-animate-opacity">Driven, Intellectual, Coachable</p>
      
    </header>

    <!-- Grid -->
    <div class="w3-row-padding w3-padding-64 w3-container">
      <div class="w3-content w3-animate-opacity">
        <div>

        <!-- paragraph on Myself -->
        <style>
.circular--square {
  border-radius: 50%;
  height: 300px;
  width: auto;
  
}
        </style>

        <div style="text-align: center;">
            <img class="circular--square" src="BUsquare.jpg" alt="avatar" class="profile-pic">
        
        <h3>
<b>Boston University
<br>
Division I Men's Lacrosse Player
<br>
Questrom School of Business | Kilachand Honors College '19
<br>
Finance and Information Systems Major</b>
<br>
<span style="color:#00477e">Greater Boston Area</span>
</div>

</h3>
        </p>


            <!-- form for action buttons -->
            <form>
                <center><input type="submit" name="ResumePage" value="Resume"  style="width:40%" class="w3-button w3-highway-blue w3-padding-large w3-large w3-margin-top" w3-hover-black></center>
                <center><input type="submit" name="PortfolioPage" value="Portfolio"  style="width:40%" class="w3-button w3-highway-blue w3-padding-large w3-large w3-margin-top" w3-hover-black></center>
                <center><input type="submit" name="ContactPage" value="Contact Me" style="width:40%" class="w3-button w3-highway-blue w3-padding-large w3-large w3-margin-top" w3-hover-black></center>
            </form> 


<br><br>
<h1>About Me:</h1>
I am an undergraduate student in Boston University's Questrom School of Business,
as well as one of 250 students in the Kilachand Honors College; I am pursuing a degree in Business Administration with a
concentration in Finance and Information Systems. 
<br><br>
I have a passion for technology and finance, a strong fervor for continued learning, and a love for problem solving.
I utilize my exemplary work ethic to push past my limits and excel in whatever I partake in.
I connect with and unite people from all walks of life, and have used this to <a href="http://www.bu.edu/khc/for-current-students/student-groups-2/klab/?csspreview=true">lead my peers in the honors college</a>,
captain multiple varsity sports teams, lead my Boy Scout Troop, and more. 
<br><br>
I seek to gain further experience in the investment banking and leveraged finance arena, and plan to utilize my work ethic,
ability to perform in high-pressure situations, as well as my overall coachability to
allow me to quickly learn and work effectively in team settings.
<br><br>

        </div>
      </div>
    </div>

    </div>
</div>
    """)


################################################################################
def ResumePage():
    '''

    '''

    print("""
<!-- Grid -->
<!-- This grid and image header are on all subsequent presentation functions -->
<div class="w3-row-padding w3-padding-64 w3-container">
  <div class="w3-content w3-animate-opacity">
    <h2><b>Resume:</b></h2>
    <iframe src="http://docs.google.com/gview?url=http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWG_7.20.18.pdf&embedded=true" frameborder="0"></iframe>

    <br>
    <table align="center">
    <tr>
    <td>
        <a href="GWG_7.20.18.pdf" download class="w3-bar-item w3-button w3-highway-blue w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">Download</a>
    </td>
    <td>
    <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">Home</a>    
    </td>
    </tr>
    </table>

    <style>
iframe {
    width: 100%;
    margin-right:auto;
    margin-left:auto;
    display: block;
    
    height: 70%;
}

@media only screen and (min-width: 768px) {
    iframe {
        height: 1080px;
    }
}
</style>
        """)

################################################################################
def PortfolioPage():
    '''

    '''
    print('''
    <!-- Grid -->
    <!-- This grid and image header are on all subsequent presentation functions -->
    <div class="w3-row-padding w3-padding-64 w3-container">
      <div class="w3-content w3-animate-opacity">

        <h2><b>Portfolio:</b></h2>
    
        Numerous projects I have created - each one encompases a different discipline.
        <br>
        Jump to a specific seciton:
        <table>
        <tr>
        <td>
            <a href="#section1" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:100px; margin-right:auto; margin-left:auto; display:block;">Business</a>
        </td>
        <td>
            <a href="#section2" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:100px; margin-right:auto; margin-left:auto; display:block;">Coding</a>    
        </td>
        <td>
            <a href="#section3" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:100px; margin-right:auto; margin-left:auto; display:block;">Research</a>    
        </td>
        </tr>
        </table>
        <br>
        <br>

        <p>
        <span class="anchor" id="section1"></span>
        <div class="section">
        <h3><b>Core Business Project: Complete Business Plan</b></h3>
        <a href="http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/Slides.pdf" target="_blank"><img src="RemBandLogo.png" alt="RemBand" width="150" height=auto></a>
        <h5>
        I created this business plan with a team of nine other students in the business school;
        together, we created a business plan for RemBand - a Life Alert and FitBit inspired product.
        The business plan includes a comprehensive marketing plan, operations strategy, and accompanying financial projections and risk projections.
        I constructed all of the financial statements, calculated our VaR figures, and helped design our pitch deck.
        <br>
        <table>
        <tr>
        <td>
            <a href="http://docs.google.com/gview?url=http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/Slides.pdf" target="_blank" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">Pitch Deck</a>    
        </td>
        <td>
            <a href="http://docs.google.com/gview?url=http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/RemBand.pdf" target="_blank" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">Business Plan</a>
        </td>
        <td>
            <a href="http://docs.google.com/gview?url=http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/IntegratedWorkbook.xlsx" target="_blank" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">Integrated Workbook</a>    
        </td>
        </tr>
        </table>
        <br>
        </h5>
        </p>
        </div>

        <p>
        <span class="anchor" id="section2"></span>
        <div class="section">
        <h3><b>Coding Project: Medical Record Database</b></h3>
        <br>
        <a href="http://apollohealth.net"><img src="ApolloLogoOptimized.png" alt="Apollo" width="150" height=auto></a>
        <h5>
        This coding project is a prototype for my Senior Keystone Project for the Honors College;
        By creating a database through MySQL, I developed a python web application for my CS108 class that can
        create, modify, or delete records in the database. I also created a YouTube video to walk through the project.
        During this project, I tought myself JavaScript and CSS in order to provide enhanced functionality for my app.
        <br>
        <table>
        <tr>
        <td>
            <a href="http://apollohealth.net" target="_blank" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">View the App</a>
        </td>
        <td>
            <a href="https://youtu.be/dlvu-XYp2DQ" target="_blank" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">YouTube Video Tour</a>
        </td>
        </tr>
        </table>
        <br>
        </h5>
        </p>
        </div>
        
        <p>
        <span class="anchor" id="section3"></span>
        <div class="section">
        <h3><b>Research Paper: Technology's Enslavement of the Working Classes</b></h3>
        <h5>
        This research paper examines the abhorent conditions of the working classes during Victorian England's Industrial Revolution
        and shows how many developing countries (ex: the Congo) suffer from this same poor quality of life as they mine metals used in today's
        electronic devices. My thesis states that as technology progresses, the onus of providing the fuel for that technology falls upon a small section of society;
        as demand for fuel increases (whether that be coal, cobalt, etc.), living and working conditions worsen until
        unfathomable poverty prevades these communities.
        <br>
        <table>
        <tr>
        <td>
            <a href="http://docs.google.com/gview?url=http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/ResearchPaper.pdf" target="_blank" class="w3-bar-item w3-button w3-light-gray w3-hover-black" style="width:200px; margin-right:auto; margin-left:auto; display:block;">Research Paper</a>    
        </td>
        </tr>
        </table>
        </h5>
        </p>
        </div>


        <style>
.anchor {
  display: block;
  height: 25px;
  margin-top: -25px; 
  visibility: hidden;
}
</style>

      ''')

################################################################################
def ContactPage():
    '''

    '''

    print("""
<!-- Grid -->
<!-- This grid and image header are on all subsequent presentation functions -->
<div class="w3-row-padding w3-padding-64 w3-container">
  <div class="w3-content w3-animate-opacity">
    
        <!-- Contact Page -->
    <div>
        <h2><b>Contact Me:</b></h2>
        <h3>
        <b>Cell:</b> 
        <br>
        <span style="color:#00477e">(508) 654-3900</span>
        <br><br>
        <b>Email:</b>
        <br>
        <a class="auto-generated-link" data-auto-recognition="true" data-content="ggregory@bu.edu" data-type="mail" href="mailto:ggregory@bu.edu" style="color: #00477e">ggregory@bu.edu</a>
        <br><br>
        <b>Social:</b>
        <br>
        <a href="http://www.linkedin.com/in/grantwgregory/" style="color:#00477e">LinkedIn</a>
        </h3>
    </div>
    """)
################################################################################
    # UPLOAD IMAGE - See imageUpload.py & showImage.py
################################################################################

################################################################################
################################################################################
# MAIN FUNCTION:
# TO DO: change link, add all the functions
if __name__ == "__main__":

    # get form field data
    form = cgi.FieldStorage()

    # call debug function (comment out when not needed)
    #DebugFormData(form)

    # call html head
    DoHTMLHead("Grant W. Gregory")

    ##########################################################################################
        #Update______SQL Section
    ##########################################################################################
    # most specific case #
    if 'ResumePage' in form:
        ResumePage()

    elif 'PortfolioPage' in form:
        PortfolioPage()

    elif 'ContactPage' in form:
        ContactPage()

    # or else show the homepage.
    else:
        WelcomePage()  

    # call html tail to conclude page
    DoHTMLTail()    

################################################################################
################################################################################
# Test - complete
# webpage: http://cs-webapps.bu.edu/cgi-bin/cs108/ggregory/GWGpage.py
################################################################################
################################################################################

