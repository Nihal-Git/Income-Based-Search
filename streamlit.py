import pandas
import streamlit as st
from pycaret.classification import load_model, predict_model

countries= ['Select',
    'united kingdom', 'united states' ,'united arab emirates' ,'vietnam',
 'hungary' ,'france' ,'india' ,'switzerland', 'ireland' ,'italy', 'philippines',
 'bhutan',  'thailand' ,'belgium', 'canada' ,'indonesia', 'chile',
 'south africa', 'australia' ,'ecuador' ,'brazil', 'netherlands' ,'denmark',
 'botswana', 'bangladesh' ,'ukraine', 'peru' 'iran' ,'spain' ,'malaysia',
 'taiwan', 'new zealand', 'hong kong' ,'colombia' ,'austria', 'sri lanka',
 'ghana' ,'nigeria', 'germany', 'romania' ,'nepal', 'bosnia and herzegovina',
 'jordan', 'egypt' ,'singapore', 'japan' import pandas
import streamlit as st
from pycaret.classification import load_model, predict_model
import numpy
import pickle

countries= ['Select',
    'united kingdom', 'united states' ,'united arab emirates' ,'vietnam',
 'hungary' ,'france' ,'india' ,'switzerland', 'ireland' ,'italy', 'philippines',
 'bhutan',  'thailand' ,'belgium', 'canada' ,'indonesia', 'chile',
 'south africa', 'australia' ,'ecuador' ,'brazil', 'netherlands' ,'denmark',
 'botswana', 'bangladesh' ,'ukraine', 'peru' 'iran' ,'spain' ,'malaysia',
 'taiwan', 'new zealand', 'hong kong' ,'colombia' ,'austria', 'sri lanka',
 'ghana' ,'nigeria', 'germany', 'romania' ,'nepal', 'bosnia and herzegovina',
 'jordan', 'egypt' ,'singapore', 'japan' ,'niger' ,'zimbabwe',
 'democratic republic of the congo', 'turkey' ,'uzbekistan' ,'uganda',
 'croatia', 'poland' ,'sudan', 'pakistan' ,'mexico' ,'sweden' ,'argentina',
 'finland' ,'madagascar' ,'slovakia' ,'saudi arabia' ,'morocco', 'china',
 'kenya' ,'lebanon' ,'south korea' ,'jamaica' ,'armenia' ,'macau', 'serbia',
 'barbados', 'nicaragua', 'burundi', 'tanzania', 'qatar' ,'guatemala', 'norway',
 'tunisia' ,'puerto rico' ,'luxembourg' ,'angola' ,'lithuania' ,'algeria',
 'costa rica', 'moldova', 'zambia' ,'bulgaria' ,'czechia', 'russia', 'myanmar',
 'israel', 'venezuela' ,'honduras' ,'oman', 'trinidad and tobago' ,'estonia',
 'portugal' ,'greece', 'papua new guinea', 'montenegro', 'cyprus',
 'timor-leste', 'kuwait' ,'latvia' ,'malta', 'burkina faso' ,'cuba', 'rwanda',
 'albania' ,'guam' ,'dominican republic', 'cayman islands' ,'senegal',
 'azerbaijan', 'mongolia' ,'cameroon', 'new caledonia' ,'bolivia' ,'mauritius'
 'namibia', 'cambodia', 'côte d’ivoire' ,'el salvador'
]

industries=['Select',
    'government administration' ,'construction' ,'computer software',
 'financial services', 'building materials',
 'electrical/electronic manufacturing', 'medical practice',
 'mechanical or industrial engineering' ,'business supplies and equipment',
  'education management', 'civil engineering', 'apparel & fashion',
 'consumer services', 'design', 'textiles', 'higher education' ,'banking',
 'management consulting' ,'retail' ,'leisure, travel, & tourism',
 'automotive' ,'information technology and services' ,'food production',
 'commercial real estate' ,'maritime' ,'hospital & health care', 'insurance',
 'marketing and advertising' ,'hospitality' ,'media production',
 'government relations' ,'furniture', 'chemicals', 'legal services',
 'human resources', 'consumer electronics' ,'law practice',
 'paper & forest products' ,'utilities' ,'accounting' ,'music', 'sports',
 'package/freight delivery', 'oil & energy',
 'transportation/trucking/railroad' ,'research', 'telecommunications',
 'health, wellness and fitness', 'consumer goods' ,'pharmaceuticals',
 'online media', 'defense & space', 'logistics and supply chain',
 'non-profit organization management', 'medical devices' ,'publishing',
 'think tanks' ,'entertainment', 'aviation & aerospace' ,'graphic design',
 'newspapers' ,'internet' ,'real estate', 'machinery', 'biotechnology',
 'computer & network security', 'semiconductors',
 'security and investigations', 'wholesale' ,'staffing and recruiting',
 'airlines/aviation' ,'civic & social organization' ,'mining & metals',
 'cosmetics' ,'military', 'glass, ceramics, & concrete',
 'facilities services', 'environmental services',
 'public relations and communications', 'printing',
 'professional training & coaching', 'farming' ,'renewables & environment',
 'arts and crafts' ,'international affairs', 'investment management',
 'architecture & planning', 'fine art' ,'import and export',
 'mental health care' ,'translation and localization', 'broadcast media',
 'market research' ,'primary/secondary education' ,'events services',
 'outsourcing/offshoring' ,'e-learning', 'wine and spirits' ,'public policy',
 'motion pictures and film' ,'computer games', 'luxury goods & jewelry',
 'industrial automation' ,'gambling & casinos', 'tobacco' 'animation',
 'restaurants' ,'dairy', 'libraries', 'packaging and containers',
 'public safety' ,'computer hardware' ,'individual & family services',
 'shipbuilding' ,'writing and editing' ,'capital markets' 'warehousing',
 'computer networking' ,'information services' ,'political organization',
 'executive office', 'philanthropy' ,'religious institutions' ,'veterinary',
 'ranching' ,'district of columbia', 'recreational facilities and services',
 'photography' ,'international trade and development',
 'law enforcement' ,'venture capital & private equity',
 'plastics', 'food & beverages' ,'program development', 'judiciary',
 'investment banking'
]



st.title('Income Based Search')

job= st.text_input('Enter Job Title')
job_title= job.lower()

industry= st.selectbox(label= 'Select Industry', options= industries)

location_country= st.selectbox(label= 'Select Country',options= countries )

data_test= {
    'industry': industry,
    'job_title': job_title,
    'location_country': location_country
}
input_data= pandas.DataFrame(data_test, index= [0])

complete_model= load_model("Complete_Data_Frame/Complete_RF_Model")
complete_model_without_20K= load_model("Data_Frame_without_20K/Model_without_20K")
model_1 = load_model("Data_Frame_1/RF_Model_1")
model_2 = load_model("Data_Frame_2/RF_Model_2")
model_3 = load_model("Data_Frame_3/RF_Model_3")
model_4 = load_model("Data_Frame_4/RF_Model_4")



col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Calculate Salary Ranges')

if center_button:
    
    predict_1= predict_model(model_1, data=input_data)
    predict_2= predict_model(model_2, data=input_data)
    predict_3= predict_model(model_3, data=input_data)
    predict_4= predict_model(model_4, data=input_data)
    predict_complete= predict_model(complete_model, data=input_data)
    predict_without_20K= predict_model(complete_model_without_20K, data=input_data)



    labels= [predict_1["Label"][0], predict_2["Label"][0], predict_3["Label"][0], predict_4["Label"][0], predict_complete["Label"][0], predict_without_20K["Label"][0]]
    confidence= [predict_1["Score"][0], predict_2["Score"][0], predict_3["Score"][0], predict_4["Score"][0], predict_complete["Score"][0], predict_without_20K["Score"][0]]
    model_name= ["Model 1", "Model 2", "Model 3", "Model 4", "Complete Model", "Model Without 20K"]

    predictions_data= {"Model": model_name, "Inferred Salary": labels, "Confidence Level": confidence}
    predictions_data_frame= pandas.DataFrame(predictions_data)
    st.dataframe(predictions_data_frame)

else:
    st.error('Give Inputs')
,'niger' ,'zimbabwe',
 'democratic republic of the congo', 'turkey' ,'uzbekistan' ,'uganda',
 'croatia', 'poland' ,'sudan', 'pakistan' ,'mexico' ,'sweden' ,'argentina',
 'finland' ,'madagascar' ,'slovakia' ,'saudi arabia' ,'morocco', 'china',
 'kenya' ,'lebanon' ,'south korea' ,'jamaica' ,'armenia' ,'macau', 'serbia',
 'barbados', 'nicaragua', 'burundi', 'tanzania', 'qatar' ,'guatemala', 'norway',
 'tunisia' ,'puerto rico' ,'luxembourg' ,'angola' ,'lithuania' ,'algeria',
 'costa rica', 'moldova', 'zambia' ,'bulgaria' ,'czechia', 'russia', 'myanmar',
 'israel', 'venezuela' ,'honduras' ,'oman', 'trinidad and tobago' ,'estonia',
 'portugal' ,'greece', 'papua new guinea', 'montenegro', 'cyprus',
 'timor-leste', 'kuwait' ,'latvia' ,'malta', 'burkina faso' ,'cuba', 'rwanda',
 'albania' ,'guam' ,'dominican republic', 'cayman islands' ,'senegal',
 'azerbaijan', 'mongolia' ,'cameroon', 'new caledonia' ,'bolivia' ,'mauritius'
 'namibia', 'cambodia', 'côte d’ivoire' ,'el salvador'
]

