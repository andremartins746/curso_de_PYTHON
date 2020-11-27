def fibinacci(quantidade, sequencia=(0,1)):
    return sequencia if len(sequencia) == quantidade else fibinacci(quantidade, sequencia + (sum(sequencia[-2:]),))


for fib in fibinacci(20):
    print(fib)