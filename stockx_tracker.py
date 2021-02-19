from stockx_scraper import (stockx_scraper, stockx_page_finder, stockx_page_scraper)
import csv

class stockx_tracker:

	DETAILS_FILE = 'details.csv'

	def __init__(self, stockx_scraper):
		self.__stockx_scraper = stockx_scraper

	def track(self, product, size):
		details = self.__stockx_scraper.get_product_info(product)

		with open(self.DETAILS_FILE, mode='a') as csv_file:
			csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'size', 'price'])
			csv_writer.writerow({'name' : details['product-name'], 'size' : size, 'price' : details['prices'][size]})

if __name__ == '__main__':
	from time import sleep

	tracker = stockx_tracker(stockx_scraper(stockx_page_finder(), stockx_page_scraper()))

	while True:
		tracker.track('Yeezy 350 V2 Bred', '10')
		sleep(3600)