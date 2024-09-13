from fdfs_client.client import Fdfs_client, get_tracker_conf


# 上传图片
path = get_tracker_conf('/Users/samplecatalina/PycharmProjects/courtyard/courtyard/courtyard/utils/fastdfs/client.conf')
client = Fdfs_client(path)

ret = client.upload_by_filename('/Users/samplecatalina/Documents/icon/32321.jpeg')

if __name__ == '__main__':
    print(ret)
    print(type(ret))
    print(type(ret.get('Remote file_id')))