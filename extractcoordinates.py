import xml.etree.ElementTree as ET
with open("locations.xml", "a") as myfile:
	myfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<places>")
tree = ET.parse('map1.osm')
root = tree.getroot()
placename = ''
placenodeid = ''
placecoordlat = ''
placecoordlon = ''
avoidduplicates = []

for group in root:
	for child in group.iter('tag'):
		if child.get('k') == 'name':
			placename = child.get('v')
			if group.get('lat') is not None:
				if placename in avoidduplicates:
					print placename
					break
				else:
					avoidduplicates.append(placename)
					placecoordlat = group.get('lat')
					placecoordlon = group.get('lon')
					with open("locations.xml", "a") as myfile:
						myfile.write("\n<place>\n" + "<name>" + placename + "</name>\n" + "<latitude>" + placecoordlat + "</latitude>\n" + "<longitude>" + placecoordlon + "</longitude>\n" + "</place>")
for group in root:
	for child in group.iter('tag'):
		if child.get('k') == 'name':
			placename = child.get('v')
			for child in group.iter('nd'):
				if child.get('ref') is not None:
					if placename in avoidduplicates:
						print placename
						break
					else:
						placenodeid = child.get('ref')
						for node in root.iter('node'):
							if node.get('id') == placenodeid:
								placecoordlat = node.get('lat')
								placecoordlon = node.get('lon')
								with open("locations.xml", "a") as myfile:
									myfile.write("\n<place>\n" + "<name>" + placename + "</name>\n" + "<latitude>" + placecoordlat + "</latitude>\n" + "<longitude>" + placecoordlon + "</longitude>\n" + "</place>")
						break
tree = ET.parse('map2.osm')
root = tree.getroot()
placename = ''
placenodeid = ''
placecoordlat = ''
placecoordlon = ''

for group in root:
	for child in group.iter('tag'):
		if child.get('k') == 'name':
			placename = child.get('v')
			if group.get('lat') is not None:
				if placename in avoidduplicates:
					print placename
					break
				else:
					avoidduplicates.append(placename)
					placecoordlat = group.get('lat')
					placecoordlon = group.get('lon')
					with open("locations.xml", "a") as myfile:
						myfile.write("\n<place>\n" + "<name>" + placename + "</name>\n" + "<latitude>" + placecoordlat + "</latitude>\n" + "<longitude>" + placecoordlon + "</longitude>\n" + "</place>")
for group in root:
	for child in group.iter('tag'):
		if child.get('k') == 'name':
			placename = child.get('v')
			for child in group.iter('nd'):
				if child.get('ref') is not None:
					if placename in avoidduplicates:
						print placename
						break
					else:
						placenodeid = child.get('ref')
						for node in root.iter('node'):
							if node.get('id') == placenodeid:
								placecoordlat = node.get('lat')
								placecoordlon = node.get('lon')
								with open("locations.xml", "a") as myfile:
									myfile.write("\n<place>\n" + "<name>" + placename + "</name>\n" + "<latitude>" + placecoordlat + "</latitude>\n" + "<longitude>" + placecoordlon + "</longitude>\n" + "</place>")
						break
tree = ET.parse('map3.osm')
root = tree.getroot()
placename = ''
placenodeid = ''
placecoordlat = ''
placecoordlon = ''

for group in root:
	for child in group.iter('tag'):
		if child.get('k') == 'name':
			placename = child.get('v')
			if group.get('lat') is not None:
				if placename in avoidduplicates:
					print placename
					break
				else:
					avoidduplicates.append(placename)
					placecoordlat = group.get('lat')
					placecoordlon = group.get('lon')
					with open("locations.xml", "a") as myfile:
						myfile.write("\n<place>\n" + "<name>" + placename + "</name>\n" + "<latitude>" + placecoordlat + "</latitude>\n" + "<longitude>" + placecoordlon + "</longitude>\n" + "</place>")
for group in root:
	for child in group.iter('tag'):
		if child.get('k') == 'name':
			placename = child.get('v')
			for child in group.iter('nd'):
				if child.get('ref') is not None:
					if placename in avoidduplicates:
						print placename
						break
					else:
						placenodeid = child.get('ref')
						for node in root.iter('node'):
							if node.get('id') == placenodeid:
								placecoordlat = node.get('lat')
								placecoordlon = node.get('lon')
								with open("locations.xml", "a") as myfile:
									myfile.write("\n<place>\n" + "<name>" + placename + "</name>\n" + "<latitude>" + placecoordlat + "</latitude>\n" + "<longitude>" + placecoordlon + "</longitude>\n" + "</place>")
						break
with open("locations.xml", "a") as myfile:
	myfile.write("\n</places>")		
		
			
