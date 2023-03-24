import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.kaleido.scope.default_format = "jpeg"
pio.kaleido.scope.default_width = 1000
pio.kaleido.scope.default_height = 500
st.set_page_config(
     page_title="Data Summary",
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
da_position = st.session_state['da_position']
db_position = st.session_state['db_position']
trig_position = st.session_state['trig_position']
    
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
test_end_time = st.session_state['test_end_time']
test_end_time_idx = st.session_state['test_end_time_idx']
test_start_limit_idx = st.session_state['test_start_limit_idx']
test_start_limit = st.session_state['test_start_limit']

######################## Criteria 1, 2 ##########################################
#vehicle position at the start of the corridor, start of test, and end of test
veh_entercorridor_time = st.session_state['veh_entercorridor_time']
# veh_d_corridor = st.session_state['veh_d_corridor']
# veh_d_start = st.session_state['veh_d_start']
# veh_d_end = st.session_state['veh_d_end']
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
d_bike_acc = st.session_state['d_bike_acc']
d_bike_start = st.session_state['d_bike_start']
d_bike_end =st.session_state['d_bike_end']
crit_5= st.session_state['crit_5']
######################## Criteria 8 ##########################################
d_da_meas = st.session_state['d_da_meas']
d_db_meas = st.session_state['d_db_meas']
d_db_meas_dbadj = st.session_state['d_db_meas_dbadj']
da_meas_time = st.session_state['da_meas_time']

crit_8= st.session_state['crit_8']
##############################################################################
#what is the last point and first point of information
Veh_collision_pt = st.session_state['Veh_collision_pt']
LPI = st.session_state['LPI']
LPI_time_idx = st.session_state['LPI_time_idx']
LPI_time = st.session_state['LPI_time']
LPI_Frame = st.session_state['LPI_Frame']
FPI = st.session_state['FPI']
FPI_time_idx = st.session_state['FPI_time_idx']
FPI_time = st.session_state['FPI_time'] 
FPI_Frame = st.session_state['FPI_Frame']
##############################################################################

#position of vehicle bumper when the bike has reached test velocity
veh_entercorridor_time = st.session_state['veh_entercorridor_time']
veh_end_location = st.session_state['veh_end_location']
veh_entercorridor_location = st.session_state['veh_entercorridor_location']
veh_entercorridor_time = st.session_state['veh_entercorridor_time']
start_time_trans = st.session_state['start_time_trans']
bike_trig_location = st.session_state['bike_trig_location']
veh_trig_location = st.session_state['veh_trig_location']
db_delta_plus_time = st.session_state['db_delta_plus_time']
db_delta_minus_time = st.session_state['db_delta_minus_time']
db_delta_plus_idx = st.session_state['db_delta_plus_idx']
db_delta_minus_idx = st.session_state['db_delta_minus_idx']
##############################################################################
def pass_or_fail(criteria, crit_number):
    if criteria == True:
        pass_crit = f"""<p style="font-family:sans-serif; color:Green; font-size: 28px;">Test Criteria {crit_number} = **PASS**</p>"""
        st.markdown(pass_crit, unsafe_allow_html=True)
    else:
        fail_crit = f"""<p style="font-family:sans-serif; color:Red; font-size: 28px;">Test Criteria {crit_number} = **FAIL**</p>"""
        st.markdown(fail_crit, unsafe_allow_html=True)

test_file = f"""<p style="font-family:sans-serif; text-align: Center; color:Black; font-size: 38px;">{test_options} : Data Summary</p>"""
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
    #dsiplay FPI and LPI frame numbers
    if dd > 0:
        FPIframe = f"""<p style="font-family:sans-serif; color:Green; font-size: 21px;">FPI Frame # : {FPI_Frame}</p>"""
        st.markdown(FPIframe, unsafe_allow_html=True)
        LPIframe = f"""<p style="font-family:sans-serif; color:Green; font-size: 21px;">LPI Frame # : {LPI_Frame}</p>"""
        st.markdown(LPIframe, unsafe_allow_html=True)
        st.write('Number of Frames between LPI and FPI:', LPI_Frame-FPI_Frame)
        if LPI_Frame-FPI_Frame <10:
            warningframe = f"""<p style="font-family:sans-serif; color:Red; font-size: 32px;">!! Warning !! Check FrameID</p>"""
            st.markdown(warningframe, unsafe_allow_html=True)
    else:
        FPIframe = f"""<p style="font-family:sans-serif; color:Green; font-size: 21px;">FPI Frame # : None - dwell case</p>"""
        st.markdown(FPIframe, unsafe_allow_html=True)
        LPIframe = f"""<p style="font-family:sans-serif; color:Green; font-size: 21px;">LPI Frame # : {LPI_Frame}</p>"""
        st.markdown(LPIframe, unsafe_allow_html=True)

    
    
with columns[2]:
    pass_or_fail(crit_5, 5)
    st.write('Bicycle- Time to accelerate to Test Velocity (s):' ,  round(test_start-t_start,2))
    st.write('Bicycle- Distance to accelerate to Test Velocity (m):' , round(d_bike_acc,2))
    # st.write('The bike start has a ', round(test_start-t_start, 1),' second bounce')
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
    if trig_position-veh_trig_location > 2:
        st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_position, 2), 'Actual -->', round(veh_trig_location,2))
        st.write('Bicycle is triggered :', round(trig_position-veh_trig_location,2), 'meters to early')

    elif veh_trig_location -trig_position > 2:
        st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_position, 2), 'Actual -->', round(veh_trig_location,2))
        st.write('Bicycle is triggered :', round(veh_trig_location-trig_position,2), 'meters to late')
        st.write('---')
    else:
        st.write('Location of Vehicle at Trigger pt (m):' , 'Calc -->', round(trig_position, 2), 'Actual -->', round(veh_trig_location,2))
        # st.write('---')
    st.write('da_calc', round(da_position,2), 'da_actual', round(d_da_meas,2))
    st.write('db_calc', round(db_position,2), 'db_actual', round(d_db_meas,2))        
    st.write('---')

