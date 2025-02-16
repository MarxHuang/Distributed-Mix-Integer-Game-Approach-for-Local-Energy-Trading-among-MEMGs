"""
Created on Mon Jan  8 19:49:53 2024

@author: DELL
"""

import numpy
import pandas
import networkx as nx


def doConvert2PU(eBus, eBranch, baseKV):
    Vbase = baseKV * 1e3
    Sbase = 1 * 1e6
    VS = Vbase ** 2 / Sbase
    
    eBusUpdate = eBus[:, 2:] / 1e3
    eBusUpdate = numpy.hstack((eBus[:, :2], eBusUpdate))
    
    eBranchUpdate = eBranch[:, 2:] / VS
    eBranchUpdate = numpy.hstack((eBranch[:, :2], eBranchUpdate))
    
    return eBusUpdate, eBranchUpdate

        
MGOneeBus = numpy.array([
    [1, 3, 0, 0],
    [2, 1, 60, 60],
    [3, 1, 40, 30],
    [4, 1, 55, 55],
    [5, 1, 30, 30],
    [6, 1, 20, 15],
    [7, 1, 55, 55],
    [8, 1, 45, 45],
    [9, 1, 40, 40],
    [10, 1, 35, 30],
    [11, 1, 40, 30],
    [12, 1, 15, 15]
    ])

MGOneeBranch = numpy.array([
    [1, 2, 1.093, 0.455],
    [2, 3, 1.184, 0.494],
    [3, 4, 2.095, 0.873],
    [4, 5, 3.188, 1.329],
    [5, 6, 1.093, 0.455],
    [6, 7, 1.002, 0.417],
    [7, 8, 4.403, 1.215],
    [8, 9, 5.642, 1.597],
    [9, 10, 2.89, 0.818],
    [10, 11, 1.514, 0.428],
    [11, 12, 1.238, 0.351]
    ])
    
    
MGTwoeBus = numpy.array([  
    [1, 3, 0, 0],
    [2, 1, 44.1, 44.991],
    [3, 1, 70, 71.4143],
    [4, 1, 140, 142.8286],
    [5, 1, 44.1, 44.991],
    [6, 1, 140, 142.8286],
    [7, 1, 140, 142.8286],
    [8, 1, 70, 71.4143],
    [9, 1, 70, 71.4143],
    [10, 1, 44.1, 44.991],
    [11, 1, 140, 142.8286],
    [12, 1, 70, 71.4143],
    [13, 1, 44.1, 44.991],
    [14, 1, 70, 71.4143],
    [15, 1, 140, 142.8286]
    ])
 
MGTwoeBranch = numpy.array([
    [1, 2, 1.35309, 1.32349],
    [2, 3, 1.17024, 1.14464],
    [3, 4, 0.84111, 0.82271],
    [4, 5, 1.52348, 1.0276],
    [2, 9, 2.01317, 1.3579],
    [9, 10, 1.68671, 1.1377],
    [2, 6, 2.55727, 1.7249],
    [6, 7, 1.0882, 0.734],
    [6, 8, 1.25143, 0.8441],
    [3, 11, 1.79553, 1.2111],
    [11, 12, 2.44845, 1.6515],
    [12, 13, 2.01317, 1.3579],
    [4, 14, 2.23081, 1.5047],
    [4, 15, 1.19702, 0.8074]
    ])
 

   
MGThreeeBus = numpy.array([
    [1, 3, 0, 0],
    [2, 1, 100, 60],
    [3, 1, 90, 40],
    [4, 1, 120, 80],
    [5, 1, 60, 30],
    [6, 1, 60, 20], 
    [7, 1, 200, 100],
    [8, 1, 200, 100],
    [9, 1, 60, 20],
    [10, 1, 60, 20],
    [11, 1, 45, 30],
    [12, 1, 60, 35],
    [13, 1, 60, 35],
    [14, 1, 120, 80],
    [15, 1, 60, 10],
    [16, 1, 60, 20],
    [17, 1, 60, 20],
    [18, 1, 90, 40],
    [19, 1, 90, 40],
    [20, 1, 90, 40],
    [21, 1, 90, 40],
    [22, 1, 90, 40],
    [23, 1, 90, 40],
    [24, 1, 420, 200],
    [25, 1, 420, 200],
    [26, 1, 60, 25],
    [27, 1, 60, 25],
    [28, 1, 60, 20],
    [29, 1, 120, 70],
    [30, 1, 200, 600],
    [31, 1, 150, 70],
    [32, 1, 210, 100],
    [33, 1, 60, 40]
    ])
    
