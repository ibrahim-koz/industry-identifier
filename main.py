import requests
import json


def get_available_domain_names():
    response = requests.get("http://localhost:8080/api/scrape")
    json_data = json.loads(response.text)
    return json_data


def get_scrape_results(domain_names):
    responses = map(lambda domain_name: requests.post("http://localhost:8080/api/scrape", json={"path": domain_name}),
                    domain_names)
    result = map(lambda response: json.loads(response.text), responses)
    return result



domain_names = get_available_domain_names()
print(list(get_scrape_results(domain_names)))

# print(requests.post("http://localhost:8080/api/scrape", json={"path": "https://slack.com/"}).text)
#
# tokenizer = AutoTokenizer.from_pretrained("sampathkethineedi/industry-classification")
# model = AutoModelForSequenceClassification.from_pretrained("sampathkethineedi/industry-classification")
#
# industry_tags = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
# industry_tags(
#     "Stellar Capital Services Limited is an India-based non-banking financial company ... loan against property, management consultancy, personal loans and unsecured loans.")
#
# '''Ouput'''
# [{'label': 'Consumer Finance', 'score': 0.9841355681419373}]