################################################################################################### 


st.markdown("<h1 style='text-align: center; color: black;'>Lateral Relative Distances and Tolerances</h1>", unsafe_allow_html=True)
###################################################################################################
# Provide easy access to criteria being tested
expander = st.expander("Criteria for Lateral distances", expanded=False)
with expander:
    st.caption('**Criteria 1:**	*Lateral deviation:*  Ego Vehicle must not deviate beyond +/- 0.1 m from the test path while the Ego Vehicle is between the CORRIDOR LINE and the COLLISION LINE.')
    st.caption('**Criteria 2:**	*Lateral deviation:*  Target VRU must not deviate beyond +/- 0.2 m from the test path d_Path_Lateral m to the nearside (right) edge of the Ego Vehicle while the Target VRU is between the BICYCLE START LINE and the COLLISION LINE.')

###################################################################################################
# display pass or fail test criteria

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
placeholder = st.empty()
with placeholder.container():
    fig = px.line(df, x='Time', y=['Vehicle Lateral position','Bike Lateral position'],color_discrete_sequence = ['navy', 'darkorange'])
    # fig.add_vline(x=veh_entercorridor_time,line_width=1, line_dash="dash", line_color="red")
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

    fig.add_vline(x=t_start,line_width=1, line_dash="dash", line_color="green")
    fig.add_vline(x=test_end_time,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=0.1,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=-0.1,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=0.2+b_lim,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=-0.2+b_lim,line_width=1, line_dash="dash", line_color="red")
    fig.add_annotation(x=t_start, y=-.5,
                text="Start of Bicycle",
                showarrow=True,
                arrowhead=1)
    # fig.add_annotation(x=veh_entercorridor_time, y=-1,
    #         text="Start of Corridor",
    #         showarrow=True,
    #         arrowhead=1)                            
    fig.add_annotation(x=test_end_time, y=-1,
                text="Simulated Collision",
                showarrow=True,
                arrowhead=1)
    fig.update_layout({'title':{'text': 'Lateral Distance of Vehicle and Bicycle over Time', 
                        'x':0.5, 'y':0.95, 
                        'font_size':20, 
                        'font_color':'red'}},
                legend_title="",         
                showlegend=True)
    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
    ))
    my_saved_image = "plot1.jpeg"
    pio.write_image(fig, my_saved_image)  
    st.plotly_chart(fig, use_container_width=True)

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
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Vehicle Criteria 6 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)

