max_score = 10  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import normalize_text, load_student_code, format_error_message, exception_message_for_students, round_match, get_similarity_feedback
import re, pytest, os

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_02_excel_file_created(current_test_name):
    try:

        try:
            import pandas as pd
        except ImportError:
            exception_message_for_students(ImportError("This test requires the pandas library being installed on your computer, but pandas is not installed"), input_test_case=None, current_test_name=current_test_name) 

        # Expected data
        expected_data = pd.DataFrame({
            "city": ["Boston", "San Francisco", "Seattle"],
            "salary": [81500.00, 69000.00, 75666.67]
        })

        expected_data_str = expected_data.to_string(index=False).strip()

        expected_file_name = r"mean_salary_by_city.xlsx"

        assert os.path.isfile(expected_file_name), f"{expected_file_name} does not exist."
    
        actual_data = pd.read_excel(expected_file_name)

        actual_data_str = actual_data.to_string(index=False).strip()

        try:
            pd.testing.assert_frame_equal(actual_data, expected_data, check_dtype=False, atol=.2)
        except AssertionError as e:
            pytest.fail(format_error_message(
            custom_message=("Your 'mean_salary_by_city.xlsx' file didn't contain the expected values. "
                            f"Note that the test will still pass as long as the values are within .2 of each other:\n\n"
                            f"EXPECTED EXCEL FILE VALUES:\n"
                            f"---------------------------\n"
                            f"{expected_data_str}\n\n"
                             f"YOUR EXCEL FILE VALUES:\n"
                            f"------------------------\n"
                            f"{actual_data_str}\n\n"
                            f"HOW TO FIX IT:\n"
                            f"--------------\n"
                            f"You likely aren't following the instructions to only show the city name and the mean salary of that city, "
                            f"or you are not doing it on the filtered DataFrame.\n"
                            f"\n\n"),
            current_test_name=current_test_name,
            input_test_case=None,
            display_inputs=False,
        ))
            
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, input_test_case=None, current_test_name=current_test_name)

            