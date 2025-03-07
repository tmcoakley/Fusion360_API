import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        activeSel = ui.activeSelections
        totalSelections = activeSel.count # get total number of selections
       

        xarr, yarr, zarr = [], [], [] # create empty arrays to hold x, y, z
    
        if totalSelections != 4: 
            ui.messageBox(str('You need to select four corners of the antenna!'))

        else: 
            for iter in range(0, totalSelections): 

                occurrenceSel = activeSel.item(iter).entity 
                vertex = (occurrenceSel.geometry.asArray()) # this will give coordinate of vertex in cm
            

                x, y, z = vertex[0] / 2.54, vertex[1] / 2.54, vertex[2] / 2.54 # save and convert to in
                
                xarr.append(x)
                yarr.append(y)
                zarr.append(z)

            # get the midpoints of all coordinates
            coordx = sum(xarr) / 4
            coordy = sum(yarr) / 4
            coordz = sum(zarr) / 4

            # report back value
            ui.messageBox(str('Coordinate: ({}, {}, {})'.format(coordx, coordy, coordz)))
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


