
from distutils.command.upload import upload
import streamlit as st
import pandas as pd
import heapq
from PIL import Image
import math
import time
import openpyxl
import os

st.set_page_config(
     page_title="UN Regulation 151",
     layout="wide",
     initial_sidebar_state="expanded",
     page_icon = ':truck:',
     
 )

###################################################################################################
# Provide easy access to criteria being tested
st.markdown("<h1 style='text-align: center; color: black;'>Reference Point Inputs for Vehicle and Bicycle</h1>", unsafe_allow_html=True)
expander = st.expander("Reference Point Inputs", expanded=False)
with expander:   
    st.markdown("<h1 style='text-align: center; color: black;'>Reference Point Inputs</h1>", unsafe_allow_html=True)
    columns = st.columns((1,6,1,1,6,1))
    with columns[1]:

            image1 = Image.open('Ego vehicle.JPG')
            st.image(image1, caption='Ego vehicle reference pt')
            st.subheader("Vehicle Parameters")


            with st.form(key='vehicleform'):
                vs_m = st.number_input("S (meters)", value = 2.9)
                vo_m = st.number_input("O (meters)", value = 1.0)
                vb_m = st.number_input("B (meters)", value = 2.7)
                vl_m = st.number_input("L (meters)", value = 4.8)
                vw_m = st.number_input("W (meters)", value = 2.1)
                vv_m = st.number_input("V (meters)", value = 0.6)
                vx_m = st.number_input("X (meters)", value = -3.8)
                vy_m = st.number_input("Y (meters)", value = -1.0)
                
                # Important
                submit_button = st.form_submit_button(label='Submit Parameters')

            # Results Can be either form or outside
            if submit_button:
                st.success("Submission of Vehicle Parameters are complete")
                vehicle_elements = st.write(vl_m,vw_m,vs_m,vo_m,vb_m, vv_m,vx_m,vy_m)
    with columns[4]:

        
            image1 = Image.open('Target bicycle.JPG')
            st.image(image1, caption='Target bicycle reference pt')     
            st.subheader("Bicycle Parameters")

            with st.form(key='bicycleform'):
                bs_m = st.number_input("S (meters)", step=1e-3, format="%.3f",value = .273)
                bo_m = st.number_input("O (meters)", step=1e-3, format="%.3f",value = .186)
                bb_m = st.number_input("B (meters)", step=1e-3, format="%.3f",value = .545)
                bl_m = st.number_input("L (meters)", step=1e-3, format="%.3f",value = .917)
                bw_m = st.number_input("W (meters)", step=1e-3, format="%.3f",value = .876)
                bv_m = st.number_input("V (meters)", step=1e-3, format="%.3f",value = 0.0)
                bx_m = st.number_input("X (meters)", step=1e-3, format="%.3f",value = -0.273)
                by_m = st.number_input("Y (meters)", step=1e-3, format="%.3f",value = .250)
                
                # Important
                submit_button = st.form_submit_button(label='Submit Parameters')

            # Results Can be either form or outside
            if submit_button:
                st.success("Submission of Bicycle Parameters are complete")
                bicycle_elements = st.write(bl_m,bw_m,bs_m,bo_m,bb_m, bv_m, bx_m, by_m)

###############################################################################################################################################################
def text_2_csv(uploaded_file):
    df = pd.read_csv(uploaded_file, skiprows =[0,1,2,4], delimiter='\t', encoding='unicode_escape',low_memory=False)
    df_ABD= pd.DataFrame(df)
    return df_ABD


