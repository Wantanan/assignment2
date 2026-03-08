import httpx
import logging
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

class BreachDirectoryClient:
    def __init__(self):
        self.api_key = os.getenv("BREACHDIRECTORY_API_KEY")
        self.host = os.getenv("BREACHDIRECTORY_HOST")
        print(f"Debug: BranchDirectory key length = {len(self.api_key) if self.api_key else 0}")
        
        self.base_url = "https://breachdirectory.p.rapidapi.com/"

        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.host
        }

    async def check_breach(self, client: httpx.AsyncClient,email: str) -> dict:
        logging.info(f"Checking BreachDirectory for: {email}")

        params = {
            "func" : "auto",
            "term" : email
        }

        try:
            response = await client.get(self.base_url, headers= self.headers, params= params, timeout=10, follow_redirects= True)
            response.raise_for_status()

            data = response.json()
            print("Debug BreachDirectory response", data)

            if not data.get("success", False):
                return {
                    "email_address": email,
                    "breached" : False,
                    "site_where_breached": f"API Error: {data.get('error', 'Unknown error')}"
                }
            
            results = data.get("result", 0)
            breached = len(results) > 0 

            if breached:
                sites = [item.get("sources", "Unknow") for item in results]
            else:
                sites = "No breach found"

            return{
                "email_address": email,
                "breached": breached,
                "site_where_breached": sites
            }
        
        except Exception as e:
            logging.error(f"BreachDirectory API Error for {email}: {e}")
            return{
                "email_address": email,
                "breached": False,
                "site_where_breached": f"Error: {str(e)}"
            }