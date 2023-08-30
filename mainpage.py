from datetime import time
import sys
import mysql.connector
import pandas as pd

sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\PhonepePulse\venv\Lib\site-packages')
import streamlit as st
import streamlit_option_menu
import plotly.express as px

Connection=mysql.connector.connect(host="localhost", user="root", password="root")
mycursor = Connection.cursor()
mycursor.execute("use phonepepulse;")
with st.sidebar:
    selected = streamlit_option_menu.option_menu("Menu", ["About", "Data Explore", "Charts", 'Statistics'],
                                                 icons=["exclamation-circle","pie-chart","bar-chart-line","graph-up-arrow" ],
                                                 menu_icon= "menu-button-wide",
                                                 default_index=0,
                                                 styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#f5da42"},
                        "nav-link-selected": {"background-color": "#4287f5"}})

if selected == "About":
    st.markdown("# :violet[PhonePe Pulse]")
    st.markdown("## :green[Application using Streamlit and Plotly to explore Phonepe Pulse Data Visualization and Exploration]")
    col1, col2 = st.columns([500, 1], gap="small")
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :green[Domain :] Fintech")
        st.markdown(
            "##### :green[Technologies used :] "
            "Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.")
        st.markdown(
            """### :green[Overview :]
The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data."
When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?
This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.
This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.""")

