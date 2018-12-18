from pyspark import SparkContext
import MySQLdb

"""
sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
count = pages.reduceByKey(lambda x,y: int(x)+int(y))        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for page_id, count in output:
    print ("page_id %s count %d" % (page_id, count))
print ("Popular items done")

"""
def create_co_views(sc, data):
    pairs = data.map(lambda line: line.split("\t"))
    user_coviews = pairs.join(pairs).filter(lambda x: x[1][0] > x[1][1])
    co_views = user_coviews.map(lambda x: ((int(x[1][0]), int(x[1][1])), int(x[0])))
    co_views = co_views.groupByKey().map(lambda x: (x[0], len(x[1]))).filter(lambda x: x[1] >= 3)
    co_views = co_views.collect()


if __name__ == '__main__':
    sc = SparkContext("spark://spark-master:7077", "PopularItems")
    data = sc.textFile("/tmp/data/access.log")
    create_co_views(sc, data)
