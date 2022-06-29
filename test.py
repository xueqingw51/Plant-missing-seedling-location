center = [(300, 181), (349, 296), (255, 54)]

sorted_list = sorted(center,key = lambda d:d[1],reverse=True)
print(sorted_list)

cotton_coords = [[183, 126, 417, 237],[268, 237, 431, 355],[174, 0, 336, 109]]

sorted_list = sorted(cotton_coords,key = lambda d:d[1],reverse=True)
print(sorted_list)
#a = center
#   new = []
 #   for index, x in enumerate(a):
  #      try:
   #         new.append([x, a[index + 1]])
    #    except:
     #       break
    #x_combs = list(new)
    #print(x_combs)
#0    1    2    3
#[183, 126, 417, 237]    #(300, 181) 2
#[268, 237, 431, 355]    #(349, 296) 1
#[174, 0, 336, 109]     #(255, 54 ) 3
cotton_coords = [[183, 126, 417, 237],[268, 237, 431, 355],[174, 0, 336, 109]]
print (*cotton_coords)


