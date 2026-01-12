# In order to understand how much memory is being used and what is taking up memory during execution: tracemalloc
# DO NOT USE IN PROD
import tracemalloc
tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

result = my_function(10000)

snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("Top 10 memory usages")
for stat in sorted(top_stats, key=lambda x: x.size, reverse=True )[:10]:
    print(f"{stat.traceback} {stat.size / 1024:.2f} KiB")

tracemalloc.stop()



# The actual amount of memory occupied by an object, including all its references, lists, dictionaries, and other nested objects (recursively).
from pympler import asizeof
print(asizeof.asizeof(my_complex_object))
