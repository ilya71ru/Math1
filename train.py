import Model
from Sundail import Sundail 
import numpy as np
from Model import TDormandPrince
from Model import AModel
from threading import Thread

if __name__ =='__main__':
    X=np.array([
        -2.566123740124270e+7,
        1.339350231544666e+8,
        5.805149372446711e+7,
        -29.83549561177192,
        -4.846747552523134,
        -2.100585886567924
    ])


    E_S=Sundail(0,50000,1,X)
    E_M=Sundail(0,50000,1,X)

    def fun_1():
        Integrator=TDormandPrince()
        Integrator.setPrecision(1e-14)
        Integrator.Run(E_S)

    def fun_2():
        Integrator=TDormandPrince()
        Integrator.setPrecision(1e-14)
        Integrator.Run(E_M)

    t1 = Thread(target=fun_1)
    t2 = Thread(target=fun_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    Result=E_S.getResult()
    Result2=E_M.getResult()


    print("hello")