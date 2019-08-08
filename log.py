import psycopg2

DBNAME = "hello"



      
      
def top():
       """Returns top 5 most read articles"""
       
       #Build Query String
       query = """
            SELECT articles.title, COUNT(*) AS num
            FROM articles
            JOIN log
            ON log.path LIKE concat('/article/%', articles.slug)
            GROUP BY articles.title
            ORDER BY num DESC
            LIMIT 5;
       """
       
  def operate(query):
      """connects to the database, operates the query passed to it,
      and returns our results"""
      db = psycopg2.connect('dbname=' + DBNAME)
      rows = a.fetchall()
      a = db.cursor()
      a.execute(query)
      db.close()
      return rows
            
            
       #Run Query
       results = operate(query)
       
       
       #print Result
       c = 1
       for i in results:
            number = '(' + str(count) + ')"'
            title = i[0]
            views = '" with ' + str(i[1]) + " views"
            print(number + title + views)
            c += 1
            
            
def top_authors():
       
       #Build Query String
       query = """
            SELECT authors.name, COUNT(*) AS num
            FROM authors
            JOIN articles
            ON authors.id = articles.author
            JOIN log
            ON log.path like concat('/article/%', articles.slug)
            GROUP BY authors.name
            ORDER BY num DESC
            LIMIT 5;
       """
       
       #Run Query
       results = operate(query)
       
       # Print Results
       print('\nTOP FIVE AUTHORS BY VIEWS:')
       c = 1
       for i in results:
            print('(' + str(c) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
            c += 1

def days_errors():
    """returns days with more than 1% errors"""
    
    #Build Query String
    query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 5) AS percent
        FROM (
          SELECT date_trunc('day',time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 5) > 0.01)
        ORDER BY percent DESC;
    """

    # Run Query
    results = operate(query)

    # Print Results
    print('\nDAYS WITH MORE THAN 1% ERRORS:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " -- " + errors)

print('Calculating Results...\n')
top()
top_authors()
days_errors()
© 2019 GitHub, Inc.
          
        
