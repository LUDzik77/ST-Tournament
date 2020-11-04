import unittest
from unittest.mock import Mock
from ST_controller import Controller
from ST_model import Model
from ST_view import View
import ST_SCreature
import ST_classes


class Test_ST_Model(unittest.TestCase):
    
    def setUp(self):
        print("setUP")
        
        self.c1=ST_classes.creature("top")
        self.c2=ST_classes.creature("center")
        self.c3=ST_classes.creature("down")
        self.c4=ST_classes.creature("top")
        self.c5=ST_classes.creature("center")
        self.c6=ST_classes.creature("down")
        
        self.p1=ST_classes.player("Player1", 100, 5)
        self.p2=ST_classes.player("Player2", 100, 5)        
        
        self.t1=ST_classes.SCreature(*ST_SCreature.Zergling)
        self.t2=ST_classes.SCreature(*ST_SCreature.Hydralisk)
        self.t3=ST_classes.SCreature(*ST_SCreature.Mutalisk)
        self.t4=ST_classes.SCreature(*ST_SCreature.Ultralisk)   
        
        self.p1.board={"top":self.c1, "center":self.c2, "down":self.c3}
        self.p2.board={"top":self.c4, "center":self.c5, "down":self.c2}
        
        self.p1.race = "zerg"
        self.p2.race = "zerg"
        
        self.p1.options= [self.t1,self.t2,self.t3,self.t4, self.t1]
        self.p2.options= [self.t1,self.t2,self.t3,self.t4, self.t1]
        
        self.active_player = self.p1
        self.inactive_player = self.p2        
        
        self.name_of_played_creature = ""        
        
    def tearDown(self):
        print("tearDown\n")
    
    def test_len_player_options(self):
        print("test_len_player_options")
        self.assertEqual(len(self.p1.options), 5)
        self.assertEqual(len(self.p2.options), 5)
        
    def test_len_player_board(self):
        print("test_len_player_board")
        self.assertEqual(len(self.p1.board), 3)
        self.assertEqual(len(self.p2.board), 3)
        
    def test_stat_display(self):
        print("test_creatures_data")
        self.assertEqual(self.p1.board["top"].stat_display(), "placeholder")
        self.assertEqual(self.p1.board["center"].stat_display(), "placeholder")
        self.assertEqual(self.p1.board["down"].stat_display(), "placeholder")
        self.p1.board={"top":self.t1, "center":self.c2, "down":self.c3}
        self.assertEqual(self.p1.board["top"].stat_display(), "zergling: 2 / 5(0)")
        mock = Mock()
        print(mock)
        
    #WHY it isn't working?
    @patch('ST_model.p1.board')
    def test_creature_data(self, mock_write): 
        self.assertEqual(mock_write["top"].stat_display(), "placeholder")
        #self.assertEqual(self.creatures_data(), 
                         #("placeholder", "placeholder", "placeholder", "placeholder","placeholder","placeholder"))

    #def test_find_data_for_creature_photo(self)

#player_description_data


if __name__ == '__main__':
    unittest.main()
