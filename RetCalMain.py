# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\pythonstuff\retraction.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from RetCalui import Ui_MainWindow
from decimal import Decimal


ui=None

#Start Raft
#def raft (file,xpos,ypos,ps,eValueresult,lh):
#    return file,xpos,ypos




#Start Gcode
 
def gengcode ():
    global ui
    

    name = QtWidgets.QFileDialog.getSaveFileName(ui.centralwidget, 'Save Gcode', filter="(*.gcode)")
    if len(name[0])>0:
        
        file = open(name[0],'w')

#Start Gcode Retraction Distance
        srd = float(ui.startRetractiondistance.text())
        ird = float(ui.incrementRetractiondistance.text())
        
        file.write(f";Calibration Generator 1.3.1\n")
        file.write(f";\n")
        file.write(f";\n")
        file.write(f";Retraction Distance from the top looking down\n")
        file.write(f";\n")
        file.write(f";       {round(Decimal(srd+ird*11),2)}    {round(Decimal(srd+ird*10),2)}    {round(Decimal(srd+ird*9),2)}    {round(Decimal(srd+ird*8),2)}\n")
        file.write(f";		|		|		|		|\n")
        file.write(f";\n")
        file.write(f";{round(Decimal(srd+ird*12),2)}-                               -{round(Decimal(srd+ird*7),2)}\n")
        file.write(f";\n")
        file.write(f";\n")
        file.write(f";{round(Decimal(srd+ird*13),2)}-                               -{round(Decimal(srd+ird*6),2)}\n")
        file.write(f";\n")
        file.write(f";\n")
        file.write(f";{round(Decimal(srd+ird*14),2)}-                               -{round(Decimal(srd+ird*5),2)}\n")
        file.write(f";\n")
        file.write(f";\n")
        file.write(f";{round(Decimal(srd+ird*15),2)}-                               -{round(Decimal(srd+ird*4),2)}\n")
        file.write(f";\n")
        file.write(f";		|		|		|		|\n")
        file.write(f";       {round(Decimal(srd+ird*0),2)}    {round(Decimal(srd+ird*1),2)}    {round(Decimal(srd+ird*2),2)}    {round(Decimal(srd+ird*3),2)}\n")
        file.write(f";\n")
        file.write(f";\n")

        #Variables by Height


        srs = float(ui.startRetractionspeed.text())
        irs = float(ui.incrementRetractionspeed.text())
        tsh = float(ui.tempStarthotend.text())
        tih = float(ui.tempIncrementhotend.text())
        fs = float(ui.speedFan.text())
        fsi = float(ui.speedFanIncrement.text())
        #{Ben
        sre = float(0.05) #starting de-retract extra distance
        ire = float(0.05) #increment de-retract extra distance
        sds = srs #float(5) #starting de-retract speed
        ids = irs #float(5) #increment de-retract speed
        #}Ben
        lh = float(ui.layerHeight.text())
        ts = float(ui.speedTravel.text())
        lt = float(ui.layersTest.text())
        nt = float(ui.NumTests.text())


        file.write(f";Variables by Height\n")
        file.write(f";\n")
        file.write(f";Height         Retraction     De-retract      Nozzle      Fan         Extra De-retract \n")
        file.write(f";               Speed          Speed           Temp        Speed       Distance\n")
        file.write(f";\n")

        cnt = int(nt-1)

        for loopx in range(int(nt)):
            file.write(f";{int(lt)} layers      {round(Decimal(srs+irs*cnt),2)}             {round(Decimal(sds+ids*cnt),2)}             {round(Decimal(tsh+tih*cnt),2)}      {round(Decimal(fs+fsi*cnt),2)}      {round(Decimal(sre+ire*cnt),2)}\n")
            cnt = cnt-1


