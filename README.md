rondo
=====

Record and replay mouse and keyboard actions in VirtualBox sessions.

Rondo records actual execution behavior, not video, essentially enabling VirtualBox users to create OS-wide macros.

VMware offers a similar feature called [Enhanced Execution Record / Replay](http://blogs.vmware.com/workstation/2008/04/enhanced-execut.html) since 2008, but Rondo brings that functionality to Oracle VirtualBox.

Installation
---
Install the Python requirements with:

    pip install -r requirements.txt

Usage
---
First, start the virtual machine you would like to record/replay executions on. Then run rondo with the following:

    python rondo.py [--r record_log_file] [--p replay_log_file] virtual_machine_name

Tips
---
It helps to start the mouse at the same location between record and replay sessions because Rondo stores relative mouse movements. Pay close attention to the guest OS's state to avoid misplaced mouse/keyboard executions.