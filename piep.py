from matplotlib import pyplot as plt
k={'Pinki':314,'Sathwika':400,'Tinnu':430,'Chinni':245}
l=list(k.keys())
m=list(k.values())
plt.figure(figsize=(30,30))
plt.pie(m,labels=l,autopct='%0.0f%%',shadow='true')
plt.show()
