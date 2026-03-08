import logging
import os 
import asyncio
import httpx
from src.processor import read_emails, write_results
from src.api_client import BreachDirectoryClient


#setup logging config
logging.basicConfig(
    level= logging.INFO,
    format= '%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("logs/alc_scanner.log"), #save in file
        logging.StreamHandler() #display on monitor
    ],
    force= True
)

async def run_app():
    logging.info("--- Begining ALC Risk Assessment Tool System ")
    
    #LODING
    input_file = 'email_list.csv'
    emails = read_emails(input_file)

    if not emails:
        logging.error("Don't have detail of email to tested")
        return
    #Begining API client
    client = BreachDirectoryClient()

    async with httpx.AsyncClient() as http_client:
        logging.info(f"Starting async check for {len(emails)} email...")

        tasks = [client.check_breach(http_client, email)for email in emails]

        final_results = await asyncio.gather(*tasks)

    # #looping test each email
    # for email in emails:
    #     result = client.check_breach(email)
    #     final_results.append(result)

    #save the result
    output_file = 'output_result.csv'
    write_results(output_file, final_results)

    logging.info(f" Testing is successful, Check result at {output_file}")

if __name__ == "__main__":
    asyncio.run(run_app())        
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     