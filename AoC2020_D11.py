import numpy as np

def update_seating(floor_plan):
    # floor_plan: 2_D array
    x_size,y_size = floor_plan.shape
    new_plan = floor_plan*0
    changed=False
    for i in range(0,x_size):
        for j in range (0,y_size):
            if floor_plan[i,j] !=0:
                start_x = 0 if i==0 else i-1
                end_x = x_size if i==x_size-1 else i+2
                start_y = 0 if j== 0 else j-1
                end_y = y_size if j==y_size-1 else j+2
                if j == y_size:
                    print(j)
                curr_window= floor_plan[start_x:end_x, start_y:end_y]
                if floor_plan[i,j]==1:
                    if not sum(curr_window.flatten())>9:
                        new_plan[i,j]=8
                        changed=True
                    else: new_plan[i,j]=1
                if floor_plan[i,j]==8:
                    if sum(curr_window.flatten())>39:
                        new_plan[i,j]=1
                        changed=True
                    else: new_plan[i,j]=8
    return new_plan,changed





seat_mapper = lambda s: 1 if s == b'L' else 0
converters = {i: seat_mapper for i in range(95)}
floor_plan= np.genfromtxt("input_D11", delimiter=1, converters=converters, dtype=int, comments=None)
changed =  True
while changed:
    floor_plan,changed=update_seating(floor_plan)
    print(floor_plan)
    print('\n')
occupied_seats= sum( int(k) == 8 for k in floor_plan.flatten())
print(f' solution 1 : {occupied_seats}')
