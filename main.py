import requests
import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


def get_available_domain_names():
    response = requests.get("http://localhost:8080/api/scrape")
    json_data = json.loads(response.text)
    return json_data


def get_scrape_results(domain_names):
    responses = map(lambda domain_name: requests.post("http://localhost:8080/api/scrape", json={"path": domain_name}),
                    domain_names)
    result = map(lambda response: json.loads(response.text), responses)
    return result


def identify_industry(scrape_results):
    tokenizer = AutoTokenizer.from_pretrained("sampathkethineedi/industry-classification")
    model = AutoModelForSequenceClassification.from_pretrained("sampathkethineedi/industry-classification")
    industry_tags = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
    model_results = [{scrape_result["name"]: industry_tags(scrape_result["description"])} for scrape_result in scrape_results]
    return model_results


domain_names = get_available_domain_names()

scrape_results = get_scrape_results(domain_names)

model_results = identify_industry(scrape_results)

print(model_results)
