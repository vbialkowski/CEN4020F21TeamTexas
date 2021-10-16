import Challenge_5
from tud_test_base import set_keyboard_input, get_display_output


def test_max_jobs_posted():
    set_keyboard_input(["1", "2", "12"])
    Challenge_5.signedIn = True
    Challenge_5.searchJob()
    output = get_display_output()
    assert output == ["\nSearch for a Job",
                        "[1] Post a Job",
                        "[2] Return to menu",
                        "Enter Your Option: ",
                        "\nPost a Job!",
                        "There are already 5 jobs posted!",
                        "\nSearch for a Job",
                        "[1] Post a Job",
                        "[2] Return to menu",
                        "Enter Your Option: ",
                        "Returning to Menu",
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