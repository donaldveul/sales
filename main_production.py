import os
import json
import asyncio
from apify_client import ApifyClient
from openai import OpenAI

class SalesLeadEnrichmentAgent:
    def __init__(self, openai_api_key):
        # Initialize OpenAI client
        self.client = OpenAI(api_key=openai_api_key)

    async def enrich_lead(self, company_name, contact_person, industry=None, current_pain_point=None):
        """
        Uses AI to synthesize insights and draft a personalized outreach email.
        """
        print(f"Enriching lead for {contact_person} at {company_name} using AI...")

        # Construct a high-quality prompt for the AI
        prompt = f"""
        You are a world-class sales development representative (SDR).
        
        TASK:
        Research the company '{company_name}' and the contact person '{contact_person}'.
        Industry: {industry if industry else 'General Business'}
        Known Pain Point: {current_pain_point if current_pain_point else 'Unknown'}

        1. Synthesize 3 key business insights about this company and person.
        2. Draft a highly personalized, short outreach email (max 150 words).
        3. The email should focus on how an AI Automation service could help them.
        4. Use a professional yet conversational tone. No generic 'I hope this finds you well' intros.

        FORMAT:
        Return your response as a JSON object with two keys: 'insights' (a list of 3 strings) and 'email_draft' (a string).
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "You are a sales expert."}, {"role": "user", "content": prompt}],
                response_format={ "type": "json_object" }
            )
            ai_data = json.loads(response.choices[0].message.content)
            
            return {
                "company_name": company_name,
                "contact_person": contact_person,
                "industry": industry,
                "ai_generated_insights": ai_data.get("insights", []),
                "personalized_email": ai_data.get("email_draft", ""),
                "status": "Success"
            }
        except Exception as e:
            return {"status": "Error", "message": str(e)}

async def main():
    # Initialize the ApifyClient with the API token
    client = ApifyClient(os.environ["APIFY_TOKEN"])

    # Get the Actor input
    actor_input = await client.key_value_store("default").get_record("INPUT")
    if not actor_input or not actor_input.get("value"):
        print("No input found!")
        return
    
    data = actor_input["value"]
    
    # Get OpenAI API Key from Environment Variables
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        await client.push_data({"status": "Error", "message": "Missing OPENAI_API_KEY in environment variables."})
        return

    agent = SalesLeadEnrichmentAgent(openai_key)

    # Run the enrichment
    result = await agent.enrich_lead(
        company_name=data.get("company_name"),
        contact_person=data.get("contact_person"),
        industry=data.get("industry"),
        current_pain_point=data.get("current_pain_point")
    )

    # Push the result to the dataset
    await client.dataset("default").push_items([result])
    print("Lead enrichment complete!")

if __name__ == "__main__":
    asyncio.run(main())
