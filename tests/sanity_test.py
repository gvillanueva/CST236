import os, sys, types, inspect, ast
from unittest import TestCase

class TestSanity(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testPath = "/home/giancarlo/Documents/classes/CST236/pyTona"
        sys.path.append(cls.testPath)

        # Read in known good parameters for invocations
        cls.invokeParams = {}
        with open('sanity_test.data', 'r') as f:
            for line in f.readlines():
                nameAndParams = line.split('=')
                cls.invokeParams[nameAndParams[0]] = ast.literal_eval(nameAndParams[1])

    def test_01_module_import(self):
        for file in os.listdir(TestSanity.testPath):
            if file.endswith(".py"):
                # strip the extension
                module = file[:-3]

                # Set the module name in the current global namespace
                try:
                    globals()[module] = __import__(module)
                except:
                    self.fail("Importing {0} raised an exception".format(file))

    def test_02_class_creation(self):
        # Iterate each item in global symbols
        for name, module in globals().items():
            # Test to ensure current symbol represents a module (hopefully not built-in)
            if isinstance(module, types.ModuleType) and name not in sys.builtin_module_names:
                try:
                    # Only include modules in the test path
                    if os.path.dirname(inspect.getfile(module)) == self.testPath:
                        # Get a list of classes in the module
                        classes = inspect.getmembers(module, inspect.isclass)
                        # Iterate the list of classes and try to instantiate them
                        for classInfo in classes:
                            class_ = getattr(module, classInfo[0])
                            try:
                                # Use known good parameters, if they have been defined in the data file
                                if classInfo[0] in TestSanity.invokeParams:
                                    instance = class_(**TestSanity.invokeParams[classInfo[0]])
                                else:
                                    instance = class_()
                            except:
                                # Fail the test if class instantiation throws an exception
                                self.fail("Instantiating {0} raised an exception".format(classInfo))
                except TypeError as te:
                    # Ignore TypeErrors on this level (due to loitering built-in modules)
                    continue
                except:
                    # Raise other exceptions
                    raise

    def test_03_function_calls(self):
        # Iterate each item in global symbols
        for name, module in globals().items():
            # Test to ensure current symbol represents a module (hopefully not built-in)
            if isinstance(module, types.ModuleType) and name not in sys.builtin_module_names:
                try:
                    # Only include modules in the test path
                    if os.path.dirname(inspect.getfile(module)) == self.testPath:
                        # Get a list of functions in the module
                        functions = inspect.getmembers(module, inspect.isfunction)
                        for funcInfo in functions:
                            func_ = getattr(module, funcInfo[0])
                            try:
                                # Use known good parameters, if they have been defined in the data file
                                if funcInfo[0] in TestSanity.invokeParams:
                                    instance = func_(**TestSanity.invokeParams[funcInfo[0]])
                                else:
                                    instance = func_()
                            except:
                                # Fail the test if class instantiation throws an exception
                                self.fail("Instantiating {0} raised an exception".format(funcInfo))
                except TypeError as te:
                    # Ignore TypeErrors on this level (due to loitering built-in modules)
                    continue
                except:
                    # Raise other exceptions
                    raise
