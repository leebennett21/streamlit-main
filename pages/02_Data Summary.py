import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.kaleido.scope.default_format = "jpeg"
pio.kaleido.scope.default_width = 1000
pio.kaleido.scope.default_height = 500

st.set_page_config(
     page_title="Troubleshoot Guide",
     layout="wide",
     initial_sidebar_state="expanded",
     page_icon = ':hospital:',
     
 )

test_options = st.session_state['test_options']
df = st.session_state['df'] 
# test criteria parameters
bike_vel = st.session_state['bike_vel']
veh_vel = st.session_state['veh_vel']
d_lat = st.session_state['d_lat']
da = st.session_state['da']
db = st.session_state['db']
dc = st.session_state['dc']
dd = st.session_state['dd']
length = st.session_state['length']
radius = st.session_state['radius']
da_pos = st.session_state['da_pos']
db_pos = st.session_state['db_pos']
trig_pos = st.session_state['trig_pos']
    
df = st.session_state['df']
testfile = st.session_state['Test File']
db_adj = st.session_state['db_adj']
da_db_distance = st.session_state['da_db_distance']
# da_db_sync_mid_point = st.session_state['da_db_sync_mid_point']
b_lim = st.session_state['b_lim']
t_start_idx = st.session_state['t_start_idx']
t_start = st.session_state['t_start']
test_start = st.session_state['test_start']
test_start_idx = st.session_state['test_start_idx']
test_end = st.session_state['test_end']
test_end_idx = st.session_state['test_end_idx']

######################## Criteria 1, 2 ##########################################
#vehicle position at the start of the corridor, start of test, and end of test
veh_t_corridor = st.session_state['veh_t_corridor']
veh_d_corridor = st.session_state['veh_d_corridor']
veh_d_start = st.session_state['veh_d_start']
veh_d_end = st.session_state['veh_d_end']
veh_lat_mean = st.session_state['veh_lat_mean']
veh_lat_std = st.session_state['veh_lat_std']
bike_lat_mean = st.session_state['bike_lat_mean']
bike_lat_std = st.session_state['bike_lat_std']
crit_1= st.session_state['crit_1']
crit_2= st.session_state['crit_2']

######################## Criteria 3, 4, 6, 7  ##########################################
veh_vel_corr_mean = st.session_state['veh_vel_corr_mean']
veh_vel_corr_std = st.session_state['veh_vel_corr_std']
bike_vel_corr_max = st.session_state['bike_vel_corr_max']
veh_vel_mean = st.session_state['veh_vel_mean']
veh_vel_std = st.session_state['veh_vel_std']
bike_vel_mean = st.session_state['bike_vel_mean']
bike_vel_std = st.session_state['bike_vel_std']
crit_3= st.session_state['crit_3']
crit_4= st.session_state['crit_4']
crit_6= st.session_state['crit_6']
crit_7= st.session_state['crit_7']
######################## Criteria 5 ##########################################
bike_d_acc = st.session_state['bike_d_acc']
bike_d_start = st.session_state['bike_d_start']
bike_d_end =st.session_state['bike_d_end']
crit_5= st.session_state['crit_5']
######################## Criteria 8 ##########################################
da_meas = st.session_state['da_meas']
db_meas = st.session_state['db_meas']
crit_8= st.session_state['crit_8']
#find lateral distances during test

# t_bike_acc = st.session_state['t_bike_acc']
bike_d_acc = st.session_state['bike_d_acc']
#first point of info and last point of info

Veh_collision_pt = st.session_state['Veh_collision_pt']
LPI = st.session_state['LPI']
LPI_time_idx = st.session_state['LPI_time_idx']
LPI_time = st.session_state['LPI_time']
FPI = st.session_state['FPI']
FPI_time_idx = st.session_state['FPI_time_idx']
FPI_time = st.session_state['FPI_time'] 

#position of vehicle bumper when the bike has reached test velocity
x_start  = st.session_state['x_start']

def pass_or_fail(criteria, crit_number):
    if criteria == True:
        pass_crit = f"""<p style="font-family:sans-serif; color:Green; font-size: 28px;">Test Criteria {crit_number} = **PASS**</p>"""
        st.markdown(pass_crit, unsafe_allow_html=True)
    else:
        fail_crit = f"""<p style="font-family:sans-serif; color:Red; font-size: 28px;">Test Criteria {crit_number} = **FAIL**</p>"""
        st.markdown(fail_crit, unsafe_allow_html=True)

