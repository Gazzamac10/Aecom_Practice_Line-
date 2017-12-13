import os
import xlrd

dir = "C:\Users\mccarthyg\PycharmProjects\Aecom_Practice_Line-"
def SaveoutTxtFile(data,Pathout):
    f = open(Pathout,"w")
    for item in data:
        f.write("%s\n" % item)
    f.close()
AecomFamilyPrefix = "_ACM_S_SBM_"
specialprefix = "SP_"


"""CHS"""
CFCHSName = "CFCHS"
CFCHSExcelSheet = dir+"\\CFCHS-secpropsdimsprops-EC3(UKNA)-UK-8-10-2017.xlsx"
CFCHStemplateline = ",Diameter##SECTION_PROPERTY##MILLIMETERS,Wall Nominal Thickness##SECTION_PROPERTY##MILLIMETERS," \
                     "Wall Design Thickness##SECTION_PROPERTY##MILLIMETERS," \
                     "Section Area##SECTION_AREA##SQUARE_CENTIMETERS," \
                     "Perimeter##SURFACE_AREA##SQUARE_METERS_PER_METER," \
                     "Nominal Weight##WEIGHT_PER_UNIT_LENGTH##KILOGRAMS_FORCE_PER_METER," \
                     "Moment of Inertia strong axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER," \
                     "Elastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS," \
                     "Plastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS," \
                     "Torsional Moment of Inertia##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER," \
                     "Torsional Modulus##SECTION_MODULUS##CUBIC_CENTIMETERS,Section Name Key##other##"
CFCHSindexes = [1,1,4,12,3,6,8,9,10,11]

def CHScreatetextfile(name,ExcelSheet,templateline,indexofparam):
    workbook = xlrd.open_workbook(ExcelSheet)
    sheet = workbook.sheet_by_index(0)

    columns = []
    for colx in range(sheet.ncols):
        columns.append(sheet.col_values(colx))
    rows = []
    for rowx in range(sheet.nrows):
        rows.append(sheet.row_values(rowx))

    row1 = columns[0]
    row2 = columns[1]
    row3 = columns[2]

    row2stp = row2[10:len(row2)]

    row2len = len([item for item in row2stp if item.strip()])
    colrange = range(10, row2len + 10)

    filter = [row3[item] for item in colrange]

    Sections = [row1[item] for item in colrange]
    UniqueSections = [item for item in Sections if item.strip()]

    def ifequal(b, a):
        indiceslist = []
        for lA in a:
            counter = 0
            for lB in b:
                if (lA == lB):
                    indiceslist.append(counter)
                counter += 1
        return indiceslist

    series = ifequal(Sections, UniqueSections)

    v = [x[0] - x[1] for x in zip(series[1:], series[:-1])]
    v.append(row2len - series[-1])

    def repeat(a, n):
        list = []
        for i in range(n):
            list.append(a)
        return list

    namelistoflists = []
    for i in range(len(UniqueSections)):
        namelistoflists.append(repeat(UniqueSections[i], v[i]))

    sectionliststart = [j for i in namelistoflists for j in i]
    sectionlistend = [row2[item]for item in colrange]

    def getrange(li, ra):
        return [li[item] for item in ra]

    truncols1 = []
    for i in range(len(columns)):
        truncols1.append(getrange(columns[i], colrange))

    truncols = [truncols1[item] for item in indexofparam]

    Sectioname = []
    for i in range(len(sectionliststart)):
        Sectioname.append([name + sectionliststart[i] +"x"+ sectionlistend[i]])

    j = map(list, zip(*truncols))
    j = [Sectioname[i]+[sectionliststart[i]]+j[i]+Sectioname[i]for i in range(len(Sectioname))]

    fileoutstandard = [templateline]
    fileoutspecials = [templateline]
    for i in range(len(j)):
        if len(filter[i]) > 0:
            fileoutspecials.append(",".join(j[i]))
        else:
            fileoutstandard.append(",".join(j[i]))
    return fileoutstandard,fileoutspecials

