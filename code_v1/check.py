import numpy as np
import imageio
import matplotlib.pyplot as plt
import time


def svt(mat, tau):
    u, s, v = np.linalg.svd(mat, full_matrices = 0)
    vec = s - tau
    vec[vec < 0] = 0
    return np.matmul(np.matmul(u, np.diag(vec)), v)
 
def LRMC(sparse_mat, dense_mat, rho, maxiter):
    
    pos_train = np.where(sparse_mat != 0)
    pos_test = np.where((sparse_mat == 0) & (dense_mat != 0))
    binary_mat = sparse_mat.copy()
    binary_mat[pos_train] = 1
    
    X = sparse_mat.copy()
    Z = sparse_mat.copy()
    T = sparse_mat.copy()
    rse = np.zeros(maxiter)
    
    for it in range(maxiter):
        print('now--',it)
        Z = svt(X + T / rho, 1 / rho)
        print('Z')
        X = Z - T / rho
        print('X')
        X[pos_train] = sparse_mat[pos_train]
        print('X[]')
        T = T - rho * (Z - X)
        print('T')
        rse[it] = (np.linalg.norm(X[pos_test] - dense_mat[pos_test], 2) 
                   / np.linalg.norm(dense_mat[pos_test], 2))
        print('res')
    return X, rse

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 
lena = imageio.imread('/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/test.bmp')/255.0
sparse_lena=imageio.imread('/Users/cesar/Desktop/同步储存/net/jpeg/code_v1/result.jpeg')/255.0
print('The shape of the image is {}.'.format(lena.shape))
 
dim1, dim2,dim3 = lena.shape
mask = np.round(np.random.rand(dim1, dim2,dim3))  # Generate a binary mask.
mask1 = np.round(np.random.rand(dim1, dim2,dim3))
# mask2 = np.round(np.random.rand(dim1, dim2))
 
plt.figure(figsize=(15,12))
plt.imshow(lena)
plt.title('The original Lena')
plt.axis('off')
print('1 done')
 
plt.figure(figsize=(15,12))
plt.imshow(sparse_lena)
plt.title('The incomplete Lena')
plt.axis("off")
print('2 done')
 
plt.show()
print('show done')
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
start = time.time()
rho = 0.005
maxiter = 50
print('1 start')
mat_hat, rse_svt = LRMC(sparse_lena[:,:,0], lena[:,:,0], rho, maxiter)
end = time.time()
print('1 end')
print('Running time: %d seconds.'%(end - start))
start = time.time()
print('2 start')
mat_hat1, rse_svt1 = LRMC(sparse_lena[:,:,1], lena[:,:,1], rho, maxiter)
end = time.time()
print('2 end')
print('Running time: %d seconds.'%(end - start))
start = time.time()
print('3 start')
mat_hat2, rse_svt2 = LRMC(sparse_lena[:,:,2], lena[:,:,2], rho, maxiter)
end = time.time()
print('3 end')
print('Running time: %d seconds.'%(end - start))
 
#修复完把三张图拼接在一起
c=[]
for i in range(dim1):
    c.append([])
    for j in range(dim2):
        print('i=',i,'j=',j)
        c[i].append([mat_hat[i][j],mat_hat1[i][j],mat_hat2[i][j]])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
plt.figure(figsize=(20,15))
# plt.imshow(mat_hat)
plt.imshow(c)
# plt.imshow(mat_hat2)
plt.savefig("lbk.png")
plt.axis('off')
plt.show()

