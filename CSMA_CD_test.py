import unittest
import CSMA_CD_Simulator
import queue
import time
'''
1. initialization code for CSMA_CD_Simulator. Load the simulator with four or five ARRIVAL
events (in chronological order) and check that the event queue has the correct number of
events and that the event objects have the correct data.
'''


'''
2.	Load the simulator with four or five TRANSMISSION_ATTEMPT events, and then insert TRANSMIT_COMPLETE
and RECEPTION_COMPLETE events for these transmission attempts (assuming no collisions, etc.). Arrange the
parameters so that the completion events are interleaved with the transmission events. Test not only the
ordering of the events but also their timing; that is, use simulator class methods to compute the completion
time, but put literal values in the assertions. Use assertAlmostEquals, not assertEquals, to compare floating
point values.
'''

'''
3.	Test Example 1 above, verifying that the additional TRANSMISSION_ATTEMPT event has been added at the
appropriate time.
'''

'''
4.	Test Example 2 above, verifying that the additional COLLISION_DECTECT, JAMMING_END, AND TRANSMISSION_ATTEMPT
events has been added at the appropriate time and that the completion events have been removed.To  this part, you
will need to replace the random binary exponential backoff with predictable backoffs
(1,1,3,6,14,22,51,122,201,455, 985, 985, 985, 985, 985, 985). You can leave these in place for the simulation run.
'''

class CSMA_CD_test(unittest.TestCase):
    simulator = CSMA_CD_Simulator.CSMA_CD_Simulator()
    time_ = ''

    def test_create_events(self):
        self.time_ = time.time()
        result = self.simulator.create_event(self.time_, 1, "Hello simulator.")
        self.assertTrue(result)

    def test_get_events(self):
        queue = self.simulator.get_events()
        event1 = queue.get()
        self.assertTrue(1, event1.stationId)
        self.assertTrue("Hello simulator.", event1.msg)


if __name__ == '__main__':
    unittest.main()
