import os

class ScvFileUtil:
    _has_header = False
    file = None
    
    def open_write(self, file_name, mode="w+", encoding="utf-8", buffering=0):
        self.file = open(file_name, mode, encoding=encoding)

    def write_header(self, header):
        if self.file and self._has_header == False:
            self._has_header = True
            self.write_data(header)

    def write_data(self, data):
        if self.file:
            self.file.write(data + "\n")

    def close(self):
        if self.file:
            self.file.close()

if __name__ == "__main__":
    f = ScvFileUtil()
    f.open_write("{}/data.txt".format(os.path.dirname(__file__)))
    f.write_header("header 1")
    f.write_header("header 2")
    f.write_data("data")
    f.close()