if selected == "Charts":
    col1, col = st.columns([100, 1])
    with col1:
        st.info(
            """
            #### This page provides insights like :
            - Overall Transaction and User.
            - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
            - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
            - Top 10 mobile brands and its percentage based on the how many people use phonepe.
            """
        )
    Type = st.selectbox('All India', ('Transaction', 'User'))
    col2, col3 = st.columns([1.5, 1, ], gap="large")
    with col2:
        Year = st.selectbox('Year', (2018,2019,2020,2021,2022,2023))
    with col3:
        if Year==2023:
            Quarter = st.selectbox('Quarter', (1,2))
        else:
            Quarter = st.selectbox("Quarter",(1,2,3,4))

    if Type == "Transaction":
        mycursor.execute(f'select sum(Amount) as Total_TR_Amount,  sum(Count) as Total_TR_Count from phonepepulse.map_all_india_transaction_df where Year={Year} and Quarter={Quarter}')
        df=pd.DataFrame(mycursor.fetchall(), columns=['Total_TR_Amount', 'Total_TR_Count'])
        Amount=df['Total_TR_Amount'][0]
        Count=df['Total_TR_Count'][0]
        st.header("")
        st.header("")
        st.header(f":violet[Overall Transaction in the year {Year} quarter {Quarter}]")
        st.subheader(':red[Total_TR_Amount]:  ' f':green[{Amount}]')
        st.subheader(':red[Total_TR_Count]:  ' f':green[{Count}]')
        st.header("")
        st.header("")
        st.header("")
        mycursor.execute(f'select State_Name, sum(Amount) as Total_Tr_Amount, sum(Count) as Total_Tr_Count from phonepepulse.topdata_all_india_transaction_df where Year={Year} and Quarter={Quarter}  group by State_Name order by Total_Tr_Amount desc limit 10')
        df=pd.DataFrame(mycursor.fetchall(), columns=['State_Name', 'Total_Tr_Amount', 'Total_Tr_Count'])
        image=px.pie(df, title='Top 10 States', values='Total_Tr_Amount',names='State_Name', color_discrete_sequence=px.colors.sequential.Electric_r,  hover_data=['Total_Tr_Count'],
                             labels={'Total_Tr_Count':'Total_Tr_Count'})
        image.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(image, use_container_width=True)
        st.header('Details of Top 10 States in  Table')
        st.write(df)

        mycursor.execute(
            f'select District_name, sum(Transaction_amount) as Total_Tr_Amount, sum(Transaction_count) as Total_Tr_Count from phonepepulse.tr_map_df where Year={Year} and Quarter={Quarter}  group by District_name order by Total_Tr_Amount desc limit 10')
        df = pd.DataFrame(mycursor.fetchall(), columns=['District_name', 'Total_Tr_Amount', 'Total_Tr_Count'])
        image = px.pie(df, title='Top 10 Districts', values='Total_Tr_Count', names='District_name',
                       color_discrete_sequence=px.colors.sequential.deep, hover_data=['Total_Tr_Count'],
                       labels={'Total_Tr_Count': 'Total_Tr_Count'})
        image.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(image, use_container_width=True)
        st.header('Details of Top 10 Districts in  Table')
        st.write(df)

        mycursor.execute(
            f'select Pincodes, sum(Amount) as Total_Tr_Amount, sum(Count) as Total_Tr_Count from phonepepulse.topdata_all_india_transaction_pincode_df where Year={Year} and Quarter={Quarter}  group by Pincodes order by Total_Tr_Amount desc limit 10')
        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincodes', 'Total_Tr_Amount', 'Total_Tr_Count'])
        image = px.pie(df, title='Top 10 Districts', values='Total_Tr_Amount', names='Pincodes',
                       color_discrete_sequence=px.colors.sequential.Magenta_r, hover_data=['Total_Tr_Count'],
                       labels={'Total_Tr_Count': 'Total_Tr_Count'})
        image.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(image, use_container_width=True)
        st.header('Details of Top 10 Pincodes in  Table')
        st.write(df)

    if Type == "User":
        mycursor.execute(
            f'select sum(RegisteredUsers) as Total_RegisteredUsers,  sum(AppOpens) as Total_AppOpens from aggregated_all_india_user_df where Year={Year} and Quarter={Quarter}')
        df = pd.DataFrame(mycursor.fetchall(), columns=['Total_RegisteredUsers', 'Total_AppOpens'])
        Total_RegisteredUsers = df['Total_RegisteredUsers'][0]
        Total_AppOpens = df['Total_AppOpens'][0]
        st.header("")
        st.header("")
        st.header(f":violet[Overall Transaction in the year {Year} quarter {Quarter}]")
        st.subheader(':red[Total_RegisteredUsers]:  ' f':green[{Total_RegisteredUsers}]')
        st.subheader(':red[Total_AppOpens]:  ' f':green[{Total_AppOpens}]')
        st.header("")
        st.header("")
        st.header("")

        col1, col2 = st.columns([5, 5], gap="small")
        with col1:
            st.markdown("### :red[Brands]")
            mycursor.execute(
                f"select Brands, sum(Usrcount) as Total_Usr_Count, avg(percentage)*100 as Avg_Percentage from  phonepepulse.usr_ag_df where year = {Year} and quarter = {Quarter} group by Brands order by Total_Usr_Count desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Total_Usr_Count', 'Avg_Percentage'])
            img = px.bar(df,
                         title='Top 10 Brands',
                         x="Total_Usr_Count",
                         y="Brand",
                         orientation='h',
                         color='Avg_Percentage',
                         color_continuous_scale=px.colors.sequential.Blackbody)
            st.plotly_chart(img, use_container_width=True)

            st.markdown("### :blue[District]")
            mycursor.execute(
                f"select District_name, sum(RegisteredUsers) as TotalUsrCount, sum(AppOpens) as Total_Appopens from phonepepulse.usr_map_df where year = {Year} and quarter = {Quarter} group by District_name order by TotalUsrCount desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District_name', 'TotalUsrCount', 'Total_Appopens'])
            img = px.bar(df,
                         title='Top 10 Districts',
                         x="TotalUsrCount",
                         y="District_name",
                         orientation='h',
                         color='TotalUsrCount',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(img, use_container_width=True)



        with col2:
            st.markdown("### :violet[Pincode]")
            mycursor.execute(
                f"select Pincodes, sum(RegisteredUsers) as TotalUsers from phonepepulse.usrp_tp_df where year = {Year} and quarter = {Quarter} group by Pincodes order by TotalUsers desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincodes', 'TotalUsers'])
            img = px.pie(df,
                         values='TotalUsers',
                         names='Pincodes',
                         title='Top 10 Pincodes',
                         color_discrete_sequence=px.colors.sequential.deep,
                         hover_data=['TotalUsers'])
            img.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(img, use_container_width=True)

            st.markdown("### :green[State]")
            mycursor.execute(
                f"select State, sum(Registeredusers) as TotalUsr, sum(AppOpens) as TotalAppopens from phonepepulse.usr_map_df where year = {Year} and quarter = {Quarter} group by State order by TotalUsr desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'TotalUsr', 'TotalAppopens'])
            img = px.pie(df, values='TotalUsr',
                         names='State',
                         title='Top 10 States',
                         color_discrete_sequence=px.colors.sequential.haline_r,
                         hover_data=['TotalAppopens'],
                         labels={'TotalAppopens': 'TotalAppopens'})

            img.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(img, use_container_width=True)


if selected == "Data Explore":

    col1, col = st.columns([100, 1])
    with col1:
        st.info(
            """
            ####  Data Exploration:
            - This page Shows the geo visualisation of Transaction and User information of the Phone pe application. 
            """
        )
    chart = Type = st.selectbox('Choose type of visualisation', ('Geo Visualisation', 'Charts'))
    Type = st.selectbox('All India', ('Transaction', 'User'))

    col2, col3= st.columns([1.5, 1 ], gap="large")
    with col2:
        Year = st.selectbox('Year', (2018, 2019, 2020, 2021, 2022, 2023))

    with col3:
        if Year == 2023:
            Quarter = st.selectbox('Quarter', (1, 2))
        else:
            Quarter = st.selectbox("Quarter", (1, 2, 3, 4))

    if chart=="Geo Visualisation":
        if Type == "Transaction":

            st.markdown("## :green[Overall State Data - Transactions Amount]")
            mycursor.execute(
                f"select Name, sum(Amount) as Total_Tr_Amount, sum(Count) as Total_Tr_Count from phonepepulse.map_all_india_transaction_df where Year={Year} and Quarter={Quarter}  group by Name order by Name")
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Tr_Amount', 'Total_Tr_Count'])
            df2 = pd.read_csv(r'states.csv')
            df1.State = df2

            img = px.choropleth(df1,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='Total_Tr_Amount',
                                color_continuous_scale=px.colors.sequential.Agsunset)

            img.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(img, use_container_width=True)

            st.markdown("## :green[Overall State Data - Transactions Count]")
            mycursor.execute(
                f"select Name, sum(Amount) as Total_Tr_Amount, sum(Count) as Total_Tr_Count from phonepepulse.map_all_india_transaction_df where Year={Year} and Quarter={Quarter}  group by Name order by Name")
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Tr_Amount', 'Total_Tr_Count'])
            df2 = pd.read_csv(r'states.csv')
            df1.State = df2

            img = px.choropleth(df1,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='Total_Tr_Count',
                                color_continuous_scale='dense')

            img.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(img, use_container_width=True)



        if Type == "User":

            st.markdown("## :red[Overall State Data - Total User ]")
            mycursor.execute(
                f"select State, sum(RegisteredUsers) as TotalUsr, sum(AppOpens) as TotalAppopens from phonepepulse.usr_map_df where year = {Year} and quarter = {Quarter} group by State order by State")
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'TotalUsr', 'TotalAppopens'])
            df2 = pd.read_csv(
                r'States.csv')
            df1.State = df2

            img = px.choropleth(df1,
                                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='TotalUsr',
                                color_continuous_scale='orrd')

            img.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(img, use_container_width=True)


    if chart == "Charts":
        st.markdown("### :green[State]")
        mycursor.execute(
            f"select State, sum(Registeredusers) as TotalUsr, sum(AppOpens) as TotalAppopens from phonepepulse.usr_map_df where year = {Year} and quarter = {Quarter} group by State order by TotalUsr desc")
        df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'TotalUsr', 'TotalAppopens'])
        img = px.pie(df, values='TotalUsr',
                     names='State',
                     color_discrete_sequence=px.colors.sequential.Aggrnyl_r,
                     hover_data=['TotalAppopens'],
                     labels={'TotalAppopens': 'TotalAppopens'})

        img.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(img, use_container_width=True)



        st.markdown("### :blue[District]")
        mycursor.execute(
            f"select District_name, sum(RegisteredUsers) as TotalUsrCount, sum(AppOpens) as Total_Appopens from phonepepulse.usr_map_df where year = {Year} and quarter = {Quarter} group by District_name order by TotalUsrCount desc limit 15")
        df = pd.DataFrame(mycursor.fetchall(), columns=['District_name', 'TotalUsrCount', 'Total_Appopens'])
        img = px.bar(df,
                     x="TotalUsrCount",
                     y="District_name",
                     orientation='h',
                     color='TotalUsrCount',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(img, use_container_width=True)

        st.markdown("### :violet[Pincode]")
        mycursor.execute(
            f"select Pincodes, sum(RegisteredUsers) as TotalUsers from phonepepulse.usrp_tp_df where year = {Year} and quarter = {Quarter} group by Pincodes order by TotalUsers desc limit 15")
        df = pd.DataFrame(mycursor.fetchall(), columns=['Pincodes', 'TotalUsers'])
        img = px.pie(df,
                     values='TotalUsers',
                     names='Pincodes',
                     color_discrete_sequence=px.colors.sequential.deep,
                     hover_data=['TotalUsers'])
        img.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(img, use_container_width=True)


if selected=='Statistics':

    col2, col3 = st.columns([1.5, 1], gap="large")
    with col2:
        Year = st.selectbox('Year', (2018, 2019, 2020, 2021, 2022, 2023))

    with col3:
        if Year == 2023:
            Quarter = st.selectbox('Quarter', (1, 2))
        else:
            Quarter = st.selectbox("Quarter", (1, 2, 3, 4))

    charttype=st.selectbox("Chart type", ('Bar', 'Pie'))

    if charttype=='Bar':
        st.markdown("## :orange[Top Payment Category]")
        mycursor.execute(
            f"select Category, sum(Count) as Total_Transactions_Count, sum(Amount) as Total_TR_amount from phonepepulse.aggregated_all_india_transaction_df where year= {Year} and quarter = {Quarter} group by Category order by Category")
        df = pd.DataFrame(mycursor.fetchall(), columns=['Category', 'Total_Transactions_Count', 'Total_TR_amount'])

        img = px.bar(df,
                     title='Category vs Total_Transactions_Count',
                     x="Category",
                     y="Total_Transactions_Count",
                     orientation='v',
                     color='Total_TR_amount',
                     color_continuous_scale=px.colors.sequential.deep)
        st.plotly_chart(img, use_container_width=False)


    if charttype=='Pie':
        col2, col3 = st.columns([20, 1], gap="large")
        with col2:
            st.markdown("## :orange[Top Payment Category]")
            mycursor.execute(
                f"select Category, sum(Count) as Total_Transactions_Count, sum(Amount) as Total_TR_amount from phonepepulse.aggregated_all_india_transaction_df where year= {Year} and quarter = {Quarter} group by Category order by Category")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Category', 'Total_Transactions_Count', 'Total_TR_amount'])

            img = px.pie(df,values='Total_TR_amount', names='Category', hover_data=['Total_TR_amount'],color_discrete_sequence=px.colors.sequential.Agsunset)
            st.plotly_chart(img, use_container_width=False)
        with col3:
            st.markdown('## :orange[Top Brands]')
            mycursor.execute(
                f"select Brands, sum(UsrCount) as Total_Usr_Count, sum(Percentage) as Total_Usr_Percentage from  phonepepulse.usr_ag_df where year= 2018 and quarter = 1 group by Brands order by Brands")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Brands', 'Total_Usr_Count', 'Total_Usr_Percentage'])
            img = px.pie(df, values='Total_Usr_Count', names='Brands', hover_data=['Total_Usr_Count'],
                         color_discrete_sequence=px.colors.sequential.Pinkyl_r)
            st.plotly_chart(img, use_container_width=False)