industries=['Select',
    'government administration' ,'construction' ,'computer software',
 'financial services', 'building materials',
 'electrical/electronic manufacturing', 'medical practice',
 'mechanical or industrial engineering' ,'business supplies and equipment',
  'education management', 'civil engineering', 'apparel & fashion',
 'consumer services', 'design', 'textiles', 'higher education' ,'banking',
 'management consulting' ,'retail' ,'leisure, travel, & tourism',
 'automotive' ,'information technology and services' ,'food production',
 'commercial real estate' ,'maritime' ,'hospital & health care', 'insurance',
 'marketing and advertising' ,'hospitality' ,'media production',
 'government relations' ,'furniture', 'chemicals', 'legal services',
 'human resources', 'consumer electronics' ,'law practice',
 'paper & forest products' ,'utilities' ,'accounting' ,'music', 'sports',
 'package/freight delivery', 'oil & energy',
 'transportation/trucking/railroad' ,'research', 'telecommunications',
 'health, wellness and fitness', 'consumer goods' ,'pharmaceuticals',
 'online media', 'defense & space', 'logistics and supply chain',
 'non-profit organization management', 'medical devices' ,'publishing',
 'think tanks' ,'entertainment', 'aviation & aerospace' ,'graphic design',
 'newspapers' ,'internet' ,'real estate', 'machinery', 'biotechnology',
 'computer & network security', 'semiconductors',
 'security and investigations', 'wholesale' ,'staffing and recruiting',
 'airlines/aviation' ,'civic & social organization' ,'mining & metals',
 'cosmetics' ,'military', 'glass, ceramics, & concrete',
 'facilities services', 'environmental services',
 'public relations and communications', 'printing',
 'professional training & coaching', 'farming' ,'renewables & environment',
 'arts and crafts' ,'international affairs', 'investment management',
 'architecture & planning', 'fine art' ,'import and export',
 'mental health care' ,'translation and localization', 'broadcast media',
 'market research' ,'primary/secondary education' ,'events services',
 'outsourcing/offshoring' ,'e-learning', 'wine and spirits' ,'public policy',
 'motion pictures and film' ,'computer games', 'luxury goods & jewelry',
 'industrial automation' ,'gambling & casinos', 'tobacco' 'animation',
 'restaurants' ,'dairy', 'libraries', 'packaging and containers',
 'public safety' ,'computer hardware' ,'individual & family services',
 'shipbuilding' ,'writing and editing' ,'capital markets' 'warehousing',
 'computer networking' ,'information services' ,'political organization',
 'executive office', 'philanthropy' ,'religious institutions' ,'veterinary',
 'ranching' ,'district of columbia', 'recreational facilities and services',
 'photography' ,'international trade and development',
 'law enforcement' ,'venture capital & private equity',
 'plastics', 'food & beverages' ,'program development', 'judiciary',
 'investment banking'
]



