# Data File Converter
Converts a csv file to json and xml.

### 11/15/17

### Natalie Ramirez

## Project Description
The purpose of this project was to read in a `csv` file that contained bootcamp graduate data and convert the data in that file into `json` and `xml` formats.

### Tools Used
- python
- python libs csv, json
- vs code

### Data Details
**Data Source** - `csv` clean file (data/bootcamp_data.csv)<br/>
**Data Output** - `json` formatted file (data/bootcamp_data.json)<br/>
**Data Output** - `xml` formatted file (data/bootcamp_data.xml)<br />
**Data Dictionary** - `xlxs` spreadsheet(data_dictionary.xlxs)

### Scripts
**JSON Converter Script**(scripts/convert_to_json.py)<br />
**XML Converter Script** (scripts/convert_to_xml.py)<br />

### Key Findings
- Reporting data for technical bootcamps has only been reported since 16. So being that it is fairly new and unstructured it was hard to find consistent data.
- Most data that had been reported by bootcamps was in `pdf` forms online reported by [CIRR](https://cirr.org/data). 
- Generating scripts for conversion was pretty simple. Structuring the data was the difficult and time consuming part.

### Methods
#### Understanding the data:
- Since the data was in pdfs, I had to convert the file to csv using an online converter and downloading the csv file.
- After looking at the data, I realized it was unstructured and had categories within fields.

#### Structuring the data
- Since the data was inconsistant, I had to do some manual cleansing to consolidate all the schools.
- I created codes for fields and grouping.
- I also created a data dictionary to show what each code represents.

#### Creating scripts:
- The only two libraries I needed for this project were the python csv library and json library.
- The difficulty in generating the scripts came with formatting the output. Using built in methods and trial and error, I was able to create the format I wanted.

### Conclusion