################################################################################################################################################
st.markdown("<h1 style='text-align: center; color: red;'>Please Load Data for Analysis</h1>", unsafe_allow_html=True)    
uploaded_file = st.file_uploader("Choose AB Dynamics Test file", type=(["txt"]))
if uploaded_file is not None:
    if os.path.splitext(uploaded_file.name)[1] == '.txt':
        df_ABD = text_2_csv(uploaded_file)
        st.session_state['df'] = df_ABD
        st.session_state['Test File'] = uploaded_file
        df = st.session_state['df']
        testfile = st.session_state['Test File']
        
        filename = f"""<p style="font-family:sans-serif; color:Blue; font-size: 28px;">Test file: {testfile.name}</p>"""
        st.session_state['filename_txt'] = testfile.name
        st.markdown(filename, unsafe_allow_html=True)
        
        if ("00030066" in uploaded_file.name):
            test_options = 'Test Case 1'
            row_index = 0
        elif ("00030077" in uploaded_file.name):
            test_options = 'Test Case 2'
            row_index = 1
        elif ("00030071" in uploaded_file.name):
            test_options = 'Test Case 3'
            row_index = 2
        elif ("00030072" in uploaded_file.name):
            test_options = 'Test Case 4'
            row_index = 3
        elif ("00030076" in uploaded_file.name):
            test_options = 'Test Case 5'
            row_index = 4
        elif ("00030078" in uploaded_file.name):
            test_options = 'Test Case 6'
            row_index = 5
        elif ("00030079" in uploaded_file.name):
            test_options = 'Test Case 7'
            row_index = 6
        else:
            st.write("Unknown test file")
        st.session_state['test_options'] = test_options    
        testcase= f"""<p style="font-family:sans-serif; color:Blue; font-size: 28px;">{test_options}</p>"""
        st.markdown(testcase, unsafe_allow_html=True)    
################################################################################################################################################

