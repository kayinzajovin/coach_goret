def clean_database(record_ids):
# Requirement: Remove all odd numbers from the list
   for record_id in record_ids[:]:
    if record_id % 2 != 0:
     record_ids.remove(record_id)
   return record_ids
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [3, 4, 6, 9, 10]


def clean_database(record_ids):
    # Requirement: Remove all odd numbers from the list
    cleaned_records = []
    for record_id in record_ids:
        if record_id % 2 == 0:
            cleaned_records.append(record_id)
    return cleaned_records

#I ran the code and found that the actual output is not as expected. The issue is that when we remove an item from the list while iterating over it,
#  it can cause the loop to skip the next item. To fix this, we can iterate over a copy of the list instead of the original list. Here's the corrected code:
#I checked the condition and confirmed  it was working correctly. The issue was with the way we were iterating over the list. 
#I found that using .remove()while looping  through the same list caused errors
#I discovered the return statement was inside the loop stopping it tooo early
#I fixed the logic to avoid modifying the the list during the iteration and let the loopcomplete
#I ended with a safer solution that correctly  filters and returnsthe expected result



# COMMENTS USING THE NEW CODE:
# The function now creates a new list called cleaned_records to store the even numbers.
# It iterates through the original list of record_ids and checks if each record_id is even.
# If a record_id is even, it is appended to the cleaned_records list.
# Finally, the function returns the cleaned_records list, which contains only the even numbers.

