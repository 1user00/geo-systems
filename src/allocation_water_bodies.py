import geopandas as gpd
import matplotlib.pyplot as plt
df = gpd.read_file(r'C:\Users\User\Downloads\S2B_MSIL2A_20200926T084719_N0214_R107_T37VCD_20200926T114459.SAFE\GRANULE\L2A_T37VCD_A018580_20200926T085042\IMG_DATA\R10m\out_vectors.shp')

df = df[df.CLASS_NAME=="Class 1"].plot(figsize = (20,16))
