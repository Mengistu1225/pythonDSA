def ArrayChallenge(arr):
   """
   Determines the number of ways two students can be seated next to each other in a classroom with a two-column desk arrangement.

   Args:
       arr: An array of integers in the format [K, r1, r2, r3, ...], where:
           - K represents the number of desks in the classroom.
           - r1, r2, r3, ... represent occupied desks in sorted order.

   Returns:
       The number of ways two students can be seated next to each other.
   """

   K = arr[0]  # Total number of desks
   occupied_desks = set(arr[1:])  # Set of occupied desks for efficient lookup
   varOcg = 0  # __define-ocg__

   available_pairs = 0

   # Iterate through each available desk
   for desk in range(1, K + 1):
       if desk not in occupied_desks:
           # Check for adjacent desks in the same column
           if desk + 1 <= K and desk + 1 not in occupied_desks:
               available_pairs += 1

           # Check for adjacent desk in the other column (taking odd/even desk numbers into account)
           adjacent_desk = desk + K if desk % 2 == 1 else desk - K
           if 1 <= adjacent_desk <= K and adjacent_desk not in occupied_desks:
               available_pairs += 1

   return available_pairs
