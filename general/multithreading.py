# import time
# import threading

# def calc_square(arr):
#     print("Calculate square of a number.")
#     for a in arr:
#         time.sleep(0.2)
#         print({f"square of {a} is:{a*a}"})

# def calc_cube(arr):
#     print("Calculate cube of a number.")
#     for a in arr:
#         time.sleep(0.2)
#         print({f"cube of {a} is:{a*a*a}"})


# arr=[3,4,5,12,7,8]

# if __name__=='__main__':
#     t=time.time()
#     t1=threading.Thread(target=calc_square,args=(arr,))
#     t2=threading.Thread(target=calc_cube,args=(arr,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()
#     print(f"The program took {time.time()-t} secs")
    

