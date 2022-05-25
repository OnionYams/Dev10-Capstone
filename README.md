# Dev10-Capstone

### Group Members: Alex, Isaac, Will, Yansong

Since all of our group members will be working at Northwestern Mutual, a large life insurance company, our primary goal was to learn more about this industry so that we're better prepared to work there. In doing so, we looked various stats about life insurance, such as why people do or do not buy life insurance and how many Americans have life insurance coverage among other things, compared some of these to the fairly similar field of health insurance, and made some visualizations to showcase our findings. Additionally, we found information on the costs of life insurance coverage, and looked into state life expectancies in the US to give some context as to why the prices changed as they did. We then tried create a machine learing model of our own to predict life expectancies based on the data that we found with middling results. Based on our model, the primary things determining life expectancy were not any sorts of demographic data, but rather median income and health insurance coverage, which isn't necessarily in line with conventional knowledge. For more information on our project and why it resulted in the way that it did, check out the Project Technical Report.



The primary documents for this project are found in the [main_project_files](main_project_files) folder, including a [PowerBI report](Boogaloo-Capstone-Visualizations.pbix), a [Powerpoint presentation](CapstonePresentationSlides.pdf), and a [Technical Report](ProjectTechnicalReport.pdf).

The Project Specifications folder contains a copy of the Project mangagement plan, an executive summary of the project, the Dataflow/Data Platform diagram, an erd of our tables and the various sources we used.

The code folder contains some copies of our machine learning model, SQL scripts that we used to create tables in our Azure SQL Database, and the automated code for getting our web data and performing the Kafka Consumer-Producer flow int bgl2-auto, as well as a few other Jupyter notebooks that were used to clean and create the various machine learning models found in the folder

For those with access, the database we used is boogaloo-capstone-human-life, and the data factory is boogaloo2-capstone
