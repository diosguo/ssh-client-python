#!/usr/bin/env python3
"""
File: :
Author: xuyang
Email: 943024256@qq.com
Github: theDoctor2013
Description: 
"""
import shutil
import sys
import os
import pickle

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    config_dir = '~/.config/ssh-client-python'
    args = sys.argv
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    if not os.path.exists(os.path.join(config_dir,'hosts.pkl')):
        pickle.dump({},open(os.path.join(config_dir, 'hosts.pkl'),'wb'))
    hosts = pickle.load(open(os.path.join(config_dir, 'hosts.pkl'),'rb'))
    if len(args) == 1:
        print('Usage: [-a|-c|-r] add/connect/remove.')
        exit(0)
    else:
        if '-a' == args[1]:
            host_name = args[2]
            username = args[4]
            # password = args[4]
            address = args[3]

            hosts[host_name] = [username, address]
            pickle.dump(hosts, open(os.path.join(config_dir, 'hosts.pkl'),'wb'))            
        elif '-c' == args[1]:
            host_name = args[2]
            if host_name in hosts:
                print(hosts[host_name])
                os.system('ssh %s@%s'%(hosts[host_name][0], hosts[host_name][1]))
            else:
                print('Host not exist!')

            
         
             

if __name__ == "__main__":
    main()

