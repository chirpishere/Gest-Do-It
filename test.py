import win32gui
import win32process
import win32api
import win32con
import os
import time

def get_active_browser_title():
    window = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(window)[1]
    handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
    exe_path = win32process.GetModuleFileNameEx(handle, 0)
    return os.path.basename(exe_path)

def is_doc_viewer_application(application):
    doc_viewer_application_list = ['AcroRd32.exe', 'FoxitReader.exe', 'NotroPDFReader.exe', 'SumatraPDF.exe', 'PDFXEdit.exe', 'WINWORD.EXE', 'EXCEL.EXE', 'POWERPNT.EXE', 'Acrobat.exe', 'notepad.exe', 'write.exe']
    return any(app.lower() in application.lower() for app in doc_viewer_application_list)


while True:
    active_browser_title = get_active_browser_title()
    if active_browser_title and is_doc_viewer_application(active_browser_title):
        print("Active Browser Title:", active_browser_title)
    
    time.sleep(1)  # Adjust the delay as needed
