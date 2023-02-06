
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
# define a function to convert text file to a panda and csv file
def text_2_csv(uploaded_file, test_options):
    df = pd.read_csv(uploaded_file, skiprows =[0,1,2,4], delimiter='\t', encoding='unicode_escape',low_memory=False)
    timestr = time.strftime("%Y%m%d")
    df_ABD= pd.DataFrame(df)
    csvfile = str(test_options)+' '+timestr+'.csv'
    # save txt file to csv
    df_ABD.to_csv(csvfile, index = False)
    # st.session_state['df'] = df_ABD
    return df_ABD
#####################################################################################################################
st.title('Load AB Dynamics Data for Analysis')

columns = st.columns((4,1,4))
with columns[0]:

    test_options= st.radio('Choose Test Case For Analysis', options= ['Test Case 1',
                                                                        'Test Case 2',
                                                                        'Test Case 3',
                                                                        'Test Case 4',
                                                                        'Test Case 5',
                                                                        'Test Case 6',
                                                                        'Test Case 7']) 
    st.session_state['test_options'] = test_options    

#########################################################################################################


with columns[2]:
    test_case_prompts = {
    'Test Case 1': 'Upload AB Dynamics Test Case 1 File to analyze',
    'Test Case 2': 'Upload AB Dynamics Test Case 2 File to analyze',
    'Test Case 3': 'Upload AB Dynamics Test Case 3 File to analyze',
    'Test Case 4': 'Upload AB Dynamics Test Case 4 File to analyze',
    'Test Case 5': 'Upload AB Dynamics Test Case 5 File to analyze',
    'Test Case 6': 'Upload AB Dynamics Test Case 6 File to analyze',
    'Test Case 7': 'Upload AB Dynamics Test Case 7 File to analyze'}

    uploaded_file = st.file_uploader(test_case_prompts[test_options], type=(["txt", "csv"]))
    if uploaded_file is not None:
         if os.path.splitext(uploaded_file.name)[1] == '.csv':
             df = pd.read_csv(uploaded_file, low_memory=False)
             st.session_state['df'] = df
             st.session_state['Test File'] = uploaded_file
             df = st.session_state['df']
             testfile = st.session_state['Test File']
             st.write('Test file:' , testfile.name)

         elif os.path.splitext(uploaded_file.name)[1] == '.txt':
             df_ABD = text_2_csv(uploaded_file, test_options)
             st.session_state['df'] = df_ABD
             st.session_state['Test File'] = uploaded_file
             df = st.session_state['df']
             testfile = st.session_state['Test File']
             st.write('Test file:' , testfile.name)
    else:
        st.markdown("<h1 style='text-align: center; color: red;'>Please Load Data for Analysis</h1>", unsafe_allow_html=True)         
    # df = st.session_state['df']
    # testfile = st.session_state['Test File']
    # st.write('Test file:' , testfile.name)

################################################################################################################################################

