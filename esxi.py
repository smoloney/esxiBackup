import sys
import time
import os

from pyVmomi import vim, vmodl
from pyVim.task import WaitForTask
from pyVim import connect
from pyVim.connect import Disconnect, SmartConnect, GetSi

names = {"johnson"}

data = {'ip': '10.26.62.8',
        'un': "",
        'pw': ""}
def getVM(conent, vim, vmName):
    """
    Gets information about a specified VM.  Needed to find the context to create
    vm snapshot
    """
    vm = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True)

    for i in container.view:
        if c.name == vmName:
            vm = i
            break

    return vm

def create(snapshot, despt, memory, quiesce):
    """
    Creats snapshot of VM after finding context for it.
    Important: when called set dumpMemory and quiesce to False.
    """
    vm = getVM(content, [vim.VirtualMachine], "johnson")
    WaitForTask(vm.CreateSnapshot(snapShot, description, dumpMemory, quiesce))
    
def removeOld():
    """
    Removes snapshots older than 14 days

    """  
    curTime = time.time()
    delDate = now - (14 * 86400)

    path = #find where files are stored
    for file in os.listdir(path):
        file = os.path.join(path, files)
        if os.stat(file).st_mtime < curTime - delDate:
            os.remove(os.path.join(path, file))
            
def main():
    myclust = connect.ConnectNoSSL( data['ip'], user=data['un'], pwd=data['pw'] )
    removeOld()
    for i in range(len(names)):
        create(names[i], "Snapshot for" +names[i], False, False)
    connect.Disconnect(myclust)
    

main()
