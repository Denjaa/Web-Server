import pandas as pd
from source.common import dictGenerator, csvGenerator, headers


class CSV():

	def GBI(self, inputFile, outputFile, root):
		input_ = open(inputFile, 'r', encoding = 'UTF-8').readlines()
		outputName = str(root) + '\\downloads\\' + str(outputFile) + '.csv'

		print (str(root) + '\\downloads\\' + str(outputFile) + '.csv')
		output_ = open(outputName, 'w', encoding = 'UTF-8')

		entity = dictGenerator()

		for i in range(len(input_)):
			if i == 0:
				output_.write(headers(entity) + '\n')
			elif i != 0:
				line = input_[i]
				entity['cust_ref_text_2'] = line[0:11].replace(',', '')
				entity['DUNS'] = line[12:21].replace(',', '')
				entity['bus_name'] = line[21:91].replace(',', '')
				entity['address_line_1'] = line[91:155].replace(',', '')
				entity['city'] = line[155:185].replace(',', '')
				entity['territory'] = line[185:187].replace(',', '')
				entity['postal_code'] = line[187:196].replace(',', '')
				entity['countryISOAlpha'] = 'US'
				output_.write(csvGenerator(entity) + '\n')

		output_.close()
		return outputName