if uploaded_file:

    # import test criteria maxtrix
    xlsxfile = 'Dynamic_Test_Cases.xlsx'
    df_test_crit = pd.read_excel(xlsxfile)

    test_case_indices = {'Test Case 1': 0, 'Test Case 2': 1, 'Test Case 3': 2, 'Test Case 4': 3, 'Test Case 5': 4, 'Test Case 6': 5, 'Test Case 7': 6}
    row_index = test_case_indices[test_options]
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
    df['Bike forward velocity']=conv2kmph* df['Head tracker forward velocity']

    # correct for adjustment done at the track for wider lateral distances
    if d_lat == 4.25 and test_options == 'Test Case 4':
        df["Vehicle Lateral position"]= df["Y position"]- 1
    elif d_lat == 4.25:
        df["Vehicle Lateral position"]= df["Y position"]-0.5
    else:
        df["Vehicle Lateral position"]= df["Y position"]

    df["Bike Relative Lateral position"]= df["Object 1 relative lateral distance"]
    #Reference the front tire of the bike -->front overhang + Object 1 actual X (front axle)
    df['Front tire X position']= bo_m + df['Object 1 actual X (front axle)']
    # Reference the front bumper of the vehicle -->front overhang + Subject reference X position
    df['Vehicle bumper X position']= vo_m + df['Actual X (front axle)']

    ################################################################################################################################################
    # find where does the bike starts
    #define bike start thresholds
    accel_thres = .5
    # accel_thres1 = 1.5
    vel_thres = 1.5 # can drop threshold to 1.5
    #find when the bike starts
    values = df['Object 1 forward acceleration']
    #find the first 10 (n) peaks in acceleration and check if it is a valid start
    n = 10
    pairs = heapq.nlargest(n, zip(values, range(len(values))))
    indices = [i for value, i in pairs]
    start_indices=[]
    for x in indices:
        #what is the mean acceleration for t= 150 *.01 = 1.5s
        mean_acc = df['Object 1 forward acceleration'][x:x+150].mean()
        #what is the mean velocity after 5 seconds for 1 seconds
        mean_vel = df['Object 1 forward velocity (ref point)'][x+500:x+600].mean()
        vel_std = df['Object 1 forward velocity (ref point)'][x+500:x+600].std()
        if mean_acc >= accel_thres and mean_vel >= vel_thres:
            start_indices.append(x)
        

    if start_indices:
        t_start_idx = min(start_indices)
    else:
        t_start_idx = 0
            
    st.session_state['t_start_idx'] = t_start_idx
    t_start = df['Time'].iloc[t_start_idx]
    # st.write('t start : ',t_start)
    st.session_state['t_start'] = t_start

    ##########################################################################################################################################
    # The below code finds the first time index when the bike velocity settles

    # A good estimate for the bikes velocity
    #a time index is every 10ms - wait 5s then take the mean for 8s
    b_mean=round(df['Bike forward velocity'][t_start_idx+500:t_start_idx+1300].mean(), 2)
    # st.write('b_mean : ',b_mean)

    # allow for 1 bounce through the limits
    lower_lim = b_mean - 0.5
    # the time index when the bike velocity passes through the lower limit for the first time
    test_start_idx = df.loc[(df['Bike forward velocity'] >= lower_lim), ['Time'] ].index[0]
    
    # st.write(test_start_idx)
    # create a 1 second data frame to search
    df_bounce=df[test_start_idx: test_start_idx+100] 
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
    st.session_state['test_start_idx'] = test_start_idx
    test_start = df['Time'].iloc[test_start_idx]
    st.session_state['test_start'] = test_start

#####################################################################################
# collision time is 8 seconds after the start of the test
    test_end = test_start + 8
    st.session_state['test_end'] = test_end
    test_end_idx = df.loc[(df['Time'] >= test_end), ['Time'] ].index[0]
    st.session_state['test_end_idx'] = test_end_idx

#####################################################################################    
    #vehicle position at the start of the corridor, start of test, and end of test
    veh_d_corridor = df.loc[t_start_idx,'Vehicle bumper X position']-15 # the corridor starts 15m before the start of the bike
    #find index of the start of the corridor
    veh_corridor_idx = df.loc[(df['Vehicle bumper X position'] >= veh_d_corridor), ['Time'] ].index[0]
    veh_t_corridor = df['Time'].iloc[veh_corridor_idx]
    veh_d_start = df.loc[test_start_idx,'Vehicle bumper X position'] 
    veh_d_end = df.loc[test_end_idx,'Vehicle bumper X position']
    x_start = df['Vehicle bumper X position'].iloc[test_start_idx]
    st.session_state['veh_t_corridor'] = veh_t_corridor
    st.session_state['veh_d_corridor'] = veh_d_corridor
    st.session_state['veh_d_start'] = veh_d_start
    st.session_state['veh_d_end'] = veh_d_end
    st.session_state['x_start'] = x_start