MGThreeeBranch = numpy.array([
    [1, 2, 0.0922, 0.0470],
    [2, 3, 0.4930, 0.2511],
    [3, 4, 0.3660, 0.1864],
    [4, 5, 0.3811, 0.1941],
    [5, 6, 0.8190, 0.7070],
    [6, 7, 0.1872, 0.6188],
    [7, 8, 0.7114, 0.2351],
    [8, 9, 1.0300, 0.7400],
    [9, 10, 1.0440, 0.7400],
    [10, 11, 0.1966, 0.0650],
    [11, 12, 0.3744, 0.1238],
    [12, 13, 1.4680, 1.1550],
    [13, 14, 0.5416, 0.7129],
    [14, 15, 0.5910, 0.5260],
    [15, 16, 0.7463, 0.5450],
    [16, 17, 1.2890, 1.7210],
    [17, 18, 0.7320, 0.5740],
    [2, 19, 0.1640, 0.1565],
    [19, 20, 1.5042, 1.3554],
    [20, 21, 0.4095, 0.4784],
    [21, 22, 0.7089, 0.9373],
    [3, 23, 0.4512, 0.3083],
    [23, 24, 0.8980, 0.7091],
    [24, 25, 0.8960, 0.7011],
    [6, 26, 0.2030, 0.1034],
    [26, 27, 0.2842, 0.1447],
    [27, 28, 1.0590, 0.9337],
    [28, 29, 0.8042, 0.7006],
    [29, 30, 0.5075, 0.2585],
    [30, 31, 0.9744, 0.9630],
    [31, 32, 0.3105, 0.3619],
    [32, 33, 0.3410, 0.5302],
    ])



MGOneeBus, MGOneeBranch = doConvert2PU(MGOneeBus, MGOneeBranch, 11)
MGTwoeBus, MGTwoeBranch = doConvert2PU(MGTwoeBus, MGTwoeBranch, 11)
MGThreeeBus, MGThreeeBranch = doConvert2PU(MGThreeeBus, MGThreeeBranch, 12.66)



GasNetwork_3 = numpy.array([
    [1, 2],
    [2, 3],
    [2, 5],
    [3, 4],
    [3, 6],
    [4, 7],
    [4, 8],
    [9, 10],
    [10, 11],
    [10, 14],
    [11, 12],
    [11, 15],
    [12, 13],
    [12, 16],
    [17, 18],
    [18, 22],
    [18, 19],
    [19, 23],
    [19, 20],
    [20, 24],
    [20, 21]
    ])
        
GasNetwork_1 = numpy.array([
    [1, 2],
    [2, 7],
    [2, 3],
    [3, 8],
    [3, 4],
    [4, 9],
    [4, 11],
    [4, 5],
    [5, 10],
    [5, 6]
    ])
        
GasNetwork_2 = numpy.array([
    [1, 2],
    [2, 5],
    [2, 3],
    [3, 6],
    [3, 4],
    [4, 7],
    [4, 8]
    ])

GasBus_1 = numpy.array([
    [1, 3, 0],
    [2, 1, 0],
    [3, 1, 0],
    [4, 1, 0],
    [5, 1, 0],
    [6, 3, 0],
    [7, 1, 0.75],
    [8, 1, 0.55],
    [9, 1, 0.65],
    [10, 1, 0.70],
    [11, 1, 0.55],
    ])

