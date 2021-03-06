# -*- coding: utf-8 -*-

from os import system, environ
import win32con
from win32gui import SendMessageTimeout
from _winreg import (
    CloseKey, OpenKey, QueryValueEx, SetValueEx,
    HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE,
    KEY_ALL_ACCESS, KEY_READ, REG_EXPAND_SZ, REG_SZ
)

def env_keys(user=True):
    if user:
        root = HKEY_CURRENT_USER
        subkey = 'Environment'
    else:
        root = HKEY_LOCAL_MACHINE
        subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    return root, subkey


def get_env(name, user=True):
    root, subkey = env_keys(user)
    key = OpenKey(root, subkey, 0, KEY_READ)
    try:
        value, _ = QueryValueEx(key, name)
    except WindowsError:
        return ''
    return value

# looks like this only sets for user?
def set_env(name, value, user=True):
    root, subkey = env_keys(user)
    key = OpenKey(root, subkey, 0, KEY_ALL_ACCESS)
    SetValueEx(key, name, 0, REG_EXPAND_SZ, value)
    CloseKey(key)
    #not sure how necessary this is, but it blocks when called, indefinately
#    SendMessage(
#        win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')

def broadcast_change():
#    SendMessage(
#        win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
    "Alerting active windows to the settings change..."
    SendMessageTimeout(
                       win32con.HWND_BROADCAST, 
                       win32con.WM_SETTINGCHANGE, 
                       0, 
                       'Environment', 
                       win32con.SMTO_ABORTIFHUNG, 0)
    

def remove(paths, value):
    while value in paths:
        paths.remove(value)


def unique(paths):
    unique = []
    for value in paths:
        if value not in unique:
            unique.append(value)
    return unique


def prepend_env(name, values, user=True):
    for value in values:
        paths = get_env(name, user).split(';')
        remove(paths, '')
        paths = unique(paths)
        remove(paths, value)
        paths.insert(0, value)

        set_env(name, ';'.join(paths), user)

def get_path(user=False):
    path = get_env("PATH", user=user)
    paths = unique(path.split(';'))

    return paths

def set_path(paths, user=False):
    set_env("PATH", ';'.join(paths), user=user)


if __name__ == '__main__':
    print "Starting"
    path = get_env("PATH", user=False)
    paths = unique(path.split(';'))

    print paths

#    prepend_env('Path', ['blarg'], user=False)
    
    print "finished"
    
    #set_env('Home', '%HomeDrive%%HomePath%')
    #set_env('Docs', '%HomeDrive%%HomePath%\docs')
    #set_env('Prompt', '$P$_$G$S')
    #
    #prepend_env('Path', [
    #    r'%SystemDrive%\cygwin\bin', # Add cygwin binaries to path
    #    r'%HomeDrive%%HomePath%\bin', # shortcuts and 'pass-through' bat files
    #    r'%HomeDrive%%HomePath%\docs\bin\mswin', # copies of standalone executables
    #])