test_file = f"""<p style="font-family:sans-serif; text-align: Center; color:Black; font-size: 38px;">{test_options}</p>"""
st.markdown(test_file, unsafe_allow_html=True)
# st.write('Test file:' , testfile.name)    
columns = st.columns((6,1,6))
with columns[0]:
    pass_or_fail(crit_1, 1)
    st.write('Mean Laterial Deviation of vehicle (m):', round(veh_lat_mean,2))
    st.write('Std Laterial Deviation of vehicle:', round(veh_lat_std, 2))
    st.write('---')

    pass_or_fail(crit_2, 2)
    st.write('Mean Laterial Deviation of bicycle (m):', round(bike_lat_mean,2))
    st.write('Std Laterial Deviation of bicycle:', round(bike_lat_std,2))
    st.write('---')    
  
    pass_or_fail(crit_3, 3)    
    st.write('Mean Vehicle velocity before start of test (km/h):', round(veh_vel_corr_mean,2))
    st.write('Std Vehicle velocity:', round(veh_vel_corr_std,2))
    st.write('---')

    pass_or_fail(crit_4, 4)    
    st.write('Bike max velocity in corridor before start of test (km/h):', round(bike_vel_corr_max,2))
    st.write('---')

with columns[2]:
    pass_or_fail(crit_5, 5)
    st.write('Bicycle- Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
    st.write('Bicycle- Distance to accelerate to Test Velocity (m):' , round(bike_d_acc,2))
    st.write('---')
   
    pass_or_fail(crit_6, 6)
    st.write('Vehicle mean Velocity (kph):' , round(veh_vel_mean,2) )
    st.write('Vehicle standard deviation Velocity (kph)):' , round(veh_vel_std,3) )
    st.write('---')

    pass_or_fail(crit_7, 7)
    st.write('Bicycle mean Velocity (kph):' , round(bike_vel_mean,2) )
    st.write('Bicycle standard deviation Velocity (kph)):' , round(bike_vel_std,3) )
    st.write('---')

    pass_or_fail(crit_8, 8)
    if trig_pos-db_meas > 2:
        st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_pos, 2), 'Actual -->', round(db_meas,2))
        st.write('Bicycle is triggered :', round(trig_pos-db_meas,2), 'meters to early')

    elif db_meas -trig_pos > 2:
        st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_pos, 2), 'Actual -->', round(db_meas,2))
        st.write('Bicycle is triggered :', round(db_meas-trig_pos,2), 'meters to late')
        st.write('---')
    st.write('---')

################################################################################################### 

values = [['Criteria 1', 'Criteria 2', 'Criteria 3', 'Criteria 4', 'Criteria 5', 'Criteria 6', 'Criteria 7','Criteria 8'], #1st col
  [crit_1,  crit_2,  crit_3,  crit_4,  crit_5, crit_6,  crit_7,  crit_8], # 2nd column
  ] # 3rd column]


fig = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [100,100],
  header = dict(
    values = [['<b>Test Criteria</b>'],
                  ['<b>Pass or Fail</b>'],
                  ],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['center','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'lightgreen']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
])

st.write(fig)



# colors = ['rgb(239, 243, 255)', 'rgb(189, 215, 231)', 'rgb(107, 174, 214)',
#           'rgb(49, 130, 189)', 'rgb(8, 81, 156)']
# data = {'Year' : [2010, 2011, 2012, 2013, 2014], 'Color' : colors}
# df = pd.DataFrame(data)

# fig = go.Figure(data=[go.Table(
#   header=dict(
#     values=["Color", "<b>YEAR</b>"],
#     line_color='white', fill_color='white',
#     align='center', font=dict(color='black', size=12)
#   ),
#   cells=dict(
#     values=[df.Color, df.Year],
#     line_color=[df.Color], fill_color=[df.Color],
#     align='center', font=dict(color='black', size=11)
#   ))
# ])
st.markdown("<h1 style='text-align: center; color: black;'>Lateral Relative Distances and Tolerances</h1>", unsafe_allow_html=True)
###################################################################################################
# Provide easy access to criteria being tested
expander = st.expander("Criteria for Lateral distances", expanded=False)
with expander:
    st.caption('**Criteria 1:**	*Lateral deviation:*  Ego Vehicle must not deviate beyond +/- 0.1 m from the test path while the Ego Vehicle is between the CORRIDOR LINE and the COLLISION LINE.')
    st.caption('**Criteria 2:**	*Lateral deviation:*  Target VRU must not deviate beyond +/- 0.2 m from the test path d_Path_Lateral m to the nearside (right) edge of the Ego Vehicle while the Target VRU is between the BICYCLE START LINE and the COLLISION LINE.')