######################## Criteria 1, 2 ##########################################
    def criteria_1(df, veh_corridor_idx, test_end_idx):
        #find vehicle lateral distances during the test corridor
        if df['Vehicle Lateral position'][veh_corridor_idx:test_end_idx].max()< 0.1 and df['Vehicle Lateral position'][veh_corridor_idx:test_end_idx].min()> -0.1 :
            crit_1 = True
        else:
            crit_1 = False

        veh_lat_mean = df['Vehicle Lateral position'][veh_corridor_idx:test_end_idx].mean()
        veh_lat_std = df['Vehicle Lateral position'][veh_corridor_idx:test_end_idx].std()
        return veh_lat_mean, veh_lat_std, crit_1
    veh_lat_mean, veh_lat_std, crit_1 = criteria_1(df, veh_corridor_idx, test_end_idx)    
    st.session_state['veh_lat_mean'] = veh_lat_mean
    st.session_state['veh_lat_std'] = veh_lat_std
    st.session_state['crit_1'] = crit_1
    
    def criteria_2(df, test_start_idx, test_end_idx,d_lat):
        #find bike lateral distances during the test corridor
        b_lim = -d_lat
        if df['Bike Relative Lateral position'][test_start_idx:test_end_idx].max()< 0.2+b_lim and df['Bike Relative Lateral position'][test_start_idx:test_end_idx].min()>-0.2+b_lim:
            crit_2 = True
        else:
            crit_2 = False

        bike_lat_mean = df['Bike Relative Lateral position'][test_start_idx:test_end_idx].mean()
        bike_lat_std = df['Bike Relative Lateral position'][test_start_idx:test_end_idx].std()
        return bike_lat_mean, bike_lat_std, crit_2
    bike_lat_mean, bike_lat_std, crit_2= criteria_2(df, test_start_idx, test_end_idx, d_lat)    
    st.session_state['bike_lat_mean'] = bike_lat_mean
    st.session_state['bike_lat_std'] = bike_lat_std
    st.session_state['crit_2'] = crit_2

######################## Criteria 3, 4, 6, 7  ##########################################
    def criteria_3(df,veh_corridor_idx , test_start_idx):
        # find the mean vehicle velocity in the corridor before the test starts
        veh_vel_corr_mean = df['Vehicle forward velocity'][veh_corridor_idx:test_start_idx].mean()
        veh_vel_corr_std = df['Vehicle forward velocity'][veh_corridor_idx:test_start_idx].std()
        if df['Vehicle forward velocity'][veh_corridor_idx:test_start_idx].max()< veh_vel_corr_mean +2 and df['Vehicle forward velocity'][veh_corridor_idx:test_start_idx].min()> veh_vel_corr_mean -2 :
            crit_3 = True
        else:
            crit_3 = False
        return veh_vel_corr_mean, veh_vel_corr_std, crit_3
    veh_vel_corr_mean, veh_vel_corr_std, crit_3 = criteria_3(df, veh_corridor_idx, test_start_idx)
    st.session_state['veh_vel_corr_mean'] = veh_vel_corr_mean
    st.session_state['veh_vel_corr_std'] = veh_vel_corr_std
    st.session_state['crit_3'] = crit_3

    def criteria_4(df, veh_corridor_idx, t_start_idx):
        #find the mean bike velocity in the corridor before the test starts
        bike_vel_corr_max = df['Bike forward velocity'][veh_corridor_idx:t_start_idx].max()
        if bike_vel_corr_max < 0.1:
            crit_4 = True
        else:
            crit_4 = False
        return bike_vel_corr_max, crit_4
    bike_vel_corr_max, crit_4 = criteria_4(df,veh_corridor_idx,t_start_idx)
    st.session_state['bike_vel_corr_max'] = bike_vel_corr_max
    st.session_state['crit_4'] = crit_4
    
    def criteria_6(df, test_start_idx, test_end_idx):
        #find the mean vehicle velocity between the start and end of test
        veh_vel_mean = df['Vehicle forward velocity'][test_start_idx:test_end_idx].mean()
        veh_vel_std = df['Vehicle forward velocity'][test_start_idx:test_end_idx].std()
        if df['Vehicle forward velocity'][test_start_idx:test_end_idx].max()< veh_vel_mean +2 and df['Vehicle forward velocity'][test_start_idx:test_end_idx].min()> veh_vel_mean -2 :
            crit_6 = True
        else:
            crit_6 = False
        return veh_vel_mean, veh_vel_std, crit_6
    veh_vel_mean, veh_vel_std, crit_6 = criteria_6(df, test_start_idx, test_end_idx)
    st.session_state['veh_vel_mean'] = veh_vel_mean
    st.session_state['veh_vel_std'] = veh_vel_std
    st.session_state['crit_6'] = crit_6

    def criteria_7(df, test_start_idx, test_end_idx):
        # find the bicycle mean velocity between the start and end of test 
        bike_vel_mean = df['Bike forward velocity'][test_start_idx:test_end_idx].mean()
        bike_vel_std = df['Bike forward velocity'][test_start_idx:test_end_idx].std()
        if df['Bike forward velocity'][test_start_idx:test_end_idx].max()< bike_vel_mean+0.5 and df['Bike forward velocity'][test_start_idx:test_end_idx].min()>bike_vel_mean-0.5 :
            crit_7 = True
        else:
            crit_7 = False
        return bike_vel_mean, bike_vel_std, crit_7

    bike_vel_mean, bike_vel_std, crit_7 = criteria_7(df, test_start_idx, test_end_idx)
    st.session_state['bike_vel_mean'] = bike_vel_mean
    st.session_state['bike_vel_std'] = bike_vel_std
    st.session_state['crit_7'] = crit_7
    
