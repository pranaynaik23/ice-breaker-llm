from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import AzureChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile

if __name__ ==  "__main__":

# Load environment variables from .env file
    load_dotenv()

    print("Hello Langchain")



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
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/pranaynaik/"
    )
    res = chain.invoke(input={"information": linkedin_data})
    print("Summary:/n", res)