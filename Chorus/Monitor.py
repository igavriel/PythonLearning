"""Monitor Spot on AWS

    Example of usage is implemented in the RunMonitor funciton:

    >>>import Module
    >>>Module.RunMonitor('us-west-1', 'm4.large', 0.05, 4)   # run single monitor

    >>>Module.main()    # run default parameters

    Note:
        * class public method are CamelCase,
        * class private method and members has underscore prefix
		* due to the short period, this module assume all inputs are valid
		  and there is no input validation
	
	Author: Ilan Gavriel 
	mail: igavriel@gmail.com
"""
import boto.ec2
import datetime
import time
#from pprint import pprint as pp

# debug boto logger - enable the following line for debbugging
#boto.set_stream_logger('boto')

class Monitor:
    """Monitor AWS Spot prices
        region - region to check
                'us-west-1', 'us-west-2'...
        instance_type - instance type to check: 
                "m4.large", "m4.xlarge", "m4.2xlarge"...
    """
    def __init__(self, region, instance_type):
        self._region = region
        self._instance_type = instance_type
        self._connet()

    def _connet(self):
        """encapsulate the boto connect method"""
        self._conn = boto.ec2.connect_to_region(self._region)

    def _find_price_limit(self, limit):
        """find if the price is going to exceed in the following hour"""
        now = datetime.datetime.now().isoformat()
        one_hour = (datetime.datetime.now() + datetime.timedelta(0,3600)).isoformat()
        hist = self._conn.get_spot_price_history(instance_type=self._instance_type, start_time=now, end_time=one_hour)
        for item in hist:
            if item.price > limit:
                print('Item {} time {} Above limit {}'.format(item, item.timestamp, limit))
                # return the elemet which exceeded pricing list ()
                return item
        return None

    def _loop_running_ec2(self):
        """periodic loop over all running EC2 with the same instance type
           hard-coded every 2 seconds

           NOTE: I've implemented the sending method as notification to the console due to time limitation
        """
        for i in range(self._loops):
            print('Loop-{}:'.format(i))
            self.NotifyRunningEC2()
            time.sleep(2)   # sleep 2 sec

    def _shutdown_ec2(self, instance):
        print("Shutdown EC2 Machine type='{}' ID='{}' State='{}'".format(self._instance_type, instance.id, instance.state))
        pass

    def SpotHistory(self, limit, loops):
        self._loops = loops
        self._item = self._find_price_limit(limit)
        if self._item is not None:
            # found limitation - send notification to all machine types periodicly
            print("Pricing limit exceeded at {} for {}".format(self._item.timestamp, self._item.instance_type))
            self._loop_running_ec2()

    def NotifyRunningEC2(self):
        reservations = self._conn.get_all_reservations()
        for res in reservations:
            instances = res.instances
            for inst in instances:
                if inst.instance_type == self._instance_type and inst.state=='running':
                    print("EC2 Machine type='{}' ID='{}' State='{}'".format(self._instance_type, inst.id, inst.state))
                    self._shutdown_ec2(inst)
                #DEBUG#else:
                #DEBUG#    print("EC2 Machine ID='{}' not the same type or not running".format(inst.instance_type))

#################################################
def RunMonitor(region, instance_type, price, loops):
    """RunMonitor function - helper function with try/exception block for Monitor class
        region - region to check
        instance_type - instance type to check
        price - price limitation (float)
        loops - number of loops to run this monitor 
    """
    print("* RunMonitor for region {} instance {} limitaion of {}".format(region, instance_type, price))
    try:
        mon = Monitor(region, instance_type)
        item = mon.SpotHistory(price, loops)

    except ValueError as e:
        print("Error: {0}".format(str(e)))

#################################################
def main():
    RunMonitor('us-west-1', 'm4.large', 0.05, 3)
    RunMonitor('us-west-1', 'm4.xlarge', 0.05, 3)
    RunMonitor('us-west-1', 'm4.2xlarge', 0.05, 3)
    # test method over micro machine
    #DEBUG#RunMonitor('us-west-1', 't2.micro', 0.00, 1)

#################################################
if __name__ == '__main__':
    main()
