from pprint import pprint

def shuttle_vs_walk(test_case):
    if test_case['tot_walk_time'] < test_case['shuttle_time']:
        return "%d Walk" % test_case['tot_walk_time']
    else:
        return "%d Shuttle" % test_case['shuttle_time']

tests = []

with open('shuttle.txt', 'r') as f:
    no_of_tests = int(next(f))
    for _ in range(no_of_tests):
        start, destination = next(f).split() #read one line
        test = {'start':start, 'destination':destination, 'tot_walk_time': 0}
        no_of_paths = int(next(f))
        for _ in range(no_of_paths):
            path = next(f).split(" ")
            path_walk_time = int(path[2])
            test['tot_walk_time'] += path_walk_time
        test['shuttle_time'] = int(next(f).rstrip())
        tests.append(test)

testNum = 0
for test in tests:
    print "Case #%d: " % testNum + shuttle_vs_walk(test)
    testNum += 1