CFCHSnamelist = [CFCHSName]
CFCHSexcelsheetlist = [CFCHSExcelSheet]
CFCHStemplatelist = [CFCHStemplateline]
CFCHSindexlist = [CFCHSindexes]

CFCHSnewpaths = [dir + "\\" + AecomFamilyPrefix + str(CFCHSnamelist[i] + ".txt")for i in range(len(CFCHSnamelist))]
CFCHSnewlist = [CHScreatetextfile(CFCHSnamelist[i],CFCHSexcelsheetlist[i],CFCHStemplatelist[i], \
                                  CFCHSindexlist[i])for i in range(len(CFCHSnamelist))]

#for i in range(len(CFCHSnewlist)):
    #SaveoutTxtFile(CFCHSnewlist[i][0],CFCHSnewpaths[i])

SP_CFCHSnewpaths = [dir + "\\" + AecomFamilyPrefix + specialprefix + str(CFCHSnamelist[i] + ".txt")for i in range(len(CFCHSnamelist))]
SP_CFCHSnewlist = [CHScreatetextfile(specialprefix + CFCHSnamelist[i],CFCHSexcelsheetlist[i],CFCHStemplatelist[i], \
                                  CFCHSindexlist[i])for i in range(len(CFCHSnamelist))]

#for i in range(len(SP_CFCHSnewlist)):
    #SaveoutTxtFile(SP_CFCHSnewlist[i][1],SP_CFCHSnewpaths[i])


"""RHS & SHS"""
CFRHSName = "CFRHS"
CFRHSExcelSheet = dir+"\\CFRHS-secpropsdimsprops-EC3(UKNA)-UK-8-10-2017.xlsx"
CFRHStemplateline = ",Width##SECTION_PROPERTY##MILLIMETERS,Height##SECTION_PROPERTY##MILLIMETERS,\
Wall Nominal Thickness##SECTION_PROPERTY##MILLIMETERS,Wall Design Thickness##SECTION_PROPERTY##MILLIMETERS,\
Inner Fillet##SECTION_PROPERTY##MILLIMETERS,Outer Fillet##SECTION_PROPERTY##MILLIMETERS,\
Section Area##SECTION_AREA##SQUARE_CENTIMETERS,Perimeter##SURFACE_AREA##SQUARE_METERS_PER_METER,\
Nominal Weight##WEIGHT_PER_UNIT_LENGTH##KILOGRAMS_FORCE_PER_METER,\
Moment of Inertia strong axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Elastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Plastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Torsional Moment of Inertia##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Torsional Modulus##SECTION_MODULUS##CUBIC_CENTIMETERS,Section Name Key##other##"
CFRHSindexes = [1,1,1,4,12,3,6,8,9,10,11]

CFSHSName = "CFSHS"
CFSHSExcelSheet = dir+"\\CFSHS-secpropsdimsprops-EC3(UKNA)-UK-8-10-2017.xlsx"
CFSHStemplateline = CFRHStemplateline
CFSHSindexes = CFRHSindexes

RHSSHSnamelist = [CFRHSName,CFSHSName]
RHSSHSexcelsheetlist = [CFRHSExcelSheet,CFSHSExcelSheet]
RHSSHStemplatelist = [CFRHStemplateline,CFSHStemplateline]
RHSSHSindexlist = [CFRHSindexes,CFSHSindexes]

