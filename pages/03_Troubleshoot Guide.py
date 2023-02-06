from cmath import sqrt
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from PIL import Image
import math

st.set_page_config(
     page_title="Troubleshoot Guide",
     layout="wide",
     initial_sidebar_state="expanded",
     page_icon = ':hospital:',
     
 )

test_options = st.session_state['test_options']

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


# print(bike_vel, veh_vel,d_lat,da,db,dc,dd,length,radius)    
    
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
veh_d_corridor = st.session_state['veh_d_corridor']
veh_d_start = st.session_state['veh_d_start']
veh_d_end = st.session_state['veh_d_end']
veh_lat_mean = st.session_state['veh_lat_mean']
veh_lat_std = st.session_state['veh_lat_std']
bike_lat_mean = st.session_state['bike_lat_mean']
bike_lat_std = st.session_state['bike_lat_std']

######################## Criteria 3, 4, 6, 7  ##########################################
veh_vel_corr_mean = st.session_state['veh_vel_corr_mean']
veh_vel_corr_std = st.session_state['veh_vel_corr_std']
bike_vel_corr_max = st.session_state['bike_vel_corr_max']
veh_vel_mean = st.session_state['veh_vel_mean']
veh_vel_std = st.session_state['veh_vel_std']
bike_vel_mean = st.session_state['bike_vel_mean']
bike_vel_std = st.session_state['bike_vel_std']
#find lateral distances during test

######################## Criteria 5 ##########################################
bike_d_acc = st.session_state['bike_d_acc']
bike_d_start = st.session_state['bike_d_start']
bike_d_end = st.session_state['bike_d_end']


######################## Criteria 8 ##########################################
da_meas = st.session_state['da_meas']
db_meas = st.session_state['db_meas']
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
# st.write('vehicle position when bike starts', x_start)
x_end = df['Vehicle bumper X position'].iloc[test_end_idx]
FPI_x = df['Vehicle bumper X position'].iloc[FPI_time_idx]
LPI_x = df['Vehicle bumper X position'].iloc[LPI_time_idx]

crit_1= st.session_state['crit_1']
crit_2= st.session_state['crit_2']
crit_3= st.session_state['crit_3']
crit_4= st.session_state['crit_4']
crit_5= st.session_state['crit_5']
crit_6= st.session_state['crit_6']
crit_7= st.session_state['crit_7']
crit_8= st.session_state['crit_8']

###################################################################################################
#display test plan to review

expander = st.expander("Test Plan overview", expanded=False)
with expander:
    columns = st.columns((1,2,1))
    with columns[1]:
        st.markdown("<h1 style='text-align: center; color: black;'>Test Plan overview</h1>", unsafe_allow_html=True)
        image1 = Image.open('Reg151 Test Cases.JPG')
        st.image(image1, caption='UN Regulation 151 Test Cases')

###################################################################################################
def pass_or_fail(criteria, crit_number):
    if criteria == True:
        pass_crit = f"""<p style="font-family:sans-serif; color:Green; font-size: 28px;">Test Criteria {crit_number} = **PASS**</p>"""
        st.markdown(pass_crit, unsafe_allow_html=True)
    else:
        fail_crit = f"""<p style="font-family:sans-serif; color:Red; font-size: 28px;">Test Criteria {crit_number} = **FAIL**</p>"""
        st.markdown(fail_crit, unsafe_allow_html=True)
#display Criteria Performance
expander = st.expander("Criteria Performance Overview", expanded=False)
with expander:
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

################################################################################################### 

# # find relative location of bike at d_a
# t_da_idx = df.loc[(df['Front tire X position'] >= da_pos), ['Time'] ].index[0]
# da_bike = df.loc[t_da_idx, 'Front tire X position']
# db_vehicle = df.loc[t_da_idx, 'Vehicle bumper X position']

# # position of vehicle when the bike is triggered/started
# veh_pos_trig = df['Vehicle bumper X position'].iloc[t_start_idx]
# st.write('vehicle position when bike starts', veh_pos_trig)

# db_meas = df.loc[t_start_idx,'Vehicle bumper X position']
# st.write('vehicle position when bike starts', db_meas)


# da_start = veh_pos_trig + da_pos
# db_start = veh_pos_trig + db_pos
# d_trig = veh_pos_trig + trig_pos