if uploaded_file:

    # import test criteria maxtrix
    xlsxfile = 'Dynamic_Test_Cases.xlsx'
    df_test_crit = pd.read_excel(xlsxfile)

    
    bike_vel = df_test_crit.iloc[row_index, 1]
    veh_vel = df_test_crit.iloc[row_index, 2]
    d_lat = df_test_crit.iloc[row_index, 3]
    da = df_test_crit.iloc[row_index, 4]
    db = df_test_crit.iloc[row_index, 5]
    dc = df_test_crit.iloc[row_index, 6]
    dd = df_test_crit.iloc[row_index, 7]    
    length = df_test_crit.iloc[row_index, 10]
    radius = df_test_crit.iloc[row_index, 11]
    da_pos = df_test_crit.iloc[row_index, 12]    
    db_pos = df_test_crit.iloc[row_index, 13]
    trig_pos = df_test_crit.iloc[row_index, 14]

    st.session_state['bike_vel'] = bike_vel
    st.session_state['veh_vel'] = veh_vel
    st.session_state['d_lat'] = d_lat
    st.session_state['da'] = da
    st.session_state['db'] = db
    st.session_state['dc'] = dc
    st.session_state['dd'] = dd
    st.session_state['length'] = length
    st.session_state['radius'] = radius 
    st.session_state['da_pos'] = da_pos
    st.session_state['db_pos'] = db_pos
    st.session_state['trig_pos'] = trig_pos
    #set bike lateral limits
    # b_lim= -d_lat
    st.session_state['b_lim'] = -d_lat

    #########################################################################################################

    # ABD is in meters
    conv2kmph=3.6
    df['Vehicle forward velocity'] = conv2kmph* df['Forward velocity']
    df['Bike forward velocity']=conv2kmph* df['Object 1 forward velocity (ref point)']

    # correct for adjustment done at the track for wider lateral distances
    if d_lat == 4.25:
        df["Vehicle Lateral position"]= df["Y position"]- 1
        df["Bike Lateral position"]= df["Head tracker reference Y position"]
    # elif d_lat == 4.25:
    #     df["Vehicle Lateral position"]= df["Y position"]-0.5
    else:
        df["Vehicle Lateral position"]= df["Y position"]
        df["Bike Lateral position"]= df["Head tracker reference Y position"]+1

    #Reference the front tire of the bike -->front overhang + Object 1 actual X (front axle)
    df['Front tire X position']= bo_m + df['Object 1 actual X (front axle)']
    # Reference the front bumper of the vehicle -->front overhang + Subject reference X position
    df['Vehicle bumper X position']= vo_m + df['Actual X (front axle)']

    ################################################################################################################################################
    # find where does the bike starts
    
    def find_trigger_event(df, bike_vel, threshold=0.2):
        lower_lim = (bike_vel - 0.5) / 3.6

        # Find the time index when the bike velocity passes through the lower limit for the first time
        df_lower_lim = df[df['Bike forward velocity'] >= lower_lim]
        test_start_idx = df_lower_lim.index[0]
        test_early_start_idx_ = test_start_idx - 400

        # Subtract 8 seconds from the time index
        bike_start_vel = df.loc[test_early_start_idx_:test_start_idx, 'Bike forward velocity']

        # Check if the bike velocity is above the threshold for any point in the time range
        if (bike_start_vel > threshold).any():
           
            # Find the first index greater than the threshold and closest to the test_start_idx
            threshold_idxs = df[(df['Bike forward velocity'] >= threshold) & (df.index >= test_early_start_idx_)].index
            trig_start_idx = threshold_idxs.min()-1

            # Use the time index of the closest index to find the start time of the trigger event
            t_start = df.at[trig_start_idx, 'Time']

            # Return the start time of the trigger event
            return trig_start_idx, t_start
        else:
            # If the bike velocity is never above the threshold, return None
            st.write('Could not find Bike Velocity Threshold in time range')
            return None

    trig_start_idx, t_start = find_trigger_event(df, bike_vel, threshold=0.2)  

    st.session_state['trig_start_idx'] = trig_start_idx
    st.session_state['t_start'] = t_start

    ##########################################################################################################################################
    # The below code finds the first time index when the bike velocity settles
    def find_start_time(df, bike_vel):
        # A good estimate for the bikes velocity
        #a time index is every 10ms - wait 5s then take the mean for 8s
        # b_mean=round(df['Bike forward velocity'][trig_start_idx+500:trig_start_idx+1300].mean(), 2)
        # allow for 1 bounce through the limits
        lower_lim = bike_vel - 0.5
        # the time index when the bike velocity passes through the lower limit for the first time
        test_start_idx = df.loc[(df['Bike forward velocity'] >= lower_lim), ['Time'] ].index[0]
        test_start_limit_idx = df.loc[(df['Bike forward velocity'] >= lower_lim), ['Time'] ].index[0]
        # create a 1 second data frame to search
        df_bounce=df[test_start_idx: test_start_idx+150] 
        all_indexes = []
        for index in range(len(df_bounce)):
            if round(df_bounce["Bike forward velocity"].iloc[index],2 ) <= lower_lim:
                all_indexes.append(index)
            else:
                #if no bounce then add 0
                all_indexes.append(0)

        # add 1 index to get it over the limit
        add_bounce = 1+max(all_indexes)
        test_start_idx = test_start_idx + add_bounce
        test_start = df['Time'].iloc[test_start_idx]
        test_start_limit = df['Time'].iloc[test_start_limit_idx]
        return test_start_idx, test_start, test_start_limit_idx,test_start_limit

    test_start_idx, test_start, test_start_limit_idx,test_start_limit = find_start_time(df, bike_vel)

    st.session_state['test_start_idx'] = test_start_idx
    st.session_state['test_start'] = test_start
    st.session_state['test_start_limit_idx'] = test_start_limit_idx
    st.session_state['test_start_limit'] = test_start_limit
    # st.write('t start : ',test_start)

#####################################################################################
# the end of the test is 65m after the bike has been triggered
# da is defined as =  8 seconds * Velocity of bike
    def find_end_time(df, trig_start_idx):
        d_bike_start = df.loc[trig_start_idx, "Front tire X position"]
        d_bike_end = d_bike_start + 65
        Max_bike_pos = df['Front tire X position'].max()
        d_short = round((d_bike_end -Max_bike_pos) + 2 , 1) # add 2m for a little wigle room
        if d_bike_end < Max_bike_pos:
            test_end_time_idx = df.loc[(df['Front tire X position'] >= d_bike_end), ['Time'] ].index[0]
            test_end_time = df.loc[test_end_time_idx,'Time']
        else: 
            fail_crit = f"""<p style="font-family:sans-serif; color:Red; font-size: 28px;">The bicycle did not reach the 65m mark. Try extending the bike path {d_short}m </p>"""
            st.markdown(fail_crit, unsafe_allow_html=True)
        return test_end_time_idx, test_end_time,d_bike_end
    # st.write(df['Front tire X position'])
    test_end_time_idx, test_end_time, d_bike_end = find_end_time(df, trig_start_idx)
    
    st.session_state['test_end_time'] = test_end_time
    st.session_state['test_end_time_idx'] = test_end_time_idx
    st.session_state['d_bike_end'] = d_bike_end
    
