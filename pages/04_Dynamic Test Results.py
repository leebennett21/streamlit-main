import streamlit as st
# from PIL import Image
import pandas as pd
import plotly_express as px

st.set_page_config(
     page_title="Troubleshoot Guide",
     layout="wide",
     initial_sidebar_state="expanded",
     page_icon = ':chart:',
     
 )

# add session states needed for page
df = st.session_state['df']
b_lim = st.session_state['b_lim']

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


dadbsync = st.session_state['dadbsync']
if dadbsync.empty:
    st.warning('No sync found with d_a and d_b', icon="⚠️")

t_start_idx = st.session_state['t_start_idx']
t_start = st.session_state['t_start']
test_start = st.session_state['test_start_sync']
test_start_idx = st.session_state['test_start_idx_sync']
test_end = st.session_state['test_end_sync']
test_end_idx = st.session_state['test_end_idx_sync']

#load lateral distances 
veh_lat_mean = st.session_state['veh_lat_mean_sync']
bike_lat_mean = st.session_state['bike_lat_mean_sync']
veh_lat_std = st.session_state['veh_lat_std_sync']
bike_lat_std = st.session_state['bike_lat_std_sync']


testfile = st.session_state['Test File']

#load velocity 
veh_vel_mean = st.session_state['veh_vel_mean_sync']
bike_vel_mean = st.session_state['bike_vel_mean_sync']
veh_vel_std = st.session_state['veh_vel_std_sync']
bike_vel_std = st.session_state['bike_vel_std_sync']

# bike acceleration and distance
bike_d_acc = st.session_state['bike_d_acc']
bike_d_start = st.session_state['bike_d_start']
bike_d_end = st.session_state['bike_d_end']

#first point of info and last point of info
db_adj = st.session_state['db_adj']
da_db_distance = st.session_state['da_db_distance']
Veh_collision_pt = st.session_state['Veh_collision_pt_sync']
LPI = st.session_state['LPI_sync']
LPI_time_idx = st.session_state['LPI_time_idx_sync']
LPI_time = st.session_state['LPI_time_sync']
LPI_Frame = st.session_state['LPI_Frame_sync']
FPI = st.session_state['FPI_sync']
FPI_time_idx = st.session_state['FPI_time_idx_sync']
FPI_time = st.session_state['FPI_time_sync']
FPI_Frame = st.session_state['FPI_Frame_sync']
#when is the first index when the bike reaches bottom boundary
# t_reach_idx = df.loc[(df['Bike forward velocity'] >= bike_vel-0.5), ['Time'] ].index[0]
# t_reach_time = df.loc[t_reach_idx, 'Time'] 
# t_start_x = df.loc[t_start_idx, 'Front tire X position']
# t_reach_x = df.loc[t_reach_idx, 'Front tire X position'] 
# bike_d_start_ref = df['Front tire X position'].iloc[t_start_idx]
# bike_d_start = df['Vehicle bumper X position'].iloc[t_start_idx]
da_start = df['Front tire X position'].iloc[test_start_idx] 
db_start = df['Vehicle bumper X position'].iloc[test_start_idx]
# d_trig = bike_d_start

# st.write('Collision Point ', round(Veh_collision_pt, 2))
# st.write(' LPI ', round(LPI, 2))
# st.write('LPI_time_idx ' , LPI_time_idx)
# st.write(' FPI ', round(FPI, 2), '  4*Veh_velocity', round(4*veh_vel_mean/3.6, 2),  'L adjustment ', round(length, 2))
# st.write('LPI_time  ',LPI_time)
# st.write('FPI_time  ',FPI_time)

