
## Rubric
Your grade is based on whether you pass the automated tests, listed below.

The tests will ignore spacing, capitalization, and punctuation, but you will fail the tests if you spell something wrong or calculate something incorrectly.


<table border="1" style="width: 100%; text-align: center;">
<thead style="text-align: center;">
    <tr>
        <th style="text-align: center;">Test</th>
        <th style="text-align: center;">Description</th>
        <th style="text-align: center;">Points</th>
    </tr>
</thead>
<tbody>
    <tr style="text-align: left">
        <td>1. Printed Messages</td>
        <td>
        <b>Input test cases used:</b> 1<br><br>
        Your printed output must be the same as the expected output of each input test case. 
        <br>
        <br>
        See the <code>descriptions_ot_test_cases</code> folder for expected printed messages for each input test case.
        </td>
        <td>85</td>
    </tr>
    <tr>
        <td>2. Excel File Created</td>
        <td style="text-align: left">
        <b>Input test cases used:</b> None<br><br>
          Your code should produce an Excel file named <code>mean_salary_by_city.xlsx</code> with the following data. The test will pass as long as the numbers are within .2 of the expected values, so don't worry about rounding.<br><br>
          <table border="1" class="dataframe">
            <thead>
                <tr style="text-align: right;">
                <th>city</th>
                <th>salary</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <td>Boston</td>
                <td>81500.00</td>
                </tr>
                <tr>
                <td>San Francisco</td>
                <td>69000.00</td>
                </tr>
                <tr>
                <td>Seattle</td>
                <td>75666.67</td>
                </tr>
            </tbody>
            </table>
        </td>
        <td>10</td>
    </tr>
    <tr>
        <td>3. Sufficient Comments</td>
        <td style="text-align: left">
        <b>Input test cases used:</b> None<br><br>
        Your code must include at least <code>5</code> comments. You can use any form of commenting:
        <ul>
          <li><code>#</code></li> 
          <li><code>''' '''</code></li>
          <li><code>""" """</code></li>
        </ul>
        </td>
        <td>5</td>
    </tr>
    <tr>
        <td colspan="2">Total Points</td>
        <td>100</td>
  </tr>
</tbody>
</table>

## Test Cases
If you fail a test during a specific test case, see the `descriptions_of_test_cases` folder for the following:
<table border="1" style="width: 100%; text-align: left;">
  <tr>
    <th>Test Case</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Input Test Case 01</td>
    <td>There are no inputs in this assignment, so only one set of possible printed messages should ever print out.</td>
  </tr>
</table>
