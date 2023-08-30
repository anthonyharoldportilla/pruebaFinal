import pandas as pd

datos={
    'Nombre':['Juan','Maria','Carlos'],
    'Edad':[25,27,18],
    'Ciudad' :['Lima','Sidney','Madrid']
}

df=pd.DataFrame(datos)
print(df)

df1=df['Edad']
print (df1)