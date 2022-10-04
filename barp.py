
from matplotlib import pyplot as plt
d1={'Sathwika':8.81,'Pinki':8.32,'Tinnu':9.8}
student=list(d1.keys())
marks=list(d1.values())
plt.bar(student,marks)
print(plt.show())