columns = st.columns((6,1,6))
with columns[0]:	
    # st.write('Start time (s):' , round(test_start,2) )
    # st.write('Collision time (s):' , round(test_end ,2) )
    # st.write('Start to Collision time (s):', round(test_end-test_start,2) )
    st.write('Test file:' , testfile.name)	
    st.write('Bicycle- Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
    st.write('Bicycle- Distance to accelerate to Test Velocity (m):' , round(bike_d_acc,2))
    st.write('Location of Bike start (m) Trigger pt:  ' , '  Calc', round(trig_pos, 2) , 'Sync', round(bike_d_start,2))	
    st.write('da calc position (m):  ' , da_pos,'  da sync position:  ' , round(da_start,2))
    st.write('db calc position (m):  ' , db_pos,'  db sync position:  ' , round(db_start ,2))


with columns[2]:
    st.write('Collision Point ', round(Veh_collision_pt, 2))
    st.write(' LPI position (m): ', round(LPI, 2), 'LPI_time_idx ' , LPI_time_idx, 'LPI_time  ',round(LPI_time,2))
    st.write(' FPI position (m): ', round(FPI, 2), 'FPI_time_idx ' , FPI_time_idx, 'FPI_time  ', round(FPI_time,2))
    st.write('4*Veh_velocity (m):', round(4*veh_vel_mean/3.6, 2),  'L adjustment ', round(length, 2))
    st.write('Vehicle mean Velocity (kph):' , round(veh_vel_mean,2) )
    st.write('Vehicle standard deviation Velocity (kph)):' , round(veh_vel_std,3) )    
    st.write('Bicycle mean Velocity (kph):' , round(bike_vel_mean,2) )
    st.write('Bicycle standard deviation Velocity (kph)):' , round(bike_vel_std,3) )


fig = px.line(df, x='Vehicle bumper X position', y=['Separation w db adjust', 'Front tire X position'])
fig.add_vline(x=db_pos,line_width=1, line_dash="dashdot", line_color="black")
fig.add_vline(x=db_start,line_width=1, line_dash="dash", line_color="green")
fig.add_vline(x=bike_d_start,line_width=1, line_dash="dash", line_color="green")
fig.add_vline(x=trig_pos,line_width=1, line_dash="dashdot", line_color="black")
fig.add_hline(y=da_pos,line_width=1, line_dash="dashdot", line_color="black")
fig.add_hline(y=da_start,line_width=1, line_dash="dash", line_color="green")
fig.add_hline(y=da_db_distance,line_width=1, line_dash="dash", line_color="blue")
fig.add_hrect(y0=da_db_distance-0.5, y1=da_db_distance+0.5, line_width=0, fillcolor="green", opacity=0.2)
fig.update_xaxes(title_text='Vehicle Bumper X Position',
            minor_ticks="outside", 
            showgrid=True, 
            gridwidth=1, 
            gridcolor='lightgrey')
fig.update_yaxes(title_text='Bicycle Front tire X Position wrt Vehicle', 
            minor_ticks="outside", 
            showgrid=True, 
            gridwidth=1, 
            gridcolor='lightgrey')
fig.update_layout({'title':{'text': 'da & db Positions for Calculated vs Synchronization ', 
                    'x':0.5, 'y':0.95, 
                    'font_size':20, 
                    'font_color':'red'}},
            showlegend=True)
fig.add_annotation(x=10, y=da_db_distance,
            text="da db sync position",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=0, y=da_pos,
            text="da calc position",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=10, y=da_start,
            text="da sync position",
            showarrow=True,
            arrowhead=1)						
fig.add_annotation(x=bike_d_start, y=10,
            text="Sync Trigger pt",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=trig_pos, y=-10,
            text="Calc trigger pt",
            showarrow=True,
            arrowhead=1)                                
fig.add_annotation(x=db_pos, y=2,
            text="db calc position",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=db_start, y=2,
            text="db sync position",
            showarrow=True,
            arrowhead=1)                
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))         
st.plotly_chart(fig)



st.markdown("<h1 style='text-align: center; color: black;'>Lateral Relative Distances and Tolerances</h1>", unsafe_allow_html=True)
###################################################################################################
# Provide easy access to criteria being tested
expander = st.expander("Criteria for Lateral distances", expanded=False)
with expander:
    st.caption('**Criteria 1:**	*Lateral deviation:*  Ego Vehicle must not deviate beyond +/- 0.1 m from the test path while the Ego Vehicle is between the CORRIDOR LINE and the COLLISION LINE.')
    st.caption('**Criteria 2:**	*Lateral deviation:*  Target VRU must not deviate beyond +/- 0.2 m from the test path d_Path_Lateral m to the nearside (right) edge of the Ego Vehicle while the Target VRU is between the BICYCLE START LINE and the COLLISION LINE.')

###################################################################################################
# display test parameters
columns = st.columns((3,1,6))
with columns[0]:
    st.write('Start time (s):' , round(test_start,2) )
    # st.markdown(f"<h6>Start time (s):    {round(test_start,2)}</h6>" , unsafe_allow_html=True )
    st.write('Collision time (s):' , round(test_end ,2) )
    st.write('Mean lateral separation (m):' , abs(round(bike_lat_mean,2)) )
    st.write('Vehicle standard deviation lateral distance (m):' , round(veh_lat_std,3) )
    st.write('Bicycle standard deviation lateral distance (m):' , round(bike_lat_std,3) )
    

