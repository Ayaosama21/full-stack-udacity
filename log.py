# !/usr/bin/env python3
# to connect the database

import psycopg2
DBNAME = "news"


# the most popular three articles of all times
def most_popular__three__article():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT TOP 3 title, Count(*) as articlesCount
        FROM articles
        join authors
        on articles.ID = authors.ID
        group by articles
        ORDER BY articleCount DESC;""")

    return c.fetchall()
    db.close()

# the most popular article authors of all time


def most_popular_article_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT authors.name , count(*) as authorsCount
        from authors
        join articles
        on articles.ID = authors.ID
        group by authors
        order by authorsCount desc;""")
    out = c.fetchall()
    for author, num in out:
        print(" \"{}\" -- {} views".format(author, num))
    print("-------------------------")


# which days did more than 1% of requests lead to errors
def errors_more_than_1_precentage():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select * from
                 (select date(time),round(100.0*sum(case log.status
                  when '200 OK'  then 0 else 1 end)
                  /count(log.status),3) as error from log group by
                  date(time) order by error desc) as subq where error > 1;""")
    return c.fetchall()
    db.close()
# display first query


def dis_first():
    dis_articles = most_popular__three__article()
    for name, num in dis_articles:
        print(" \"{}\" -- {} views".format(name, num))
# display third query


def dis_third():
    dis_errors = errors_more_than_1_precentage()
    for day, percentage in dis_errors:
        print("{0:%B %d, %Y} -- {1:.2f} % errors".format(day, percentage))

if __name__ == '__main__':
    dis_first()
    most_popular_article_authors()
    dis_third()