#####################################################################################  
    def db_correction(d_lat, radius, length):
        # find the added distance the vehicle will travel based on R, Y, and L
        Y = d_lat + 0.25
        R = radius
        db3 =R*math.acos((R-Y)/R) - math.sqrt(R*R - (R-Y)*(R-Y))
        db_adj = length + db3
        return db_adj
    db_adj = db_correction(d_lat,radius, length)
    
    st.session_state['db_adj'] = db_adj
    # st.write('db_adj', db_adj)


    #create df column with db adjustment due to R,Y, and L
    df['Vehicle bumper X position w turn correction'] = df['Vehicle bumper X position'] - db_adj
    # create df column with relative absolute distance between bike and vehicle
    df['ABS Separation w db adjust'] = abs(df['Vehicle bumper X position w turn correction'] - df['Front tire X position'])
    df['Separation w db adjust']= df['Vehicle bumper X position w turn correction'] - df['Front tire X position']
    df['Separation X (veh bumper - bike front tire)']= df['Vehicle bumper X position'] - df['Front tire X position']

    
#####################################################################################    
# determine the transformation for a time vs distance plot as described in the documentation
    def time_transform(df, trig_start_idx, test_end_time_idx, test_options, db):
        if test_options == 'Test Case 4':
            # location of bike at trigger point
            bike_trig_location = df.loc[trig_start_idx,'Front tire X position']
            #location of vehicle 15m before bike location
            veh_entercorridor_time_idx = df.loc[(df['Vehicle bumper X position'] >= bike_trig_location-15), ['Time'] ].index[0]
            veh_entercorridor_location = df.loc[veh_entercorridor_time_idx,'Vehicle bumper X position']
            veh_trig_location = df.loc[trig_start_idx,'Vehicle bumper X position']
            #find time index of the start of the corridor
            veh_entercorridor_time = df['Time'].iloc[veh_entercorridor_time_idx]
            veh_end_location = df.loc[test_end_time_idx,'Vehicle bumper X position']
            # translate vehicle dataframe
            df['Vehicle bumper X position trans'] = df.iloc[trig_start_idx:test_end_time_idx][['Vehicle bumper X position']].reset_index(drop=True)- (bike_trig_location+65)
            db_delta_plus = df.loc[(df['Vehicle bumper X position trans'] >= -db + 0.5), 'Time' ].index[0]
            db_delta_plus_time = df['Time'].iloc[db_delta_plus]
            # print('db_delta_plus_time', db_delta_plus_time)
            db_delta_minus = df.loc[(df['Vehicle bumper X position trans'] >= -db - 0.5), 'Time'].index[0]
            db_delta_minus_time = df['Time'].iloc[db_delta_minus]
            #translate bike dataframe
            df['Front tire X position trans'] = (df.iloc[trig_start_idx:test_end_time_idx][['Front tire X position']].reset_index(drop=True))- (bike_trig_location+65)
            #translate time dataframe
            start_time_trans = df.loc[trig_start_idx, 'Time']
            df['Time_trans'] = (df.iloc[trig_start_idx:test_end_time_idx][['Time']].reset_index(drop=True))-start_time_trans
            # sync_time_trans = da_meas_time-start_time_trans
        else: 
            # location of bike at trigger point
            bike_trig_location = df.loc[trig_start_idx,'Front tire X position']
            bike_trig_time = df.loc[trig_start_idx,'Time']
            #location of vehicle 15m before bike location
            veh_entercorridor_time_idx = df.loc[(df['Vehicle bumper X position'] >= bike_trig_location-15), ['Time'] ].index[0]
            veh_entercorridor_location = df.loc[veh_entercorridor_time_idx,'Vehicle bumper X position']
            veh_trig_location = df.loc[trig_start_idx,'Vehicle bumper X position']
            #find time index of the start of the corridor
            veh_entercorridor_time = df['Time'].iloc[veh_entercorridor_time_idx]
            veh_end_location = df.loc[test_end_time_idx,'Vehicle bumper X position']
            # translate vehicle dataframe
            df['Vehicle bumper X position trans'] = df.iloc[veh_entercorridor_time_idx:test_end_time_idx][['Vehicle bumper X position']].reset_index(drop=True)- (bike_trig_location+65)
            db_delta_plus_idx = df.loc[(df['Vehicle bumper X position trans'] >= -db + 0.5), 'Time' ].index[0]
            db_delta_plus_time = df['Time'].iloc[db_delta_plus_idx]
            # print('db_delta_plus_time', db_delta_plus_time)
            db_delta_minus_idx = df.loc[(df['Vehicle bumper X position trans'] >= -db - 0.5), 'Time'].index[0]
            db_delta_minus_time = df['Time'].iloc[db_delta_minus_idx]
            #translate bike dataframe
            df['Front tire X position trans'] = (df.iloc[veh_entercorridor_time_idx:test_end_time_idx][['Front tire X position']].reset_index(drop=True))- (bike_trig_location+65)
            #translate time dataframe
            start_time_trans = df.loc[veh_entercorridor_time_idx, 'Time']
            df['Time_trans'] = (df.iloc[veh_entercorridor_time_idx:test_end_time_idx][['Time']].reset_index(drop=True))-start_time_trans
            # sync_time_trans = da_meas_time-start_time_trans   
        return veh_trig_location, veh_entercorridor_time_idx, veh_entercorridor_location, veh_entercorridor_time, veh_end_location, start_time_trans, bike_trig_location,db_delta_plus_time,db_delta_minus_time,db_delta_plus_idx,db_delta_minus_idx
        
    veh_trig_location, veh_entercorridor_time_idx, veh_entercorridor_location, veh_entercorridor_time, veh_end_location, start_time_trans, bike_trig_location,db_delta_plus_time,db_delta_minus_time,db_delta_plus_idx,db_delta_minus_idx = time_transform(df, trig_start_idx, test_end_time_idx, test_options,db)
    st.session_state['veh_entercorridor_location'] = veh_entercorridor_location
    st.session_state['veh_entercorridor_time'] = veh_entercorridor_time
    st.session_state['veh_entercorridor_time_idx'] = veh_entercorridor_time_idx
    st.session_state['start_time_trans'] = start_time_trans
    st.session_state['bike_trig_location'] = bike_trig_location
    st.session_state['veh_trig_location'] = veh_trig_location
    st.session_state['veh_end_location'] = veh_end_location
    st.session_state['db_delta_plus_time'] = db_delta_plus_time
    st.session_state['db_delta_minus_time'] = db_delta_minus_time
    st.session_state['db_delta_plus_idx'] = db_delta_plus_idx
    st.session_state['db_delta_minus_idx'] = db_delta_minus_idx
    #####################################################################################
    #shift bike back to origin - some tests do not start at the origin

    #find the x position of the bike
    start_pos_bike = df['Front tire X position'][trig_start_idx-20:trig_start_idx].mean()
    df['Front tire X position shift2origin'] = df['Front tire X position']-start_pos_bike
    df['Separation X shift2origin (veh bumper - bike front tire)'] = df['Separation X (veh bumper - bike front tire)']-start_pos_bike
    # trigger_idx = df.loc[(df['Separation X shift2origin (veh bumper - bike front tire)'] >= d_veh_entercorridor), ['Time'] ].index[0]
    da_position = da_pos + start_pos_bike
    db_position = db_pos + start_pos_bike
    trig_position = trig_pos + start_pos_bike
    st.session_state['da_position'] = da_position
    st.session_state['db_position'] = db_position
    st.session_state['trig_position'] = trig_position
    

