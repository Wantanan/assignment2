import logging
import time
import requests
import os
from dotenv import load_dotenv



load_dotenv()

class IntelXClient:
    def __init__(self):
        self.api_key = os.getenv("INTELLX_API_KEY")
        
        print(f"Debug: Intelligence X key length = {len(self.api_key) if self.api_key else 0}")
        
        self.base_url = "https://public.intelx.io"
        self.headers = {
            "x-key": self.api_key,
            "user-agent": "IX_Python-Test"
        }

    def check_breach(self, email: str) -> dict:
        logging.info(f"Checking Intelligence X for: {email}")

        #search request
        search_url = f"{self.base_url}/intelligent/search"
        payload = {
            "term" : email,
            "maxresults": 10,
            "target": 1
        }

        try:
            response = requests.post(search_url, json= payload, headers= self.headers, timeout=10)
            response.raise_for_status()
            search_id = response.json().get('id')
            
            if not search_id:
                return{
                    "email_address": email,
                    "breached":False,
                    "site_where_breached": "No search ID returned"
                }


            result_url = f"{self.base_url}/intelligent/search/result?id={search_id}"
            
            for _ in range(10):
                result_response = requests.get(result_url, headers=self.headers, timeout = 10)
                result_data = result_response.json()
                if result_data.get("status") == 2:
                    break

                time.sleep(1)

            records = result_data.get('record',[])
            is_breached = len(records)>0

            

            sites = "; ".join([r.get('name')for r in records if r.get('name')])

            return {
                "email_address": email,
                "breached" : is_breached,
                "site_where_breached": sites if is_breached else "No breach found"
            }
            
        except Exception as e:
            logging.error(f"API Error for {email}: {e}")
            return{
                "email_address": email,
                "breached": False,
                "site_where_breached": f"Error: {str(e)}"
            }