st.title('Income Based Search')

job= st.text_input('Enter Job Title')
job_title= job.lower()

industry= st.selectbox(label= 'Select Industry', options= industries)

location_country= st.selectbox(label= 'Select Country',options= countries )

data_test= {
    'industry': industry,
    'job_title': job_title,
    'location_country': location_country
}

data_frame_test= pandas.DataFrame(data_test, index= [0])

complete_model= pickle.load(open("Complete_Data_Frame/Complete_RF_Model","rb"))
complete_model_without_20K= pickle.load(open("Data_Frame_without_20K/Model_without_20K","rb"))
model_1 = pickle.load(open("Data_Frame_1/RF_Model_1","rb"))
model_2 = pickle.load(open("Data_Frame_2/RF_Model_2","rb"))
model_3 = pickle.load(open("Data_Frame_3/RF_Model_3","rb"))
model_4 = pickle.load(open("Data_Frame_4/RF_Model_4","rb"))

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Calculate Salary Ranges')

if center_button:
    
    predict_1= model_1.predict(data_frame_test)
    predict_2= model_2.predcit(data_frame_test)
    predict_3= model_3.predict(data_frame_test)
    predict_4= model_4.predict(data_frame_test)
    predict_complete= complete_model.predict(data_frame_test)
    predict_without_20K= complete_model_without_20K.predict(data_frame_test)



    labels= [predict_1["Label"][0], predict_2["Label"][0], predict_3["Label"][0], predict_4["Label"][0], predict_complete["Label"][0], predict_without_20K["Label"][0]]
    confidence= [predict_1["Score"][0], predict_2["Score"][0], predict_3["Score"][0], predict_4["Score"][0], predict_complete["Score"][0], predict_without_20K["Score"][0]]
    model_name= ["Model 1", "Model 2", "Model 3", "Model 4", "Complete Model", "Model Without 20K"]

    predictions_data= {"Model": model_name, "Inferred Salary": labels, "Confidence Level": confidence}
    predictions_data_frame= pandas.DataFrame(predictions_data)
    st.dataframe(predictions_data_frame)

else:
    st.error('Give Inputs')
