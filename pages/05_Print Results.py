import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from fpdf import FPDF
import time

test_options = st.session_state['test_options']
# filename_txt  = st.session_state['filename_txt']
filename_txt  = '000300780027.txt'
split_filename = filename_txt.split('.')[0]
test_filename = f"{test_options} {split_filename}.pdf"
current_time = time.localtime() # get the current time as a time.struct_time object
formatted_time = time.strftime("%B %d, %Y", current_time) # format the time as month day year

# da_position = st.session_state['da_position']
# db_position = st.session_state['db_position']
# t_start = st.session_state['t_start']
# test_start = st.session_state['test_start']
# ######################## Criteria 1, 2 ##########################################
# #vehicle position at the start of the corridor, start of test, and end of test
# veh_entercorridor_time = st.session_state['veh_entercorridor_time']

# veh_lat_mean = st.session_state['veh_lat_mean']
# veh_lat_std = st.session_state['veh_lat_std']
# bike_lat_mean = st.session_state['bike_lat_mean']
# bike_lat_std = st.session_state['bike_lat_std']
crit_1= st.session_state['crit_1']
crit_2= st.session_state['crit_2']
######################## Criteria 3, 4, 6, 7  ##########################################
# veh_vel_corr_mean = st.session_state['veh_vel_corr_mean']
# veh_vel_corr_std = st.session_state['veh_vel_corr_std']
# bike_vel_corr_max = st.session_state['bike_vel_corr_max']
# veh_vel_mean = st.session_state['veh_vel_mean']
# veh_vel_std = st.session_state['veh_vel_std']
# bike_vel_mean = st.session_state['bike_vel_mean']
# bike_vel_std = st.session_state['bike_vel_std']
crit_3= st.session_state['crit_3']
crit_4= st.session_state['crit_4']
crit_6= st.session_state['crit_6']
crit_7= st.session_state['crit_7']
######################## Criteria 5 ##########################################
# d_bike_acc = st.session_state['d_bike_acc']
# d_bike_start = st.session_state['d_bike_start']
# d_bike_end =st.session_state['d_bike_end']
crit_5= st.session_state['crit_5']
######################## Criteria 8 ##########################################
# d_da_meas = st.session_state['d_da_meas']
# d_db_meas = st.session_state['d_db_meas']
# d_db_meas_dbadj = st.session_state['d_db_meas_dbadj']
# da_meas_time = st.session_state['da_meas_time']
crit_8= st.session_state['crit_8']
######################## LPI and FPI ##########################################
# LPI_time = st.session_state['LPI_time']
# LPI_Frame = st.session_state['LPI_Frame']
# FPI_time = st.session_state['FPI_time'] 
# FPI_Frame = st.session_state['FPI_Frame']
# dd = st.session_state['dd']
######################## Provide a Summary Chart ##########################################
criteria = [crit_1, crit_2, crit_3, crit_4, crit_5, crit_6, crit_7, crit_8] #boolean list of criteria
criteria_list = ['criteria_1', 'criteria_2', 'criteria_3', 'criteria_4', 'criteria_5', 'criteria_6', 'criteria_7', 'criteria_8']
criteria_int = []
for i in range(len(criteria)):
    if criteria[i]:
        criteria_int.append(1)
    else:
        criteria_int.append(-1)
        
criteria_df = pd.DataFrame({'criteria': criteria_int, 'criteria_list': criteria_list})

# Map integer values to pass/fail labels
criteria_df['pass_fail'] = criteria_df['criteria'].map({1: 'Pass', -1: 'Fail'})
criteria_df['color'] = criteria_df['pass_fail'].map({'Pass': 'green', 'Fail': 'red'})
# Set color for bars
color_sequence= criteria_df['criteria'].map({1: 'green', -1: 'Red'})

placeholder = st.empty()
with placeholder.container():        
    
    fig = go.Figure(go.Bar(
        x=criteria_df['criteria_list'], 
        y=criteria_df['criteria'],
        marker_color=criteria_df['color']
    ))

    fig.update_layout(
        title='Pass Fail Criteria Summary',
        xaxis_tickangle=-45,
        yaxis=dict(tickvals=[1,-1], ticktext=['Pass', 'Fail']),
        yaxis_title='Pass or Fail'
    )

    my_saved_image = "plot5.jpeg"
    pio.write_image(fig, my_saved_image)                
    st.plotly_chart(fig, use_container_width=True)
