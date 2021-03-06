"""Makes the connection object and runs the query using the cursor"""
import pyhs2


def make_connection(delimiter, host, user, pw, database):

    conn = pyhs2.connect(host=host,
                           user=user,
                           database=database,
                           password=pw,
                           port=10000,
                           authMechanism="PLAIN")

    cur = conn.cursor()
    # Show databases
    #print cur.getDatabases()
    return cur, conn


def run_query(sql, cur, conn):
    """sql comes as a tuple, one part is sql template, the other part is the parameters"""
    sql = sql[0] % sql[1]
    print sql
    cur.execute(sql)
    # Fetch table results
    yield cur.fetch()
