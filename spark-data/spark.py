from pyspark import SparkContext
import MySQLdb

def write_to_db(data):
    db = MySQLdb.connect("db", "www", "$3cureUS", "cs4501")
    cursor = db.cursor()
    cursor.execute("USE cs4501")


def create_co_views(data):
    pairs = data.map(lambda line: line.split("\t"))
    user_coviews = pairs.join(pairs).filter(lambda x: x[1][0] > x[1][1])
    co_views = user_coviews.map(lambda x: ((int(x[1][0]), int(x[1][1])), int(x[0])))
    co_views = co_views.groupByKey().map(lambda x: (x[0], len(x[1]))).filter(lambda x: x[1] >= 3)
    return co_views.collect()


if __name__ == '__main__':
    sc = SparkContext("spark://spark-master:7077", "PopularItems")
    data = sc.textFile("/tmp/data/access.log")
    recs = create_co_views(data)
    write_to_db(recs)
    