######################## Criteria 5  ##########################################
    
    def criteria_5(df, t_start_idx, test_start_idx, test_end_idx):

        #find the time to accelerate to within 0.5 kph of final bike velocity
        
        #Reference the front tire of the bike -->front overhang + Object 1 actual X (front axle)
        bike_d_acc_start = df.loc[t_start_idx,'Front tire X position']
        bike_d_start = df.loc[test_start_idx,'Front tire X position']
        #what distance did it take to accelerate to start of test
        bike_d_acc = bike_d_start - bike_d_acc_start
        # what is the position of the bike at the end of the test
        bike_d_end = df.loc[test_end_idx,'Front tire X position']
        if bike_d_acc < 5.66 + 1 and bike_d_acc > 5.66 - 1:
            crit_5 = True
        else:
            crit_5 = False
        return bike_d_acc, bike_d_start, bike_d_end, crit_5
    bike_d_acc, bike_d_start, bike_d_end, crit_5 = criteria_5(df, t_start_idx, test_start_idx, test_end_idx)
    st.session_state['bike_d_acc'] = bike_d_acc
    st.session_state['bike_d_start'] = bike_d_start
    st.session_state['bike_d_end'] = bike_d_end
    st.session_state['crit_5'] = crit_5

######################## Criteria 8  ##########################################
    # find da and db
    def criteria_8(df, t_start_idx, trig_pos):

        # position of vehicle when the bike is triggered/started
        # da = bike location when the test starts
        da_meas = df.loc[test_start_idx,'Front tire X position']
        # db = position of vehicle when the bike is triggered/started
        db_meas = df.loc[t_start_idx,'Vehicle bumper X position']
        if trig_pos -db_meas<=1 and db_meas -trig_pos <=1:
            crit_8 = True
        else:
            crit_8 = False
        return da_meas, db_meas, crit_8
    
    da_meas, db_meas, crit_8 = criteria_8(df, t_start_idx, trig_pos)
    st.session_state['da_meas'] = da_meas
    st.session_state['db_meas'] = db_meas
    st.session_state['crit_8'] = crit_8

