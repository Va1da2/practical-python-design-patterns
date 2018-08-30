"Sigleton logger."

class Logger(object):
    class __Logger():
        def __init__(self, file=None):
            self.file = file

        def __str__(self):
            return "{0!r} {1}".format(self, self.file)

        def _write_log(self, level, msg):
            "Writes a message to the file for a specific Logger instance."
            with open(self.file, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)

        def warn(self, msg):
            self._write_log("WARN", msg)

        def info(self, msg):
            self._write_log("INFO", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)


    instance = None

    def __new__(cls, file=None):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(file)

        return Logger.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
