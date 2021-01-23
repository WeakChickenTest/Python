# 接口测试：验证url是否能正常请求和响应的过程
import requests
import pytest
'''
class Zd():
    url = 'http://v.juhe.cn/cccn/to_telecodes.php'
    head = {'Accept':'text / css, * / *;q = 0.1',
        'Accept - Encoding':'gzip, deflate, br',
        'Accept - Language':'zh - CN, zh',
        'Connection':'keep - alive',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64;rv: 68.0) Gecko / 20100101Firefox / 68.0'}
    def test_1(self):
        par = {'key':'a4f6327a9d3cd272b2f5a35ba4568541','chars':''}
        res = requests.get(url=self.url,headers=self.head,params=par)
        html =res.json() # 将字符串直接转换为字典
        print(html)
        assert html['reason']!='success'
        print('断言失败')
    def test_2(self):
        par = {'key': 'a4f6327a9d3cd272b2f5a35ba4568541', 'chars': '博文智生'}
        res = requests.get(url=self.url, headers=self.head, params=par)
        html = res.json()
        print(html)
        assert html['error_code'] == 0
        print("断言成功")
kk = Zd()
kk.test_1()
kk.test_2()
'''

def add_test(x):
    return x + 1
def test_001():
    assert add_test(3) == 3,"用例执行失败"
def test_002():
    assert add_test(2) == 3,"用例执行成功"

if __name__ == "__main__":
    assert pytest.main()