# #Position of vehicle when the test has started
# x_start = df['Vehicle bumper X position'].iloc[test_start_idx]
# #Position of vehicle when the test has ended
# x_end = df['Vehicle bumper X position'].iloc[test_end_idx]

# #find the calculate trigger point wrt to the vehicle in time
# calc_bike_trig_idx = df.loc[(df['Vehicle bumper X position'] >= trig_pos), ['Time'] ].index[0]
# calc_bike_trig_time = df.loc[calc_bike_trig_idx, 'Time']
# # st.write('calc bike trig time', calc_bike_trig_time)
####################################################################################################################
meas_crit = f"""<h1 style='text-align: center; color: black;'>Measured Parameters for {test_options}, Test file {testfile.name} </p>"""
st.markdown(meas_crit, unsafe_allow_html=True)

# Show warnings
###################################################################################################
# spec acceleration distance
spec_d = 5.66 #meters   
if bike_d_acc > spec_d+1:
    slow_crit = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle Acceleration is **SLOW**</p>'
    st.markdown(slow_crit, unsafe_allow_html=True)
    st.write('Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
    st.write('Distance to accelerate to Test Velocity (m):' , round(bike_d_acc,2))
    st.write('---')
    
elif bike_d_acc < spec_d-1:
    fast_crit = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle Acceleration is **FAST**</p>'
    st.markdown(fast_crit, unsafe_allow_html=True)
    st.write('Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
    st.write('Distance to accelerate to Test Velocity (m):' , round(bike_d_acc,2))
    st.write('---')
###################################################################################################
#spec trigger points

if trig_pos-db_meas > 2:
    trig_early = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle is triggered **EARLY**</p>'
    st.markdown(trig_early, unsafe_allow_html=True)
    st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_pos, 2), 'Actual -->', round(db_meas,2))
    st.write('Bicycle is triggered :', round(trig_pos-db_meas,2), 'meters to early')
    st.write('---')
elif db_meas -trig_pos > 2:
    trig_late = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle is triggered **LATE**</p>'
    st.markdown(trig_late, unsafe_allow_html=True)
    st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_pos, 2), 'Actual -->', round(db_meas,2))
    st.write('Bicycle is triggered :', round(db_meas-trig_pos,2), 'meters to late')
    st.write('---')
###################################################################################################
max_separation = df['Separation w db adjust'].max()
# st.write('max sep  ', max_separation)
if max_separation < da_db_distance:
    separation = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Vehicle and Bicycle separation is **NOT ENOUGH**</p>'
    st.markdown(separation, unsafe_allow_html=True)
    st.write('---')

###################################################################################################
# Plot location of bicycle and vehicle with respect to position of vehicle
st.markdown("<h1 style='text-align: center; color: black;'>Test Plots</h1>", unsafe_allow_html=True)
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



#################################################################################################################################

# fig = px.line(df, x='Time', y=['Front tire X position', 'Vehicle bumper X position'])

# fig.add_vline(x=t_start,line_width=1, line_dash="dashdot", line_color="green")
# fig.add_vline(x=calc_bike_trig_time, line_width=1, line_dash="dash", line_color="red")
# # fig.add_hline(y=2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
# # fig.add_hline(y=-2+veh_vel_mean,line_width=1, line_dash="dash", line_color="blue")
# # fig.add_hline(y=0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
# # fig.add_hline(y=-0.5+bike_vel_mean,line_width=1, line_dash="dash", line_color="red")
# # fig.add_vline(x=calc_bike_trig_time,line_width=1, line_dash="solid", line_color="black")
# # fig.add_vline(x=LPI_time,line_width=1, line_dash="solid", line_color="black")

# fig.update_layout({'title':{'text': 'Vehicle and Bicycle distance over Time', 
#                         'x':0.4, 'y':0.95, 
#                         'font_size':20, 
#                         'font_color':'red'}},
#                 showlegend=True)

# fig.add_annotation(x=calc_bike_trig_time, y=5,
#             text="Calc trigger pt",
#             showarrow=True,
#             arrowhead=1)
# fig.add_annotation(x=t_start, y=0,
#             text="Actual trigger pt",
#             showarrow=True,
#             arrowhead=1)
# # fig.add_annotation(x=FPI_time, y=2,
# #             text="FPI",
# #             showarrow=True,
# #             arrowhead=1)
# # fig.add_annotation(x=LPI_time, y=2,
# #             text="LPI",
# #             showarrow=True,
# #             arrowhead=1)            
# # fig.add_annotation(x=test_end, y=15,
# #             text="Simulated Collision",
# #             showarrow=True,
# #             arrowhead=1)
# fig.update_xaxes(title_text='Time (s)',
#                 minor_ticks="outside", 
#                 showgrid=True, 
#                 gridwidth=1, 
#                 gridcolor='lightgrey')

