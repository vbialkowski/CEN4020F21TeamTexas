import Challenge_5
from tud_test_base import set_keyboard_input, get_display_output


def test_maximum_accounts_number():
    set_keyboard_input(["12"])
    Challenge_5.create(Challenge_5.accountCount())
    output = get_display_output()
    assert output == ["\nCreate A Account",
                      "\nAll permitted accounts have been created, please come back later.",
                      "\nWant to hear what students have to say about InCollege?",
                      "\nRead about how InCollege helped Ethan Timor:",
                      '\t "I was never able to land an interview or internship in college. ',
                      "\t Thankfully, I discovered InCollege and I couldn't be more thankful! ",
                      "\t Within days, I had interviews, and offers from companies like:",
                      "\t Tesla, Microsoft, Google, and Apple",
                      "\t I was able to graduate and find a starting job as the lead Senior VP of Programming at NASA.",
                      '\t It would not be possible without InCollege."',
                      "\nMenu",
                      "[1] Log In",
                      "[2] Create an Account",
                      "[3] Search for a Job",
                      "[4] Find Someone You Know",
                      "[5] Learn a New Skill",
                      "[6] Not Sure About InCollege? Watch this Video!",
                      "[7] Useful Links",
                      "[8] InCollege Important Links",
                      "[9] Personal Profile",
                      "[10] Show My Network",
                      "[11] See Friend Requests",
                      "[12] Exit the Program",
                      "Enter your option: "
                      ]