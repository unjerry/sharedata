import requests  # send request
from time import sleep  # set interval prevent to be blocked
import random  # generate random number

print("Hello! this is a creeper_addition program")  # greetint

length = int(input("how may number would you like to creep:"))
base_number = 600000
end = "1682524800000"  # 20230424000000


def single_share(name):
    header = {
        "cookie": "device_id=657672e32e5496b7c85150f7877f492c; s=dc12c3vwhj; xq_a_token=bf4ca35131318f0118658f3f4790584a66d8bb83; xqat=bf4ca35131318f0118658f3f4790584a66d8bb83; xq_r_token=3374a327172eff6197f4933bdfe11278fc6234ee; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY4NTE0NzQzMywiY3RtIjoxNjgyNTYwNzI0NTQyLCJjaWQiOiJkOWQwbjRBWnVwIn0.DHf3x_SC7h1JxoRlCaG62TEi4rIdqkusx1507XjAhICmufaKy5fiD9MPMCWQ4zVeMwu1yi7CszZkSee335aFQ5rHY08-GQXlPNGvGCtgGod9Rn4UuzvzlaQuv_pKIY9nHJ_mVsVrJVmDy6cMvtAK_wV0i03bWOBoQwUml1s3hENZT-tL9u5XiK_6eVckfDimqTKVWCJch9bk_xFTAJmdHP2klKGL82joSQv_tGFf7bYI1-_IPFUUVuQ62LOCdoSoZtQD6EKidkCY49yic8ZMuONZf4Wov552a4zHA80tEYc8Nw9sBtvdNW4Gt3xC38oe7e_tGhhAYbgq1T7yJqODbw; u=141682560732867; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1682251414,1682301864,1682514921,1682560735; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1682560735",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    url = "https://stock.xueqiu.com/v5/stock/chart/kline.json?"
    with open(f"{name}.share_data", "r") as fi:
        string = fi.read()

    lsts = (string.split("\n")[:-1][-1]).split(",")
    print("lasttime:"+str(lsts[0][1:]))

    begin = str(int(lsts[0][1:])+86400000)

    parameter = {
        "symbol": name,
        "begin": begin,
        "end": end,
        "period": "day",
        "type": "before",
        "indicator": "kline",
    }
    response = requests.get(url, headers=header, params=parameter)
    return response.json()


for number in range(0, length):  # for every stock
    name = "SH{}".format(base_number+number)
    print(name)
    J = single_share(name)
    if J == None:
        continue
    with open("SH{}.share_data".format(base_number+number), "a") as fo:
        print("add_seiko")
        for itm in J["data"]["item"]:
            fo.write(str(itm)+"\n")
    tm = 1 + random.random()
    sleep(tm)
    print(tm)