###################################################################################################
# display test parameters
columns = st.columns((1,1,1))
# display pass or fail test criteria
with columns[1]:
    if crit_1 == True:

        pass_crit1 = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Vehicle Criteria 1 = **PASS**</p>'
        st.markdown(pass_crit1, unsafe_allow_html=True)
        
    else:
        fail_crit1 = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Vehicle Criteria 1 = **FAIL**</p>'
        st.markdown(fail_crit1, unsafe_allow_html=True)
        
    if crit_2 == True:
        pass_crit2 = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 2 = **PASS**</p>'
        st.markdown(pass_crit2, unsafe_allow_html=True)
        
    else:
        fail_crit2 = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 2 = **FAIL**</p>'
        st.markdown(fail_crit2, unsafe_allow_html=True)
        


st.markdown('---')
###################################################################################################
# plot lateral positions
columns = st.columns((4,1,1,6))
with columns[0]:

		fig = px.line(df, x='Time', y=['Vehicle Lateral position','Bike Relative Lateral position'])

		fig.update_xaxes(title_text='Time (s)',
                        minor_ticks="outside", 
                        showgrid=True, 
                        gridwidth=1, 
                        gridcolor='LightGreen')

		fig.update_yaxes(title_text='Lateral Distance (m)', 
                        minor_ticks="outside", 
                        showgrid=True, 
                        gridwidth=1, 
                        gridcolor='LightGreen')

		fig.add_vline(x=test_start,line_width=1, line_dash="dash", line_color="green")
		fig.add_vline(x=test_end,line_width=1, line_dash="dash", line_color="red")
		fig.add_vline(x=veh_t_corridor,line_width=1, line_dash="dash", line_color="red")
		fig.add_hline(y=0.1,line_width=1, line_dash="dash", line_color="blue")
		fig.add_hline(y=-0.1,line_width=1, line_dash="dash", line_color="blue")
		fig.add_hline(y=0.2+b_lim,line_width=1, line_dash="dash", line_color="red")
		fig.add_hline(y=-0.2+b_lim,line_width=1, line_dash="dash", line_color="red")
		fig.add_annotation(x=test_start, y=1,
                    text="Start of Test",
                    showarrow=True,
                    arrowhead=1)
		fig.add_annotation(x=test_end, y=1,
                    text="Simulated Collision",
                    showarrow=True,
                    arrowhead=1)
		fig.add_annotation(x=veh_t_corridor, y=1,
                text="Start of Corridor",
                showarrow=True,
                arrowhead=1)                                
		fig.update_layout({'title':{'text': 'Lateral Distance of Vehicle and Bicycle Path', 
                            'x':0.5, 'y':0.95, 
                            'font_size':20, 
                            'font_color':'red'}},
                 showlegend=True)
		fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
        )) 
		st.plotly_chart(fig)
with columns[3]:
    fig = px.line(df[test_start_idx:test_end_idx], x='Time', y=['Vehicle Lateral position','Bike Relative Lateral position'])

    fig.update_xaxes(title_text='Time (s)',
                    minor_ticks="outside", 
                    showgrid=True, 
                    gridwidth=1, 
                    gridcolor='LightGreen')

    fig.update_yaxes(title_text='Lateral Distance (m)', 
                    minor_ticks="outside", 
                    showgrid=True, 
                    gridwidth=1, 
                    gridcolor='LightGreen')

    fig.add_vline(x=test_start,line_width=1, line_dash="dash", line_color="green")
    fig.add_vline(x=test_end,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=0.1,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=-0.1,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=0.2+b_lim,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=-0.2+b_lim,line_width=1, line_dash="dash", line_color="red")
    fig.add_annotation(x=test_start, y=1,
                text="Start of Test",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=test_end, y=1,
                text="Simulated Collision",
                showarrow=True,
                arrowhead=1)
    fig.update_layout({'title':{'text': 'Lateral Distance of Vehicle and Bicycle from Start to Collision', 
                            'x':0.5, 'y':0.95, 
                            'font_size':20, 
                            'font_color':'red'}},
                 showlegend=False)
    st.plotly_chart(fig)

st.markdown('---')

