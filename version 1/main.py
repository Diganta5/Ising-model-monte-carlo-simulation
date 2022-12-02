import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm

J=1
N=80
T=27
k = 1.380649e-23 #boltzmann constant
f = open('ising_mat.npy','wb')
great_mat=[]
mat = np.random.choice([-1,1],[N,N])
great_mat.append(mat)
def ham(mat):
    N=mat.shape[0]
    H = np.zeros([N,N])
    for i in range(1,N-1):
        H[0][i]=-J*mat[0][i]*(mat[1][i]+mat[0][i-1]+mat[0][i+1])
        H[i][0]=-J*mat[i][0]*(mat[i][1]+mat[i-1][0]+mat[i+1][0])
        H[N-1][i]=-J*mat[N-1][i]*(mat[N-2][i]+mat[N-1][i-1]+mat[N-1][i+1])
        H[i][N-1]=-J*mat[i][N-1]*(mat[i][N-2]+mat[i-1][N-1]+mat[i+1][N-1])
        for j in range(1,N-1):
            H[i][j]=-J*mat[i][j]*(mat[i-1][j]+mat[i][j-1]+mat[i+1][j]+mat[i][j+1])

    H[0][0]=-J*mat[0][0]*(mat[0][1]+mat[1][0])
    H[0][N-1]=-J*mat[0][N-1]*(mat[1][N-1]+mat[0][N-2])
    H[N-1][0]=-J*mat[N-1][0]*(mat[N-2][0]+mat[N-1][1])
    H[N-1][N-1]=-J*mat[N-1][N-1]*(mat[N-1][N-2]+mat[N-2][N-1])

    h_sum = np.sum(H)
    return h_sum

m = 0
m_list=[]

num=100000
for _ in tqdm(range(num)):
    #mat1 = np.random.choice([-1,1],[N,N])
    i=np.random.choice(range(N))
    j=np.random.choice(range(N))
    mat1=np.copy(mat)
    mat1[i][j]=-1*mat1[i][j]
    H1 = ham(mat)
    H2 = ham(mat1)
    #prob = np.exp(H1-H2)
    dE=H2-H1
    if dE<=0:
        mat=mat1
        great_mat.append(mat1)
        #np.savez(f,mat1)
        m+=1
        m_list.append(m)
        #print(m,end=" ")

    else:
        l=np.random.uniform(0,1)
        prob = np.exp(-dE/(k*T))
        if l<prob:
            mat=mat1
            great_mat.append(mat1)
            #np.savez(f,mat1)
            m+=1
            m_list.append(m)
            #print(m,end=" ")


np.save(f,great_mat)

#fig,ax=plt.subplots()
#ims=[]
N=len(great_mat)
print(N)
'''for i in range(N):
    im=ax.imshow(great_mat[i],animated=True)
    if i==0:
        ax.imshow(great_mat[0])
    ims.append([im])

ani = animation.ArtistAnimation(fig,ims,interval=200,blit=True,repeat=False)
#writervideo = animation.FFMpegFileWriter(fps=60)
ani.save('ising.gif',writer='imagemagick',fps=10)
#plt.show()
plt.close()'''