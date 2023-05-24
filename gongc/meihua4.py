import streamlit as st
import pandas as pd
import time
from PIL import Image
from datetime import datetime
st.markdown(
    """
    ## $$O_2O$$优惠券预测作业系统
    ###
    """
)
st.markdown(
    """
    #### 提交作业
    """
)

now = datetime.now().replace(microsecond=0)
st.write(now)
df = pd.read_csv('./gongc/sc.csv')
data = pd.read_csv('./gongc/111.csv')
label_t = df['label']
# 创建file_uploader组件
uploaded_file = st.file_uploader("请提交仅含[label]列的csv文件，命名需使用自己的姓名", type={"csv", "txt"})
if uploaded_file is not None:
    try:
        spectra = pd.read_csv(uploaded_file)
        label_p = spectra['label']
        sc = sum(label_t == label_p) / len(label_t)
        name = uploaded_file.name.split('.')[0]
        # st.write(name)
        st.write('准确度为：',sc)
        # st.write('排名为：')
        data1 = {'name': [name], 'score': [sc], 's_time': [now]}
        data1
        data1 = pd.DataFrame(data1)
        data = pd.concat([data, data1])
        data['s_time'] = pd.to_datetime(data['s_time'])
        data = data.sort_values(by=['score', 's_time'], ascending=[False, True])
        data = data.reset_index(drop=True)
        # st.write(data)
        data
        data.to_csv('./gongc/111.csv', index=False)
        data['rank'] = range(1, len(data) + 1)
        st.write('排名为：',int(data[(data['name'] == name) & (data['score'] == sc) & (data['s_time'] == now)]['rank'].values))


    except:
        st.error('导入文件不规范，请按照下面的例子再进行上传文件', icon="🚨")
        image = Image.open('./gongc/ces.jpg')
        st.image(image, caption='仅有一列label的csv文件')
    with st.expander("查看排行榜"):
        st.write(data)