###################################################################################################

st.markdown("<h1 style='text-align: center; color: black;'>Velocity Initiation and Maintenance</h1>", unsafe_allow_html=True)

# Provide easy access to criteria being tested
expander = st.expander("Criteria for Velocity Initiation and Maintenance", expanded=False)
with expander:
    st.caption('**Criteria 3:**	*Speed initiation:*  Ego Vehicle must reach V_EGO km/h +/- 2 km/h prior to the front edge of the Ego Vehicle reaching the nearer of the BICYCLE TRIGGER LINE or the CORRIDOR LINE')
    st.caption('**Criteria 4:**	*Speed initiation:*  If the CORRIDOR LINE is nearer than the BICYCLE TRIGGER LINE to the front edge of the Ego Vehicle, then the Target VRU must maintain 0.0 km/h while the front edge fo the Ego Vehicle is between the CORRIDOR LINE and the BICYCLE TRIGGER LINE.')
    st.caption('**Criteria 6:** *Speed maintenance:*  Ego Vehicle must maintain V_EGO km/h +/- 2 km/h until reaching  the TEST STOP LINE (not fully specified by Reg 151)')
    st.caption('**Criteria 7:** *Speed maintenance:*  Target VRU must maintain V_TRGT km/h +/- 0.5 km/h until reaching  the TEST STOP LINE (not fully specified by Reg 151)')
 
###################################################################################################
# display pass or fail test criteria
if crit_3 == True:
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Vehicle Criteria 3 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)
    
else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Vehicle Criteria 3 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)
    
if crit_4 == True:
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 4 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)
    
else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 4 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)

if crit_6 == True:
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 6 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)

else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 6 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)

if crit_7 == True:
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 7 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)

else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 7 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)


###################################################################################################
# plot velocity test parameters
columns = st.columns((6,1,6))
with columns[0]:
    fig = px.line(df, x='Time', y=['Vehicle forward velocity', 'Bike forward velocity'])
    fig.add_vline(x=test_start,line_width=1, line_dash="dash", line_color="green")
    fig.add_vline(x=test_end,line_width=1, line_dash="dash", line_color="red")
    fig.add_vline(x=veh_t_corridor,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=-2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=-0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
    fig.add_vline(x=FPI_time,line_width=1, line_dash="solid", line_color="black")
    fig.add_vline(x=LPI_time,line_width=1, line_dash="solid", line_color="black")
 
    fig.update_layout({'title':{'text': 'Velocity of Vehicle and Bicycle over Full Path', 
                            'x':0.4, 'y':0.95, 
                            'font_size':20, 
                            'font_color':'red'}},
                 showlegend=True)
    
    fig.add_annotation(x=test_start, y=5,
                text="Start of Test",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=t_start, y=0,
                text="Start of Bicycle",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=veh_t_corridor, y=0,
                text="Start of Corridor",
                showarrow=True,
                arrowhead=1)            
    fig.add_annotation(x=FPI_time, y=2,
                text="FPI",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=LPI_time, y=2,
                text="LPI",
                showarrow=True,
                arrowhead=1)            
    fig.add_annotation(x=test_end, y=15,
                text="Simulated Collision",
                showarrow=True,
                arrowhead=1)
    fig.update_xaxes(title_text='Time (s)',
                    minor_ticks="outside", 
                    showgrid=True, 
                    gridwidth=1, 
                    gridcolor='lightgrey')

    fig.update_yaxes(title_text='Velocity (kph)', 
                    minor_ticks="outside", 
                    showgrid=True, 
                    gridwidth=1, 
                    gridcolor='lightgrey')
    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
    ))                    
    st.plotly_chart(fig)
