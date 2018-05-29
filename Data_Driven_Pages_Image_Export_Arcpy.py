import arcpy

import_path = r".../image.mxd"   # Path of .mxd
export_path = r".../output"   # Path of output file
field_name = "field_name" # Name of field used to sort DDP

mxd = arcpy.mapping.MapDocument(import_path) 
for i in range(1, mxd.dataDrivenPages.pageCount + 1):
   mxd.dataDrivenPages.currentPageID = i
   row = mxd.dataDrivenPages.pageRow
   print row.getValue(field_name)
   arcpy.mapping.ExportToJPEG(mxd, export_path + "\TEST_" + row.getValue(field_name) + ".jpg") 
del mxd