import os
import glob
import pandas as pd
os.chdir('C:\Users\P.k Ahuja\Append')
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')