#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*14),2)}		{round(Decimal(tsh+tih*14),2)}		{round(Decimal(fs+fsi*14),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*13),2)}		{round(Decimal(tsh+tih*13),2)}		{round(Decimal(fs+fsi*13),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*12),2)}		{round(Decimal(tsh+tih*12),2)}		{round(Decimal(fs+fsi*12),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*11),2)}		{round(Decimal(tsh+tih*11),2)}		{round(Decimal(fs+fsi*11),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*10),2)}		{round(Decimal(tsh+tih*10),2)}		{round(Decimal(fs+fsi*10),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*9),2)}		{round(Decimal(tsh+tih*9),2)}		{round(Decimal(fs+fsi*9),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*8),2)}		{round(Decimal(tsh+tih*8),2)}		{round(Decimal(fs+fsi*8),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*7),2)}		{round(Decimal(tsh+tih*7),2)}		{round(Decimal(fs+fsi*7),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*6),2)}		{round(Decimal(tsh+tih*6),2)}		{round(Decimal(fs+fsi*6),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*5),2)}		{round(Decimal(tsh+tih*5),2)}		{round(Decimal(fs+fsi*5),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*4),2)}		{round(Decimal(tsh+tih*4),2)}		{round(Decimal(fs+fsi*4),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*3),2)}		{round(Decimal(tsh+tih*3),2)}		{round(Decimal(fs+fsi*3),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*2),2)}		{round(Decimal(tsh+tih*2),2)}		{round(Decimal(fs+fsi*2),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*1),2)}		{round(Decimal(tsh+tih*1),2)}		{round(Decimal(fs+fsi*1),2)}\n")
#        file.write(f";{int(lt)} layers		{round(Decimal(srs+irs*0),2)}		{round(Decimal(tsh+tih*0),2)}		{round(Decimal(fs+fsi*0),2)}\n")

        dx = float(ui.dimensionX.text())
        dy = float(ui.dimensionY.text())
        ps = float(ui.printSpeed.text())
        nd = float(ui.nozzleDiameter.text())
        fd = float(ui.filamentDiameter.text())
        em = float(ui.extrusionMultiplier.text())
        tb = float(ui.tempBed.text())

#Custom Gcode
        sgcode = str(ui.customGcode.toPlainText())


        file.write(f";\n")
        file.write(f";\n")
        file.write(f";All inputs\n")
        file.write(f";\n")
        file.write(f";Dimension X 					{int(dx)}\n")
        file.write(f";Dimension Y 					{int(dy)}\n")
        file.write(f";Starting Retraction Distance	{srd}\n")
        file.write(f";Increment Retraction 			{ird}\n")
        file.write(f";Start Retraction Speed 		{srs}\n")
        file.write(f";Retraction Speed Increment 	{irs}\n")
        #{Ben
        file.write(f";Starting De-Retract Speed     {sds}\n")
        file.write(f";De-Retract Speed Increment 	{ids}\n")
        file.write(f";Starting Extra De-Retract Distance {sre}\n")
        file.write(f";Increment Extra De-Restract Distance {ire}\n")
        #}Ben        
        file.write(f";Print Speed 					{ps}\n")
        file.write(f";Starting Temp 					{int(tsh)}\n")
        file.write(f";Increment Temp 				{int(tih)}\n")
        file.write(f";Bed Temp 						{int(tb)}\n")
        file.write(f";Fan Speed 						{int(fs)}\n")
        file.write(f";Fan Speed Increment 			{int(fsi)}\n")
        file.write(f";Nozzle Diameter 				{nd}\n")
        file.write(f";Layer Height 					{lh}\n")
        file.write(f";Filament Diameter 				{fd}\n")
        file.write(f";Extrusion Multiplier 			{em}\n")
        file.write(f";Layers Per Test                {lt}\n")
        file.write(f";Number of Tests                {nt}\n")
        file.write(f";\n")
        file.write(f";\n")


# Generate E Value  https://3dprinting.stackexchange.com/questions/10171/how-is-e-value-calculated-in-slic3r 

        def eValue ( extrusionLength ):

            diameterNozzle = float(ui.nozzleDiameter.text())
            heightLayer = float(ui.layerHeight.text())
            diameterFilament = float(ui.filamentDiameter.text())
            multiplierExtrusion = float(ui.extrusionMultiplier.text())

            area = (diameterNozzle - heightLayer) * heightLayer + 3.14159 * (heightLayer/2)**2
            eValueresult = (area * extrusionLength * 4)/(3.14159 * diameterFilament**2/multiplierExtrusion*1.25)
            return eValueresult