######################## Criteria 1, 2 ##########################################
    def criteria_1(df, veh_entercorridor_time_idx, test_end_time_idx):
        #find vehicle lateral distances during the test corridor
        if df['Vehicle Lateral position'][veh_entercorridor_time_idx:test_end_time_idx].max()< 0.1 and df['Vehicle Lateral position'][veh_entercorridor_time_idx:test_end_time_idx].min()> -0.1 :
            crit_1 = True
        else:
            crit_1 = False

        veh_lat_mean = df['Vehicle Lateral position'][veh_entercorridor_time_idx:test_end_time_idx].mean()
        veh_lat_std = df['Vehicle Lateral position'][veh_entercorridor_time_idx:test_end_time_idx].std()
        return veh_lat_mean, veh_lat_std, crit_1
    veh_lat_mean, veh_lat_std, crit_1 = criteria_1(df, veh_entercorridor_time_idx, test_end_time_idx)    
    st.session_state['veh_lat_mean'] = veh_lat_mean
    st.session_state['veh_lat_std'] = veh_lat_std
    st.session_state['crit_1'] = crit_1
    
    def criteria_2(df, test_start_idx, test_end_time_idx,d_lat):
        #find bike lateral distances during the test corridor
        b_lim = -d_lat
        if df['Bike Lateral position'][test_start_idx:test_end_time_idx].max()< 0.2+b_lim and df['Bike Lateral position'][test_start_idx:test_end_time_idx].min()>-0.2+b_lim:
            crit_2 = True
        else:
            crit_2 = False

        bike_lat_mean = df['Bike Lateral position'][test_start_idx:test_end_time_idx].mean()
        bike_lat_std = df['Bike Lateral position'][test_start_idx:test_end_time_idx].std()
        return bike_lat_mean, bike_lat_std, crit_2
    bike_lat_mean, bike_lat_std, crit_2= criteria_2(df, test_start_idx, test_end_time_idx, d_lat)    
    st.session_state['bike_lat_mean'] = bike_lat_mean
    st.session_state['bike_lat_std'] = bike_lat_std
    st.session_state['crit_2'] = crit_2

