import reimport

def reimportAllChangedPythonModules():
    whitelist = ('MyPackage',)  # AL.apps.EnvironmentStudio2
    modified = [m for m in reimport.modified() if m.startswith(whitelist)]
    if len(modified):
        print 'Reimport modules:', modified
        reimport.reimport(*modified)
    else:
        print 'No changed modules!'


reimportAllChangedPythonModules()