GasBus_2 = numpy.array([
    [1, 3, 0],
    [2, 1, 0],
    [3, 1, 0],
    [4, 1, 0],
    [5, 1, 0.85],
    [6, 1, 1.25],
    [7, 1, 0.95],
    [8, 3, 0]
    ])

GasBus_3 = numpy.array([
    [1, 3, 0],
    [2, 1, 0],
    [3, 1, 0],
    [4, 1, 0],
    [5, 1, 0.65],
    [6, 1, 0.75],
    [7, 1, 0.70],
    [8, 3, 0],
    [9, 3, 0],
    [10, 1, 0],
    [11, 1, 0],
    [12, 1, 0],
    [13, 3, 0],
    [14, 1, 0.65],
    [15, 1, 0.65],
    [16, 1, 0.75],
    [17, 3, 0],
    [18, 1, 0],
    [19, 1, 0],
    [20, 1, 0],
    [21, 3, 0],
    [22, 1, 0.75],
    [23, 1, 0.75],
    [24, 1, 0.70]
    ])


'''
NodeType = 1: WT;
NodeType = 2: PV;
NodeType = 3: BS;
NodeType = 5: P2G unit;

MGINformation = [
    [NodeType, NodeNumber, PowerCapacity(kW), EnergyCapacity(kWh), isTie(bool)],
     ...
    ]
'''
MGOneInformation = numpy.array([
    [1, 3, 100, 0, 0],
    [2, 3, 60, 0, 0],
    [3, 3, 50, 200, 0],
    [5, 4, 350, 0, 1],
    [1, 7, 200, 0, 0],
    [2, 7, 100, 0, 0], 
    [3, 7, 100, 350, 0]
    ], dtype='float64')

MGTwoInformation = numpy.array([
    [1, 3, 300, 0, 20],
    [2, 3, 150, 0, 20],
    [3, 3, 180, 500, 1],
    [5, 3, 500, 0, 1],
    [1, 4, 250, 0, 0],
    [2, 4, 100, 0, 0], 
    [3, 4, 150, 450, 0],
    [1, 6, 200, 0, 0],
    [2, 9, 200, 0, 0],
    [3, 9, 170, 400, 0]
    ], dtype='float64')

MGThreeInformation = numpy.array([
    [1, 4, 200, 0, 1],
    [2, 4, 100, 0, 1],
    [3, 4, 250, 800, 1],
    [5, 4, 500, 0, 1],
    [1, 6, 250, 0, 0],
    [2, 6, 150, 0, 0], 
    [3, 6, 250, 800, 0],
    [1, 11, 300, 0, 17],
    [2, 11, 100, 0, 17],
    [3, 11, 150, 480, 17],
    [5, 11, 450, 0, 17],
    [1, 13, 200, 0, 0],
    [2, 13, 100, 0, 0],
    [3, 13, 200, 640, 0],
    [1, 16, 350, 0, 0],
    [2, 16, 200, 0, 0],
    [3, 16, 100, 320, 0],
    [1, 19, 300, 0, 0],
    [2, 19, 250, 0, 0],
    [3, 19, 150, 480, 0],
    [1, 23, 350, 0, 0],
    [2, 23, 250, 0, 0],
    [3, 23, 200, 640, 0],
    [5, 28, 350, 0, 9],
    [1, 31, 350, 0, 0],
    [2, 31, 150, 0, 0],
    [3, 31, 100, 320, 0]
    ], dtype='float64')

MGOneInformation[:, 2:4] /= 1e3
MGTwoInformation[:, 2:4] /= 1e3
MGThreeInformation[:, 2:4] /= 1e3

GasBus_1[:, 2] /= 3
GasBus_2[:, 2] /= 3
GasBus_3[:, 2] /= 3

# MGOneeBus[:, 2:4] /= 10
# MGTwoeBus[:, 2:4] /= 10
# MGThreeeBus[:, 2:4] /= 10
# MGOneInformation[:, 2:4] *= 100

# MGOneeBus[:, 2:3] *= 2
# MGTwoeBus[:, 2:4] *= 3
# MGThreeeBus[:, 2:4] *= 3

