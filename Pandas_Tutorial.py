import pandas as pd
A={
    "name":["Acand","Ayod","Piggy","PooPoo"],
    "class":["A","A","B","C"],
    "marks":["95","97","88","78"]
}
D=pd.DataFrame(A)
# D.to_csv("PandasF1.csv",index=False) # is used to create a csv file , index false is used to remove index
# A["column name"][index]= something --> this can be used to change values in csv
D.index=["first","second","third","fourth"] # index label is used to change the rows headings
D.to_csv("PandasF1.csv")
