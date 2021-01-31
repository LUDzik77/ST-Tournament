import unittest
from unittest.mock import Mock, MagicMock, patch
from ST_controller import Controller
from ST_model import Model
from ST_view import View
import ST_SCreature
import ST_classes



class Test_ST_Model(unittest.TestCase):
    print("> StarCraft Tournament unittests <")
    
    def setUp(self):
        
        self.test_m = Model("mock") 
        
        self.test_m.c1=ST_classes.creature("top")
        self.test_m.c2=ST_classes.creature("center")

        self.test_m.p1=ST_classes.Terran_player("Mock1", 50, 15, 15, "#cc0000")
        self.test_m.p2=ST_classes.Terran_player("Mock2", 50, 15, 15, "#cc0000")       
         
        self.test_m.t1=ST_classes.SCreature(*ST_SCreature.Zergling)
        self.test_m.t2=ST_classes.SCreature(*ST_SCreature.Hydralisk)
        self.test_m.t3=ST_classes.SCreature(*ST_SCreature.Mutalisk)
        self.test_m.t4=ST_classes.SCreature(*ST_SCreature.Ultralisk)   
        
        self.test_m.p1.board={"top":self.test_m.c1, "center":self.test_m.c1, "down":self.test_m.c1}
        self.test_m.p2.board={"top":self.test_m.c2, "center":self.test_m.c2, "down":self.test_m.c2}
        
        self.test_m.p1.options = [self.test_m.t1, self.test_m.t2, self.test_m.t3, self.test_m.t4, self.test_m.t1]
        self.test_m.p2.options = [self.test_m.t1, self.test_m.t2, self.test_m.t3, self.test_m.t4, self.test_m.t1]
        
        self.test_m.active_player = self.test_m.p1
        self.test_m.inactive_player = self.test_m.p2        
        
        self.test_m.upgrade_1 = ST_classes.upgrade("Mock", (0,0), "mock", "mock")
        self.test_m.game_memo_archive = "mock"
        self.test_m.name_of_played_creature = "mock"        
       
        self.Mockedboard = MagicMock(return_value={"top":self.test_m.c1, "center":self.test_m.c1, "down":self.test_m.c1})        
           
       
    def tearDown(self): 
        pass
    
    def test_player_color(self):
        print("test_player_color")
        self.assertEqual(self.test_m.player_color("active_player"), "#cc0000")
        self.assertEqual(self.test_m.player_color("p1"), "#cc0000")
        with self.assertRaises(UnboundLocalError):
            self.test_m.player_color("active player")
            self.test_m.player_color("Mock!") 
            
    def test_initialize_resources(self):
        print("test_initialize_resources")
        self.test_m._initialize_resources()
        self.assertIn(self.test_m.min_top_p1.resources, [1000+x for x in range(1500)])
        self.assertIn(self.test_m.gas_top_p1.resources, [800+x for x in range(1000)])
        self.assertTupleEqual(self.test_m.all_minerals_and_gas ,\
                             (self.test_m.min_top_p1, self.test_m.min_down_p1, self.test_m.gas_top_p1, self.test_m.gas_down_p1,\
                              self.test_m.min_top_p2, self.test_m.min_down_p2, self.test_m.gas_top_p2, self.test_m.gas_down_p2))
        
    def test_initialize_creature_prototypes(self):
        print("test_initialize_creature_prototypes")
        self.test_m._initialize_creature_prototypes()
        self.assertTrue(isinstance(self.test_m.protoss0, ST_classes.SCreature))
        self.assertEqual(self.test_m.zerg2.name, "Hydralisk")    
        
    def test_upgrade_other_effect(self): 
        print("test_upgrade_other_effect", end=" ")
        self.test_m.upgrade_other_effect(self.test_m.upgrade_1)
        result = self.test_m.p1.hp
        self.assertEqual(result, 50)
        self.test_m.upgrade_1.name = "Plasma Shield"
        self.test_m.upgrade_other_effect(self.test_m.upgrade_1)
        result = self.test_m.p1.hp
        self.assertEqual(result, 55)        
    
    def test_caption_trim(self):
        print("test_caption_trim")
        self.assertIn(self.test_m.caption_trim("detector-->top"), ["top","center", "down"])
        self.assertEqual(self.test_m.caption_trim("detector-->down"), "down")
        self.assertNotIn(self.test_m.caption_trim("Mock"), ["top","center", "down"])
        
    def test_len_player_options(self):
        print("test_len_player_options")
        self.assertEqual(len(self.test_m.p1.options), 5)
        self.assertEqual(len(self.test_m.p2.options), 5)
        
    def test_len_player_board(self):
        print("test_len_player_board")
        self.assertEqual(len(self.test_m.p1.board), 3)
        self.assertEqual(len(self.test_m.p2.board), 3)
        
    def test_stat_display(self):
        print("test_creatures_data")
        self.assertEqual(self.test_m.p1.board["top"].stat_display(), "no unit")
        self.assertEqual(self.test_m.p1.board["center"].stat_display(), "no unit")
        self.assertEqual(self.test_m.p1.board["down"].stat_display(), "no unit")
        self.test_m.p1.board={"top":self.test_m.t1, "center":self.test_m.c1, "down":self.test_m.c1}
        self.assertEqual(self.test_m.p1.board["top"].stat_display(), "Zergling 2/4(land)")

    def test_decode_detector_instructions(self):
        print("test_decode_detector_instructions")
        result1 = self.test_m.decode_detector_instructions("0123456789qwertyuiop", "012345678qwertyuiop")
        self.assertNotIn(result1[0], ["top","center", "down"])
        self.assertNotIn(result1[1], ["top","center", "down"])
        result2 = self.test_m.decode_detector_instructions("move from down", "move to top")
        self.assertIn(result2[0], ["top","center", "down"])
        self.assertIn(result2[1], ["top","center", "down"])
        
    def test_initialize_board_data(self):
        print("test_initialize_board_data")
        self.test_m._initialize_board_data()
        self.assertEqual(self.test_m.c3.name, "<placeholder>")
        self.assertEqual(self.test_m.p1.board, {"top":self.test_m.c1, "center":self.test_m.c2, "down":self.test_m.c3})

    def test_all_board_objects(self):
        print("test_all_board_objects")
        self.assertListEqual(self.test_m.all_board_objects(), \
                              [self.test_m.p1.board["top"],self.test_m.p1.board["center"],\
                               self.test_m.p1.board["down"],self.test_m.p2.board["top"],\
                               self.test_m.p2.board["center"],self.test_m.p2.board["down"]]  
                              )

    def test_board_by_placement(self):
        print("test_board_by_placement")
        self.assertEqual(self.test_m.board_by_placement("top"), 1)
        self.test_m.active_player = self.test_m.p2
        self.assertEqual(self.test_m.board_by_placement("top"), 4)
              
    def test_is_empty_board_place(self):
        print("test_is_empty_board_place")
        self.assertTrue(self.test_m.is_any_empty_board_place())
        self.test_m.active_player = self.test_m.p1
        self.test_m.p1.board["top"] = self.test_m.t1
        self.test_m.p1.board["center"] = self.test_m.t2
        self.test_m.p1.board["down"] = self.test_m.t3
        self.assertTrue(not (self.test_m.is_any_empty_board_place()))
        
  

        
        #with patch('ST_model.Model.all_initializations') as PATCHING2:   ### no sense, but it is working
            #PATCHING2.return_value=1
            #print(PATCHING2()) 
        
        #with patch('ST_model.ST_classes.creature.stat_display') as PATCHING:   ###no sense, but it is working
            #PATCHING.return_value={"top":self.test_m.c1, "center":self.test_m.c1, "down":self.test_m.c1}
            #print(PATCHING())

   
        

   
    
    #def creatures_data(self):
        #results=(self.p1.board["top"].stat_display(), 
                #self.p1.board["center"].stat_display(),
                #self.p1.board["down"].stat_display(),
                #self.p2.board["top"].stat_display(),
                #self.p2.board["center"].stat_display(),
                #self.p2.board["down"].stat_display() )
        #return(results)    


        
    #@patch.object(SomeClass, 'class_method')
    #def test_creature_data(self): 
        #fake= Mock(return_value = "placeholder")
        #self.assertEqual(self.model.creatures_data(), 
                         #(fake,fake,fake,fake,fake,fake))
  
        
        
     
    #def test_find_data_for_creature_photo(self)

    #player_description_data


if __name__ == '__main__':
    unittest.main()