st.markdown('---')
#################################################################################################################
#A4 format and dimensions
pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
Width = 210
Height = 297
##################################################################################################################
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#dsiplay FPI and LPI frame numbers
# def FPI_and_LPI_pdf():
#     pdf.set_font('Arial', '', 12)
#     pdf.set_font('', 'U')
#     pdf.set_text_color(0, 0, 128)  # navy color
#     pdf.cell(Width/2, 5, 'FPI:')
#     pdf.cell(Width/2, 5, 'LPI:')
#     pdf.ln()
#     if dd > 0:
#         pdf.set_font('Arial', '', 12)
#         pdf.set_text_color(0, 0, 0) #
#         pdf.cell(Width/2, 5, f'FPI Frame # : {FPI_Frame}')
#         pdf.cell(Width/2, 5, f'LPI Frame # : {LPI_Frame}' ,ln=1)
#         pdf.cell(Width/2, 5, f'FPI time (s) : {round(FPI_time,2)}')
#         pdf.cell(Width/2, 5, f'LPI time (s) : {round(LPI_time,2)}')
#     else:
#         pdf.set_font('Arial', '', 12)
#         pdf.set_text_color(0, 0, 0)
#         pdf.cell(Width/2, 5, f'FPI Frame # : None - dwell case')
#         pdf.cell(Width/2, 5, f'LPI Frame # : {LPI_Frame}',ln=1)
#         pdf.cell(Width/2, 5, 'FPI time (s) : None - dwell case')
#         pdf.cell(Width/2, 5, f'LPI time (s) : {round(LPI_time,2)}')
        

# Add the criteria results
# def two_crit_pdf(crit1,crit2, crit_num1, crit_num2):
#     pdf.set_font('Arial', '', 12)
#     pdf.set_font('', 'U')
#     pdf.set_text_color(0, 0, 128)  # navy color
#     pdf.cell(Width/2, 5, f'Test Criteria {crit_num1}:')
#     pdf.cell(Width/2, 5, f'Test Criteria {crit_num2}:')
#     pdf.ln()
#     if crit1:
#         pdf.set_font('Arial', '', 12)
#         pdf.set_text_color(0, 128, 0)  # green
#         pdf.cell(Width/2, 5, 'PASS')
#     else:
#         pdf.set_font('Arial', '', 12)
#         pdf.set_text_color(255, 0, 0)  # red
#         pdf.cell(Width/2, 5, 'FAIL')
#     if crit2:
#         pdf.set_font('Arial', '', 12)
#         pdf.set_text_color(0, 128, 0)  # green
#         pdf.cell(Width/2, 5, 'PASS')
#     else:
#         pdf.set_font('Arial', '', 12)
#         pdf.set_text_color(255, 0, 0)  # red
#         pdf.cell(Width/2, 5, 'FAIL')    
#     # Add spacing between columns
#     pdf.ln()

def create_report(filename = "Test_report.pdf"):
    
    #first page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)

    pdf.image("sensata.jpeg", Width-60, 0,  Width/4)
    pdf.set_xy(Width-80, 10)
    pdf.cell(40,10, f'Report generated on {formatted_time}', ln=1)
    pdf.set_xy(Width/4, 20)
    pdf.set_font('', 'U')
    pdf.cell(100, 10, txt = 'Regulation 151 Summary', ln=1)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 10,f'File name:  {split_filename}', ln=1)

    # pdf.cell(40, 10,f'Data Summary for {test_options}', ln=1)
    # pdf.cell(40, 10,f'File name:  {split_filename}')
    # pdf.cell(42, 10, f'Generated on {formatted_time}')
    pdf.image("plot5.jpeg", 0, 60, Width/2)
    pdf.image("Criteria.jpg", Width/2, 60, Width/2 -5)
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    # Add the title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 20, 'Test Criteria Measurement Values', align='C')
    pdf.ln()

