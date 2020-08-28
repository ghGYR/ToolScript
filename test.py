import matplotlib.pyplot as plt


fig=plt.figure()
ax1=plt.subplot(1,1,1)
line,=ax1.plot([1,2,3,4],[1,2,3,3.2],"o",markersize="1000",clip_on=False)
ax1.set_xlim(0,3)
plt.show()