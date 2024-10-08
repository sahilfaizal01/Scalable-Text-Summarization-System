from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain import OpenAI
from api_config import get_secret

def prediction_pipeline(text):
    text_splitter = CharacterTextSplitter(separator='\n',chunk_size=1000,chunk_overlap=20)
    text_chunks = text_splitter.split_text(text) # to split the text into chunks
    #print(len(text_chunks)) # to estimate token requirement
    llm = OpenAI(openai_api_key = get_secret()) # initiate LLM model
    docs = [Document(page_content = t) for t in text_chunks] # creating document objects
    chain = load_summarize_chain(llm = llm, chain_type='map_reduce',verbose=True)
    summary = chain.run(docs)
    return summary

# text1 = """
# Kerala, called Keralam in Malayalam, is a state on the Malabar Coast of India.[15] It was formed on 1 November 1956, following the passage of the States Reorganisation Act, by combining Malayalam-speaking regions of the erstwhile regions of Cochin, Malabar, South Canara, and Travancore.[16][17] Spread over 38,863 km2 (15,005 sq mi), Kerala is the 21st largest Indian state by area. It is bordered by Karnataka to the north and northeast, Tamil Nadu to the east and south, and the Lakshadweep Sea[18] to the west. With 33 million inhabitants as per the 2011 census, Kerala is the 13th-largest Indian state by population. It is divided into 14 districts with the capital being Thiruvananthapuram. Malayalam is the most widely spoken language and is also the official language of the state.[19]

# The Chera dynasty was the first prominent kingdom based in Kerala. The Ay kingdom in the deep south and the Ezhimala kingdom in the north formed the other kingdoms in the early years of the Common Era (CE). The region had been a prominent spice exporter since 3000 BCE.[20] The region's prominence in trade was noted in the works of Pliny as well as the Periplus around 100 CE. In the 15th century, the spice trade attracted Portuguese traders to Kerala, and paved the way for European colonisation of India. At the time of Indian independence movement in the early 20th century, there were two major princely states in Kerala: Travancore and Cochin. They united to form the state of Thiru-Kochi in 1949. The Malabar region, in the northern part of Kerala, had been a part of the Madras province of British India, which later became a part of the Madras State post-independence. After the States Reorganisation Act, 1956, the modern-day state of Kerala was formed by merging the Malabar district of Madras State (excluding Gudalur taluk of Nilgiris district, Lakshadweep Islands, Topslip, the Attappadi Forest east of Anakatti), the taluk of Kasaragod (now Kasaragod District) in South Canara, and the erstwhile state of Thiru-Kochi (excluding four southern taluks of Kanyakumari district, and Shenkottai taluks).[17]

# Kerala has the lowest positive population growth rate in India, 3.44%; the highest Human Development Index (HDI), 0.784 in 2018 (0.712 in 2015); the highest literacy rate, 96.2% in the 2018 literacy survey conducted by the National Statistical Office, India;[10] the highest life expectancy, 77.3 years; and the highest sex ratio, 1,084 women per 1,000 men. Kerala is the least impoverished state in India according to NITI Aayog's Sustainable Development Goals dashboard and Reserve Bank of India's 'Handbook of Statistics on Indian Economy'.[21][22] Kerala is the second-most urbanised major state in the country with 47.7% urban population according to the 2011 Census of India.[23] The state topped in the country to achieve the Sustainable Development Goals according to the annual report of NITI Aayog published in 2019.[24] The state has the highest media exposure in India with newspapers publishing in nine languages, mainly Malayalam and sometimes English. Hinduism is practised by more than half of the population, followed by Islam and Christianity.

# In 2019–20, the economy of Kerala was the 8th-largest in India with ₹8.55 trillion (US$100 billion) in gross state domestic product (GSDP) and a per capita net state domestic product of ₹222,000 (US$2,700).[25] In 2019–20, the tertiary sector contributed around 65% to state's GSVA, while the primary sector contributed only 8%.[26] The state has witnessed significant emigration, especially to the Arab states of the Persian Gulf during the Gulf Boom of the 1970s and early 1980s, and its economy depends significantly on remittances from a large Malayali expatriate community. The production of pepper and natural rubber contributes significantly to the total national output. In the agricultural sector, coconut, tea, coffee, cashew and spices are important. The state is situated between Arabian Sea to the west and Western Ghats mountain ranges to the east. The state's coastline extends for 595 kilometres (370 mi), and around 1.1 million people in the state are dependent on the fishery industry, which contributes 3% to the state's income. Named as one of the ten paradises of the world by National Geographic Traveler,[27] Kerala is one of the prominent tourist destinations of India, with coconut-lined sandy beaches, backwaters, hill stations, Ayurvedic tourism and tropical greenery as its major attractions.
# """

# print(prediction_pipeline(text1))
