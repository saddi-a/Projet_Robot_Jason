import RPi.GPIO as GPIO
import time  # permet des pause pour l'affichage de feux


GPIO.setwarnings(False) # annulation des interruption
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD) # affectation des pin

class Feutricolore:
    def __init__(self,Rouge,Orange,Vert):
           self.Rouge=Rouge
           self.Orange=Orange
           self.Vert=Vert
           GPIO.setup(self.Rouge, GPIO.OUT, initial=GPIO.LOW)
           GPIO.setup(self.Orange, GPIO.OUT, initial=GPIO.LOW)
           GPIO.setup(self.Vert, GPIO.OUT, initial=GPIO.LOW)

    def ActRouge(self):
        GPIO.output(self.Rouge,GPIO.HIGH)
        GPIO.output(self.Orange,GPIO.LOW)
        GPIO.output(self.Vert,GPIO.LOW)
        
    def ActOrange(self):
        GPIO.output(self.Rouge,GPIO.LOW)
        GPIO.output(self.Orange,GPIO.HIGH)
        GPIO.output(self.Vert,GPIO.LOW)
        
    def ActVert(self):
        GPIO.output(self.Rouge,GPIO.LOW)
        GPIO.output(self.Orange,GPIO.LOW)
        GPIO.output(self.Vert,GPIO.HIGH)

F1_Vert=36#gpio16
F1_Orange=38#gpio20
F1_Rouge=40#gpio21

F2_Vert=33#gpio13
F2_Orange=35#gpio19
F2_Rouge=37#gpio26

F1 = Feutricolore(F1_Rouge,F1_Orange,F1_Vert)
F2 = Feutricolore(F2_Rouge,F2_Orange,F2_Vert)  

periode = 2 #duree d une periode en seconde

duree_vert_rouge=6/periode# duree en seconde
duree_rouge_orange=2/periode
duree_rouge_rouge=2/periode
nb_count = duree_rouge_rouge

phase = 'F1r_F2r2' #'F1r_F2v' 'F1r_F2o' , 'F1r_F2r1', 'F1v_F2r','F1o_F2v'



#pinBtn = 12
#GPIO.setup(pinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True :

    if (phase == 'F1r_F2v'):
        nb_count -= 1
        if (nb_count > 0) :
            F1.ActRouge();F2.ActVert();
        else:
            phase = 'F1r_F2o';nb_count = duree_rouge_orange
            
    if (phase == 'F1r_F2o'):
        nb_count -= 1
        if (nb_count > 0) :
            F1.ActRouge();F2.ActOrange();
        else:
            phase = 'F1r_F2r1';nb_count = duree_rouge_rouge
            
    if (phase == 'F1r_F2r1'):
        nb_count -= 1
        if (nb_count > 0) :
            F1.ActRouge();F2.ActRouge();
        else:
            phase = 'F1v_F2r';nb_count = duree_vert_rouge
            
    if (phase == 'F1v_F2r'):
        nb_count -= 1
        if (nb_count > 0) :
            F1.ActVert();F2.ActRouge();
        else:
            phase = 'F1o_F2r';nb_count = duree_rouge_orange
            
    if (phase == 'F1o_F2r'):
        nb_count -= 1
        if (nb_count > 0) :
            F1.ActOrange();F2.ActRouge();
        else:
            phase = 'F1r_F2r2';nb_count = duree_rouge_rouge 

    if (phase == 'F1r_F2r2'):
        nb_count -= 1
        if (nb_count > 0) :
            F1.ActRouge();F2.ActRouge();
        else:
            phase = 'F1r_F2v';nb_count = duree_vert_rouge         
    
    
    time.sleep(periode)
    
GPIO.cleanup()
GPIO.setwarnings(True)

