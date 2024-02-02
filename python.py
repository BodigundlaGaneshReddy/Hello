import requests
import xmltodict
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
 
# Fetch XML file from Jenkins
jenkins_url = 'http://3.85.83.67:8080/job/Hello/15/execution/node/3/ws/cppcheck-results.xml'
xml_data = requests.get(jenkins_url).content
 
# Parse XML
parsed_xml = xmltodict.parse(xml_data)
 
# Extract metrics from parsed XML (this part depends on your XML structure and needs)
# ...
 
# Prometheus Pushgateway setup
pushgateway_url = '3.85.83.67:9090'
registry = CollectorRegistry()
 
# Define your metrics
g = Gauge('cppcheck_metric', 'Description of your metric', registry=registry)
 
# Set metric (example)
g.set(123)  # Set this based on your actual metric
 
# Push to Pushgateway
push_to_gateway(pushgateway_url, job='cppcheck_job', registry=registry)