#start Gcode
        file.write(f";Start Gcode\n")
        # file.write(f"M140 S{int(tb)}\n")
        # file.write(f"M105\n")
        # file.write(f"M190 S{int(tb)}\n")
        # file.write(f"M104 S{int(tsh)}\n")
        # file.write(f"M105\n")
        # file.write(f"M109 S{int(tsh)}\n")
        # file.write(f"M82\n")
        # file.write(f"G28\n")
        # file.write(f"G92 E0\n")
        # file.write(f"G1 F200 E1\n")
        # file.write(f"G92 E0\n")

        file.write(f"PRINT_START EXTRUDER_TEMP={int(tsh)} BED_TEMP={int(tb)} MATERIAL=PLA\n")
        file.write(f"SET_PRESSURE_ADVANCE EXTRUDER=extruder ADVANCE=0.9\n")
        file.write(f"SET_GCODE_OFFSET Z=-0.06\n")
        
        file.write(f"{sgcode}\n")

        file.write(f";\n")
        file.write(f";\n")

        xpos = dx/2-30
        ypos = dy/2-30
        zpos = lh
        epos = 0
    


#Start Movement        
        file.write(f";Start Movement\n")
        file.write(f";\n")
        file.write(f"G1 Z2\n")
        file.write(f"G1 F{int(ts)*60} X{xpos} Y{ypos} Z{zpos}\n")
        file.write(f";\n")
        eValueresult = eValue(60)