######################## Criteria 3, 4, 6, 7  ##########################################
    def criteria_3(df,veh_entercorridor_time_idx , trig_start_idx):
        # find the vehicle velocity in the corridor before the test starts
        if trig_start_idx >veh_entercorridor_time_idx:
            veh_vel_corr_mean = df['Vehicle forward velocity'][veh_entercorridor_time_idx:trig_start_idx].mean()
            veh_vel_corr_std = df['Vehicle forward velocity'][veh_entercorridor_time_idx:trig_start_idx].std()
            if df['Vehicle forward velocity'][veh_entercorridor_time_idx:trig_start_idx].max()< veh_vel_corr_mean +2 and df['Vehicle forward velocity'][veh_entercorridor_time_idx:trig_start_idx].min()> veh_vel_corr_mean -2 :
                crit_3 = True
            else:
                crit_3 = False
        else:
            veh_vel_corr_mean = df['Vehicle forward velocity'][trig_start_idx:veh_entercorridor_time_idx].mean()
            veh_vel_corr_std = df['Vehicle forward velocity'][trig_start_idx:veh_entercorridor_time_idx].std()
            if df['Vehicle forward velocity'][trig_start_idx:veh_entercorridor_time_idx].max()< veh_vel_corr_mean +2 and df['Vehicle forward velocity'][trig_start_idx:veh_entercorridor_time_idx].min()> veh_vel_corr_mean -2 :
                crit_3 = True
            else:
                crit_3 = False

        return veh_vel_corr_mean, veh_vel_corr_std, crit_3
    veh_vel_corr_mean, veh_vel_corr_std, crit_3 = criteria_3(df, veh_entercorridor_time_idx, trig_start_idx)
    st.session_state['veh_vel_corr_mean'] = veh_vel_corr_mean
    st.session_state['veh_vel_corr_std'] = veh_vel_corr_std
    st.session_state['crit_3'] = crit_3

    def criteria_4(df, trig_start_idx):
        #find the bike velocity in the corridor before the test starts
        bike_vel_corr_max = df['Bike forward velocity'][trig_start_idx-20:trig_start_idx-10].max()
        if bike_vel_corr_max < 0.25:
            crit_4 = True
        else:
            crit_4 = False
        return bike_vel_corr_max, crit_4
    bike_vel_corr_max, crit_4 = criteria_4(df, trig_start_idx)
    st.session_state['bike_vel_corr_max'] = bike_vel_corr_max
    st.session_state['crit_4'] = crit_4
    
    def criteria_6(df, test_start_idx, test_end_time_idx,veh_vel):
        #find the mean vehicle velocity between the start and end of test
        veh_vel_mean = df['Vehicle forward velocity'][test_start_idx:test_end_time_idx].mean()
        veh_vel_std = df['Vehicle forward velocity'][test_start_idx:test_end_time_idx].std()
        if df['Vehicle forward velocity'][test_start_idx:test_end_time_idx].max()< veh_vel +2 and df['Vehicle forward velocity'][test_start_idx:test_end_time_idx].min()> veh_vel -2 :
            crit_6 = True
        else:
            crit_6 = False
        return veh_vel_mean, veh_vel_std, crit_6
    veh_vel_mean, veh_vel_std, crit_6 = criteria_6(df, test_start_idx, test_end_time_idx,veh_vel)
    st.session_state['veh_vel_mean'] = veh_vel_mean
    st.session_state['veh_vel_std'] = veh_vel_std
    st.session_state['crit_6'] = crit_6

    def criteria_7(df, test_start_idx, test_end_time_idx, bike_vel):
        # find the bicycle mean velocity between the start and end of test 
        bike_vel_mean = df['Bike forward velocity'][test_start_idx:test_end_time_idx].mean()
        bike_vel_std = df['Bike forward velocity'][test_start_idx:test_end_time_idx].std()
        if df['Bike forward velocity'][test_start_idx:test_end_time_idx].max()< bike_vel+0.5 and df['Bike forward velocity'][test_start_idx:test_end_time_idx].min()>bike_vel-0.5 :
            crit_7 = True
        else:
            crit_7 = False
        return bike_vel_mean, bike_vel_std, crit_7

    bike_vel_mean, bike_vel_std, crit_7 = criteria_7(df, test_start_idx, test_end_time_idx, bike_vel)

    st.session_state['bike_vel_mean'] = bike_vel_mean
    st.session_state['bike_vel_std'] = bike_vel_std
    st.session_state['crit_7'] = crit_7
    