# MGOneInformation[3:7, 2:4] /= 1e3
# MGTwoInformation[:, 2:4] /= 1e3
# MGThreeInformation[:, 2:4] /= 1e3
MGTwoeBus[:, 0] += 12
MGTwoeBranch[:, 0:2] += 12
MGThreeeBus[:, 0] += 27
MGThreeeBranch[:, 0:2] += 27
MGFoureBus = numpy.concatenate((MGOneeBus, MGTwoeBus, MGThreeeBus), axis=0)
MGFoureBranch = numpy.concatenate((MGOneeBranch, MGTwoeBranch, MGThreeeBranch), axis=0)

GasBus_2[:, 0] += 11
GasBus_3[:, 0] += 19
GasNetwork_2[:, 0:2] += 11
GasNetwork_3[:, 0:2] += 19
GasBus_4 = numpy.concatenate((GasBus_1, GasBus_2, GasBus_3), axis=0)
GasNetwork_4 = numpy.concatenate((GasNetwork_1, GasNetwork_2, GasNetwork_3), axis=0)

MGTwoInformation[:, 1] += 12
MGThreeInformation[:, 1] += 27
MGTwoInformation[MGTwoInformation[:, 4] != 0, 4] += 11
MGThreeInformation[MGThreeInformation[:, 4] != 0, 4] += 19
MGFourInformation = numpy.concatenate((MGOneInformation, MGTwoInformation, MGThreeInformation), axis=0)

DataFrame_WT = pandas.read_excel(
    '分布式电源出力和负荷数据.xlsx', sheet_name='WT', usecols=[i for i in range(1, 27, 2)]
    )
DataFrame_PV = pandas.read_excel(
    '分布式电源出力和负荷数据.xlsx', sheet_name='PV', usecols=[i for i in range(1, 27, 2)]
    )

DataFrame_Load = pandas.read_csv(
    'LD2011_2014.txt',sep=';', nrows=96, low_memory=False
    )
DataFrame_Load = DataFrame_Load.drop(
    DataFrame_Load.columns[DataFrame_Load.eq(0).all()], axis=1
    )

for column in DataFrame_Load.iloc[:, 1:]:
    DataFrame_Load[column] = DataFrame_Load[column].apply(lambda x: x.replace(',','.'))
    DataFrame_Load[column] = pandas.to_numeric(DataFrame_Load[column])
    MaxValue = DataFrame_Load[column].max()
    DataFrame_Load[column] = DataFrame_Load[column].div(MaxValue) 

LoadBase = numpy.array(DataFrame_Load.iloc[:, 1:])
P_WTBase = numpy.array(DataFrame_WT)
P_PVBase = numpy.array(DataFrame_PV)

PriceBase = pandas.read_csv("电力（天然气）价格.csv",sep=';')
# PriceBase = PriceBase.dropna()

ElecPriceBase = numpy.array(PriceBase.loc[26:121, "Marginal incremental price"])
GasPriceBase = numpy.array(PriceBase.loc[122:217, "Marginal incremental price"])

ElecPriceLinar = numpy.array(PriceBase.loc[218:313, "Marginal incremental price"])

GasPriceLinar = PriceBase.loc[314:409, "Marginal incremental price"]
GasPriceLinar.interpolate(method='linear', inplace=True)
GasPriceLinar = numpy.array(PriceBase.loc[314:409, "Marginal incremental price"])

ElecPriceBase = numpy.flip(ElecPriceBase)
GasPriceBase = numpy.flip(GasPriceBase)
ElecPriceBase = ElecPriceBase / 4 / 100
GasPriceBase = GasPriceBase / 20 / 100

ElecPriceLinar =ElecPriceLinar / 4
GasPriceLinar = GasPriceLinar / 20

del MaxValue, column, DataFrame_PV, DataFrame_WT, DataFrame_Load, PriceBase
# test, tes = doConvert2PU(MGTwoeBus, MGTwoeBranch, 11)