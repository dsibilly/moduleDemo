import submodule

if __name__ == "__main__":
    testString = 'todd'
    print submodule.commandMap['foo'](testString)
    print submodule.commandMap['sna'](testString)
    print submodule.commandMap['sna'](submodule.commandMap['foo'](testString))
