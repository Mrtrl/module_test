# encoding:utf-8


from starlette.datastructures import UploadFile


def test():
    f = open('./.gitignore', 'rb')
    upload_file = UploadFile('gitignorefile', f, content_type='text')

    data = upload_file.read()
    print(data.send("你好吗"))

if __name__ == '__main__':
    test()