# fig.update_yaxes(title_text='Relative distance (m)', 
#                 minor_ticks="outside", 
#                 showgrid=True, 
#                 gridwidth=1, 
#                 gridcolor='lightgrey')
# fig.update_layout(legend=dict(
#     yanchor="top",
#     y=0.99,
#     xanchor="left",
#     x=0.01
# ))               
# st.plotly_chart(fig)


# ##################################################################################################################################

# st.header('Animated Plot')

# # Skip every 10th row to speed up simulation
# df_short = df[::50] # data pt every 1 seconds
# df_short = df_short.iloc[:-3, :]
# # st.write(df_short)

# max_x = 1+df_short['Time'].round(0).max()
# min_x = -1+df_short['Time'].round(0).min()

# max_y = 1+df_short['Front tire X position'].round(0).max()
# min_y = -1+df_short['Front tire X position'].round(0).min()
# max_yy = 1+df_short['Vehicle bumper X position'].round(0).max()
# min_yy = -1+df_short['Vehicle bumper X position'].round(0).min()
# mx_y = max(max_y, max_yy)
# mn_y = min(min_y, min_yy)
# st.write('max' , max_x ,' min', min_x)
# # fig = px.line(df, x='X position', y=['ABS Separation w db adjust', 'Separation w db adjust', 'Bike forward velocity'])
# # fig = px.line(df_short, x='X position', y='Separation w db adjust', animation_frame="Time")
# fig = px.scatter(df_short, x='Time', y=['Vehicle bumper X position', 'Front tire X position', 'Separation w db adjust'], range_x=[min_x, max_x], range_y=[mn_y,mx_y], animation_frame="Time")
# # fig2 = px.scatter(df_short, x='Time', y=['X position','Object 1 relative longitudinal distance'], range_x=[0, 50], range_y=[-50,50], animation_frame="FrameNumber ()")
# fig.add_hrect(y0=da_db_distance-0.5, y1=da_db_distance+0.5, line_width=0, fillcolor="red", opacity=0.2)
# fig.add_vline(x=t_start,line_width=1, line_dash="dashdot", line_color="green")
# fig.add_vline(x=calc_bike_trig_time, line_width=1, line_dash="dash", line_color="red")
# # fig.add_hline(y=db_start,line_width=1, line_dash="solid", line_color="black")
# # fig.add_hline(y=d_trig,line_width=1, line_dash="solid", line_color="black")

# fig.update_xaxes(title_text='Time (s)',
#                 minor_ticks="outside", 
#                 showgrid=True, 
#                 gridwidth=1, 
#                 gridcolor='lightgrey')

# fig.update_yaxes(title_text='Relative distance (m)', 
#                 minor_ticks="outside", 
#                 showgrid=True, 
#                 gridwidth=1, 
#                 gridcolor='lightgrey')
# fig.update_layout(legend=dict(
#     yanchor="top",
#     y=0.99,
#     xanchor="left",
#     x=0.01
# ))
# fig.add_annotation(x=t_start, y=0,
#                 text="Trigger",
#                 showarrow=True,
#                 arrowhead=1)
# fig.add_annotation(x=calc_bike_trig_time, y=0,
#                 text="Calc Trigger",
#                 showarrow=True,
#                 arrowhead=1)
# fig.add_annotation(x=0, y=da_db_distance,
#                 text="Separation Line",
#                 showarrow=True,
#                 arrowhead=1)	

# #control speed of layout
# # fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
# # fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 100
# st.plotly_chart(fig)
# # st.plotly_chart(fig2)

##############################################################################################################
st.header('Interactive Plots')
x_axis_val = st.selectbox('Select X-axis parameter', options=df.columns)
y_axis_val = st.selectbox('Select Y-axis parameter', options=df.columns)
y_axis_val2 = st.selectbox('Select Y-axis 2nd parameter', options=df.columns)
# plot= px.scatter(df, x=x_axis_val,y=[y_axis_val])
plot= px.scatter(df, x=x_axis_val,y=[y_axis_val,y_axis_val2])
st.plotly_chart(plot)