else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Vehicle Criteria 6 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)

if crit_7 == True:
    pass_crit = '<p style="font-family:sans-serif; text-align: center; color:Green; font-size: 28px;">Bike Criteria 7 = **PASS**</p>'
    st.markdown(pass_crit, unsafe_allow_html=True)

else:
    fail_crit = '<p style="font-family:sans-serif; text-align: center; color:Red; font-size: 28px;">Bike Criteria 7 = **FAIL**</p>'
    st.markdown(fail_crit, unsafe_allow_html=True)


###################################################################################################
# plot velocity test parameters
placeholder = st.empty()
with placeholder.container():
    fig = px.line(df, x='Time', y=['Bike forward velocity','Vehicle forward velocity'],color_discrete_sequence = ['navy', 'darkorange'])
    fig.add_vline(x=test_end_time,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=2+veh_vel,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=-2+veh_vel,line_width=1, line_dash="dash", line_color="blue")
    fig.add_hline(y=0.5+bike_vel,line_width=1, line_dash="dash", line_color="red")
    fig.add_hline(y=-0.5+bike_vel,line_width=1, line_dash="dash", line_color="red")
    if dd > 0:
        fig.add_vline(x=FPI_time,line_width=1, line_dash="solid", line_color="black")
    fig.add_vline(x=LPI_time,line_width=1, line_dash="solid", line_color="black")
 
    fig.update_layout({'title':{'text': 'Velocity of Vehicle and Bicycle over Time', 
                            'x':0.4, 'y':0.95, 
                            'font_size':20, 
                            'font_color':'red'}},
                legend_title="",            
                showlegend=True)
 
    fig.add_annotation(x=t_start, y=0,
                text="Start of Bicycle",
                showarrow=True,
                arrowhead=1)
    if dd > 0:            
        fig.add_annotation(x=FPI_time, y=2,
                    text="FPI",
                    showarrow=True,
                    arrowhead=1)
    fig.add_annotation(x=LPI_time, y=2,
                text="LPI",
                showarrow=True,
                arrowhead=1)            
    fig.add_annotation(x=test_end_time, y=15,
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
    my_saved_image = "plot2.jpeg"
    pio.write_image(fig, my_saved_image)                    
    st.plotly_chart(fig, use_container_width=True)
st.markdown('---')
################################################################################################################################################

# Plot location of bicycle and vehicle with respect to position of vehicle
# st.markdown("<h1 style='text-align: center; color: black;'>Vehicle vs Bicycle Position Plot</h1>", unsafe_allow_html=True)
# fig = px.line(df, x='Vehicle bumper X position', y=['Separation w db adjust','Front tire X position', 'Separation X (veh bumper - bike front tire)'])
placeholder = st.empty()
with placeholder.container():
    fig = px.line(df, x='Vehicle bumper X position', y=['Front tire X position', 'Separation X (veh bumper - bike front tire)'],color_discrete_sequence = ['navy', 'darkorange'])
    fig.add_vline(x=db_position,line_width=1, line_dash="dashdot", line_color="blue")
    fig.add_vrect(x0=db_position-0.5, x1=db_position+0.5, line_width=0, fillcolor="green", opacity=0.2)
    fig.add_vline(x=trig_position,line_width=1, line_dash="dashdot", line_color="green")
    fig.add_vline(x=veh_trig_location,line_width=1, line_dash="dash", line_color="purple")
    fig.add_vline(x=veh_end_location,line_width=1, line_dash="dot", line_color="red")
    fig.add_hline(y=da_position,line_width=1, line_dash="dashdot", line_color="blue")
    fig.add_hline(y=d_bike_end,line_width=1, line_dash="dot", line_color="red")
    fig.add_hrect(y0=da_position-0.5, y1=da_position+0.5, line_width=0, fillcolor="green", opacity=0.2)
    fig.add_hrect(y0=da_db_distance-0.5, y1=da_db_distance+0.5, line_width=0, fillcolor="purple", opacity=.3)
    fig.update_layout({'title':{'text': 'Bicycle Position over Vehicle Position', 
                            'x':0.5, 'y':0.95, 
                            'font_size':20, 
                            'font_color':'red'}},
                    legend_title="",        
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
    fig.add_annotation(x=veh_end_location, y=d_bike_end,
                    text="Collision point",
                    showarrow=True,
                    arrowhead=1)                               
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
    my_saved_image = "plot3.jpeg"
    pio.write_image(fig, my_saved_image)                
    st.plotly_chart(fig,use_container_width=True )
st.markdown('---')
#################################################################################################################################
placeholder = st.empty()
with placeholder.container():
    if test_options == 'Test Case 4':
        
        fig = px.line(df, x='Time_trans', y=['Front tire X position trans', 'Vehicle bumper X position trans'], color_discrete_sequence = ['navy', 'darkorange'])
        fig.add_vline(x=da_meas_time-start_time_trans,line_width=1, line_dash="dash", line_color="green")
        # fig.add_vline(x=test_end_time,line_width=1, line_dash="dashdot", line_color="red")
        fig.add_hline(y=-da,line_width=1, line_dash="dash", line_color="green")
        fig.add_hline(y=-db,line_width=1, line_dash="dash", line_color="green")
        fig.add_hrect(y0=-da-0.5, y1=-da+0.5, line_width=0, fillcolor="green", opacity=0.2)
        fig.add_hrect(y0=-db-0.5, y1=-db+0.5, line_width=0, fillcolor="green", opacity=.2)

        fig.add_vline(x=FPI_time-start_time_trans,line_width=1, line_dash="solid", line_color="black")
        fig.add_vline(x=LPI_time-start_time_trans,line_width=1, line_dash="solid", line_color="black")

        fig.update_layout(
            {'title':{'text': 'Vehicle and Bicycle distance over Time', 
                                'x':0.4, 'y':0.95, 
                                'font_size':20, 
                                'font_color':'red'}},
            legend_title="",
            showlegend=True)
        fig.add_annotation(x=t_start-start_time_trans, y=-65,
                    text="Start of Bicycle",
                    showarrow=True,
                    arrowhead=1)
        
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-da,
                    text="da",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-db,
                    text="db",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=FPI_time-start_time_trans, y=0,
                    text="FPI",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=LPI_time-start_time_trans, y=0,
                    text="LPI",
                    showarrow=True,
                    arrowhead=1)            
        # fig.add_annotation(x=test_end_time-veh_entercorridor_time, y=15,
        #             text="Simulated Collision",
        #             showarrow=True,
        #             arrowhead=1)
        fig.update_xaxes(title_text='Time (s)',
                        minor_ticks="outside", 
                        showgrid=True, 
                        gridwidth=1, 
                        gridcolor='lightgrey')

        fig.update_yaxes(title_text='Distance (m)', 
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
        my_saved_image = "plot4.jpeg"
        pio.write_image(fig, my_saved_image)               
        st.plotly_chart(fig, use_container_width=True)
    else:
        
        fig = px.line(df, x='Time_trans', y=['Front tire X position trans', 'Vehicle bumper X position trans'], color_discrete_sequence = ['navy', 'darkorange'])
        fig.add_vline(x=da_meas_time-start_time_trans,line_width=1, line_dash="dash", line_color="green")
        # fig.add_vline(x=test_end_time,line_width=1, line_dash="dashdot", line_color="red")
        fig.add_hline(y=-da,line_width=1, line_dash="dash", line_color="green")
        fig.add_hline(y=-db,line_width=1, line_dash="dash", line_color="green")
        fig.add_hrect(y0=-da-0.5, y1=-da+0.5, line_width=0, fillcolor="green", opacity=0.2)
        fig.add_hrect(y0=-db-0.5, y1=-db+0.5, line_width=0, fillcolor="green", opacity=.2)
        fig.add_shape(type="rect", x0=db_delta_minus_time, y0=-da-0.5, x1=db_delta_plus_time, y1=-da+0.5, line=dict(color="Red", width=2, dash="dash"))
        # fig.add_vline(x=veh_entercorridor_time,line_width=1, line_dash="dash", line_color="red")
        # fig.add_hline(y=0.5+bike_vel,line_width=1, line_dash="dash", line_color="red")
        # fig.add_hline(y=-0.5+bike_vel,line_width=1, line_dash="dash", line_color="red")
        # fig.add_vline(x=FPI_time-veh_entercorridor_time,line_width=1, line_dash="solid", line_color="black")
        fig.add_vline(x=LPI_time-start_time_trans,line_width=1, line_dash="solid", line_color="black")

        fig.update_layout(
            {'title':{'text': 'Vehicle and Bicycle distance over Time', 
                                'x':0.4, 'y':0.95, 
                                'font_size':20, 
                                'font_color':'red'}},
            legend_title="",                    
            showlegend=True)

        # fig.add_annotation(x=da_meas_time-start_time_trans, y=d_db_meas +30,
        #             text="da db Sync time",
        #             showarrow=True,
        #             arrowhead=1)
        fig.add_annotation(x=t_start-start_time_trans, y=-65,
                    text="Start of Bicycle",
                    showarrow=True,
                    arrowhead=1)
        
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-da,
                    text="da",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-db,
                    text="db",
                    showarrow=True,
                    arrowhead=1)

        fig.add_annotation(x=LPI_time-start_time_trans, y=0,
                    text="LPI",
                    showarrow=True,
                    arrowhead=1)            

        fig.update_xaxes(title_text='Time (s)',
                        minor_ticks="outside", 
                        showgrid=True, 
                        gridwidth=1, 
                        gridcolor='lightgrey')

        fig.update_yaxes(title_text='Distance (m)', 
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
        my_saved_image = "plot4.jpeg"
        pio.write_image(fig, my_saved_image)                
        st.plotly_chart(fig, use_container_width=True)
st.markdown('---')
#################################################################################################################################


placeholder = st.empty()
with placeholder.container():        
    if test_options == 'Test Case 4':
        
        fig = px.line(df[db_delta_minus_idx-100:db_delta_plus_idx+100], x='Time_trans', y=['Front tire X position trans', 'Vehicle bumper X position trans'], color_discrete_sequence = ['navy', 'darkorange'])
        fig.add_vline(x=da_meas_time-start_time_trans,line_width=1, line_dash="dash", line_color="green")
        # fig.add_vline(x=test_end_time,line_width=1, line_dash="dashdot", line_color="red")
        fig.add_hline(y=-da,line_width=1, line_dash="dash", line_color="green")
        fig.add_hline(y=-db,line_width=1, line_dash="dash", line_color="green")
        fig.add_hrect(y0=-da-0.5, y1=-da+0.5, line_width=0, fillcolor="green", opacity=0.2)
        fig.add_hrect(y0=-db-0.5, y1=-db+0.5, line_width=0, fillcolor="green", opacity=.2)

        fig.add_vline(x=FPI_time-start_time_trans,line_width=1, line_dash="solid", line_color="black")
        fig.add_vline(x=LPI_time-start_time_trans,line_width=1, line_dash="solid", line_color="black")

        fig.update_layout(
            {'title':{'text': 'Vehicle and Bicycle distance over Time', 
                                'x':0.4, 'y':0.95, 
                                'font_size':20, 
                                'font_color':'red'}},
            legend_title="",
            showlegend=True)
        fig.add_annotation(x=t_start-start_time_trans, y=-65,
                    text="Start of Bicycle",
                    showarrow=True,
                    arrowhead=1)
        
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-da,
                    text="da",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-db,
                    text="db",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=FPI_time-start_time_trans, y=0,
                    text="FPI",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=LPI_time-start_time_trans, y=0,
                    text="LPI",
                    showarrow=True,
                    arrowhead=1)            
        # fig.add_annotation(x=test_end_time-veh_entercorridor_time, y=15,
        #             text="Simulated Collision",
        #             showarrow=True,
        #             arrowhead=1)
        fig.update_xaxes(title_text='Time (s)',
                        minor_ticks="outside", 
                        showgrid=True, 
                        gridwidth=1, 
                        gridcolor='lightgrey')

        fig.update_yaxes(title_text='Distance (m)', 
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
        my_saved_image = "plot6.jpeg"
        pio.write_image(fig, my_saved_image)               
        st.plotly_chart(fig, use_container_width=True)
    else:
        
        fig = px.line(df[db_delta_minus_idx-100:db_delta_plus_idx+100], x='Time_trans', y=['Front tire X position trans', 'Vehicle bumper X position trans'], color_discrete_sequence = ['navy', 'darkorange'])
        fig.add_vline(x=da_meas_time-start_time_trans,line_width=1, line_dash="dash", line_color="green")
        # fig.add_vline(x=test_end_time,line_width=1, line_dash="dashdot", line_color="red")
        fig.add_hline(y=-da,line_width=1, line_dash="dash", line_color="green")
        fig.add_hline(y=-db,line_width=1, line_dash="dash", line_color="green")
        fig.add_hrect(y0=-da-0.5, y1=-da+0.5, line_width=0, fillcolor="green", opacity=0.2)
        fig.add_hrect(y0=-db-0.5, y1=-db+0.5, line_width=0, fillcolor="green", opacity=.2)
        fig.add_shape(type="rect", x0=db_delta_minus_time, y0=-da-0.5, x1=db_delta_plus_time, y1=-da+0.5, line=dict(color="Red", width=2, dash="dash"))
        # fig.add_vline(x=veh_entercorridor_time,line_width=1, line_dash="dash", line_color="red")
        # fig.add_hline(y=0.5+bike_vel,line_width=1, line_dash="dash", line_color="red")
        # fig.add_hline(y=-0.5+bike_vel,line_width=1, line_dash="dash", line_color="red")
        # fig.add_vline(x=FPI_time-veh_entercorridor_time,line_width=1, line_dash="solid", line_color="black")
        fig.add_vline(x=LPI_time-start_time_trans,line_width=1, line_dash="solid", line_color="black")

        fig.update_layout(
            {'title':{'text': 'Vehicle and Bicycle distance over Time', 
                                'x':0.4, 'y':0.95, 
                                'font_size':20, 
                                'font_color':'red'}},
            legend_title="",                    
            showlegend=True)

        # fig.add_annotation(x=da_meas_time-start_time_trans, y=d_db_meas +30,
        #             text="da db Sync time",
        #             showarrow=True,
        #             arrowhead=1)
        fig.add_annotation(x=t_start-start_time_trans, y=-65,
                    text="Start of Bicycle",
                    showarrow=True,
                    arrowhead=1)
        
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-da,
                    text="da",
                    showarrow=True,
                    arrowhead=1)
        fig.add_annotation(x=da_meas_time-start_time_trans, y=-db,
                    text="db",
                    showarrow=True,
                    arrowhead=1)

        fig.add_annotation(x=LPI_time-start_time_trans, y=0,
                    text="LPI",
                    showarrow=True,
                    arrowhead=1)            

        fig.update_xaxes(title_text='Time (s)',
                        minor_ticks="outside", 
                        showgrid=True, 
                        gridwidth=1, 
                        gridcolor='lightgrey')

        fig.update_yaxes(title_text='Distance (m)', 
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
        my_saved_image = "plot6.jpeg"
        pio.write_image(fig, my_saved_image)                
        st.plotly_chart(fig, use_container_width=True)
st.markdown('---')
#################################################################################################################################
# video_file = open('./Test1 _MERGE.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)

# firebird = pd.DataFrame({'test track' : ['Firebird Racetrack', 'Sensata'], 'lat' :[ 43.7674206156433,43.60960308154709] , 'lon' : [-116.469511058211,-116.31195661539411]})
# st.write(firebird)
# st.map(firebird)
# from fpdf import FPDF
