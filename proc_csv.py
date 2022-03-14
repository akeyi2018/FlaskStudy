import pandas as pd

def qr_test():
    df = pd.read_csv('mileage.csv',encoding='cp932')
    # print(df.head(10))
    label_1 = "マイレージ情報１"
    key_1 = "航空会社：JAL"
    key_2 = "航空会社：ANA"
    label_2 = "マイレージ情報２"
    # res = df.query('@label_1 in @key_1')
    # print(df[label_1].head(10))
    sr1 = df[label_1]
    sr2 = df[label_2]
    m1_jal_ct = 0
    m1_ana_ct = 0
    m2_jal_ct = 0
    m2_ana_ct = 0
    for r1,r2 in zip(sr1,sr2):
        # JAL
        if (pd.notna(r1)) & (r1 == key_1) & (pd.isna(r2)):
            # res = f'{r1},{r2}'
            # print(res)
            m1_jal_ct += 1
        # ANA
        if (pd.notna(r1)) & (r1 == key_2) & (pd.isna(r2)):
            # res = f'{r1},{r2}'
            # print(res)
            m1_ana_ct += 1

        # JAL
        if (pd.notna(r2)) & (r2 == key_1) & (pd.notna(r1)):
            # res = f'{r1},{r2}'
            # print(res)
            m2_jal_ct += 1
        # ANA
        if (pd.notna(r2)) & (r2 == key_2) & (pd.notna(r1)):
            # res = f'{r1},{r2}'
            # print(res)
            m2_ana_ct += 1

    res = f'M1 JAL Count:{m1_jal_ct}, M1 ANA Count:{m1_ana_ct}, M2 JAL Count:{m2_jal_ct}, M2 ANA Count:{m2_ana_ct}'
    print(res)

qr_test()