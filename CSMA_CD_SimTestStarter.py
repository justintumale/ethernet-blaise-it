import CSMA_CD_Simulator, Station
import unittest
from Event import Event
from Frame import Frame



class CSMA_CD_SimulatorTest(unittest.TestCase):
    '''Test class for the CSMA_CD Simulator'''


    def testAddEvent(self):
        #test adding events to the simulator
        simulator = CSMA_CD_Simulator.CSMA_CD_Simulator(500) #500 meters diameter
        station1 = Station.Station(1,20.0)
        station2 = Station.Station(2,80.0)
        simulator.addStation(station1)
        simulator.addStation(station2)
        msg1 = Frame(1,'Hello Station 2',1,2)
        msg2 = Frame(2,'Hello Station 1',2,1)
        evt1 = Event(Event.ARRIVAL,123.45,1,msg1)
        evt2 = Event(Event.ARRIVAL,234.56,2,msg2)
        simulator.addEvent(evt2)
        simulator.addEvent(evt1) # not in time order
        evtQ = simulator.evtQ
        self.assertEquals(evtQ._qsize(),2)


    def testScheduleCompletion(self):
        #Verify scheduling completion of an arrival
        simulator = CSMA_CD_Simulator.CSMA_CD_Simulator(500)
        #create first station
        station1 = Station.Station(1,20.0)
        #create second station
        station2 = Station.Station(2,40.0)
        #add stations to simulator
        simulator.addStation(station1)
        simulator.addStation(station2)

        #create frame
        msg1 = Frame(1,'Hello Station 2',1,2)

        #create event
        evt1 = Event(Event.ARRIVAL,123.45, 1, msg1)

        #add event to q
        simulator.addEvent(evt1)

        #process event
        simulator.processSingleEvent()
        evtQ = simulator.evtQ
        self.assertEquals(evtQ._qsize(),2)

        #evt2 = evtQ[0]
        evt2 = evtQ.get()
        self.assertEquals(evt2.eventType,Event.TRANSMIT_COMPLETE)
        self.assertAlmostEquals(evt2.time,126.73)
        self.assertEquals(evt2.stationId,1)
        #evt3 = evtQ[1]
        evt3 = evtQ.get()


    def testMediaBusy(self):
        #Test whether the media is bus
        simulator2 = CSMA_CD_Simulator.CSMA_CD_Simulator(500)
        station1 = Station.Station(1,20.0)
        station2 = Station.Station(2,40.0)
        simulator2.addStation(station1)
        simulator2.addStation(station2)
        msg1 = Frame(1,'Hello Station 2',1,2)
        evt1 = Event(Event.ARRIVAL,123.45,1,msg1)
        simulator2.addEvent(evt1)

        simulator2.processSingleEvent() #should transmit msg
                                       #and schedule completion

        self.assertFalse(simulator2.media_busy(40,123.50))
        self.assertTrue (simulator2.media_busy(40,123.60))
        #check media after the transmission is completed at 126.73
        self.assertFalse(simulator2.media_busy(40,126.85))
        self.assertTrue (simulator2.media_busy(60,126.85))




    def testCollisionDetect(self):
        #Verify that both stations detect a collision
        simulator = CSMA_CD_Simulator.CSMA_CD_Simulator(500)
        station1 = Station.Station(1,20.0)
        simulator.addStation(station1)
        msg1 = Frame(1,'Hello Station 2',1,2)
        evt1 = Event(Event.ARRIVAL,123.45,1,msg1)
        station2 = Station.Station(2,40.0)
        simulator.addEvent(evt1)
        simulator.addStation(station1)
        simulator.addStation(station2)
        msg2 = Frame(2,'Hello Station 1',2,1)
        evt2 = Event(Event.ARRIVAL,123.50,2,msg2)
        simulator.addEvent(evt2)
        simulator.processSingleEvent()

        self.assertAlmostEquals(simulator.simTime,123.45)
        simulator.processSingleEvent() #should transmit msg2
                                       #and schedule collision detection

        evtQ = simulator.evtQ
        self.assertEquals(evtQ._qsize(),2)
        evt3 = evtQ.get()
        self.assertEquals(evt3.eventType,Event.COLLISION_DETECT)
        self.assertAlmostEquals(evt3.time,123.45, 0)
        self.assertEquals(evt3.stationId, 2)
        evt4 = evtQ.get()
        self.assertEquals(evt4.eventType,Event.COLLISION_DETECT)
        self.assertAlmostEquals(evt4.time,126.45, 0)
        self.assertEquals(evt4.stationId,1)

        def testJamming(self):
            simulator = CSMA_CD_Simulator.CSMA_CD_Simulator(500)
            station1 = Station.Station(1,20.0)
            simulator.addStation(station1)
            msg1 = Frame(1,'Hello Station 2',1,2)
            evt1 = Event(Event.ARRIVAL,123.45,1,msg1)
            station2 = Station.Station(2,40.0)
            simulator.addEvent(evt1)
            simulator.addStation(station1)
            simulator.addStation(station2)
            msg2 = Frame(2,'Hello Station 1',2,1)
            evt2 = Event(Event.ARRIVAL,123.50,2,msg2)
            simulator.addEvent(evt2)
            simulator.processSingleEvent()

            self.assertAlmostEquals(simulator.simTime,123.45)
            simulator.processSingleEvent() #should transmit msg2
                                           #and schedule collision detection

            evtQ = simulator.evtQ
            self.assertEquals(evtQ._qsize(),2)
            evt3 = evtQ.get()
            self.assertEquals(evt3.eventType,Event.COLLISION_DETECT)
            self.assertAlmostEquals(evt3.time,123.45, 0)
            self.assertEquals(evt3.stationId, 2)
            evt4 = evtQ.get()
            self.assertEquals(evt4.eventType,Event.COLLISION_DETECT)
            self.assertAlmostEquals(evt4.time,126.45, 0)
            self.assertEquals(evt4.stationId,1)
            #test jamming
            simulator.processSingleEvent()
            evt4 = evtQ.get()
            self.assertEquals(evt4.eventType,Event.JAMMING_END)
            simulator.processSingleEvent()
            evt5 = evtQ.get()
            self.assertEquals(evt5.eventType,Event.JAMMING_END)

        def testBackoff1(self):
            #Test retransmission after one collision, using specified
            #rather than random backoff
            simulator = CSMA_CD_Simulator.CSMA_CD_Simulator(500)
            station1 = Station.Station(1,20.0)
            simulator.addStation(station1)
            msg1 = Frame(1,'Hello Station 2',1,2)
            evt1 = Event(Event.ARRIVAL,123.45,1,msg1)
            station2 = Station.Station(2,40.0)
            simulator.addEvent(evt1)
            simulator.addStation(station1)
            simulator.addStation(station2)
            msg2 = Frame(2,'Hello Station 1',2,1)
            evt2 = Event(Event.ARRIVAL,123.50,2,msg2)
            simulator.addEvent(evt2)
            simulator.processSingleEvent()

            self.assertAlmostEquals(simulator.simTime,123.45)
            simulator.processSingleEvent() #should transmit msg2
                                           #and schedule collision detection

            evtQ = simulator.evtQ
            self.assertEquals(evtQ._qsize(),2)
            evt3 = evtQ.get()
            self.assertEquals(evt3.eventType,Event.COLLISION_DETECT)
            self.assertAlmostEquals(evt3.time,123.45, 0)
            self.assertEquals(evt3.stationId, 2)
            evt4 = evtQ.get()
            self.assertEquals(evt4.eventType,Event.COLLISION_DETECT)
            self.assertAlmostEquals(evt4.time,126.45, 0)
            self.assertEquals(evt4.stationId,1)

            simulator.processSingleEvent()
            evt4 = evtQ.get()
            self.assertEquals(evt4.eventType,Event.JAMMING_END)
            simulator.processSingleEvent()
            evt5 = evtQ.get()
            self.assertEquals(evt5.eventType,Event.JAMMING_END)

            simulator.processSingleEvent()
            simulator.set_back_off_time(1.5)
            evt6 = evtQ.get()
            self.assertEquals(evt6.eventType,Event.TRANSMIT_ATTEMPT)
            self.assertAlmostEquals(evt6.time, 126.45 + 1.5)

            simulator.processSingleEvent()
            simulator.set_back_off_time(.9)
            evt7 = evtQ.get()
            self.assertEquals(evt7.eventType,Event.TRANSMIT_ATTEMPT)
            self.assertAlmostEquals(evt7.time, 126.45 + .9)



        def testBackoff2(self):
            #Test retransmission after two collisions, using specified
            #rather than random backoff
            simulator = CSMA_CD_Simulator.CSMA_CD_Simulator(500)
            station1 = Station.Station(1,20.0)
            simulator.addStation(station1)
            msg1 = Frame(1,'Hello Station 2',1,2)
            evt1 = Event(Event.ARRIVAL,123.45,1,msg1)
            station2 = Station.Station(2,40.0)
            simulator.addEvent(evt1)
            simulator.addStation(station1)
            simulator.addStation(station2)
            msg2 = Frame(2,'Hello Station 1',2,1)
            evt2 = Event(Event.ARRIVAL,123.50,2,msg2)
            simulator.addEvent(evt2)
            simulator.processSingleEvent()

            self.assertAlmostEquals(simulator.simTime,123.45)
            simulator.processSingleEvent() #should transmit msg2
                                           #and schedule collision detection

            evtQ = simulator.evtQ
            self.assertEquals(evtQ._qsize(),2)
            evt3 = evtQ.get()
            self.assertEquals(evt3.eventType,Event.COLLISION_DETECT)
            self.assertAlmostEquals(evt3.time,123.45, 0)
            self.assertEquals(evt3.stationId, 2)
            evt4 = evtQ.get()
            self.assertEquals(evt4.eventType,Event.COLLISION_DETECT)
            self.assertAlmostEquals(evt4.time,126.45, 0)
            self.assertEquals(evt4.stationId,1)

            simulator.processSingleEvent()
            evt4 = evtQ.get()
            self.assertEquals(evt4.eventType,Event.JAMMING_END)
            simulator.processSingleEvent()
            evt5 = evtQ.get()
            self.assertEquals(evt5.eventType,Event.JAMMING_END)

            simulator.processSingleEvent()
            simulator.set_back_off_time(1.5)
            evt6 = evtQ.get()
            self.assertEquals(evt6.eventType,Event.TRANSMIT_ATTEMPT)
            self.assertAlmostEquals(evt6.time, 126.45 + 1.5)

            simulator.processSingleEvent()
            simulator.set_back_off_time(.9)
            evt7 = evtQ.get()
            self.assertEquals(evt7.eventType,Event.TRANSMIT_ATTEMPT)
            self.assertAlmostEquals(evt7.time, 126.45 + .9)


            simulator.processSingleEvent()
            evt8 = evtQ.get()
            self.assertEquals(evt8.eventType, Event.COLLISION_DETECT)
            evt9 = evtQ.get()
            self.assertEquals(evt9.eventType, Event.COLLISION_DETECT)
            evt10 = evtQ.get()
            self.assertEquals(evt10.eventType, Event.JAMMING_END)
            evt11 = evtQ.get()
            self.assertEquals(evt11.eventType, Event.JAMMING_END)

            simulator.processSingleEvent()
            simulator.set_back_off_time(1.7)
            evt6 = evtQ.get()
            self.assertEquals(evt6.eventType,Event.TRANSMIT_ATTEMPT)
            self.assertAlmostEquals(evt6.time, 126.45 + 1.7)

            simulator.processSingleEvent()
            simulator.set_back_off_time(.3)
            evt7 = evtQ.get()
            self.assertEquals(evt7.eventType,Event.TRANSMIT_ATTEMPT)
            self.assertAlmostEquals(evt7.time, 126.45 + .3)

if __name__ == '__main__':
    unittest.main()
