from operator import itemgetter, attrgetter
def parse_busses(busLine):
    items = busLine.split(',')

    busses = []
    for i in items:
        try:
            busses.append(int(i))
        except:
            pass
    return busses

def parse_bus_positions(busLine):
    items = busLine.split(',')
    buspositions = []
    time = 0
    for i in items:
        try:
            buspositions.append((int(i),time))
        except:
            pass
        time+=1
    return buspositions

def next_bus(earliest, busses):
    delay = [i - earliest % i for i in busses]
    min_delay = delay.index(min(delay))
    return (busses[min_delay],min(delay))

def calcTimePoint(buspositions):
    sortedBusses = sorted(buspositions, key=itemgetter(0), reverse=True)
    timepoint = sortedBusses[0][0] - sortedBusses[0][1]
    timeNotFound = True
    while timeNotFound:
        timeWorking = True
        for busposition in sortedBusses:
            if (timepoint + busposition[1]) % busposition[0] != 0:
                timeWorking = False
                break
        if timeWorking:
            timeNotFound = False
        else:
            timepoint += sortedBusses[0][0]
    return timepoint


with open('input_D13') as fi:
    data = fi.readlines()
    earliest = int(data[0])
    busses = parse_busses(data[1])
    bus_ID, delay = next_bus(earliest,busses)
    print(f'solution 1 is {bus_ID*delay}')

with open('input_D13') as fi:
    data = fi.readlines()
    busses = parse_bus_positions(data[1])
    timepoint = calcTimePoint(busses)
    print(f'solution 2 is {timepoint}')