# DSA210 Project - Umut Can Çubukçu  
## How Matchdays and Their Results Affect My Daily Activity Levels


**Sabancı University DSA210 Introduction to Data Science Course**  
**Fall 2024-2025 Term Project**  

Hi, my name is **Umut Can Çubukçu (Student ID: 32453)**.  
My project focuses on analyzing my daily step count data to explore how matchdays for the team I support, along with the outcomes of those matches, influence my physical activity levels compared to non-matchdays. 

---
  
### **MOTIVATION**  
I am passionate about understanding how my emotions and interests influence my daily habits. Matchdays for the team I support bring a unique mix of excitement and anticipation, and the outcome of these matches;as a win, loss, or draw can make these feelings stronger or weaker. This project aims to explore whether the emotional highs and lows associated with matchdays and their results have a measurable impact on my physical activity, as reflected in my step count data. By analyzing these patterns, I will aim to gain insights into how emotionally charged events shape my behavior and routine.    

---
### Hypothesis

I hypothesize that on matchdays, my step count will increase compared to regular days due to the excitement and energy associated with supporting my team. Additionally, I expect my step count to be higher on matchdays when my team wins, as positive emotions may encourage more physical activity, and lower on matchdays when my team loses, as negative emotions could result in reduced activity levels.

---

### **Plan**

#### **Data Collection (Early December 2024):**
- Parsing match data from the Transfermarkt website by using web scraping techniques.  
- Extracting and organizing relevant variables such as match dates and results into a structured format for analysis.  
- Collecting daily step count data from the mobile phone’s health app.  

#### **Data Cleaning (Mid-December 2024):**
- Ensuring match records are complete and accurate.  
- Standardizing data formats for dates and step counts to ensure consistency across datasets.  

#### **Exploratory Data Analysis (EDA) (Mid to Late December 2024):**
- Visualizing trends in daily step counts across matchdays and non-matchdays.  
- Analyzing how step counts vary based on match outcomes.  
- Calculating descriptive statistics such as average, minimum, and maximum step counts for matchdays versus non-matchdays.
  
#### **Hypothesis Testing**
To assess whether "Matchdays and match outcomes influence my daily step count:"

- **(H₀):** Matchdays and match outcomes do not have a significant impact on my daily step count.  
- **(H₁):** Matchdays and match outcomes have a significant impact on my daily step count, with increased steps on matchdays and more steps on wins compared to losses. 

#### **Modeling and Analysis (Late December 2024 to Early January 2025):**
- Using statistical methods to evaluate the relationship between matchdays, match outcomes, and daily step counts.  
- Investigating the influence of factors like venue (home/away) or match importance on activity levels.  
- Making predictions about expected step counts on future matchdays based on past trends.  

#### **Final Review and Submission (Early January 2025):**
- Reviewing all findings, visualizations, and insights.   


---



## **Data Source**
I will collect step count data from my mobile phone's health app and gather matchday information using the website Transfermarkt. 
### **Match Data**

The match data used in this project will be sourced from Transfermarkt, specifically the match schedule and results for **Fenerbahçe Istanbul**. You can access the data at the following link:

[Transfermarkt Fenerbahçe Match Schedule](https://www.transfermarkt.com.tr/fenerbahce-istanbul/spielplandatum/verein/36)

### Example Image

Here is an sample image showing the matches played until **September 15, 2024**:

<img src="https://github.com/user-attachments/assets/ae74b7bd-3d9b-427c-9a18-84fb4173667e" alt="Match Schedule" width="700"/>

### Dataset Overview

The dataset contains match-related information for the football team, structured in a table format. Key variables include:

- **Date:** The date the match took place.  
- **Match Results:** The outcome of each match, represented as the final score .  

Other details in the dataset include:  
- **Competition Type:** Whether the match is part of a league or an international tournament.  
- **Opponent Team:** The name of the opposing team.  
- **Venue:** Indicates if the match was played at home or away.  
- **Attendance Numbers:** The number of spectators present at the match.  
- **Formation:** The tactical setup used during the match.  

For the purpose of this project, I will focus on extracting and analyzing the **Date** and **Match Results** columns. These variables will be used to investigate the relationship between matchdays, match outcomes, and my daily step count data.

## **Step Count Data**

The step count data used in this project is collected from the **Apple's health app**, which tracks the number of steps taken on a daily basis. 

The example image from my iPhone is below.

<img src="https://github.com/user-attachments/assets/e8600d9a-1f9e-4b75-a9c1-df27de619608" alt="Step Count Data" width="400"/>




### Dataset Overview

The dataset consists of daily step count data, structured in a table format with the following key variables:

- **Date:** The date on which the step count was recorded .  
- **Steps:** The total number of steps taken on that particular day.
  
---

## **Data Collection Method**

-To collect the relevant match data, I will parse the HTML page of the match schedule for **Fenerbahçe Istanbul** using web scraping techniques. Specifically, I will extract the **Date** and **Match Results** for each match to use in the analysis.

-Step count data will be collected using Apple's Health app, which automatically tracks and logs daily steps.The step data will be extracted from a xml file requested from Apple using Python library BeatifulSoup to parse xml file,finding Step count data from that file.

##FUTURE WORK
Our analysis showed that on matchdays, I tend to walk slightly less compared to usual days. Although the p-value is greater than 0.05, indicating that the difference is not statistically significant, there is still a noticeable variation in step counts. To explore this further, we could investigate factors that may contribute to this trend, such as screen time. Including such variables in future analyses could provide insights into whether increased screen time on matchdays is linked to reduced physical activity.

Additionally, when comparing step counts between days after a win and usual days, we observed a significant difference. Specifically, my step count tends to be lower on days following a matchday with a win. This finding warrants further investigation to understand the potential psychological or behavioral factors influencing this pattern, and whether other external factors could be contributing to this discrepancy.