#Overextruding Raft
        evalueincrease = eValueresult*1.25
        eValueresult = evalueincrease


        remx = xpos
        remy = ypos

        file.write(f";Layer 1\n")

    #Horizontal

        for loopx in range(30):
            file.write(f"G1 F{int(ps*60/2)} X{xpos+60} Y{ypos} E{round(Decimal(eValueresult),5)}\n")
            xpos = xpos + 60
            eValueresult = eValueresult + evalueincrease
            file.write(f"G0 F{int(ts)*60} X{xpos} Y{ypos+1}\n")
            ypos = ypos + 1
            file.write(f"G1 F{int(ps*60/2)} X{xpos-60} Y{ypos} E{round(Decimal(eValueresult),5)}\n")
            xpos = xpos - 60
            eValueresult = eValueresult + evalueincrease
            file.write(f"G0 F{int(ts)*60} X{xpos} Y{ypos+1}\n")
            ypos = ypos + 1

    #Bring back to raft origin

        file.write(f"G0 F{int(ts)*60} X{xpos} Y{ypos} Z{round(Decimal(lh*3),2)}\n")
        file.write(f"G0 F{int(ts)*60} X{remx} Y{remy} Z{lh+lh}\n")
        xpos = remx
        ypos = remy

        file.write(f";Layer 2\n")

    #Vertical

        for loopx in range(30):
            file.write(f"G1 F{int(ps*60/2)} X{xpos} Y{ypos+60} E{round(Decimal(eValueresult),5)}\n")
            ypos = ypos + 60
            eValueresult = eValueresult + evalueincrease
            file.write(f"G0 F{int(ts)*60} X{xpos+1} Y{ypos}\n")
            xpos = xpos + 1
            file.write(f"G1 F{int(ps*60/2)} X{xpos} Y{ypos-60} E{round(Decimal(eValueresult),5)}\n")
            ypos = ypos - 60
            eValueresult = eValueresult + evalueincrease
            file.write(f"G0 F{int(ts)*60} X{xpos+1} Y{ypos}\n")
            xpos = xpos + 1    

    #Bring back to Calibration Starting Position

        file.write(f"G0 F{int(ts)*60} X{remx+5} Y{remy+5} Z{round(Decimal(lh*3),2)}\n")

    #Relative Movements

        file.write(f"M83\n")
        file.write(f"G91\n")

    #Start Calibration

        eValueresult = eValue(10)
        corenermarker = eValue(1)

        loopbigcount = 0
        loopsmallcount = 0

        layer = 3

        cnt = int(nt)
        lt = lt - 1

        for loopbig in range(int(cnt)):

    #set Fan every 15 layers
            file.write(f"M106 S{(round(Decimal((fs+fsi*loopbigcount)) * 255 / 100,0))  }\n")
            file.write(f"M104 S{round(Decimal(tsh+tih*loopbigcount),0)}\n")

            file.write(f";Layer {layer}\n")

            file.write(f"SET_RETRACTION RETRACT_SPEED={round(Decimal((srs+irs*loopbigcount) * 60),2)} UNRETRACT_EXTRA_LENGTH={round(Decimal(sre+ire*loopbigcount),5)} UNRETRACT_SPEED={round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")

            #Layer Marker Bottom Left
            file.write(f"G1 F{int(ps*60)} X-2 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y-2 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} X2 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y2 E{round(Decimal(corenermarker),5)}\n")


            #Begin 

            #Bottom
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*0),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*0),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*0)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*1),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*1),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*1)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*2),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*2),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*2)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*3),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*3),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*3)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")

            #Layer Marker Bottom Right
            file.write(f"G1 F{int(ps*60)} X1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y-1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} X-1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y1 E{round(Decimal(corenermarker),5)}\n")

            #Right
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*4),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*4),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*4)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*5),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*5),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*5)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*6),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*6),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*6)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*7),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*7),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*7)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")

            #Layer Marker Top Right
            file.write(f"G1 F{int(ps*60)} X1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} X-1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y-1 E{round(Decimal(corenermarker),5)}\n")

            #Top
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*8),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*8),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*8)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*9),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*9),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*9)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*10),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*10),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*10)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*11),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*11),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*11)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")

            #Layer Marker Top Left
            file.write(f"G1 F{int(ps*60)} X-1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} X1 E{round(Decimal(corenermarker),5)}\n")
            file.write(f"G1 F{int(ps*60)} Y-1 E{round(Decimal(corenermarker),5)}\n")

            #Left
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*12),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*12),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*12)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*13),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*13),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*13)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*14),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*14),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*14)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            #file.write(f"G1 E{round(Decimal(srd+ird*15),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*15),5)}\n")
            file.write(f"G10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            #file.write(f"G1 E{round(Decimal((srd+ird*15)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
            file.write(f"G11\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")

            #Zup layer height

            file.write(f"G1 Z{lh}\n")
                 
#           loopbigcount = loopbigcount +1
            layer = layer + 1


            for loopsmall in range(int(lt)):

                file.write(f";Layer {layer}\n")
            #Bottom
                file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*0),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*0),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*0)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*1),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*1),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*1)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*2),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*2),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*2)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*3),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*3),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*3)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")

            #Right
                file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*4),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*4),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*4)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*5),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*5),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*5)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*6),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*6),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*6)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*7),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*7),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*7)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")

                #Top
                file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*8),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*8),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*8)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*9),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*9),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*9)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*10),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*10),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*10)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*11),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*11),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} Y10\n")
                file.write(f"G0 F{int(ts)*60} Y-10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*11)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")

            #Left
                file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*12),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*12),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*12)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*13),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*13),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*13)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*14),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*14),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*14)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
                #file.write(f"G1 E{round(Decimal(srd+ird*15),5) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
                file.write(f"SET_RETRACTION RETRACT_LENGTH={round(Decimal(srd+ird*15),5)}\n")
                file.write(f"G10\n")
                file.write(f"G0 F{int(ts)*60} X-10\n")
                file.write(f"G0 F{int(ts)*60} X10\n")
                #file.write(f"G1 E{round(Decimal((srd+ird*15)+(sre+ire*loopbigcount)),5)} F{round(Decimal((sds+ids*loopbigcount) * 60),2)}\n")
                file.write(f"G11\n")
                file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")

                file.write(f"G1 Z{lh}\n")
                layer = layer + 1

            loopbigcount = loopbigcount +1


    #End Game

    # #Raise 5mm
    #     file.write(f"G1 Z5\n")    
    # #Absolute Position
    #     file.write(f"G90\n")
    # #Home X Y
    #     file.write(f"G28 X0 Y0\n")
    # #Turn off Steppers
    #     file.write(f"M84\n")
    # #Turn off Fan
    #     file.write(f"M107\n")
    # #Turn off Hotend
    #     file.write(f"M104 S0\n")
    # #Turn off Bed
    #     file.write(f"M140 S0\n")
    #Print_End macro
        file.write(f"PRINT_END\n")




        file.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.genGcode.clicked.connect(gengcode)
    MainWindow.show()
    sys.exit(app.exec_())