#     two_crit_pdf(crit_1, crit_2, 1,2)
#     pdf.set_text_color(0, 0, 0)
#     pdf.cell(Width/2, 5, f'Mean Laterial Deviation of vehicle (m): {round(veh_lat_mean, 2)}')
#     pdf.cell(Width/2, 5, f'Mean Laterial Deviation of bicycle (m): {round(bike_lat_mean, 2)}', ln=1)
#     pdf.cell(Width/2, 5, f'Std Laterial Deviation of vehicle: {round(veh_lat_std, 2)}')
#     pdf.cell(Width/2, 5, f'Std Laterial Deviation of bicycle: {round(bike_lat_std, 2)}', ln=1)
#     pdf.ln()
#     pdf.ln()
#     two_crit_pdf(crit_3, crit_4, 3,4)
#     pdf.set_text_color(0, 0, 0)
#     pdf.cell(Width/2, 5, f'Mean Vehicle velocity before trigger pt (km/h): {round(veh_vel_corr_mean, 2)}')
#     pdf.cell(Width/2, 5, f'Bike Velocity before triggered (km/h): {round(bike_vel_corr_max,2)}', ln=1)
#     pdf.cell(Width/2, 5, f'Std Vehicle velocity: {round(veh_vel_corr_std, 2)}', ln=1)
#     pdf.ln()
#     pdf.ln()
#     two_crit_pdf(crit_5, crit_6, 5,6)
#     pdf.set_text_color(0, 0, 0)
#     pdf.cell(Width/2, 5,f'Bike- Time to accelerate to Test Velocity (s): {round(test_start-t_start,2)}')
#     pdf.cell(Width/2, 5, f'Vehicle mean Velocity (kph): {round(veh_vel_mean,2)}', ln=1)
#     pdf.cell(Width/2, 5,  f'Bike-Distance to accelerate to Test Velocity(m): {round(d_bike_acc,2)}')
#     pdf.cell(Width/2, 5, f'Vehicle standard deviation Velocity (kph)): {round(veh_vel_std,3)}', ln=1)
#     pdf.ln()
#     pdf.ln()
#     two_crit_pdf(crit_7, crit_8, 7,8)
#     pdf.set_text_color(0, 0, 0)
#     pdf.cell(Width/2, 5, f'Bicycle mean Velocity (kph): {round(bike_vel_mean,2)}')
#     pdf.cell(Width/2, 5, f'Calculated da: {round(da_position,2)}m   Measured da: {round(d_da_meas,2)}m', ln=1)
#     pdf.cell(Width/2, 5, f'Bicycle standard deviation Velocity (kph): {round(bike_vel_std,3)}')
#     pdf.cell(Width/2, 5, f'Calculated db: {round(db_position,2)}m   Measured db: {round(d_db_meas,2)}m', ln=1)
#     pdf.ln()
#     FPI_and_LPI_pdf()
#     #page 2 of the results
#     pdf.add_page()
#     pdf.set_font('Arial', 'B', 20)
#     pdf.cell(0, 20, txt = 'Plot Illustrating Criteria 1 and 2', align='C')
#     pdf.image("plot1.jpeg", 0, 30, Width )
#     pdf.ln()
#     pdf.set_xy(10, Height/2)
#     pdf.cell(0, 20, txt = 'Plot Illustrating Criteria 3, 4, 5, 6, 7', align='C')
#     pdf.image("plot2.jpeg", 0, 20+ Height/2, Width)

#     #page 3 of the results
#     pdf.add_page()
#     pdf.cell(0, 20, txt = 'Position Plot Illustrating Criteria 8', align='C')
#     pdf.image("plot3.jpeg", 0, 30, Width )
#     pdf.ln()
#     pdf.set_xy(10, Height/2)
#     pdf.cell(0, 20, txt = 'Time Plot Illustrating Criteria 8', align='C')
#     pdf.image("plot4.jpeg", 0, 20+ Height/2, Width)
#     # Save the PDF
    pdf.output(filename)

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if __name__ == '__main__':
    # local_css("style/style.css")
    if st.button('Do you want to generate a report?'):
        create_report(test_filename) 
        with st.spinner('Generating Report'):
            time.sleep(4)
        st.success('Report is Complete!')
    
    