################################################################################
    Veh_collision_pt = df.loc[test_end_idx,'Vehicle bumper X position']

    LPI = df.loc[test_end_idx,'Vehicle bumper X position'] -15   # will need to change 15 for speeds outside of test criteria
    LPI_time_idx = df.loc[(df['Vehicle bumper X position'] >= LPI), ['Time'] ].index[0]
    LPI_time = df.loc[LPI_time_idx, 'Time']
    LPI_Frame = df.loc[LPI_time_idx, 'FrameID']

    FPI = df.loc[test_end_idx,'Vehicle bumper X position'] -(15 + (4*veh_vel_mean/3.6) + (6-length))
    FPI_time_idx = df.loc[(df['Vehicle bumper X position'] >= FPI), ['Time'] ].index[0]
    FPI_time = df.loc[FPI_time_idx, 'Time']
    FPI_Frame = df.loc[FPI_time_idx, 'FrameID']
    
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
    ################################################################################################################################################
    # Sync point of da and db

    # find the relative da and db sync point in the data
    # find the determined synd pt in meters from the front tire of the bike and bumper of vehicle
    da_db_sync_distance = (da-db)

    st.session_state['da_db_distance'] = da_db_sync_distance
    # st.write('Sync Distance = da - db', round(da_db_sync_distance,2))

    def db_correction(d_lat, radius, length):
        # find the added distance the vehicle will travel based on R, Y, and L
        Y = d_lat + 0.25
        R = radius
        db3 =R*math.acos((R-Y)/R) - math.sqrt(R*R - (R-Y)*(R-Y))
        db_adj = length + db3
        return db_adj
    db_adj = db_correction(d_lat,radius, length)
    
    st.session_state['db_adj'] = db_adj

    #create df column with db adjustment due to R,Y, and L
    df['Vehicle bumper X position w turn correction'] = df['Vehicle bumper X position'] - db_adj
    # create df column with relative absolute distance between bike and vehicle
    df['ABS Separation w db adjust'] = abs(df['Vehicle bumper X position w turn correction'] - df['Front tire X position'])
    df['Separation w db adjust']= df['Vehicle bumper X position w turn correction'] - df['Front tire X position']
    df['Separation w/o db adjust']= df['Vehicle bumper X position'] - df['Front tire X position']

    # find indexes where sync distance is within specifications +/- 0.5 meters
    l_lim = da_db_sync_distance - 0.5
    u_lim = da_db_sync_distance + 0.5

    # dadbsync = df[(df['Separation w/o db adjust'] >= l_lim) & (df['Separation w/o db adjust'] <= u_lim) & (df['Bike forward velocity'] >= bike_vel-0.5)]
    
    dadbsync = df[(df['Separation w db adjust'] >= l_lim) & (df['Separation w db adjust'] <= u_lim) & (df['Bike forward velocity'] >= bike_vel-0.5)]
    st.session_state['dadbsync'] = dadbsync

    if dadbsync.empty:
        st.warning('No valid sync distance found with d_a and d_b', icon="⚠️")
        st.markdown("<h1 style='color: red;'>Proceed to Troubleshoot Guide Page</h1>", unsafe_allow_html=True)
    else:
        # first location of sync points
        test_start_idx_sync = dadbsync['Time'].idxmin()

        test_start_sync = df.loc[test_start_idx_sync, 'Time']

        st.session_state['test_start_idx_sync'] = test_start_idx_sync
        st.session_state['test_start_sync'] = test_start_sync
        
        #collision time is 8 seconds after the start of the test
        test_end_sync = test_start_sync+8
        test_end_idx_sync = df.loc[(df['Time'] >= test_end_sync), ['Time'] ].index[0]
        st.session_state['test_end_idx_sync'] = test_end_idx_sync
        st.session_state['test_end_sync'] = test_end_sync

        # verify that sync points are valid
        max_idx = df['Time'].idxmax()
        if test_end_idx_sync > max_idx:
            st.markdown("<h1 style='text-align: center; color: red;'>No valid Sync time found!!!!</h1>", unsafe_allow_html=True)
        else:
            
            #find da db sync mid point
            da_db_sync_vehicle = df.loc[test_start_idx_sync, 'Vehicle bumper X position']+0.5
            da_db_sync_bike = df.loc[test_start_idx_sync, 'Front tire X position']+0.5
            st.session_state['da_db_sync_vehicle'] = da_db_sync_vehicle
            st.session_state['da_db_sync_bike'] = da_db_sync_bike
            
            #find location of bike and vehicle when bike reaches spec velocity
            vehicle_start = df.loc[test_start_idx, 'Vehicle bumper X position']
            bike_start = df.loc[test_start_idx, 'Front tire X position']
            
            #find da and db sync locations
            da_meas_sync = da_db_sync_bike - bike_start
            db_meas_sync = da_db_sync_vehicle - vehicle_start
            st.session_state['da_meas_sync'] = da_meas_sync
            st.session_state['db_meas_sync'] = db_meas_sync

        #####################################################################################    
            #vehicle position at the start of test, and end of test
            
            veh_d_start_sync = df.loc[test_start_idx_sync,'Vehicle bumper X position'] 
            veh_d_end_sync = df.loc[test_end_idx_sync,'Vehicle bumper X position']
    
            st.session_state['veh_d_start_sync'] = veh_d_start_sync
            st.session_state['veh_d_end_sync'] = veh_d_end_sync

        ######################## Criteria 1, 2 ##########################################
          
            veh_lat_mean_sync, veh_lat_std_sync, crit_1_sync = criteria_1(df, veh_corridor_idx, test_end_idx_sync)    
            st.session_state['veh_lat_mean_sync'] = veh_lat_mean_sync
            st.session_state['veh_lat_std_sync'] = veh_lat_std_sync
            st.session_state['crit_1_sync'] = crit_1_sync

            bike_lat_mean_sync, bike_lat_std_sync, crit_2_sync = criteria_2(df, test_start_idx_sync, test_end_idx_sync, d_lat)
            st.session_state['bike_lat_mean_sync'] = bike_lat_mean_sync
            st.session_state['bike_lat_std_sync'] = bike_lat_std_sync
            st.session_state['crit_2_sync'] = crit_2_sync

        ######################## Criteria 3, 4, 6, 7  ##########################################
            
            veh_vel_corr_mean_sync, veh_vel_corr_std_sync, crit_3_sync = criteria_3(df, veh_corridor_idx, test_start_idx_sync)
            st.session_state['veh_vel_corr_mean_sync'] = veh_vel_corr_mean_sync
            st.session_state['veh_vel_corr_std_sync'] = veh_vel_corr_std_sync
            st.session_state['crit_3_sync'] = crit_3_sync

            # same as non sync criteria 4
            
            veh_vel_mean_sync, veh_vel_std_sync, crit_6_sync = criteria_6(df, test_start_idx_sync, test_end_idx_sync)
            st.session_state['veh_vel_mean_sync'] = veh_vel_mean_sync
            st.session_state['veh_vel_std_sync'] = veh_vel_std_sync
            st.session_state['crit_6_sync'] = crit_6_sync

            bike_vel_mean_sync, bike_vel_std_sync, crit_7_sync = criteria_7(df, test_start_idx_sync, test_end_idx_sync)
            st.session_state['bike_vel_mean_sync'] = bike_vel_mean_sync
            st.session_state['bike_vel_std_sync'] = bike_vel_std_sync
            st.session_state['crit_7_sync'] = crit_7_sync

        ######################## Criteria 5  ##########################################
            # same as non sync criteria 5

        ######################## Criteria 8  ##########################################
            # by definition a sync point has been found
            
        #####################################################################################
            Veh_collision_pt_sync = df.loc[test_end_idx_sync,'Vehicle bumper X position']

            LPI_sync = df.loc[test_end_idx_sync,'Vehicle bumper X position'] -15   # will need to change 15 for speeds outside of test criteria
            LPI_time_idx_sync = df.loc[(df['Vehicle bumper X position'] >= LPI_sync), ['Time'] ].index[0]
            LPI_time_sync = df.loc[LPI_time_idx_sync, 'Time']
            LPI_Frame_sync = df.loc[LPI_time_idx_sync, 'FrameID']

            FPI_sync = df.loc[test_end_idx_sync,'Vehicle bumper X position'] -(15 + (4*veh_vel_mean_sync/3.6) + (6-length))
            FPI_time_idx_sync = df.loc[(df['Vehicle bumper X position'] >= FPI_sync), ['Time'] ].index[0]
            FPI_time_sync = df.loc[FPI_time_idx_sync, 'Time']
            FPI_Frame_sync = df.loc[FPI_time_idx_sync, 'FrameID']

            st.session_state['Veh_collision_pt_sync'] = Veh_collision_pt_sync
            st.session_state['LPI_sync'] = LPI_sync
            st.session_state['LPI_time_idx_sync'] = LPI_time_idx_sync
            st.session_state['LPI_time_sync'] = LPI_time_sync
            st.session_state['LPI_Frame_sync'] = LPI_Frame
            st.session_state['FPI_sync'] = FPI_sync
            st.session_state['FPI_time_idx_sync'] = FPI_time_idx_sync
            st.session_state['FPI_time_sync'] = FPI_time_sync
            st.session_state['FPI_Frame_sync'] = FPI_Frame_sync
            