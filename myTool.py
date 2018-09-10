import database

def run():
    
    print ""
    first_question()
    
    print "\n"
    second_question()
    
    print "\n"
    third_question()
    

def first_question():
    print "Q1. What are the most popular three articles of all time ?\n"
    R = database.the_three_popular_articles()
    for row in R:
            print "%s - %s views" % (row[0], row[1])
            
def second_question():
    print "Q2. Who are the most popular article authors of all time ?\n"
    R = database.the_popular_author()
    for row in R:
            print "%s - %s views" % (row[0], row[1])
            
def third_question():
    print "Q3. On which days did more than 1% of requests lead to errors ?\n"
    R = database.error()
    for row in R:
            print "%s - %s errors" % (row[0], row[1])            
            
run()            