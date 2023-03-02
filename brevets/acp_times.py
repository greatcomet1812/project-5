"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

# Control location Speeds
# (checkpoint1, checkpoint2) : (min speed, max speed)
dist_to_speed = {
   (0, 200): (15, 34),
   (200, 400): (15, 32),
   (400, 600): (15, 30),
   (600, 1000): (11.428, 28),
   (1000, 1300): (13.333, 26)
}

# Brevet Time Limits
# brevet distance (km) : hours 
time_limits = {
   200 : 13.5,
   300 : 20,
   400 : 27,
   600 : 40,
   1000 : 75
}

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
      brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """

   # distance past the brevet dist clipped to the brevet dist
   if control_dist_km > brevet_dist_km:
      control_dist_km = brevet_dist_km

   mins = 0  # minutes
   dist_left = control_dist_km  # distance left 

   for dist in dist_to_speed:
      # current distance to travel
      if((dist[1] - dist[0]) <= dist_left):
         curr_dist = dist[1] - dist[0]
      else:
         curr_dist = dist_left

      max_speed = dist_to_speed[dist][1]
      mins += (curr_dist / max_speed * 60)

      # checks if the control distance is shorter than the next checkpoint
      if control_dist_km <= dist[1]: 
         break

      dist_left = control_dist_km - dist[1]
            
   return brevet_start_time.shift(minutes=round(mins))


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
         brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """

   # at last checkpoint
   if control_dist_km >= brevet_dist_km:
      hrs = time_limits[brevet_dist_km]
      return brevet_start_time.shift(hours=hrs)

   # within the first 60km
   if control_dist_km <= 60:
      mins = (control_dist_km / 20 + 1) * 60
      return brevet_start_time.shift(minutes=round(mins))

   mins = 0  # minutes
   dist_left = control_dist_km  # distance left

   for dist in dist_to_speed:
      # current distance to travel
      if((dist[1] - dist[0]) <= dist_left):
         curr_dist = dist[1] - dist[0]
      else:
         curr_dist = dist_left
         
      min_speed = dist_to_speed[dist][0]
      mins += (curr_dist / min_speed * 60)

      # checks if the control distance is shorter than the next checkpoint
      if control_dist_km <= dist[1]: 
         break

      dist_left = control_dist_km - dist[1]

      
   return brevet_start_time.shift(minutes=round(mins))


# if __name__ == "__main__":
#    t = arrow.get('2013-05-11T21:23:58.970460+07:00')
#    print(open_time(60, 200, t))
#    print(open_time(120, 200, t))

#    print(close_time(1200, 1000, t))
#    print(open_time(305, 300, t))