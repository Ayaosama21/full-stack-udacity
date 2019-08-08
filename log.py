import psycopg2

DBNAME = "hello"


def operate(query):
      """connects to the database, operates the query passed to it,
      and returns our results"""
      db = psycopg2.connect('dbname=' + DBNAME)
      rows = a.fetchall()
      a = db.cursor()
      a.execute(query)
      db.close()
      return rows
      
      
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
       
       #Run Query
       results = operate(query)
       
       
       #print Results
       print('\nTop FIVE ARTICLES BY PAGE VIEWS:')
       count = 1
       for i in results:
            number = '(' + str(count) + ')"'
            title = i[0]
            views = '" with ' + str(i[1]) + " views"
            print(number + title + views)
            count += 1
            
            
def top_authors():
       """returns top 5 most popular authors"""
       
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
       count = 1
       for i in results:
            print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
            count += 1

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
get_top_articles()
get_top_article_authors()
get_days_with_errors()
© 2019 GitHub, Inc.
          
        