######################## Criteria 5  ##########################################
    
    def criteria_5(df, trig_start_idx, test_start_idx):

        #find the time to accelerate to within 0.5 kph of final bike velocity
        
        #Reference the front tire of the bike -->front overhang + Object 1 actual X (front axle)
        d_bike_acc_start = df.loc[trig_start_idx,'Front tire X position']
        d_bike_start = df.loc[test_start_idx,'Front tire X position']
        #what distance did it take to accelerate to start of test
        d_bike_acc = d_bike_start - d_bike_acc_start
        # what is the position of the bike at the end of the test
        # bike_d_end = df.loc[test_end_time_idx,'Front tire X position']
        if d_bike_acc < 5.66 + 1 and d_bike_acc > 5.66 - 1:
            crit_5 = True
        else:
            crit_5 = False
        return d_bike_acc, d_bike_start,crit_5
    d_bike_acc, d_bike_start,  crit_5 = criteria_5(df, trig_start_idx, test_start_limit_idx)
    st.session_state['d_bike_acc'] = d_bike_acc
    st.session_state['d_bike_start'] = d_bike_start
    st.session_state['crit_5'] = crit_5

######################## Criteria 8  ##########################################
 
# find dynamic da and db based on average speed of bike and vehicle
    
    def da_measurement(df, d_bike_end, vel_mean_bike):
        #definition of da
        da_meas = 8 * vel_mean_bike/3.6
        #location of da = collision point - da_meas = 65 - da 
        d_da_meas = d_bike_end - da_meas
        da_meas_time_idx = df.loc[(df['Front tire X position'] >= d_da_meas), ['Time'] ].index[0]
        da_meas_time = df.loc[da_meas_time_idx,'Time'] 
        return d_da_meas, da_meas_time,da_meas_time_idx
    
    d_da_meas, da_meas_time, da_meas_time_idx = da_measurement(df, d_bike_end, bike_vel_mean)
    st.session_state['d_da_meas'] = d_da_meas
    st.session_state['da_meas_time'] = da_meas_time
    
    d_da_endmeas = df.loc[test_end_time_idx, 'Front tire X position']
  
    def db_measurement(df, da_meas_time_idx):
        d_db_meas = df.loc[da_meas_time_idx,'Vehicle bumper X position']
        d_db_meas_dbadj = df.loc[da_meas_time_idx,'Vehicle bumper X position w turn correction']
        return d_db_meas, d_db_meas_dbadj
        
    
    d_db_meas, d_db_meas_dbadj = db_measurement(df, da_meas_time_idx)
    st.session_state['d_db_meas'] = d_db_meas
    st.session_state['d_db_meas_dbadj'] = d_db_meas_dbadj
    da_db = df.loc[da_meas_time_idx,'Separation w db adjust']
  

