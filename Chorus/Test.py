import datetime
from pprint import pprint as pp

import boto.ec2
#boto.set_stream_logger('boto')
conn = boto.ec2.connect_to_region('us-west-1')
type(conn)
print(conn.APIVersion)

reservations = conn.get_all_reservations()
type(reservations)
print(reservations)
i =None
for res in reservations:
    pp (res)
    instances = res.instances
    for inst in instances:
        i = inst
        print("{}".format(inst.instance_type))
