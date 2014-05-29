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

last_record_log = None

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

def main():
    global last_record_log
    parser = argparse.ArgumentParser(
        description='Record and replay mouse and keyboard actions in VirtualBox sessions')
    parser.add_argument('vm_name', help='Name of virtual machine')
    parser.add_argument('--r', dest='record', 
                        default=False, help='Record a session to a log file')
    parser.add_argument('--p', dest='replay', 
                        default=False, help='Replay a session from a log file')
    args = parser.parse_args()

    if args.record and args.replay:
        raise Exception("Cannot simultaneously record and replay.")

    logging.info("Connecting to virtual machine")
    try:
        vbox = virtualbox.VirtualBox()
        vm = vbox.find_machine(args.vm_name)
        session = vm.create_session()
    except:
        raise Exception("Could not find virtual machine %s. Please make sure it exists." % args.vm_name)

    if args.record:
        try:
            logging.info("Registering to receive keyboard and mouse events")
            session.console.keyboard.register_on_guest_keyboard(record_keyboard)
            session.console.mouse.register_on_guest_mouse(record_mouse)
        except:
            raise Exception("Could not register with virtual machine %s. Please make sure it exists." % args.vm_name)
        f = open(args.record,"w")
        last_record_log = datetime.datetime.now()
        logging.info("Recording... Press <ENTER> to stop.")
        stop = raw_input()
        f.close()
    elif args.replay:
        try:
            f = open(args.replay,"r")
        except:
            raise Exception("Could not find log file %s." % args.replay)
        for line in f.readlines():
            line = line.replace("\n","")
            line_split = line.strip().split(" ")
            time_delta = float(line_split[0])
            event_type = line_split[1]
            options = line_split[2:]

            time.sleep(time_delta)

            if event_type == "M":
                logging.info("Executing mouse %s" % line)
                session.console.mouse.put_mouse_event(2*int(options[1]), 2*int(options[2]), int(options[3]), int(options[4]), int(options[0]))

            if event_type == "K":
                logging.info("Executing keyboard %s" % line)
                session.console.keyboard.put_scancodes([int(x) for x in options])
    else:
        raise Exception("You must specify either --r to record or --p to replay.")

if __name__ == "__main__":
    main()