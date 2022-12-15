opmultiparm /obj/geo1/add1 
# Print the multiparm references for /obj/geo1/add1.
opmultiparm /obj/geo1/add1 "pt#x" "../add2/pt#x" "pt#y" "../add2/pt#y" 
# Creates links between the x and y components of the pt instance parameter. 
# So any new instances of this parameter on the add1 SOP will automatically be set to channel references of the corresponding pt instance parameter on the add2 SOP.