def RHSSHScreatetextfile(name,ExcelSheet,templateline,indexofparam):
    workbook = xlrd.open_workbook(ExcelSheet)
    sheet = workbook.sheet_by_index(0)

    columns = []
    for colx in range(sheet.ncols):
        columns.append(sheet.col_values(colx))
    rows = []
    for rowx in range(sheet.nrows):
        rows.append(sheet.row_values(rowx))

    row1 = columns[0]
    row2 = columns[1]
    row3 = columns[2]

    row2stp = row2[10:len(row2)]

    row2len = len([item for item in row2stp if item.strip()])
    colrange = range(10, row2len + 10)

    filter = [row3[item] for item in colrange]

    Sections = [(row1[item].replace(" ","")) for item in colrange]
    UniqueSections = [item for item in Sections if item.strip()]

    def ifequal(b, a):
        indiceslist = []
        for lA in a:
            counter = 0
            for lB in b:
                if (lA == lB):
                    indiceslist.append(counter)
                counter += 1
        return indiceslist

    series = ifequal(Sections, UniqueSections)

    v = [x[0] - x[1] for x in zip(series[1:], series[:-1])]
    v.append(row2len - series[-1])

    def repeat(a, n):
        list = []
        for i in range(n):
            list.append(a)
        return list

    namelistoflists = []
    for i in range(len(UniqueSections)):
        namelistoflists.append(repeat(UniqueSections[i], v[i]))

    sectionliststart = [j for i in namelistoflists for j in i]
    sectionlistend = [row2[item]for item in colrange]

    sectionwidth1= [item.split("x")[1] for item in sectionliststart]
    sectionwidth2 = [item.split("x")[0] for item in sectionliststart]

    def getrange(li, ra):
        return [li[item] for item in ra]

    truncols1 = []
    for i in range(len(columns)):
        truncols1.append(getrange(columns[i], colrange))

    truncols = [truncols1[item] for item in indexofparam]

    Sectioname = []
    for i in range(len(sectionliststart)):
        Sectioname.append([name + sectionliststart[i] +"x"+ sectionlistend[i]])

    j = map(list, zip(*truncols))
    j = [Sectioname[i]+[sectionwidth1[i]]+[sectionwidth2[i]]+j[i]+Sectioname[i]for i in range(len(Sectioname))]

    def changestringatindex(stringlist, index):
        for item in stringlist:
            return item[0:index + index] + [str(float(item[index]) * 2)] + item[index + index:]

    newlist = []
    for item in j:
        newlist.append(changestringatindex([item], 3))

    fileoutstandard = [templateline]
    fileoutspecials = [templateline]
    for i in range(len(newlist)):
        if len(filter[i]) > 0:
            fileoutspecials.append(",".join(newlist[i]))
        else:
            fileoutstandard.append(",".join(newlist[i]))
    return fileoutstandard, fileoutspecials

RHSSHSnewpaths = [dir + "\\" + AecomFamilyPrefix + str(RHSSHSnamelist[i] + ".txt")for i in range(len(RHSSHSnamelist))]
RHSSHSnewlist = [RHSSHScreatetextfile(RHSSHSnamelist[i],RHSSHSexcelsheetlist[i],RHSSHStemplatelist[i], \
                                      RHSSHSindexlist[i])for i in range(len(RHSSHSnamelist))]

#for i in range(len(RHSSHSnewlist)):
    #SaveoutTxtFile(RHSSHSnewlist[i][0],RHSSHSnewpaths[i])

SP_RHSSHSnewpaths = [dir + "\\" + AecomFamilyPrefix + specialprefix + str(RHSSHSnamelist[i] + ".txt")for i in range(len(RHSSHSnamelist))]
SP_RHSSHSnewlist = [RHSSHScreatetextfile(specialprefix + RHSSHSnamelist[i],RHSSHSexcelsheetlist[i],RHSSHStemplatelist[i], \
                                      RHSSHSindexlist[i])for i in range(len(RHSSHSnamelist))]
#for i in range(len(SP_RHSSHSnewlist)):
    #SaveoutTxtFile(SP_RHSSHSnewlist[i][1],SP_RHSSHSnewpaths[i])


