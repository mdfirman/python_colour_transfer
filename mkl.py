'''
Colour transfer algorithm based on linear Monge-Kantorovitch solution

This code is a direct reimplementation of this previous MATLAB code:
https://github.com/frcs/colour-transfer/blob/master/colour_transfer_MKL.m
'''
import numpy as np


def colour_transfer_MKL(I0, I1):

    assert len(I0.shape) == 3

    X0 = I0.reshape(-1, I0.shape[2])
    X1 = I1.reshape(-1, I1.shape[2])

    A = np.cov(X0.T);
    B = np.cov(X1.T);

    T = MKL(A, B);

    XR = (X0-X0.mean(0)).dot(T) + X1.mean(0);

    return XR.reshape(I0.shape);


def MKL(A, B):
    eps = 2.2204e-16
    N = A.shape[0]

    Da2, Ua = np.linalg.eig(A);
    Da2[Da2<0] = 0
    Da2 = Da2[::-1]
    Ua = Ua[:, ::-1]

    Da = np.diag(np.sqrt(Da2 + eps));
    C = Da.dot(Ua.T).dot(B).dot(Ua).dot(Da);

    Dc2, Uc = np.linalg.eig(C);
    Dc2[Dc2<0] = 0;
    Dc = np.diag(np.sqrt(Dc2 + eps));
    Da_inv = np.diag(1./(np.diag(Da)))

    return Ua.dot(Da_inv).dot(Uc).dot(Dc).dot(Uc.T).dot(Da_inv).dot(Ua.T);
