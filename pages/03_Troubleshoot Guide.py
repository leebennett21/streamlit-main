from cmath import sqrt
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image


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
da_position = st.session_state['da_position']
db_position = st.session_state['db_position']
trig_position = st.session_state['trig_position']

# print(bike_vel, veh_vel,d_lat,da,db,dc,dd,length,radius)    
    
df = st.session_state['df']
testfile = st.session_state['Test File']
db_adj = st.session_state['db_adj']
da_db_distance = st.session_state['da_db_distance']
# da_db_sync_mid_point = st.session_state['da_db_sync_mid_point']
b_lim = st.session_state['b_lim']
# t_start_idx = st.session_state['t_start_idx']
t_start = st.session_state['t_start']
test_start = st.session_state['test_start']
test_start_idx = st.session_state['test_start_idx']
# test_end = st.session_state['test_end']
test_end_time_idx = st.session_state['test_end_time_idx']

######################## Criteria 1, 2 ##########################################
#vehicle position at the start of the corridor, start of test, and end of test
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
d_bike_acc = st.session_state['d_bike_acc']
d_bike_start = st.session_state['d_bike_start']
d_bike_end =st.session_state['d_bike_end']
test_start_limit = st.session_state['test_start_limit']

######################## Criteria 8 ##########################################

d_da_meas = st.session_state['d_da_meas']
d_db_meas_dbadj = st.session_state['d_db_meas_dbadj']
#first point of info and last point of info

Veh_collision_pt = st.session_state['Veh_collision_pt']
LPI = st.session_state['LPI']
LPI_time_idx = st.session_state['LPI_time_idx']
LPI_time = st.session_state['LPI_time']
FPI = st.session_state['FPI']
FPI_time_idx = st.session_state['FPI_time_idx']
FPI_time = st.session_state['FPI_time']
FPI_x = df['Vehicle bumper X position'].iloc[FPI_time_idx]
LPI_x = df['Vehicle bumper X position'].iloc[LPI_time_idx]

#position of vehicle bumper when the bike has reached test velocity
veh_entercorridor_time = st.session_state['veh_entercorridor_time']
veh_end_location = st.session_state['veh_end_location']
veh_entercorridor_location = st.session_state['veh_entercorridor_location']
veh_entercorridor_time = st.session_state['veh_entercorridor_time']
start_time_trans = st.session_state['start_time_trans']
bike_trig_location = st.session_state['bike_trig_location']
veh_trig_location = st.session_state['veh_trig_location']
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
#display Criteria Performance
expander = st.expander("Criteria Performance Overview", expanded=False)
with expander:
    columns = st.columns((6,1,6))
    with columns[0]:
        st.write(test_options)	
        st.write('Test file:' , testfile.name)

        crit1 = '<p style="font-family:sans-serif; color:Black; font-size: 21px;">Test Criteria 1</p>'
        st.markdown(crit1 ,unsafe_allow_html=True)
        st.write('Mean Laterial Deviation of vehicle (m):', round(veh_lat_mean,2))
        st.write('Std Laterial Deviation of vehicle:', round(veh_lat_std, 2))

        crit2 = '<p style="font-family:sans-serif; color:Black; font-size: 21px;">Test Criteria 2</p>'
        st.markdown(crit2 ,unsafe_allow_html=True)	
        st.write('Mean Laterial Deviation of bicycle (m):', round(bike_lat_mean,2))
        st.write('Std Laterial Deviation of bicycle:', round(bike_lat_std,2))

        crit3 = '<p style="font-family:sans-serif; color:Black; font-size: 21px;">Test Criteria 3</p>'
        st.markdown(crit3 ,unsafe_allow_html=True)
        st.write('Mean Vehicle velocity before start of test (km/h):', round(veh_vel_corr_mean,2))
        st.write('Std Vehicle velocity:', round(veh_vel_corr_std,2))

        crit4 = '<p style="font-family:sans-serif; color:Black; font-size: 21px;">Test Criteria 4</p>'
        st.markdown(crit4 ,unsafe_allow_html=True)
        st.write('Bike max velocity in corridor before start of test (km/h):', round(bike_vel_corr_max,2))
    with columns[2]:
        crit5 = '<p style="font-family:sans-serif; color:Black; font-size: 21px;">Test Criteria 5</p>'
        st.markdown(crit5 ,unsafe_allow_html=True)
        st.write('Bicycle- Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
        st.write('Bicycle- Distance to accelerate to Test Velocity (m):' , round(d_bike_acc,2))

        crit6 = '<p style="font-family:sans-serif; color:Black; font-size: 21px;">Test Criteria 6</p>'
        st.markdown(crit6 ,unsafe_allow_html=True)
        st.write('Vehicle mean Velocity (kph):' , round(veh_vel_mean,2) )
        st.write('Vehicle standard deviation Velocity (kph)):' , round(veh_vel_std,3) )

        crit7 = '<p style="font-family:sans-serif; color:Black; font-size: 21px;">Test Criteria 7</p>'
        st.markdown(crit7 ,unsafe_allow_html=True) 
        st.write('Bicycle mean Velocity (kph):' , round(bike_vel_mean,2) )
        st.write('Bicycle standard deviation Velocity (kph)):' , round(bike_vel_std,3) )

####################################################################################################################

st.markdown("<h1 style='text-align: center; color: black;'>Test case and file</h1>", unsafe_allow_html=True)
st.write(test_options)	
st.write('Test file:' , testfile.name)	
st.write('---')

# Show warnings
###################################################################################################
# spec acceleration distance
spec_d = 5.66 #meters   
if d_bike_acc > spec_d+1:
    slow_crit = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle Acceleration is **SLOW**</p>'
    st.markdown(slow_crit, unsafe_allow_html=True)
    st.write('Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
    st.write('Distance to accelerate to Test Velocity (m):' , round(d_bike_acc,2))
    # st.write('Bicycle- Time to accelerate to Test Velocity (s):' ,  round(test_start-test_start_limit,2))
    # st.write('Bicycle- Distance to accelerate to Test Velocity (m):' , round(d_bike_acc,2))
    st.write('---')
    
elif d_bike_acc < spec_d-1:
    fast_crit = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle Acceleration is **FAST**</p>'
    st.markdown(fast_crit, unsafe_allow_html=True)
    st.write('Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
    st.write('Distance to accelerate to Test Velocity (m):' , round(d_bike_acc,2))
    st.write('---')
###################################################################################################
#spec trigger points

if trig_position-veh_trig_location > 2:
    trig_early = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle is triggered **EARLY**</p>'
    st.markdown(trig_early, unsafe_allow_html=True)
    st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_position, 2), 'Actual -->', round(veh_trig_location,2), 'db_adj -->', round(db_adj,2))
    st.write('Bicycle is triggered :', round(trig_position-veh_trig_location,2), 'meters to early')
    st.write('---')
elif veh_trig_location -trig_position > 2:
    trig_late = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Bicycle is triggered **LATE**</p>'
    st.markdown(trig_late, unsafe_allow_html=True)
    st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_position, 2), 'Actual -->', round(veh_trig_location,2))
    st.write('Bicycle is triggered :', round(veh_trig_location-trig_position,2), 'meters to late')
    st.write('---')
