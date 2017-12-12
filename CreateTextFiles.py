import xlrd

beamColxlsx  = "C:\\temp\Python\Dev\Blue Book Steelwork\Direct Export\UB-secpropsdimsprops-EC3(UKNA)-UK-8-8-2017.xlsx"
beamColtemplateline = [",Width##SECTION_PROPERTY##MILLIMETERS," \
               "Height##SECTION_PROPERTY##MILLIMETERS," \
               "Flange Thickness##SECTION_PROPERTY##MILLIMETERS," \
               "Web Thickness##SECTION_PROPERTY##MILLIMETERS," \
               "Web Fillet##SECTION_PROPERTY##MILLIMETERS," \
               "Section Area##SECTION_AREA##SQUARE_CENTIMETERS," \
               "Nominal Weight##WEIGHT_PER_UNIT_LENGTH##KILOGRAMS_FORCE_PER_METER," \
               "Moment of Inertia strong axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER," \
               "Moment of Inertia weak axis##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER," \
               "Elastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS," \
               "Elastic Modulus weak axis##SECTION_MODULUS##CUBIC_CENTIMETERS," \
               "Plastic Modulus strong axis##SECTION_MODULUS##CUBIC_CENTIMETERS," \
               "Plastic Modulus weak axis##SECTION_MODULUS##CUBIC_CENTIMETERS," \
               "Torsional Moment of Inertia##MOMENT_OF_INERTIA##CENTIMETERS_TO_THE_FOURTH_POWER," \
               "Warping Constant##WARPING_CONSTANT##CENTIMETERS_TO_THE_SIXTH_POWER,Section Name Key##other##"]
indexofparam = [3, 4, 5, 6]
beamColPathout = "C:\\temp\Python\Dev\Blue Book Steelwork\Direct Export\\test.txt"

def createtextfile(name,templateline,indexofparam):
    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_index(0)

    columns = []
    for colx in range(sheet.ncols):
        columns.append(sheet.col_values(colx))
    rows = []
    for rowx in range(sheet.nrows):
        rows.append(sheet.row_values(rowx))

    row1 = columns[0]
    row2 = columns[1]

    row2len = len([item for item in row2 if item.strip()])
    colrange = range(10, row2len + 10)

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
    sectionlistend = [item for item in row2 if item.strip()]

    sectionlist1 = []
    for i in range(len(sectionliststart)):
        sectionlist1.append(str(sectionliststart[i] + " " + str(sectionlistend[i])))
    sectionlist = []
    for item in sectionlist1:
        sectionlist.append(item.replace(" ", ""))

    def getrange(li, ra):
        return [li[item] for item in ra]

    truncols1 = []
    for i in range(len(columns)):
        truncols1.append(getrange(columns[i], colrange))

    truncols = [truncols1[item] for item in indexofparam]

    j = [zip(sectionlist, *truncols)[i] for i in range(len(sectionlist))]

    fileout = templateline
    for item in j:
        fileout.append(",".join(item))

    return fileout

    f = open(beamColPathout,"w")


f = open(beamColPathout,"w")
for item in createtextfile(beamColxlsx,beamColtemplateline,indexofparam):
    f.write("%s\n" % item)
f.close()