"""Universal Beams & Columns"""
UCName = "UC"
UCExcelSheet = dir+"\\UC-secpropsdimsprops-EC3(UKNA)-UK-8-16-2017.xlsx"
UCtemplateline = ",Width##SECTION_PROPERTY##MILLIMETERS,Height##SECTION_PROPERTY##MILLIMETERS,\
Flange Thickness##SECTION_PROPERTY##MILLIMETERS,Web Thickness##SECTION_PROPERTY##MILLIMETERS,\
Web Fillet##SECTION_PROPERTY##MILLIMETERS,Section Area##SECTION_AREA##SQUARE_CENTIMETERS,\
Nominal Weight##WEIGHT_PER_UNIT_LENGTH##KILOGRAMS_FORCE_PER_METER,\
Moment of Inertia strong axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Moment of Inertia weak axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Elastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Elastic Modulus weak axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Plastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Plastic Modulus weak axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Torsional Moment of Inertia##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Warping Constant##WARPING_CONSTANT##CENTIMETERS_TO_THE_SIXTH_POWER,Section Name Key##other##"
UCindexes = [5,4,7,6,8,29,3,17,18,21,22,23,24,28,27]

UBName = "UB"
UBExcelSheet = dir+"\\UB-secpropsdimsprops-EC3(UKNA)-UK-8-4-2017.xlsx"
UBtemplateline = UCtemplateline
UBindexes = UCindexes

UCUBnamelist = [UCName,UBName]
UCUBexcelsheetlist = [UCExcelSheet,UBExcelSheet]
UCUBtemplatelist = [UCtemplateline,UBtemplateline]
UCUBindexlist = [UCindexes,UBindexes]

def UCUBcreatetextfile(name,ExcelSheet,templateline,indexofparam):
    workbook = xlrd.open_workbook(ExcelSheet)
    sheet = workbook.sheet_by_index(0)

    columns = []
    for colx in range(sheet.ncols):
        columns.append(sheet.col_values(colx))
    rows = []
    for rowx in range(sheet.nrows):
        rows.append(sheet.row_values(rowx))

    row1 = columns[0]
    row2 = columns[1]
    row3 = columns[2]

    row2stp = row2[10:len(row2)]

    row2len = len([item for item in row2stp if item.strip()])
    colrange = range(10, row2len + 10)

    filter = [row3[item] for item in colrange]

    Sections = [row1[item] for item in colrange]
    UniqueSections = [item for item in Sections if item.strip()]

    def ifequal(b, a):
        indiceslist = []
        for lA in a:
            counter = 0
            for lB in b:
                if (lA == lB):
                    indiceslist.append(counter)
                counter += 1
        return indiceslist

    series = ifequal(Sections, UniqueSections)

    v = [x[0] - x[1] for x in zip(series[1:], series[:-1])]
    v.append(row2len - series[-1])

    def repeat(a, n):
        list = []
        for i in range(n):
            list.append(a)
        return list

    namelistoflists = []
    for i in range(len(UniqueSections)):
        namelistoflists.append(repeat(UniqueSections[i], v[i]))

    sectionliststart = [j.replace(" ","") for i in namelistoflists for j in i]
    sectionlistend = [(row2[item]).replace(" ","")for item in colrange]

    def getrange(li, ra):
        return [li[item] for item in ra]

    truncols1 = []
    for i in range(len(columns)):
        truncols1.append(getrange(columns[i], colrange))

    truncols = [truncols1[item] for item in indexofparam]

    Sectioname = []
    for i in range(len(sectionliststart)):
        Sectioname.append([name + sectionliststart[i] + sectionlistend[i]])

    j = map(list, zip(*truncols))
    j = [Sectioname[i]+j[i]+Sectioname[i]for i in range(len(Sectioname))]

    fileoutstandard = [templateline]
    fileoutspecials = [templateline]
    for i in range(len(j)):
        if len(filter[i]) > 0:
            fileoutspecials.append(",".join(j[i]))
        else:
            fileoutstandard.append(",".join(j[i]))
    return fileoutstandard, fileoutspecials

UCUBnewpaths = [dir + "\\" + AecomFamilyPrefix + str(UCUBnamelist[i] + ".txt")for i in range(len(UCUBnamelist))]
UCUBnewlist = [UCUBcreatetextfile(UCUBnamelist[i],UCUBexcelsheetlist[i],UCUBtemplatelist[i],\
                              UCUBindexlist[i])for i in range(len(UCUBnamelist))]