###################################################################################################
max_separation = df['Separation X (veh bumper - bike front tire)'].max()
# st.write('max sep  ', max_separation)
if max_separation < da_db_distance:
    separation = '<p style="font-family:sans-serif; color:Red; font-size: 28px;">Vehicle and Bicycle separation is **NOT ENOUGH**</p>'
    st.markdown(separation, unsafe_allow_html=True)
    st.write('---')

###################################################################################################
# Plot location of bicycle and vehicle with respect to position of vehicle
st.markdown("<h1 style='text-align: center; color: black;'>Vehicle vs Bicycle Position Plot</h1>", unsafe_allow_html=True)
fig = px.line(df, x='Vehicle bumper X position', y=['Front tire X position', 'Separation X (veh bumper - bike front tire)'])
# fig = px.line(df, x='Vehicle bumper X position', y=['Front tire X position shift2origin', 'Separation X shift2origin (veh bumper - bike front tire)'])
fig.add_vline(x=db_position,line_width=1, line_dash="dashdot", line_color="blue")
fig.add_vrect(x0=db_position-0.5, x1=db_position+0.5, line_width=0, fillcolor="green", opacity=0.2)
fig.add_vline(x=trig_position,line_width=1, line_dash="dashdot", line_color="green")
fig.add_vline(x=veh_trig_location,line_width=1, line_dash="dash", line_color="purple")
# fig.add_vline(x=d_veh_start,line_width=1, line_dash="dot", line_color="black")
fig.add_hline(y=da_position,line_width=1, line_dash="dashdot", line_color="blue")
fig.add_hrect(y0=da_position-0.5, y1=da_position+0.5, line_width=0, fillcolor="green", opacity=0.2)
fig.add_hrect(y0=da_db_distance-0.5, y1=da_db_distance+0.5, line_width=0, fillcolor="purple", opacity=.3)
fig.update_layout({'title':{'text': 'da & db Calculated Positions', 
						'x':0.5, 'y':0.95, 
						'font_size':20, 
						'font_color':'red'}},
				showlegend=True)

fig.add_annotation(x=db_position, y=da_position,
			text="da db calc position",
			showarrow=True,
			arrowhead=1)
					
fig.update_xaxes(title_text='Vehicle Bumper X Position',
				minor_ticks="outside", 
                dtick=10,
				showgrid=True, 
				gridwidth=1, 
				gridcolor='lightgrey')
fig.add_annotation(x=10, y=da_db_distance,
				text="Separation X Veh bumper & Bike tire",
				showarrow=True,
				arrowhead=1) 
fig.add_annotation(x=veh_trig_location, y=0,
				text="Bike start - Trigger pt",
				showarrow=True,
				arrowhead=1) 
# fig.add_annotation(x=d_veh_start, y=5,
# 				text="Test start",
# 				showarrow=True,
# 				arrowhead=1)                               
# fig.add_annotation(x=db_pos, y=da_pos-10,
# 			text="db calc position",
# 			showarrow=True,
# 			arrowhead=1)
fig.add_annotation(x=trig_position, y=-20,
			text="Calc Trigger pt",
			showarrow=True,
			arrowhead=1)                
fig.update_yaxes(title_text='Bicycle Front tire X Position', 
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


st.header('Interactive Plots')
x_axis_val = st.selectbox('Select X-axis parameter', options=df.columns)
y_axis_val = st.selectbox('Select Y-axis parameter', options=df.columns)
plot= px.scatter(df, x=x_axis_val,y=[y_axis_val])
st.plotly_chart(plot)

##############################################################################################################
st.header('Interactive Plots')
x_axis_val = st.selectbox('X-axis parameter', options=df.columns)
y_axis_val = st.selectbox('Y-axis parameter', options=df.columns)
y_axis_val2 = st.selectbox('Y-axis 2nd parameter', options=df.columns)
# plot= px.scatter(df, x=x_axis_val,y=[y_axis_val])
plot= px.scatter(df, x=x_axis_val,y=[y_axis_val,y_axis_val2])
st.plotly_chart(plot)
