import json
import csv
import pandas
import math
from Elevator import Elevator
from Call import Call
from Building import Building

class Algo:

    def __init__(self):
        self.B = self.getbulding()
        self.C = self.getcalls()
        self.indexes = []

    # Loading JSON files.
    def getbulding(self):
        with open('B5.json') as B1:
            B1 = json.load(B1)
            E =[]
            min = B1['_minFloor']
            max = B1['_maxFloor']
            the_elevator = B1['_elevators']
            for c in the_elevator:
                E.append((Elevator(c['_id'], c['_speed'], c['_minFloor'], c['_maxFloor'], c['_closeTime'],
                                   c['_openTime'], c['_startTime'], c['_stopTime'])))
            B = Building(min, max, E)
            return B

    def getcalls(self):
        C1 = pandas.read_csv('Calls_d.csv', header=None)
        return C1

    # Offline Algorithm
    def OurCalculation(self, e, c):
        if e.minFloor != c.src:
            t1 = e.closeTime + e.startTime + (abs(e.currentPos - c.src))*e.speed + e.stopTime + e.openTime
            t2 = e.closeTime + e.startTime + (abs(c.src - c.dest))*e.speed + e.stopTime + e.openTime
            return t1 + t2
        else:
            return (e.currentPos-c.src)*e.speed+e.closeTime + e.startTime + (abs(c.src - c.dest))*e.speed + e.stopTime + e.openTime

    def MyAlgo(self):
        c = self.C.values
        My_Elevators_List = self.B.eles
        for call in c:
            List_Of_Total_Speed_Time = []
            oneCall = Call(call[0], call[1], call[2], call[3], call[4], call[5])
            for elevator in My_Elevators_List:
                if self.can_do_it(oneCall,elevator)==1:
                    List_Of_Total_Speed_Time.append(self.OurCalculation(elevator, oneCall))
                else:
                    List_Of_Total_Speed_Time.append(-1)
            OurRequiredTST = List_Of_Total_Speed_Time[0]
            for ind in List_Of_Total_Speed_Time:
                if ind < OurRequiredTST and ind !=-1:
                    OurRequiredTST = ind
            OurRequiredIndex = List_Of_Total_Speed_Time.index(OurRequiredTST)
            self.indexes.append(My_Elevators_List[OurRequiredIndex].id)
            My_Elevators_List[OurRequiredIndex].setCurrentPos(oneCall.dest)

    def can_do_it(self, mycall ,myelve):
        if mycall.src <= myelve.maxFloor and mycall.src >= myelve.minFloor and mycall.dest <= myelve.maxFloor and mycall.dest >= myelve.minFloor :
            return 1
        else:
            return 0
    def save_to_csv(self):
        with open("Calls_d.csv",'r') as file:
            read=csv.reader(file)
            i=0
            with open("out_5_4.csv",'w',newline="") as out :
                write=csv.writer(out)
                for line in read:
                    line[5]=self.indexes[i]
                    if line[5] ==16 :
                        line[5]=13
                    i=i+1
                    write.writerow(line)
            file.close()

if __name__ == "__main__":
    A = Algo()
    A.MyAlgo()
    A.save_to_csv()
