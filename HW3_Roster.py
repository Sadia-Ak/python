# Prolog
# Author: Sadia Akther
# Email: sakther1@student.gsu.edu
# Section: DSCI- 006
'''
 Purpose:
    To build team 
 Pre-conditions (input): 
    the stats of the team player 
 post-conditions (output): 
   to find the result of the the players
'''



import unittest

#def main():

brave_roster = {
    "Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
	"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266",
}
print ()
print( '*** Braves Stats ***')
print()



status = input (
 ''' Welcome to My Braves Stats! What can I do for you?
1. Search for a player
2. Add a new player
3. Remove a player

'''

)

if status == '1':
        player = input('Enter the name of the player you want to look up:')
        if player == "Austin Riley":
              print("Here's are Austin stats: AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273")
        if player == "Ronald Acuna":
               print("AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266")
        if player not in brave_roster:
               print("uh typo?", {player}, "does not play for us :)")


if status == '2':
       player = input('Enter the name of the player you want to add:')
       stats = input("Please add Matt's stats")
       new_player = {player},":",stats 
       brave_roster = {
    "Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
	"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266",
       player:stats
}

       print("Here's the complete team roster:",
              brave_roster,)
       

if status == '3':
       player = input("Enter the name of the player you want to remove:")
       if player in brave_roster:
              brave_roster.pop(player)
              print(brave_roster)
              print(player,'is no longer with Braves.')
       if player not in brave_roster:
              print("uh typo?", player, "does not play for us :)")

test_dict = {
    "Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
	"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266",
}
number = input('Please type your choice number:')
choice_number = '123'


def lookup_player(roster,name):
      if name in roster:
             return roster[name]
      else:
             return "N/A"
if number == '1': 
        lookup_player = input('Enter the name of the player you want to look up:') 
        if lookup_player in test_dict:
             print(lookup_player,":",test_dict(lookup_player))
        else:
             print('not in roster')

elif number == '2':
       add_player = input('Enter the name of the player you want to add:')
       if add_player not in test_dict:
              add_player_to_dict = input('add player stats:')
              test_dict[add_player] = add_player_to_dict
              print(test_dict)

elif number == '3':
       delete_in_dict = input('Enter the name of the player you want to remove:')
       if delete_in_dict in test_dict:
              del test_dict[delete_in_dict]
              print('this player is removed')
              print(test_dict)

#main()
              
class TestDictFunctions(unittest.TestCase):

  def test_search_player_success(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = test_dict["Austin Riley"]
    expected = lookup_player(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_search_player_no_result(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = "N/A"
    expected = lookup_player(test_dict, "Ronald Acuna")
    self.assertEqual(actual, expected)

  def test_add_player_sucess(self):
    test_dict = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"
    }
    actual = {
		"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
		"Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266"
    }
    expected = add_player_to_dict(test_dict, "Ronald Acuna", "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266")

    self.assertEqual(actual, expected)

  def test_add_player_duplicate(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    actual = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273", "Austin Riley(2)": "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214"}
    expected = add_player_to_dict(test_dict, "Austin Riley", "AB: 350, R: 20, H: 120, HR: 5, AVG: 0.214")
    self.assertEqual(actual, expected)

  def test_delete_player_sucess(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = {}
    actual = delete_in_dict(test_dict, "Austin Riley")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self):
    test_dict = {"Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273"}
    expected = test_dict
    actual = delete_in_dict(test_dict, "Shohei Ohtani")
    self.assertEqual(actual, expected)