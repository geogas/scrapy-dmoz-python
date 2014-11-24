import sys, psycopg2
from scrapy.exceptions import DropItem
from scrapy.conf import settings

class ItemsToPostgres(object):

    conn = None
    cursor = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'" % (settings['DB_HOST'], settings['DB_NAME'], settings['DB_USER'], settings['DB_PASSWD']))
            self.cursor = self.conn.cursor()
        except:
            print "Unable to connect to the database!"

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO Dmoz(category, title, description) VALUES(%s, %s, %s);", (item['category'], item['title'], item['desc']))
            self.conn.commit() 

        except psycopg2.DatabaseError, e:
            if self.conn:
                self.conn.rollback()
                print 'Error %s' % e    
                sys.exit(1)

        return item

    def __del__(self):
        if self.conn:
            self.conn.close()
        print "closed"
