from pyspark import SparkContext
import MySQLdb
import sys
def write_to_db(data):
    for entry in data:
        print("INSERT INTO recommendations(Page, Recos) VALUES ({}, \"{}\")".format(entry[0], entry[1]))

    db = MySQLdb.connect("db", "www", "$3cureUS", "cs4501")
    cursor = db.cursor()
    cursor.execute("USE cs4501")
    cursor.execute("""
        CREATE TABLE recommendations (
            Page int not null,
            Recos varchar(255)
        )
    """)
    for entry in data:
        cursor.execute("INSERT INTO recommendations(Page, Recos) VALUES ({}, \"{}\")".format(entry[0], entry[1]))
    db.commit()


def create_co_views(data):
    # Form (uid, (lid, date)) keyed by the user ID
    pairs = data.map(lambda line: line.split(","))
    pairs = pairs.map(lambda x: (x[0], ( x[1], x[2] )))
    # Form co-view pairs ((lid1, lid2), uid)
    user_coviews = pairs.join(pairs).filter(lambda x: x[1][0][1] < x[1][1][1])
    co_views = user_coviews.map(lambda x: ((x[1][0][0], x[1][1][0]), x[0]))
    # Group by pairs ((lid1, lid2), # of unique uids), only for those with more than 3 uids
    co_views = co_views.groupByKey().map(lambda x: (x[0], len(x[1]))).filter(lambda x: x[1] >= 3)
    views = co_views.map(lambda x: (x[0][0], x[0][1])).groupByKey()
    # Convert to (lid1, recommendations for lid)
    views = views.map(lambda y: ( y[0], ", ".join(list(y[1])) )).collect()

    return views



if __name__ == '__main__':
    sc = SparkContext("spark://spark-master:7077", "PopularItems")
    data = sc.textFile("/tmp/data/access.log")
    recs = create_co_views(data)
    write_to_db(recs)
