def tower_hanoi(n_disc,source,helper,dest):
    if n_disc==1:
        print('Move 1st disc from', source, 'to ', dest)
        return
    tower_hanoi(n_disc-1,source,dest,helper)
    print('move ', n_disc , "th disk from ",source, "to ", dest)
    tower_hanoi(n_disc-1,helper,source,dest)

tower_hanoi(2,'source','helper','dest')