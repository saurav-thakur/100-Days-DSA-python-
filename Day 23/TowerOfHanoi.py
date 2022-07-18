def toh(N,frm,aux,to):

    if N == 1:
        print(f"Move Disk {N} from rod {frm} to {to}")
        return 1

    toh(N-1,frm,aux,to)