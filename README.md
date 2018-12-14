## h1b statistics 

## Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify **the occupations and states with the most number of approved H1B visas**. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data.]( https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis)But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years.

The goal of this project is to create a mechanism to analyze past years data, specifically calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications. 

## Approach

### Pre-requisites
[Python 3.6](https://www.python.org/downloads/release/python-360/)
### Step 0: Parse input arguments
Using `argparse` define and parse required and optional arguments. 


### Step 1: Process csv Data for extracting required information
1. Read and process each row to get the occupation and state columns for applications with certified case status (e.g. if we are interested to know about CASE_STATUS = 'CERTIFIED' applications),
2. Maintain the information about occupation and states in two dictionaries:
  * occupation_status_count dictionary: 
    * key: occupation
    * value: count
  * state_status_count dictionary:
    * key: state
    * value: count
3. As we have to look at all the applications before returning the dictionaries, the run time and space complexity for this method would be O(N)


### Step 2: Get the top (k=10) occupations and states with certified applicants
This step is taken care by a helper method `get_topk_metrics`
1. `get_topk_metrics(dictionary with aggregated values, k)`: 
Given two dictionaries with key-value pair as (string, integer) and an integer k, return a list of frequent `k` key-value pairs sorted by value in descending order. Break the ties by alphabetical order.
2. I used minheap to get top k elements from the occupation and state counter dictionaries

### Step 3: Writing results to the output files
In this step output for top 10 occupations and top 10 states is written into respective files.
1. `output_data(args, output_file_path, top_k_results,
                            total_status_count,
                            output_columns)`: 
                            write given list of tuples to the given output file path with given output_columns names

## Run Instructions
1. Place the input file in the `input` folder and name it as `h1b_input.csv`
2. Place the required tests in the `insight_testsuite folder`
3. Run `./run.sh` command to start the program  
4. Program takes four mandatory arguments: program name, input file path and two output file paths. <br></br>
To run: <br></br>
`python3 ./src/h1b_counting.py  -i inputfilepath  -o1 output1filepath -o2 output2filepath` <br></br>
Example: <br></br>
`python3 ./src/h1b_counting.py  -i ./input/h1b_input.csv  -o1 ./output/top_10_occupations.txt -o2 ./output/top_10_states.txt` <br></br>
5. There will be two files the output folder:
  * top_10_occupations.txt - the file containing top 10 occupations for certified visa applications
  * top_10_states.txt - the file containing top 10 states for certified visa applications
