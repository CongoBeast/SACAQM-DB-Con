#!/usr/bin/env python

import os
import sys
import json
import datetime
import urllib.parse
import urllib.request

class sacaqm:
  
  def __init__(self):
    self.base="https://sacaqm.web.cern.ch/dbread.php"
    self.verbose=False
    pass

  def set_verbose(self,enable):
    self.verbose=enable
    pass

  def request(self,pars):
    url=self.base+'?'+urllib.parse.urlencode(pars)
    if self.verbose: print("request: %s"%url)
    resp = urllib.request.urlopen(url)
    reply = json.loads(resp.read())
    if self.verbose: print(reply)
    return reply
    pass
    
  def get_sen55(self, sensor_id, datetime_from, datetime_to=None):
    pars={"cmd":"get_sen55","sensor_id":sensor_id}
    pars["from"]=datetime_from.strftime("%y-%m-%d %H:%M:%S")
    if datetime_to: pars["to"]=datetime_to.strftime("%y-%m-%d %H:%M:%S")
    return self.request(pars)
    
  def get_sensors(self):
    pars={"cmd":"get_sensors"}
    return self.request(pars)
    
if __name__=='__main__':
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose',action='store_true')
    args = parser.parse_args()

    cli=sacaqm()
    cli.set_verbose(args.verbose)
    sensors=cli.get_sensors()

    for sensor in sensors:
      print("data for sensor: %s" % sensor['sensor_id'])
      data=cli.get_sen55(sensor['sensor_id'],datetime.datetime.today()-datetime.timedelta(days=1))
      for dp in data:
        print("%(timestamp)s: pm1=%(pm1p0)5s, pm2.5=%(pm2p5)5s, pm4.0=%(pm4p0)5s, pm10.0=%(pm10p0)5s" % dp)
        pass
      pass
    pass
      