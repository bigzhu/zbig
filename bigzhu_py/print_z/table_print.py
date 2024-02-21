# 获取最长
def get_max_lens(rows: list):
    max_len = [0] * len(rows[0])
    for row in rows:
        for i in range(len(row)):
            # 要转 str, 避免错误
            if len(str(row[i])) > max_len[i]:
                max_len[i] = len(row[i])
    return max_len


def table_print(rows: list, spliter: str):
    max_lens = get_max_lens(rows)
    for row in rows:
        # 有可能塞入其他类型, 一律转 str
        formated_row = [str(row[i]).ljust(max_lens[i]) for i in range(len(row))]
        print(spliter.join(formated_row))


if __name__ == "__main__":
    data = [
        ["User", "Host", "Description"],
        ["root", "h.bigzhu.net", "dump"],
        ["root", "racknerd.bigzhu.net", "racknerd"],
        ["bigzhu", "ssh.entube.app", "digitalocean"],
    ]
    table_print(data, " ~ ")
