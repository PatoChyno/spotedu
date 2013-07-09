import random
from random import randrange
import itertools
from collections import OrderedDict, deque



def time(fn):
    """
    decorator, that adds extra parameter named as 'log_time' to the function's signature (default
    False). If then log_time is set to True, function measures and prints its name and time to the
    terminal
    """
    import time as sys_time
    def _fn(*args, **kwargs):
        #find out whether time should be logged
        prof_time=kwargs.get('log_time', False)
        #delete log_time from kwargs
        try:
            del kwargs['log_time']
        except Exception:
            pass
        if prof_time:
            start=sys_time.time()
            res=fn(*args, **kwargs)
            end=sys_time.time()
            print('execution of %s, took %.3f' % (fn.__name__, end-start))
            return res
        else:
            return fn(*args, **kwargs)
    return _fn


@time
def simple(n, forb):
    """
    simple solution of the rook excercise
    """

    def good(perm):
        return not set(enumerate(perm)).intersection(forb)

    return sum(1 for perm in itertools.permutations(range(n)) if good(perm))


@time
def fast(n, forb):
    """
    advanced solution of the rook excercise; bad permutations are skipped as soon as detected
    """
    pos=[-1]*n
    move=0
    cnt=0
    taken=[]
    while True:
        if move==n:
            cnt+=1
            move-=1
            taken=taken[:-1]
        elif move==-1:
            return cnt
        else:
            pos[move]+=1
            act_pos=pos[move]
            if act_pos>=n:
                pos[move]=-1
                move-=1
                taken=taken[:-1]
            elif act_pos not in taken and (act_pos, move) not in forb:
                taken.append(act_pos)
                move+=1


from fib import memo
@time
def super_fast(n, forb):
    """
    fastest (at least for now) solution of the rook exercise based on recursion. Memo decorator adds
    caching capabilities, which speeds up computation dramatically
    """
    @memo
    def get_pos(num_rows, col_set):
        row=num_rows-1
        if num_rows==0:
            return 1
        return sum(get_pos(num_rows-1, col_set-{i}) for i in range(n) if i in col_set and (row, i) not in forb)

    return get_pos(n,frozenset(range(n)))
    
#size of the board
n=8
#forbid cca one half of the fields, pick them randomly
forb={(randrange(n), randrange(n)) for i in range(n*n//2)}

#common pythonic pattern, executes following code only if, this module (file) is the main module
#that was launched (i.e. code is not executed when only importing from this module
if __name__=="__main__":
    print(simple(n,forb,log_time=True))
    print(fast(n,forb,log_time=True))
    print(super_fast(n,forb,log_time=True))
    
