from starter_code.cartpole import CartPoleEnv
import time


def partB():
    cartpole = CartPoleEnv()
    cartpole.reset()
    done = False
    if cartpole.state[3] > 0:
        choice = 1
    else:
        choice = 0

    while not done:
        cartpole.render()

        arr, reward, done, dic = cartpole.step(choice)

        if arr[3] > 0:
            choice = 1
        else:
            choice = 0

        time.sleep(0.01)

        print(arr[2], arr[3])

    cartpole.close()

    


partB()