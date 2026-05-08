# Apify AI Agent Deployment and Monetization Guide

This guide provides step-by-step instructions for deploying your **AI-Powered Sales Lead Enrichment Agent** to the Apify Store and setting up its monetization.

## 1. Deployment Package Overview

Your AI agent is packaged with the following files:

*   `main.py`: The core Python script containing the agent's logic.
*   `INPUT_SCHEMA.json`: Defines the input fields for your agent, which Apify uses to generate a user-friendly interface.
*   `Dockerfile`: Specifies the environment and dependencies required to run your Python agent on the Apify platform.
*   `requirements.txt`: Lists the Python libraries your agent depends on (e.g., `apify-client`, `openai`).

## 2. Deploying Your Agent to Apify

To deploy your agent, you will need an Apify account and the Apify CLI installed. If you don't have them, follow the instructions on the [Apify website](https://apify.com/docs/cli) to set them up.

1.  **Log in to Apify CLI**: Open your terminal and run:
    ```bash
    apify login
    ```
    Follow the prompts to log in with your Apify account.

2.  **Initialize a New Actor**: Navigate to the directory containing your agent files (`main.py`, `INPUT_SCHEMA.json`, `Dockerfile`, `requirements.txt`) and run:
    ```bash
    apify init my-sales-lead-agent
    ```
    Choose `Python` as the language and `Actor` as the type. This will create a new directory `my-sales-lead-agent` with a basic structure. You will then copy your prepared files into this new directory, overwriting the default ones.

3.  **Copy Your Agent Files**: Copy `main.py`, `INPUT_SCHEMA.json`, `Dockerfile`, and `requirements.txt` into the `my-sales-lead-agent` directory.

4.  **Deploy Your Actor**: Navigate into the `my-sales-lead-agent` directory and run:
    ```bash
    apify push
    ```
    This command will upload your code to the Apify platform and build your Actor. You can monitor the build process in the Apify Console.

## 3. Setting Up Monetization

Once your Actor is deployed and successfully built, you can enable monetization through the Apify Console.

1.  **Navigate to Your Actor**: Go to the Apify Console, find your `my-sales-lead-agent` Actor, and click on it.

2.  **Enable Monetization**: In the Actor's settings, look for the 
‘Monetization’ tab or section. Here you can:
    *   **Choose a Pricing Model**: Apify typically offers a pay-per-use model. You can set the price per successful run or per unit of data processed.
    *   **Set Pricing Tiers**: Offer different pricing based on usage volume.
    *   **Add a Description**: Write a compelling description for your agent, highlighting its benefits and use cases for potential customers.
    *   **Add Tags**: Use relevant tags to improve discoverability on the Apify Store.

3.  **Publish to Apify Store**: After configuring monetization, you can choose to publish your Actor to the Apify Store. This makes your agent publicly available for others to use and generates income for you.

## 4. Important Considerations

*   **API Keys**: If your agent uses external APIs (like OpenAI), ensure that API keys are handled securely. Apify allows you to store sensitive information as Actor secrets, which are not exposed in your code or logs.
*   **Error Handling**: Implement robust error handling in your `main.py` to gracefully manage issues like API rate limits, network errors, or unexpected data formats. This improves user experience and reduces support requests.
*   **Documentation**: Provide clear and concise documentation for your agent, explaining its inputs, outputs, and typical use cases. This will help users understand and effectively utilize your agent.
*   **Marketing**: Even with an automated agent, some marketing effort can significantly boost its visibility and usage. Consider sharing your agent on relevant forums, social media, or through your own network.

By following these steps, your **AI-Powered Sales Lead Enrichment Agent** will be live on the Apify Store, generating automated income as businesses leverage its capabilities.
