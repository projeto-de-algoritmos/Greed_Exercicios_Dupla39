class Solution(object):
  def eraseOverlapIntervals(self, intervals):
    fim, cont = 0, 0
    for inicio, fimIntervalo in sorted(intervals, key=lambda x: x[1]):
        if inicio >= fim: 
            fim = fimIntervalo
        else: 
            cont += 1
    return cont