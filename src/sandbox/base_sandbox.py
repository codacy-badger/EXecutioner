'''Base sandbox class'''

class SandBox:

    '''SandBox base class'''

    class CompiledProgram:

        '''compiled program class for file based sandboxing'''

        def __init__(self, lang_settings, compiled_file_location):
            '''initialize file location of compiled code'''
            self.lang_settings = lang_settings
            self.file_location = compiled_file_location

    def can_run(self, language: str):
        '''Check if the sandbox can this language'''
        return language in self.supported_languages

    def compile(self, program, **kwarg):
        '''compile Program and return compiledProgram'''
        raise NotImplementedError

    def execute(self, compiledProgram, **kwargs):
        '''execute the compiledProgram'''
        raise NotImplementedError

    def delete(self, program, **kwargs):
        raise NotImplementedError