#####################################################################################
    
    def criteria_8(da, d_da_meas, db, d_db_meas ):
        abs_meas = abs(d_da_meas - d_db_meas)
        abs_calc = abs(da - db)
        if abs_meas <= abs_calc + 0.5 and abs_meas >= abs_calc - 0.5:
            crit_8 = True
        else:
            crit_8 = False
        return crit_8, abs_meas, abs_calc
    
    crit_8,abs_meas, abs_calc = criteria_8(da, d_da_meas, db, d_db_meas)
    st.session_state['crit_8'] = crit_8

################################################################################
    Veh_collision_pt = df.loc[test_end_time_idx,'Vehicle bumper X position']
    Bike_collision_pt = df.loc[test_end_time_idx,'Front tire X position']
    
    # Find LPI and FPI
    def LPI_calc(df, dc, test_end_time_idx):
        LPI = df.loc[test_end_time_idx,'Vehicle bumper X position'] - dc   
        LPI_time_idx = df.loc[(df['Vehicle bumper X position'] >= LPI), ['Time'] ].index[0]
        LPI_time = df.loc[LPI_time_idx, 'Time']
        LPI_Frame = df.loc[LPI_time_idx, 'FrameID']
        return LPI, LPI_time_idx, LPI_time, LPI_Frame
    LPI, LPI_time_idx, LPI_time, LPI_Frame = LPI_calc(df, dc, test_end_time_idx)

    def FPI_calc(df, dd, test_end_time_idx):
        FPI = df.loc[test_end_time_idx,'Vehicle bumper X position'] - dd 
        FPI_time_idx = df.loc[(df['Vehicle bumper X position'] >= FPI), ['Time'] ].index[0]
        FPI_time = df.loc[FPI_time_idx, 'Time']
        FPI_Frame = df.loc[FPI_time_idx, 'FrameID']
        return FPI, FPI_time_idx, FPI_time, FPI_Frame
    FPI, FPI_time_idx, FPI_time, FPI_Frame = FPI_calc(df, dd, test_end_time_idx)

    st.session_state['Veh_collision_pt'] = Veh_collision_pt
    st.session_state['LPI'] = LPI
    st.session_state['LPI_time_idx'] = LPI_time_idx
    st.session_state['LPI_time'] = LPI_time
    st.session_state['LPI_Frame'] = LPI_Frame
    st.session_state['FPI'] = FPI
    st.session_state['FPI_time_idx'] = FPI_time_idx
    st.session_state['FPI_time'] = FPI_time
    st.session_state['FPI_Frame'] = FPI_Frame

    ################################################################################################################################################       
   
    # find the relative da and db sync point in the data
    # find the determined synd pt in meters from the front tire of the bike and bumper of vehicle
    da_db_distance = (da-db)
    st.session_state['da_db_distance'] = da_db_distance
    # st.write('Distance = da - db', round(da_db_distance,2))
    
    ################################################################################################################################################ 