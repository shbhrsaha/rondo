"""
    Record and replay mouse and keyboard actions in VirtualBox sessions

    Usage:

        python rondo.py [--r record_log_file] [--p replay_log_file] virtual_machine_name
"""

import time
import datetime
import logging
import argparse
import virtualbox

logging.basicConfig(level=logging.INFO)

def record_keyboard(event):
    """
    Save a keyboard action.
    """
    global last_record_log
    logging.info("Keyboard %s" % event.scancodes)
    
    now = datetime.datetime.now()
    diff = now - last_record_log
    last_record_log = now

    scan_codes = [str(x) for x in event.scancodes]
    f.write("%s K %s \n" % (diff.total_seconds(), " ".join(scan_codes)))

def record_mouse(event):
    """
    Save a mouse action
    """
    global last_record_log
    logging.info("Mouse %s %s %s %s %s %s" % (event.mode, event.buttons, event.x, event.y, event.z, event.w))
    
    now = datetime.datetime.now()
    diff = now - last_record_log
    last_record_log = now
    
    f.write("%s M %s %s %s %s %s \n" % (diff.total_seconds(), event.buttons, event.x, event.y, event.z, event.w))