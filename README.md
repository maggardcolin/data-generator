# Data Generator

## Overview

- This program prompts the user for statistical parameters such as the intended average, standard deviation, number of data points, and other specifications.
- The main loop body involves determining the "differential" of each point, indicating how far it is from the desired mean value.
- Intermediary calculations and factors from previous iterations are considered in the loop.
- The program updates a value called "leftovers," representing the amount of "pull" needed to balance the data points around the desired mean.
- Generated points are appended to an array until all data points are created.
- The program offers a file output option to save the generated data.

## Goal

- The aim of this app is to generate a set of numbers based on user-specified statistical parameters, specifically mean and standard deviation.
- Options include controlling precision (number of decimal places), the number of points generated, and maximum allowable error.
- I created this in Spring 2022, this project played a role in sparking my interest in programming and pursuing further education in the field.

## How it Works

- The user provides intended statistical parameters.
- The program calculates intermediary values and factors for each data point.
- A main loop creates data points, ensuring they adhere to the specified statistical parameters.
- Options for precision, number of points, and permissible error are considered.

## Usage

- Users can run the program to generate mock numerical data based on specific statistical criteria.
- File output option available for saving the generated data.

Feel free to explore the code associated with this project by checking out the repository.