#for i in range(len(UCUBnewlist)):
    #SaveoutTxtFile(UCUBnewlist[i][0],UCUBnewpaths[i])

SP_UCUBnewpaths = [dir + "\\" + AecomFamilyPrefix + specialprefix + str(UCUBnamelist[i] + ".txt")for i in range(len(UCUBnamelist))]
SP_UCUBnewlist = [UCUBcreatetextfile(specialprefix + UCUBnamelist[i],UCUBexcelsheetlist[i],UCUBtemplatelist[i],\
                              UCUBindexlist[i])for i in range(len(UCUBnamelist))]

#for i in range(len(SP_UCUBnewlist)):
    #SaveoutTxtFile(SP_UCUBnewlist[i][1],SP_UCUBnewpaths[i])


"""Equal Angle (needs units checking)"""
EAName = "EA"
EAExcelSheet = dir+"\\L-equal-secpropsdimsprops-EC3(UKNA)-UK-10-5-2017.xlsx"
EAtemplateline = ",Width##SECTION_PROPERTY##MILLIMETERS,Height##SECTION_PROPERTY##MILLIMETERS,\
Flange Thickness##SECTION_PROPERTY##MILLIMETERS,Web Thickness##SECTION_PROPERTY##MILLIMETERS,\
Flange Fillet##SECTION_PROPERTY##MILLIMETERS,Web Fillet##SECTION_PROPERTY##MILLIMETERS,\
Centroid Horizontal##SECTION_PROPERTY##MILLIMETERS,Centroid Vertical##SECTION_PROPERTY##MILLIMETERS,\
Section Area##SECTION_AREA##SQUARE_CENTIMETERS,Nominal Weight##WEIGHT_PER_UNIT_LENGTH##KILOGRAMS_FORCE_PER_METER,\
Moment of Inertia strong axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Moment of Inertia weak axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Elastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Elastic Modulus weak axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Torsional Moment of Inertia##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Section Name Key##other##"
EAindexes = [1,1,5,4,6,6,16,3,7,7,13,13,14]

EAnamelist = [EAName]
EAexcelsheetlist = [EAExcelSheet]
EAtemplatelist = [EAtemplateline]
EAindexlist = [EAindexes]

def EAcreatetextfile(name,ExcelSheet,templateline,indexofparam):
    workbook = xlrd.open_workbook(ExcelSheet)
    sheet = workbook.sheet_by_index(0)

    columns = []
    for colx in range(sheet.ncols):
        columns.append(sheet.col_values(colx))
    rows = []
    for rowx in range(sheet.nrows):
        rows.append(sheet.row_values(rowx))

    row1 = columns[0]
    row2 = columns[1]
    row3 = columns[2]

    row2stp = row2[10:len(row2)]

    row2len = len([item for item in row2stp if item.strip()])
    colrange = range(10, row2len + 10)

    filter = [row3[item] for item in colrange]

    Sections = [(row1[item].replace(" ","")) for item in colrange]
    UniqueSections = [item for item in Sections if item.strip()]

    def ifequal(b, a):
        indiceslist = []
        for lA in a:
            counter = 0
            for lB in b:
                if (lA == lB):
                    indiceslist.append(counter)
                counter += 1
        return indiceslist

    series = ifequal(Sections, UniqueSections)

    v = [x[0] - x[1] for x in zip(series[1:], series[:-1])]
    v.append(row2len - series[-1])

    def repeat(a, n):
        list = []
        for i in range(n):
            list.append(a)
        return list

    namelistoflists = []
    for i in range(len(UniqueSections)):
        namelistoflists.append(repeat(UniqueSections[i], v[i]))

    sectionliststart = [j for i in namelistoflists for j in i]
    sectionlistend = [row2[item]for item in colrange]

    sectionwidth1= [item.split("x")[1] for item in sectionliststart]
    sectionwidth2 = [item.split("x")[0] for item in sectionliststart]

    def getrange(li, ra):
        return [li[item] for item in ra]

    truncols1 = []
    for i in range(len(columns)):
        truncols1.append(getrange(columns[i], colrange))

    truncols = [truncols1[item] for item in indexofparam]

    Sectioname = []
    for i in range(len(sectionliststart)):
        Sectioname.append([name + sectionliststart[i] +"x"+ sectionlistend[i]])

    j = map(list, zip(*truncols))
    j = [Sectioname[i]+[sectionwidth1[i]]+[sectionwidth2[i]]+j[i]+Sectioname[i]for i in range(len(Sectioname))]

    def changestringatindex(stringlist, index):
        for item in stringlist:
            return item[0:index + index] + [str(float(item[index]) * 2)] + item[index + index:]

    newlist = []
    for item in j:
        newlist.append(changestringatindex([item], 3))

    fileoutstandard = [templateline]
    fileoutspecials = [templateline]
    for i in range(len(j)):
        if len(filter[i]) > 0:
            fileoutspecials.append(",".join(j[i]))
        else:
            fileoutstandard.append(",".join(j[i]))
    return fileoutstandard, fileoutspecials