with columns[2]:
    fig = px.line(df[test_start_idx:test_end_idx], x='Time', y=['Vehicle forward velocity', 'Bike forward velocity'])
    fig.add_vline(x=test_start,line_width=1, line_dash="dash", line_color="green")
    fig.add_vline(x=test_end,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=-2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=-0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
    
    fig.update_layout({'title':{'text': 'Velocity of Vehicle and Bicycle from Start to Collision', 
                            'x':0.5, 'y':0.95, 
                            'font_size':20, 
                            'font_color':'red'}},
                 showlegend=False)
    fig.add_annotation(x=test_start, y=5,
                text="Start of Test",
                showarrow=True,
                arrowhead=1)
    fig.add_annotation(x=test_end, y=15,
                text="Simulated Collision",
                showarrow=True,
                arrowhead=1)
    fig.update_xaxes(title_text='Time (s)',
                    minor_ticks="outside", 
                    showgrid=True, 
                    gridwidth=1, 
                    gridcolor='lightgrey')

    fig.update_yaxes(title_text='Velocity (kph)', 
                    minor_ticks="outside", 
                    showgrid=True, 
                    gridwidth=1, 
                    gridcolor='lightgrey')
    st.plotly_chart(fig)



################################################################################################################################################
st.markdown("<h1 style='text-align: center; color: black;'>Speed Initiation</h1>", unsafe_allow_html=True)

# Provide easy access to criteria being tested
expander = st.expander("Speed Initiation", expanded=False)
with expander:
    st.caption('**Criteria 5:**	*Speed initiation:*  Target VRU must reach V_TRGT km/h +/- 0.5 km/h prior to reaching the BICYCLE SPEED LINE that is 5.66 m in front of the BICYCLE START LINE')
  
###################################################################################################
# display pass or fail test criteria
if crit_5 == True:
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Vehicle Criteria 5 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)
    
else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Vehicle Criteria 5 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)
fig = px.line(df, x='Time', y='Front tire X position')
fig.add_vline(x=test_start,line_width=1, line_dash="dash", line_color="green")
fig.add_vline(x=test_end,line_width=1, line_dash="dash", line_color="red")
fig.add_vline(x=veh_t_corridor,line_width=1, line_dash="dash", line_color="red")
# fig.add_hline(y=2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
# fig.add_hline(y=-2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
# fig.add_hline(y=0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
# fig.add_hline(y=-0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
fig.add_vline(x=FPI_time,line_width=1, line_dash="solid", line_color="black")
fig.add_vline(x=LPI_time,line_width=1, line_dash="solid", line_color="black")

fig.update_layout({'title':{'text': 'Velocity of Vehicle and Bicycle over Full Path', 
                        'x':0.4, 'y':0.95, 
                        'font_size':20, 
                        'font_color':'red'}},
                showlegend=True)

fig.add_annotation(x=test_start, y=5,
            text="Start of Test",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=t_start, y=0,
            text="Start of Bicycle",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=veh_t_corridor, y=0,
            text="Start of Corridor",
            showarrow=True,
            arrowhead=1)            
fig.add_annotation(x=FPI_time, y=2,
            text="FPI",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=LPI_time, y=2,
            text="LPI",
            showarrow=True,
            arrowhead=1)            
fig.add_annotation(x=test_end, y=15,
            text="Simulated Collision",
            showarrow=True,
            arrowhead=1)
fig.update_xaxes(title_text='Time (s)',
                minor_ticks="outside", 
                showgrid=True, 
                gridwidth=1, 
                gridcolor='lightgrey')

fig.update_yaxes(title_text='Front tire X position', 
                minor_ticks="outside", 
                showgrid=True, 
                gridwidth=1, 
                gridcolor='lightgrey')
fig.update_layout(legend=dict(
yanchor="top",
y=0.99,
xanchor="left",
x=0.01
))                    
st.plotly_chart(fig)

################################################################################################### 
st.markdown("<h1 style='text-align: center; color: black;'>Position Maintenance</h1>", unsafe_allow_html=True)

# Provide easy access to criteria being tested
expander = st.expander("Position Maintenance", expanded=False)
with expander:
    st.caption('**Criteria 8:**	*Position maintenance:*  The front edge of the Ego Vehicle must be within +/- 0.5 m of LINE B at the instance the front edge of the Target VRU either reaches LINE A – 0.5 m, or LINE A + 0.5 m.')
  
###################################################################################################   
if crit_8 == True:
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 8 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)
    
else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 8 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)
# Plot location of bicycle and vehicle with respect to position of vehicle
st.markdown("<h1 style='text-align: center; color: black;'> Test Plot for da and db position</h1>", unsafe_allow_html=True)
fig = px.line(df, x='Vehicle bumper X position', y=['Separation w db adjust','Front tire X position'])
fig.add_vline(x=db_pos,line_width=1, line_dash="dashdot", line_color="blue")
fig.add_vrect(x0=db_pos-0.5, x1=db_pos+0.5, line_width=0, fillcolor="green", opacity=0.2)
fig.add_vline(x=trig_pos,line_width=1, line_dash="dashdot", line_color="green")
fig.add_vline(x=db_meas,line_width=1, line_dash="dash", line_color="purple")
fig.add_vline(x=x_start,line_width=1, line_dash="dot", line_color="black")
fig.add_hline(y=da_pos,line_width=1, line_dash="dashdot", line_color="blue")
fig.add_hrect(y0=da_pos-0.5, y1=da_pos+0.5, line_width=0, fillcolor="green", opacity=0.2)
fig.add_hrect(y0=da_db_distance-0.5, y1=da_db_distance+0.5, line_width=0, fillcolor="purple", opacity=.3)
fig.update_layout({'title':{'text': 'Calculated Required Positions', 
						'x':0.5, 'y':0.95, 
						'font_size':20, 
						'font_color':'red'}},
				showlegend=True)

