import csv
import logging
import yaml


logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

#FUNCTION FOR READ FILE FROM CSV
def read_emails(file_path: str) -> list:
    emails = []
    try:
        with open(file_path, mode = 'r', encoding= 'utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                emails.append(row['email_address'])
        logging.info(f"The email have load {len(emails)} list.")
        return emails
    except Exception as e:
        logging.error(f"error to read file: {e}")
        return []
    

#FUNCTION FOR WRITE THE RESULT TO CSV FILE    
def write_results(file_path: str, results: list):
    email_key = 'email_address'.ljust(35)
    breach_key = 'breached'.ljust(10)
    site_key = 'site_where_breached'
    fieldnames = [email_key, breach_key, site_key]
    try:
        with open(file_path, mode= 'w', newline= '', encoding= 'utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames) 
            writer.writeheader() 
            formatted_rows = []
            for row in results: 
                formatted_rows.append({
                    email_key: row['email_address'].ljust(35),
                    breach_key:("Y" if row["breached"] else "N").ljust(10),
                    site_key: (
                        "; ".join(row["site_where_breached"])
                        if isinstance(row["site_where_breached"],list)
                        else row["site_where_breached"]
                    )
                })
            writer.writerows(formatted_rows)
        logging.info(f"save the result in {file_path} successful.")
    
    except Exception as e:
        logging.error(f"can not write file: {e}")

#TEST BASIC PERFORMANCE
if __name__ == "__main__":
    #test read file
    data = read_emails('email_list.csv')
    print(f'Email: {data}')

    #test reading result for prepare to write a file
    sample_results = [
        {'email_address': 'customer1@example.com', 'breached': True, 'site_where_breached': 'Adobe; LinkedIn'},
        {'email_address': 'secure-user@alc.com', 'breached': False, 'site_where_breached': ''}
    ]
    write_results('output_result.csv', sample_results)

#function for read YAML
def load_config(config_path: str = 'config.yaml') -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)