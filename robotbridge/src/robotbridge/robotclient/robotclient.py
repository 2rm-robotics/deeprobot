#!/usr/bin/env python3


fifo = []

def drive_robot(linear, angular):
    global fifo
    if not fifo:
        try:
            fifo = open('/tmp/robotfifo', 'w')
        except FileNotFoundError:
            print('La FIFO de contrôle du robot n''existe pas. Vérifiez que le noeud ''robotbridge'' est bien lancé')
            return

    fifo.write('{{"linear":{linear}, "angular":{angular}}}'.format(linear = linear,angular = angular))
    fifo.flush()
