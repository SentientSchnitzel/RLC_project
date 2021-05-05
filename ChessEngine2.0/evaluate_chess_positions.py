
# imports all functions for testing (includes chess
from evalFuncs import *

# imports all test positions
from test_positions import *

all_tests = BK_test + sbd_test
all_sols = BK_sols + sbd_sols

depths = [1, 2, 3, 4, 5]
numTests = len(BK_test+sbd_test)

solved1 = []
accuracies1 = []
timings1 = []

solved2 = []
accuracies2 = []
timings2 = []

for depth in depths:

    s1, a1, d1 = test(BK_test, BK_sols, depth)
    solved1.append(s1)
    accuracies1.append(a1)
    timings1.append(d1)

    s2, a2, d2 = test(sbd_test, sbd_sols, depth)
    solved2.append(s2)
    accuracies2.append(a2)
    timings2.append(d2)

    print(f"At depth = {depth}\nNumber of correct solved: {s1+s2} out of {numTests}.\nWhich gives an accuracy of {round((s1+s2)/numTests*100, 2)} % in {round(d1+d2, 2)} seconds")


BK = pd.DataFrame([depths, solved1, accuracies1, timings1], index=['depth', '# solved', 'accuracy', 'time'])
sbd = pd.DataFrame([depths, solved2, accuracies2, timings2], index=['depth', '# solved', 'accuracy', 'time'])

all_pos = pd.DataFrame([depths, [s1+s2 for s1, s2 in zip(solved1, solved2)],
                        [(s1+s2)/numTests*100 for s1, s2 in zip(solved1, solved2)],
                        [t1+t2 for t1, t2 in zip(timings1, timings2)]], index=['depth', '# solved', 'accuracy', 'time'])

cum_tests = pd.concat([BK, sbd, all_pos], axis=1).round(4)
print(cum_tests)

cum_tests.round(4).to_excel('results_2.xlsx')
