import arcpy, os

mxd = arcpy.mapping.MapDocument(r".../ExportMaps.mxd")

df = arcpy.mapping.ListDataFrames(mxd, '')[0] # assuming there is only 1 df you're interested in

output_path = ".../Output"

output_extension =".jpg"

#Turn off all kernel density raster layers but not the boundary(base maps)lyrs in list
for lyr in arcpy.mapping.ListLayers(mxd, 'sym_ming_*', df):
        lyr.visible = False

arcpy.RefreshActiveView()

# Loop through each layer, turn it on and export map as PNG
for lyr in arcpy.mapping.ListLayers(mxd, 'sym_ming_*', df):
    lyr.visible = True
    arcpy.RefreshActiveView()
    #output_file =output_path+lyr.name
    output_filename = output_path + "\\" + lyr.name + output_extension
    arcpy.mapping.ExportToJPEG(mxd,output_filename,"PAGE_LAYOUT")
    lyr.visible = False
    print "Created the JPEG for"+ " "+ lyr.name

print "Done!"   
mxd.save()



