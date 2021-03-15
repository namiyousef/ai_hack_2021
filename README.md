# ai_hack_2021

Link to website: https://namiyousef.github.io/ai_hack_2021/

Link to blogpost: https://techcommunity.microsoft.com/t5/educator-developer-blog/mech-eng-defectors-a-hackathon-story-ai-hack-2021/ba-p/2178670

## Project Abstract

The Boston Housing Market dataset is ubiquitous but imperfect: with
problems like small size, inconsistent definitions, incorrect coordinates
and many many. However, it is still a very rich dataset containing
informative geographical information, powerful socioeconomic
indicators, and continuous levels of Nitrogen Oxides (NOx).
This report explores the effect of developing low income
neighbourhoods on NOx. This involves three logical steps: 1) Verifying
that the dataset is rich enough to form clusters of economic class, 2)
train a regressor for predicting NOx values, and finally 3) creating
synthetic data simulating ‘improved’ low income neighbourhoods by
bootstrapping values from higher income classes, while keeping
geographical constraints fixed.
The evidence suggests that improving low income neighbourhoods does
indeed decrease overall NOx levels, giving non-humanitarian reasons for
supporting social uplifting policy. This project also corrects erroneous
longitude and latitude values of the Boston dataset using Google’s
geocoder API.

## Contents of repository

### Files

- **environment.yml:** conda environment file to reproduce work

### Directories

- **PythonScripts:** a folder containing Python scripts used througout this project

- **data:** a folder containing data pertaining project (inlcuding images)

- **data_exploration:** a folder containing data exploration notebooks

- **modelling:** a folder containing modelling work (includes clustering)

- **reports:** a folder containing profile reports or actual project reports

- **UsefulDocs:** AI hack welcome info and links
