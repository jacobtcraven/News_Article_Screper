'''Main function for using and testing modules'''

## Import needed classes and functions
from module_1.RawData import RawData, InputOutput
from module_2.FormatData import FormatData


if __name__ == '__main__':
    ## Read the URLs from the file
    urls = InputOutput.read_urls('urls.txt')

    ## initialize counter for file naming
    counter = 1

    ## For each url, scrape the raw data, format it, and write it to a file
    for URL in urls:
        source = RawData.scrape(URL)

        ## Write html to raw file
        InputOutput.write_to_file(str(source), f'Data/raw/raw{counter}.txt')

        ## Format the raw file
        formatted = FormatData.remove_html(source)
        formatted = FormatData.add_newlines(formatted)

        ## Write the formatted file
        InputOutput.write_to_file(formatted, f'Data/processed/formatted{counter}.txt')

        ## Increment counter so next url can be scraped and written to a new file
        counter += 1