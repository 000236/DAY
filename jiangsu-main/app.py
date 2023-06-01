import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
st.set_page_config(
     page_title="教学评价系统",
     page_icon="🧊",
     layout="wide",    # 'wide' or 'centered'
     initial_sidebar_state="expanded",
 )

# st.markdown('# 教学评价系统')
st.markdown("<h1 style='text-align: center; color: grey;'>教学评价系统</h1>", unsafe_allow_html=True)
st.sidebar.markdown('# :house:首页')
st.sidebar.markdown('# :book:课程信息')
st.sidebar.markdown('''
- 课程任务点
- 章节学习
- 教学预警
''')
st.sidebar.markdown('# :book:课程报表')
st.sidebar.markdown('''
- 课堂活动
- 课堂积分
- 教师评价
- 学生评价
- 作业统计
- 考试统计
- 课程分析报表
''')
st.sidebar.markdown('# :book:信息管理')

st.markdown('## :heart:课堂分析报表')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(':star:**知识目标** 前测和后测考核')
    df = pd.DataFrame({
        'name': ['盈利能力分析', '运营能力分析', '营业收入分析', '发展能力分析', '偿债能力分析', '成本费用分析', '国资委考核指标'],
        'before': [50, 40, 54, 60, 55, 50, 55],
        'after': [85, 90, 84, 80, 85, 80, 85]
    })
    # fig1 = px.bar(df, x='name', y=['before', 'after'], barmode='group', orientation='h')
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(y=df['name'], x=df['before'],
                          orientation='h',
                          text=df['before'],  # 显示number的数据信息
                          name='前测',
                          textposition="outside"  # ['inside', 'outside', 'auto', 'none']
                          ))
    fig1.add_trace(go.Bar(y=df['name'], x=df['after'],
                          orientation='h',
                          name='后测',
                          text=df['after'],  # 显示number的数据信息
                          textposition="outside"  # ['inside', 'outside', 'auto', 'none']
                          ))
    fig1.update_layout(barmode='group')  # title_text='前测和后测考核',
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.markdown(':star:**能力目标** 首轮和二轮考核')
    df = pd.DataFrame({
        'name': ['盈利能力分析', '运营能力分析', '营业收入分析', '发展能力分析', '偿债能力分析', '成本费用分析', '国资委考核指标'],
        'before': [50, 40, 54, 60, 55, 50, 55],
        'after': [85, 90, 84, 80, 85, 80, 85]
    })
    fig1 = go.Figure()
    fig1.add_trace(
        go.Bar(y=df['name'], x=df['before'],
                          orientation='h',
                          text=df['before'],  # 显示number的数据信息
                          name='首轮',
                          textposition="outside"  # ['inside', 'outside', 'auto', 'none']
                          ))
    fig1.add_trace(go.Bar(y=df['name'], x=df['after'],
                          orientation='h',
                          name='二轮',
                          text=df['after'],  # 显示number的数据信息
                          textposition="outside"  # ['inside', 'outside', 'auto', 'none']
                          ))
    fig1.update_layout(barmode='group')  # title_text='首轮和二轮考核',
    st.plotly_chart(fig1, use_container_width=True)
# col3, col4 = st.columns(2)
with col3:
    st.markdown(':star:**素养目标**')
    df = pd.DataFrame({
        'name': ['7S管理', '企业操作', '职业精神', '创新精神', '团队协作'],
        '第一组': [4, 5, 5, 5, 4], '第二组': [5, 4, 3, 3, 5], '第三组': [3, 5, 3, 1, 4],
        # 'four': [4, 2, 3, 1, 4], 'five': [4, 1, 3, 2, 4],
    })
    d = []
    for name in ['第一组', '第二组', '第三组']:
        d.append(
            go.Scatterpolar(theta=df['name'], r=df[name], mode='lines', name=name)
        )
    fig3 = go.Figure(data=d)
    # 颜色填充
    fig3.update_traces(fill='toself')
    st.plotly_chart(fig3, use_container_width=True)
with col4:
    st.markdown(':star:**企业评价**')
    df = pd.DataFrame({
        'name': ['理解能力', '实操能力', '协助能力'],
        '首轮': [4, 3, 3],  '二轮': [5, 4, 4],
    })
    d = []
    for name in ['首轮', '二轮',]:
        d.append(
            go.Bar(x=df['name'], y=df[name], name=name, text=df[name], textposition="outside")
        )
    fig4 = go.Figure(data=d)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown('## :heart:课堂积分')
col1, col2  = st.columns(2)
col3, col4, col5 = st.columns(3)
with col1:
    st.markdown(':star:首轮训练评分')
    df = pd.DataFrame({
        'name': ['60-65', '65-70', '70-75', '75-80', '80-85', '85-90', '90-95', '95-100'],
        'num': [1, 2, 3, 4, 7, 5, 3, 1],
    })
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df['name'], y=df['num'],
                          ))
    fig1.add_trace(go.Scatter(x=df['name'], y=df['num'],
                          ))
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)
with col3:
    st.markdown(':star:团队积分')
    df = pd.DataFrame({
        'name': ['第一组', '第二组', '第三组'],
        '首轮': [50, 40, 54],
        '二轮': [70, 60, 58],
    })
    fig1 = go.Figure()
    for name in ['首轮', '二轮']:
        fig1.add_trace(
            go.Bar(y=df['name'], x=df[name],
                              orientation='h',
                              text=df[name],  # 显示number的数据信息
                              name=name,
                              textposition="outside"  # ['inside', 'outside', 'auto', 'none']
                              ))

    fig1.update_layout(barmode='group')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown(':star:二轮训练评分')
    df = pd.DataFrame({
        'name': ['60-65', '65-70', '70-75', '75-80', '80-85', '85-90', '90-95', '95-100'],
        'num': [0, 1, 2, 4, 5, 7, 5, 2],
    })
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=df['name'], y=df['num'],
                          ))
    fig1.add_trace(go.Scatter(x=df['name'], y=df['num'],
                              ))
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)
with col4:
    st.markdown(':star:个人积分榜')
    df = pd.DataFrame({
        'name': ['郭晓峰', '马伊琍', '何丽丽', '杨璐', '王文刚'],
        'num': [90, 87, 75, 65, 60]
    }).sort_values('num')
    fig1 = go.Figure()
    fig1.add_trace(
        go.Bar(y=df['name'], x=df['num'],
               orientation='h',
               text=df['num'],  # 显示number的数据信息
               textposition="outside"  # ['inside', 'outside', 'auto', 'none']
               ))

    st.plotly_chart(fig1, use_container_width=True)

# col3, col4 = st.columns(2)
with col5:
    st.markdown('## :heart:课堂活动')
    df = pd.DataFrame({
        'name': ['签到', '讨论', '随堂练习', '抢答', '互动'],
        '第一组': [4, 5, 5, 5, 4], '第二组': [5, 4, 3, 3, 5], '第三组': [3, 5, 3, 1, 4],
        # 'four': [4, 2, 3, 1, 4], 'five': [4, 1, 3, 2, 4],
    })
    d = []
    for name in ['第一组', '第二组', '第三组']:
        d.append(
            go.Scatterpolar(theta=df['name'], r=df[name], mode='lines', name=name)
        )
    fig4 = go.Figure(data=d)
    # 颜色填充
    fig4.update_traces(fill='toself')
    st.plotly_chart(fig4, use_container_width=True)

# with col4:
#     st.markdown('## :heart:师生互动')
#     txt = st.text_area('', '''
#         你想告诉我们的……
#         ''')


