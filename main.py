import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
from sklearn import svm

data = pd.read_csv("dataset employee.txt", sep = ",", header = None, skiprows = 1)
data.columns = ["Satisfaction level", "Last evaluation", "Projects finished", "Avg monthly hours", "Years at company", "Work accident", "Left", "Promotion", "Department", "Salary"]

    #satisfaction_level: Level of satisfaction {0–1}.
    #last_evaluationTime: Time since last performance evaluation (in years).
    #number_project: Number of projects completed while at work.
    #average_montly_hours: Average monthly hours at the workplace.
    #time_spend_company: Number of years spent in the company.
    #Work_accident: Whether the employee had a workplace accident.
    #left: Whether the employee left the workplace or not {0, 1}.
    #promotion_last_5years: Whether the employee was promoted in the last five years.
    #sales: Department the employee works for.
    #salary: Relative level of salary {low, medium, high}.

##################################### Employees leaving/staying at the company #########################################################

employees = len(data)
data_left = data.loc[data["Left"] == 1]
data_stay = data.loc[data["Left"] == 0]
employees_left = len(data_left)
employees_stay = len(data_stay)

def function_stay():

    lab = "Left", "Stayed"
    sizes = [len(data_left), len(data_stay)]
    colors = ["gold", "red"]

    plt.pie(sizes, labels = lab, colors = colors, autopct = "%1.1f%%", shadow = True, explode = (0.1, 0))

    plt.show()

    print("People that left: ", len(data_left))
    print("People that stayed: ", len(data.loc[data["Left"] == 0]))

#function_stay()


############################ Employee retention per Satisfaction level ############################

def function_satis():
    bins = [0, 0.5, 0.75, 1]
    labels = ["Low", "Medium", "High"]

    data["Sat class"] = pd.cut(data_left["Satisfaction level"], bins = bins, labels = labels)
    counts = data["Sat class"].value_counts()
    counts.plot(kind="bar", label = "Employees that left")
    plt.legend(loc="upper right")
    plt.title("Employee that left per Satisfaction level")
    plt.show()
    print ("Satisfaction level: \n", counts)


#function_satis()

############################ Employee retention per Promotion ############################

def function_promo():

    label = "Promoted", "Not promoted"
    sizes = [len(data.loc[data["Promotion"] == 1]) , len(data.loc[data["Promotion"] == 0])]
    plt.pie(sizes, labels=label,autopct="%1.1f%%", shadow = True, explode = (0.1,0))
    plt.show()
    print(len(data.loc[data["Promotion"] == 1]))
#function_promo()


############################ Employee retention per Department ############################



def function_department():

    data_dep = data_left.groupby("Department").count()["Left"].sort_values(ascending = False)
    deps = ["Sales", "Technical", "Support", "IT", "hr", "marketing", "product_mng", "accounting", "RandD", "management"]
    data_dep["% left"] = (data_dep / employees_left)

    val = data_dep.loc["% left"].values.tolist()

    newdf = pd.DataFrame({"Department" : deps, "%Left" : val})
    plt.pie(newdf["%Left"], autopct="%.2f%%", labels=deps, shadow = True, explode=(0.1, 0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1))
    plt.show()
    print(newdf)
#function_department()

############################ Employee retention per Years at the company ############################


def function_years():
    data_years = (data_left.groupby(['Years at company']).size()).reset_index()
    x = data_years.iloc[:,0].values.tolist()
    y = data_years.iloc[:,1].values.tolist()
    plt.bar(x, y, label="Employees that left", color="purple")
    for i in range(len(x)):
        plt.text(x = x[i]-0.2 , y = y[i], s = y[i], size = 18)
    plt.legend(loc="upper right")
    plt.title("Employee that left per years at company")
    plt.show()

#function_years()

############################ Employee retention per Salary ############################

def function_salary():
    data_salary = data_left.groupby(["Salary"]).size().sort_values(ascending = False).reset_index()
    x = data_salary.iloc[:,0].values.tolist()
    y = data_salary.iloc[:,1].values.tolist()
    plt.barh(x, y, color ="green", label="Employees that left")
    for index, value in enumerate(y):
        plt.text(value, index, str(value), size = 18)
    plt.legend(loc="upper right")
    plt.title("Employee that left per Salary")

    plt.show()

function_salary()











"""
data_dep = data_left.groupby("Department").count()["Left"].sort_values(ascending = False)#.plot(kind = "bar")
data_sal = data_left.groupby("Salary").count()["Left"].sort_values(ascending = False)#.plot(kind = "bar")
data_promo = data_left.groupby("Promotion").count()["Left"].sort_values(ascending = False)#.plot(kind = "bar")
data_acc = data_left.groupby("Work accident").count()["Left"].sort_values(ascending = False)#.plot(kind = "bar")
data_years = data_left.groupby("Years at company").count()["Left"].sort_values(ascending = False)#.plot(kind = "bar")
data_sat = data_left.groupby("Sat class").count()["Left"].sort_values(ascending = False)#.plot(kind = "bar")

"""
