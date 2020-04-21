import flat_world1 as fl1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def write_xls(df, name):
    writer = pd.ExcelWriter(name)
    df.to_excel(writer)
    writer.save()


timeline = fl1.Timeline()

region = fl1.Region()

fl1.fill_region_basic(region)

region.apply_sunlight(timeline)
#a_maper =pd.DataFrame(region.make_squares_supply_map('a'))
#write_xls(a_maper,'a_map.xlsx')

#fl1.resources_over_time_graph(tl= timeline, rg=region, interval=10, iterations=100, resource_type='a')