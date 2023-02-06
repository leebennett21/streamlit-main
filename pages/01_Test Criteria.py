import streamlit as st
from PIL import Image

st.title('Test Criteria and Cases for Regulation 151 -- Lemhi')
st.markdown(""" ## Test Validity Criteria
            
**Criteria 1:**	*Lateral deviation:*  Ego Vehicle must not deviate beyond +/- 0.1 m from the test path while the Ego Vehicle is between the CORRIDOR LINE and the COLLISION LINE.(If not specified, tolerances are +/-0.1 m)

**Criteria 2:**	*Lateral deviation:*  Target VRU must not deviate beyond +/- 0.2 m from the test path d_Path_Lateral m to the nearside edge (right edge, North America) of the Ego Vehicle while the Target VRU is between the BICYCLE START LINE and the COLLISION LINE. (6.5.6 The lateral deviation of the dummy with respect to a straight line connecting initial starting position and theoretical collision point (as defined in Figure 1 of Appendix 1) shall be maximum ±0.2 m.)

**Criteria 3:**	*Speed initiation:*  Ego Vehicle must reach V_EGO km/h +/- 2 km/h prior to the front edge of the Ego Vehicle reaching the nearer of the BICYCLE TRIGGER LINE or the CORRIDOR LINE (6.5.4 Drive the vehicle at a speed as shown in Table 1 of Appendix 1 to this Regulation with a tolerance of ±2 km/h through the corridor)

**Criteria 4:**	*Speed initiation:*  If the CORRIDOR LINE is nearer than the BICYCLE TRIGGER LINE to the front edge of the Ego Vehicle, then the Target VRU must maintain 0.0 km/h while the front edge fo the Ego Vehicle is between the CORRIDOR LINE and the BICYCLE TRIGGER LINE.

**Criteria 5:**	*Speed initiation:*  Target VRU must reach V_TRGT km/h +/- 0.5 km/h prior to reaching the BICYCLE SPEED LINE that is 5.66 m in front of the BICYCLE START LINE (6.5.6 If the acceleration distance cannot be achieved, adjust bicycle starting position and vehicle corridor length by the same amount.)

**Criteria 6:** *Speed maintenance:*  Ego Vehicle must maintain V_EGO km/h +/- 2 km/h until reaching the TEST STOP LINE (6.5.4 Drive the vehicle at a speed as shown in Table 1 of Appendix 1 to this Regulation with a tolerance of ±2 km/h through the corridor. )

**Criteria 7:** *Speed maintenance:*  Target VRU must maintain V_TRGT km/h +/- 0.5 km/h until reaching the TEST STOP LINE (6.5.6 the dummy shall move in a steady pace for at least 8 seconds with a speed tolerance of ±0.5 km/h.)

**Criteria 8:**	*Position maintenance:*  The front edge of the Ego Vehicle must be within +/- 0.5 m of LINE B at the instance the front edge of the Target VRU either reaches LINE A – 0.5 m, or LINE A + 0.5 m. (6.5.6 The dummy shall cross line A (Figure 1 of Appendix 1) with a tolerance of ±0.5 m at the same time as the vehicle cross line B (Figure 1 of Appendix 1) with a tolerance of ±0.5 m.)

            
            
             """)
image2 = Image.open('Reg151 Test Cases Chart Amend1.JPG')
st.image(image2, caption='UN Regulation 151 Test Cases')

image1 = Image.open('Reg151 Test Cases.JPG')
st.image(image1, caption='UN Regulation 151 Test Cases')

image = Image.open('Reg151.JPG')
st.image(image, caption='UN Regulation 151 Dynamic')

image3 = Image.open('Reg151 Static.JPG')
st.image(image3, caption='UN Regulation 151 Static')


st.markdown(""" ## Calculations  """)
     