fig.add_annotation(x=db_pos-10, y=da_pos,
			text="da calc position",
			showarrow=True,
			arrowhead=1)
					
fig.update_xaxes(title_text='Vehicle Bumper X Position',
				minor_ticks="outside", 
                dtick=10,
				showgrid=True, 
				gridwidth=1, 
				gridcolor='lightgrey')
fig.add_annotation(x=10, y=da_db_distance,
				text="Distance require between Veh & Bike (da-db)",
				showarrow=True,
				arrowhead=1) 
fig.add_annotation(x=db_meas, y=0,
				text="Bike start - Trigger pt",
				showarrow=True,
				arrowhead=1) 
fig.add_annotation(x=x_start, y=5,
				text="Test start",
				showarrow=True,
				arrowhead=1)                               
fig.add_annotation(x=db_pos, y=da_pos-10,
			text="db calc position",
			showarrow=True,
			arrowhead=1)
fig.add_annotation(x=trig_pos, y=-20,
			text="Calc Trigger pt",
			showarrow=True,
			arrowhead=1)                
fig.update_yaxes(title_text='Bicycle Front tire X Position wrt Vehicle', 
				minor_ticks="outside",
                dtick = 10, 
				showgrid=True, 
				gridwidth=1, 
				gridcolor='lightgrey')
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))                
st.plotly_chart(fig)









fig = px.line(df, x='Time', y=['Front tire X position', 'Vehicle bumper X position'])
# fig = px.line(df, x='Time', y=['X position', 'Actual X (front axle)', 'Object 1 actual X (front axle)','Object 1 relative longitudinal distance'])
# fig = px.line(df, x='Time', y=['X position', 'Object1 actual X (front axle)'])
fig.add_vline(x=test_start,line_width=1, line_dash="dash", line_color="green")
fig.add_vline(x=test_end,line_width=1, line_dash="dash", line_color="red")
# fig.add_hline(y=2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
# fig.add_hline(y=-2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
# fig.add_hline(y=0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
# fig.add_hline(y=-0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
fig.add_vline(x=FPI_time,line_width=1, line_dash="solid", line_color="black")
fig.add_vline(x=LPI_time,line_width=1, line_dash="solid", line_color="black")

fig.update_layout({'title':{'text': 'Vehicle and Bicycle distance over Full Path', 
                        'x':0.4, 'y':0.95, 
                        'font_size':20, 
                        'font_color':'red'}},
                showlegend=True)

fig.add_annotation(x=test_start, y=5,
            text="Start of Test",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=t_start, y=0,
            text="Start of Bicycle",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=FPI_time, y=2,
            text="FPI",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=LPI_time, y=2,
            text="LPI",
            showarrow=True,
            arrowhead=1)            
fig.add_annotation(x=test_end, y=15,
            text="Simulated Collision",
            showarrow=True,
            arrowhead=1)
fig.update_xaxes(title_text='Time (s)',
                minor_ticks="outside", 
                showgrid=True, 
                gridwidth=1, 
                gridcolor='lightgrey')

fig.update_yaxes(title_text='Relative distance (m)', 
                minor_ticks="outside", 
                showgrid=True, 
                gridwidth=1, 
                gridcolor='lightgrey')
fig.update_layout(legend=dict(
yanchor="top",
y=0.99,
xanchor="left",
x=0.01
))                
st.plotly_chart(fig)








# video_file = open('./Test1 _MERGE.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)

# firebird = pd.DataFrame({'test track' : ['Firebird Racetrack', 'Sensata'], 'lat' :[ 43.7674206156433,43.60960308154709] , 'lon' : [-116.469511058211,-116.31195661539411]})
# st.write(firebird)
# st.map(firebird)


# st.write(fig)