from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import AzureChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent



def ice_break_with(name: str) -> str:

    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    # Create LLM API
    llm = AzureChatOpenAI(model="gpt-35",
    api_version="2023-03-15-preview",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )

# Define the prompt template
    summary_template = """
        given the information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_template)

# Generate summary using LCEL
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": linkedin_data})
    print("Summary:/n", res)

if __name__ ==  "__main__":

# Load environment variables from .env file
    load_dotenv()
    ice_break_with(name="Pranay Naik TCS")