from concurrent.futures import ThreadPoolExecutor

from constants import REGIONS
from data_collector.collector import DataCollector
from data_processor.processor import DataProcessor

with ThreadPoolExecutor(len(REGIONS)) as executor:
    results = executor.map(
        DataCollector.region_offers,
        (DataCollector(region) for region in REGIONS)
    )

for region, result in zip(REGIONS, results):
    instanse = DataProcessor(region, result)
    instanse.create_heat_map()
    instanse.create_average_price_graph()
    instanse.create_average_area_graph()