###################################################################################################
# display pass or fail test criteria
with columns[2]:
    if df['Vehicle Lateral position'][test_start_idx:test_end_idx].max()< 0.1 and df['Vehicle Lateral position'][test_start_idx:test_end_idx].min()> -0.1 :
        pass_crit1 = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Vehicle Criteria 1 = **PASS**</p>'
        st.session_state['crit1'] = True
        st.markdown(pass_crit1, unsafe_allow_html=True)
        
    else:
        fail_crit1 = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Vehicle Criteria 1 = **FAIL**</p>'
        st.session_state['crit1'] = False
        st.markdown(fail_crit1, unsafe_allow_html=True)
        
    if df['Bike Relative Lateral position'][test_start_idx:test_end_idx].max()< 0.2+b_lim and df['Bike Relative Lateral position'][test_start_idx:test_end_idx].min()>-0.2+b_lim :
        pass_crit2 = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 2 = **PASS**</p>'
        st.session_state['crit2'] = True
        st.markdown(pass_crit2, unsafe_allow_html=True)
        
    else:
        fail_crit2 = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 2 = **FAIL**</p>'
        st.session_state['crit2'] = False
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
		fig.update_layout({'title':{'text': 'Lateral Distance of Vehicle and Bicycle Path', 
                            'x':0.5, 'y':0.95, 
                            'font_size':20, 
                            'font_color':'red'}},
                 showlegend=True)
		fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
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
    st.caption('**Criteria 5:**	*Speed initiation:*  Target VRU must reach V_TRGT km/h +/- 0.5 km/h prior to reaching the BICYCLE SPEED LINE that is 5.66 m in front of the BICYCLE START LINE')
    st.caption('**Criteria 6:** *Speed maintenance:*  Ego Vehicle must maintain V_EGO km/h +/- 2 km/h until reaching  the TEST STOP LINE (not fully specified by Reg 151)')
    st.caption('**Criteria 7:** *Speed maintenance:*  Target VRU must maintain V_TRGT km/h +/- 0.5 km/h until reaching  the TEST STOP LINE (not fully specified by Reg 151)')
    st.caption('**Criteria 8:**	*Position maintenance:*  The front edge of the Ego Vehicle must be within +/- 0.5 m of LINE B at the instance the front edge of the Target VRU either reaches LINE A – 0.5 m, or LINE A + 0.5 m.')

###################################################################################################
# display test parameters
st.write('Test file:' , testfile.name)
columns = st.columns((6,1,6))
with columns[0]:
    st.write('Start time (s):' , round(test_start,2) )
    st.write('Collision time (s):' , round(test_end ,2) )
    st.write('Bicycle- Amount of Time: start bike to start of test (s):' ,  round(test_start-t_start,2))
    st.write('Bicycle- Distance: start bike to start of test (m):' , round(bike_d_acc,2))
with columns[2]:
    st.write('Vehicle mean Velocity (kph):' , round(veh_vel_mean,2) )
    st.write('Vehicle standard deviation Velocity (kph)):' , round(veh_vel_std,3) )    
    st.write('Bicycle mean Velocity (kph):' , round(bike_vel_mean,2) )
    st.write('Bicycle standard deviation Velocity (kph)):' , round(bike_vel_std,3) )
    
###################################################################################################
# display pass or fail test criteria
if df['Vehicle forward velocity'][test_start_idx:test_end_idx].max()< veh_vel_mean +2 and df['Vehicle forward velocity'][test_start_idx:test_end_idx].min()> veh_vel_mean -2 :
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Vehicle Criteria 3 = **PASS**</p>'
    st.session_state['crit3'] = True
    st.markdown(pass_crit, unsafe_allow_html=True)
    
else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Vehicle Criteria 3 = **FAIL**</p>'
    st.session_state['crit3'] = False
    st.markdown(fail_crit, unsafe_allow_html=True)
    
if df['Bike forward velocity'][test_start_idx:test_end_idx].max()< bike_vel_mean+0.5 and df['Bike forward velocity'][test_start_idx:test_end_idx].min()>bike_vel_mean-0.5 :
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 7 = **PASS**</p>'
    st.session_state['crit7'] = True
    st.markdown(pass_crit, unsafe_allow_html=True)
    
else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 7 = **FAIL**</p>'
    st.session_state['crit7'] = False
    st.markdown(fail_crit, unsafe_allow_html=True)


###################################################################################################
# plot velocity test parameters
columns = st.columns((6,1,6))
with columns[0]:
    fig = px.line(df, x='Time', y=['Vehicle forward velocity', 'Bike forward velocity'])
    fig.add_vline(x=test_start,line_width=1, line_dash="dash", line_color="green")
    fig.add_vline(x=test_end,line_width=1, line_dash="dash", line_color="red")
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

