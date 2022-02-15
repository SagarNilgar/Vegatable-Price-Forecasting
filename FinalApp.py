import streamlit as st
import pickle



st.title('Vegatable Price Prediction')
st.image('./header.jpg')
model = pickle.load(open(
    r'D:\VIT\Sem 5 (3 yr)\vegatble_forcatsing\Vegatable-Price-Forecasting\models\rf0.pkl', 'rb'))


def run():

    # For state
    gen_display = ('Andhra Pradesh', 'Chattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal', 'Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala','Madhya Pradesh', 'Maharashtra', 'Nagaland', 'NCT of Delhi', 'Odisha', 'Punjab', 'Rajasthan', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttrakhand', 'West Bengal')
    gen_options = list(range(len(gen_display)))
    state = st.selectbox("State", gen_options,
                        format_func=lambda x: gen_display[x])
    

    # For district
    gen_display = ('Agra', 'Ahmedabad', 'Ahmednagar', 'Ajmer', 'Alappuzha', 'Aligarh', 'Alirajpur', 'Allahabad', 'Alwar', 'Amarawati', 'Ambala', 'Ambedkarnagar', 'Amreli', 'Amritsar', 'Anand', 'Anantnag', 'Angul', 'Anupur', 'Auraiya', 'Aurangabad', 'Azamgarh', 'Badaun', 'Badwani', 'Bagalkot', 'Baghpat', 'Bahraich', 'Balasore', 'Ballia', 'Balrampur', 'Banaskanth', 'Banda ', 'Bangalore', 'Bankura', 'Barabanki', 'Bareilly', 'Bargarh', 'Barmer', 'Barnala', 'Basti', 'Beed', 'Belgaum','Bellary', 'Bhadohi(Sant Ravi Nagar)', 'Bhadrak', 'Bharatpur', 'Bharuch', 'Bhatinda', 'Bhavnagar', 'Bhilwara', 'Bhiwani', 'Bhopal', 'Bidar', 'Bijapur', 'Bijnor', 'Bikaner', 'Bilaspur', 'Birbhum', 'Bolangir', 'Boudh', 'Bulandshahar', 'Buldhana', 'Burdwan', 'Burhanpur', 'Chamba', 'Champawat', 'Chamrajnagar', 'Chandauli', 'Chandrapur', 'Chhatarpur', 'Chhindwara', 'Chikmagalur', 'Chitrakut', 'Chittorgarh', 'Churu', 'Coochbehar ', 'Cuttack', 'Dahod', 'Damoh', 'Darjeeling','Dhar','Dharwad','Dhenkanal','Dhule','Durg','Ernakulam','Etah','Etawah','Faizabad','Faridabad','Faridkot','Farukhabad','Fatehabad','Fatehgarh','Fatehpur','Fazilka','Ferozpur','Firozabad','Gadag','Ganganagar','Ganjam','Garhwal(Pauri)','Gautam Budh Nagar','Ghaziabad','Ghazipur','Gonda','Gorakhpur','Guna','Gurdaspur','Gurgaon','Gwalior','Hamirpur','Hanumangarh','Harda','Hardoi','Haridwar','Hassan','Hathras','Haveri','Hissar','Hooghly','Hoshangabad','Hoshiarpur','Howrah','Hyderabad','Idukki','Indore','Jabalpur','Jaipur','Jaisalmer','Jajpur','Jalandhar','Jalaun(Orai)','Jalgaon','Jalore','Jalpaiguri','Jammu','Jamnagar','Jaunpur','Jhabua','Jhajar','Jhansi','Jharsuguda','Jhunjunu','Jind','Jodhpur','Junagarh','Jyotiba Phule Nagar','Kaithal','Kalahandi','Kangra','Kannuj','Kannur','Kanpur','kapurthala','Karnal','Kasargod','Kathua','Kaushambi','Kendrapara','Keonjhar','Khandwa','Kheda','Khiri(Lakhimpur)','Khowai','Khurda','Kolar','Kolhapur','Kolkata','Kollam','Kota','Kottayam','Kozhikode(Calicut)','Kullu','Kurnool','Kurukshetra','Lakhimpur','Lalitpur','Lohardaga','Lucknow','Ludhiana','Maharajganj','Mahendragarh-Narnaul','Mahoba','Mainpuri','Malappuram','Malda','Malkangiri','Mandi','Mandsaur','Mandya','Mangalore(Dakshin Kannad)','Mansa','Mathura','Mau(Maunathbhanjan)','Mayurbhanja','Medak','Medinipur(E)','Medinipur(W)','Meerut','Mehsana','Mewat','Mirzapur','Moga','Mohali','Mokokchung','Morena','Muktsar','Mumbai','Muradabad','Murshidabad','Muzaffarnagar','Mysore','Nadia','Nagaur','Nagpur','Nandurbar','Nanital','Narsinghpur','Nashik','Navsari','Nawanshahr','Neemuch','North 24 Parganas','North Goa','North Tripura','Nuapada','Osmanabad','Padrauna(Kusinagar)','Palakad','Pali','Palwal','Panchkula','Panchmahals','Panipat','Pathankot','Patiala','Pillibhit','Porbandar','Pratapgarh','Pune','Puruliya','Raebarelli','Raichur','Raigad','Raigarh','Raisen','Rajasamand','Rajgarh','Rajkot','Rajnandgaon','Rajouri','Rampur','Ranchi','Ratlam','Ratnagiri','Rayagada','Rewari','Rohtak','Ropar(Rupnagar)','Sagar','Saharanpur','Sangli','Sangrur','SantKabirNagar','Satara','Satna','Sehore','Sepahijala','Shahjahanpur','Shajapur','Sheopur','Shimla','Shimoga','Shivpuri','Sholapur','SiddharthNagar','Sikar','Sirmore','Sirohi','Sirsa','Sitapur','Solan','Sonbhadra','Sonepur','Sonipat','Sounth 24 Parganas','South District','Srinagar','Sultanpur','Sundergarh','Surat','Surendranagar','Tarntaran','Thane','Thirssur','Thiruvananthapuram','Tonk','Tumkur','Udaipur','Udhampur','UdhamSinghNagar','Udupi','Ujjain','Una','Unnao','Unokoti','Vadodara(Baroda)','Varanasi','YamunaNagar')
    gen_options = list(range(len(gen_display)))
    district = st.selectbox("District", gen_options,
                                format_func=lambda x: gen_display[x])
    
    
    

    # For month
    mar_display = ('', 'January', 'Febuary', 'March', 'April','May', 'June', 'july', 'Augest', 'September')
    mar_options = list(range(len(mar_display)))
    month = st.selectbox("Month", mar_options,
                        format_func=lambda x: mar_display[x])

    # day
    dep_display = (' ','1','2','3','4','5','6','7','8','9','10','11','12','13', '13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30')
    dep_options = list(range(len(dep_display)))
    day = st.selectbox("Day",  dep_options,
                    format_func=lambda x: dep_display[x])
    
    dep_display = ('1st Sort','2nd Sort','Bangalore-Samal','Beelary-Red','Bellary','Big','Bombay (U.P.)','Dry F.A.Q.','Hybrid','Local','Medium','Nasik','Onion','Other','Pole','Puna','Pusa-Red','Red','Small','Telagi','White')
    dep_options = list(range(len(dep_display)))
    variety = st.selectbox("Variety",  dep_options,
                    format_func=lambda x: dep_display[x])

    if st.button("Submit"):

        features = [[state, district, month, day,variety]]
        print(features)
        prediction = model.predict(features)
        st.caption('The predicted price of onion.')
        st.text(prediction)
        


run()
