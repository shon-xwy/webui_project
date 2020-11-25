'''
@Author:shon
'''

def read_txt(filename):
    filepath = '../data/' + filename
    with open(filepath,'r',encoding='utf-8') as f:
        all_list = f.readlines()
        arrs = []
        for data in all_list:
            arrs.append(tuple(data.strip().split(',')))
        return arrs[1:]


if __name__ == '__main__':
    print(read_txt('login_data.txt'))


