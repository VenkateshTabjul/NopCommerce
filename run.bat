pytest -v -s –m "sanity" --html=Reports\report.html testCases/test_Login.py --browser chrome
rem pytest -v -s –m "regression" --html=Reports\report.html testCases/test_Login.py --browser chrome
rem pytest -v -s –m "sanity or regression" --html=Reports\report.html testCases/test_Login.py --browser chrome
rem pytest -v -s –m "sanity and regression" --html=Reports\report.html testCases/test_Login.py --browser chrome


rem is comment in bat file