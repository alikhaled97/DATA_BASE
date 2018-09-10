import psycopg2

DBNAME = "news"

The_Three_Popular_Articles = """ 
      select 
          articles.title, 
          count(log.id) as num
      from 
          articles 
          left join log on log.path = ('/article/' || articles.slug) 
      group by
          articles.title
      order by
          num desc
      limit 
          3
      """

The_Popular_author = """
      select
          authors.name,
          count (log.id) as num
      from
          authors
          left join articles on articles.author = authors.id 
          left join log on log.path = ('/article/' || articles.slug)
      group by 
          authors.name
      order by
          num desc
      """

The_Error = """
      select
            to_char(error.date,'Month DD, YYYY') as date,
            to_char(((error.count::decimal
                    /all_status.count::decimal)*100)
                    ,'9.99')
                    || '%' as perc
        from
            (select date(time),count(*) from log
                        group by date(time)) as all_status,
            (select date(time),count(*) from log where status != '200 OK'
                        group by date(time)) as error
        where
            all_status.date = error.date
            and ((error.count::decimal
                    /all_status.count::decimal)*100) > 1;
            """

def get(a):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(a)
    return cursor.fetchall()
    db.close()
    
def the_three_popular_articles():
    return get(The_Three_Popular_Articles)

def the_popular_author():
    return get(The_Popular_author)

def error():
    return get(The_Error)