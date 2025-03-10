#import json
#import traceback

'''from model_configurations import get_model_configuration'''

#from langchain_openai import AzureChatOpenAI
#from langchain_core.messages import HumanMessage

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
#from rich import print as pprint

'''
gpt_chat_version = 'gpt-4o'
gpt_config = get_model_configuration(gpt_chat_version)

llm = AzureChatOpenAI(
        model=gpt_config['model_name'],
        deployment_name=gpt_config['deployment_name'],
        openai_api_key=gpt_config['api_key'],
        openai_api_version=gpt_config['api_version'],
        azure_endpoint=gpt_config['api_base'],
        temperature=gpt_config['temperature']
)
'''
q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = text_splitter.split_documents(docs)
    return chunks[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    full_text = ''
    for docs_element in docs:
        full_text += docs_element.page_content + '\n'
    text_splitter = RecursiveCharacterTextSplitter(separators=['法規名稱.*\n修正日期：.*\n','第.*[0-9]*-*[0-9]*.*條\n','第 .* 章.*\n'],
                                                    chunk_size = 1,
                                                    is_separator_regex = True,
                                                    chunk_overlap=0)
    chunks = text_splitter.split_text(full_text)
    return len(chunks)
    #pprint(chunks)