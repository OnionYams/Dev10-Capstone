import pandas as pd
import pymssql
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from joblib import dump,load

database = "boogaloo-capstone-human-life"
tableLE_All="dbo.Model_Data"
user = "bglcap"
password  = "48Gheq0Iz9t"
server = "gen10-data-fundamentals-22-02-sql-server.database.windows.net"


conn=pymssql.connect(server,user,password,database)
cursor=conn.cursor()
query=f"SELECT * FROM {tableLE_All}"
Model_Data=pd.read_sql(query,conn)

LE_restricted_Data_pandas=Model_Data[["Male","White","Black or African American","American Indian and Alaska Native","Asian","Native Hawaiian and other Pacific Islander","Other","Multiracial","Hispanic or Latino","Median Household Income","Percent Insured","Life Expectancy"]]
LE_restricted_Data_pandas["Median Household Income"]=LE_restricted_Data_pandas["Median Household Income"]/100000.0

LE_restricted_dep=LE_restricted_Data_pandas["Life Expectancy"]
LE_restricted_ind=LE_restricted_Data_pandas.drop(columns={"Life Expectancy"},inplace=False)


ss = StandardScaler()
zscore_restricted = ss.fit_transform(LE_restricted_ind)
LE_restricted_ind_normalized = pd.DataFrame(zscore_restricted, columns=LE_restricted_ind.columns.tolist())


X1_train, X1_test, y1_train, y1_test = train_test_split(LE_restricted_ind_normalized, LE_restricted_dep,random_state=42)

normal_lin_reg = LinearRegression().fit(X1_train, y1_train)
print("No Female Data normalized")
print(normal_lin_reg.score(X1_test,y1_test))
restricted_normal_coefficients_list=normal_lin_reg.coef_
print(restricted_normal_coefficients_list)
print("--------")

svr = SVR().fit(X1_train, y1_train)
svr_predictions=svr.predict(X1_test)
print("non-tuned SVR")
print(svr.score(X1_test,y1_test))
print("--------")


svr_restricted_param_grid = {'C': [ 10,11,12,13,14,15], 
              'gamma': [.1,.15,.2,.25,.3,.35],
              'kernel': ['rbf'],
              'epsilon':[.1,.15,.2,.25,.3]}   
ml = svm.SVR()
svr_restricted_grid = GridSearchCV(ml, svr_restricted_param_grid, refit = True, verbose = 1,cv=5)
  
# fitting the model for grid search
svr_tuned=svr_restricted_grid.fit(X1_train, y1_train)
print("No Female Data SVR")
print(svr_tuned.best_params_)
svr_restricted_predictions=svr_tuned.predict(X1_test)
print(svr_tuned.score(X1_test,y1_test))
print("--------")

LE_demographic_Data_pandas=Model_Data[["Male","White","Black or African American","American Indian and Alaska Native","Asian","Native Hawaiian and other Pacific Islander","Other","Multiracial","Hispanic or Latino","Life Expectancy"]]
LE_demographic_dep=LE_demographic_Data_pandas["Life Expectancy"]
LE_demographic_ind=LE_demographic_Data_pandas.drop(columns={"Life Expectancy"},inplace=False)

zscore_demographic = ss.fit_transform(LE_demographic_ind)
LE_demographic_ind_normalized = pd.DataFrame(zscore_demographic, columns=LE_demographic_ind.columns.tolist())

X2_train, X2_test, y2_train, y2_test = train_test_split(LE_demographic_ind_normalized, LE_demographic_dep,random_state=42)

demographic_lin_reg = LinearRegression().fit(X2_train, y2_train)
normal_demo_score=demographic_lin_reg.score(X2_test,y2_test)
print("normal demo only")
print(normal_demo_score)
demographic_normal_coefficients_list=demographic_lin_reg.coef_
print(demographic_normal_coefficients_list)
print("--------")

demographic_svr = SVR().fit(X2_train, y2_train)
svr_predictions=demographic_svr.predict(X2_test)
print("non-tuned SVR")
print(demographic_svr.score(X2_test,y2_test))
print("--------")

svr_demographic_param_grid = {'C': [ 10,11,12,13,14,15], 
              'gamma': [.2,.25,.3,.35,.4,.45,.5],
              'kernel': ['rbf'],
              'epsilon':[.1,.15,.2,.25,.3]}   
svr_demographic_grid = GridSearchCV(ml, svr_demographic_param_grid, refit = True, verbose = 1,cv=5)
  
# fitting the model for grid search
demographic_svr_tuned=svr_demographic_grid.fit(X2_train, y2_train)
print("demo only SVR")
print(demographic_svr_tuned.best_params_)
svr_demographic_predictions=demographic_svr_tuned.predict(X2_test)
print(demographic_svr_tuned.score(X2_test,y2_test))
print("--------")


# dump(normal_lin_reg,"Linear Regression Model.Model")
# dump(svr,"SVR Model.model")
# dump(svr_tuned,"Tuned SVR Model.model")
# dump(demographic_lin_reg,"Linear Regression with only Demographing Data.model")
# dump(demographic_svr,"SVR Model with only Demographic Data.model")
# dump(demographic_svr_tuned,"Tuned SVR Model with only Demographic Data.model")