EAnewpaths = [dir + "\\" + AecomFamilyPrefix + str(EAnamelist[i] + ".txt")for i in range(len(EAnamelist))]
EAnewlist = [EAcreatetextfile(EAnamelist[i],EAexcelsheetlist[i],EAtemplatelist[i], \
                                  EAindexlist[i])for i in range(len(EAnamelist))]

#for i in range(len(EAnewlist)):
    #SaveoutTxtFile(EAnewlist[i][0],EAnewpaths[i])

SP_EAnewpaths = [dir + "\\" + AecomFamilyPrefix + specialprefix + str(EAnamelist[i] + ".txt")for i in range(len(EAnamelist))]
SP_EAnewlist = [EAcreatetextfile(specialprefix + EAnamelist[i],EAexcelsheetlist[i],EAtemplatelist[i], \
                                  EAindexlist[i])for i in range(len(EAnamelist))]

#for i in range(len(SP_EAnewlist)):
    #SaveoutTxtFile(SP_EAnewlist[i][1],SP_EAnewpaths[i])


"""Unequal Angle (needs units checking)"""
UEAName = "UEA"
UEAExcelSheet = dir+"\\L-unequal-secpropsdimsprops-EC3(UKNA)-UK-10-6-2017.xlsx"
UEAtemplateline = ",Width##SECTION_PROPERTY##MILLIMETERS,Height##SECTION_PROPERTY##MILLIMETERS,\
Flange Thickness##SECTION_PROPERTY##MILLIMETERS,Web Thickness##SECTION_PROPERTY##MILLIMETERS,\
Flange Fillet##SECTION_PROPERTY##MILLIMETERS,Web Fillet##SECTION_PROPERTY##MILLIMETERS,\
Centroid Horizontal##SECTION_PROPERTY##MILLIMETERS,Centroid Vertical##SECTION_PROPERTY##MILLIMETERS,\
Section Area##SECTION_AREA##SQUARE_CENTIMETERS,Nominal Weight##WEIGHT_PER_UNIT_LENGTH##KILOGRAMS_FORCE_PER_METER,\
Moment of Inertia strong axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Moment of Inertia weak axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Elastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Elastic Modulus weak axis##SECTION_MODULUS##CUBIC_CENTIMETERS,\
Torsional Moment of Inertia##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER,\
Principal Axes Angle##ANGLE##DEGREES,Section Name Key##other##"
UEAindexes = [1,1,5,4,7,6,10,3,8,9,16,17,19,18]

UEAnamelist = [UEAName]
UEAexcelsheetlist = [UEAExcelSheet]
UEAtemplatelist = [UEAtemplateline]
UEAindexlist = [UEAindexes]

