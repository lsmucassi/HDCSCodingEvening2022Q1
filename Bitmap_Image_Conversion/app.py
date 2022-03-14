
time_in_bits = [ 
    "11101000001010100",
    "01001110000100111",
    "11000010101100001",
    "11101110001110111",
    "10101010100010101",
    "10101000101010101",
    "10101000101010100",
    "11101110001110001",
    "11101110001110111",
    "11100010001110001",
    "10101110001110111",]

stime = "05:44"

def split_time(stime):
    return [int(num) for num in stime]

def to_bit_string(stime):
    time_list = []
    #making sure the time is 5 cgars long
    if len(stime) == 5:
        split_stime = stime.split(":")
        
        for x in split_stime:
            time_list.append(split_time(x))
        flat_list = [item for sublist in time_list for item in sublist]
        print(flat_list)

        print(time_in_bits[flat_list[0]]+time_in_bits[flat_list[1]]+time_in_bits[10]+time_in_bits[flat_list[2]]+time_in_bits[flat_list[3]])
    else:
        print("Incorrect Time Formats")

to_bit_string(stime)