def UEAcreatetextfile(name,ExcelSheet,templateline,indexofparam):
    workbook = xlrd.open_workbook(ExcelSheet)
    sheet = workbook.sheet_by_index(0)

    columns = []
    for colx in range(sheet.ncols):
        columns.append(sheet.col_values(colx))
    rows = []
    for rowx in range(sheet.nrows):
        rows.append(sheet.row_values(rowx))

    row1 = columns[0]
    row2 = columns[1]
    row3 = columns[2]

    row2stp = row2[10:len(row2)]

    row2len = len([item for item in row2stp if item.strip()])
    colrange = range(10, row2len + 10)

    filter = [row3[item] for item in colrange]

    Sections = [(row1[item].replace(" ","")) for item in colrange]
    UniqueSections = [item for item in Sections if item.strip()]

    def ifequal(b, a):
        indiceslist = []
        for lA in a:
            counter = 0
            for lB in b:
                if (lA == lB):
                    indiceslist.append(counter)
                counter += 1
        return indiceslist

    series = ifequal(Sections, UniqueSections)

    v = [x[0] - x[1] for x in zip(series[1:], series[:-1])]
    v.append(row2len - series[-1])

    def repeat(a, n):
        list = []
        for i in range(n):
            list.append(a)
        return list

    namelistoflists = []
    for i in range(len(UniqueSections)):
        namelistoflists.append(repeat(UniqueSections[i], v[i]))

    sectionliststart = [j for i in namelistoflists for j in i]
    sectionlistend = [row2[item]for item in colrange]

    sectionwidth1= [item.split("x")[1] for item in sectionliststart]
    sectionwidth2 = [item.split("x")[0] for item in sectionliststart]

    def getrange(li, ra):
        return [li[item] for item in ra]

    truncols1 = []
    for i in range(len(columns)):
        truncols1.append(getrange(columns[i], colrange))

    truncols = [truncols1[item] for item in indexofparam]

    Sectioname = []
    for i in range(len(sectionliststart)):
        Sectioname.append([name + sectionliststart[i] +"x"+ sectionlistend[i]])

    j = map(list, zip(*truncols))
    j = [Sectioname[i]+[sectionwidth1[i]]+[sectionwidth2[i]]+j[i]+Sectioname[i]for i in range(len(Sectioname))]

    def changestringatindex(stringlist, index):
        for item in stringlist:
            return item[0:index + index] + [str(float(item[index]) * 2)] + item[index + index:]

    newlist = []
    for item in j:
        newlist.append(changestringatindex([item], 3))

    fileoutstandard = [templateline]
    fileoutspecials = [templateline]
    for i in range(len(j)):
        if len(filter[i]) > 0:
            fileoutspecials.append(",".join(j[i]))
        else:
            fileoutstandard.append(",".join(j[i]))
    return fileoutstandard, fileoutspecials

UEAnewpaths = [dir + "\\" + AecomFamilyPrefix + str(UEAnamelist[i] + ".txt")for i in range(len(UEAnamelist))]
UEAnewlist = [UEAcreatetextfile(UEAnamelist[i],UEAexcelsheetlist[i],UEAtemplatelist[i], \
                                  UEAindexlist[i])for i in range(len(UEAnamelist))]

#for i in range(len(UEAnewlist)):
   #SaveoutTxtFile(UEAnewlist[i][0],UEAnewpaths[i])

SP_UEAnewpaths = [dir + "\\" + AecomFamilyPrefix + specialprefix + str(UEAnamelist[i] + ".txt")for i in range(len(UEAnamelist))]
SP_UEAnewlist = [UEAcreatetextfile(specialprefix + UEAnamelist[i],UEAexcelsheetlist[i],UEAtemplatelist[i], \
                                  UEAindexlist[i])for i in range(len(UEAnamelist))]

#for i in range(len(SP_UEAnewlist)):
   #SaveoutTxtFile(SP_UEAnewlist[i][1],SP_UEAnewpaths[i])


