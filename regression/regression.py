import sys
import os
import math

def main(argv):
  if (len(argv) < 3):
    print "Usage: %s <order> <format> <files>" % (argv[0])
    print "\n\tOrder indicates the desired order of the interpolated polynomial."
    print "\tFormat can be either 'plain' or 'code' to print plain text or array-style output."
    print "\tThe file parser expects an optional tab-separated header line and tab-separated columns."
    print "\tThe first column will be used as X coordinate, all other columns as Y coordinates."
    exit(0)

  order = int(argv[1])

  format_code = (argv[2] == "code")

  files = argv[3:]

  fullrec = []

  for fn in files:
    if format_code:
        print codify(fn) + " = ["
    else:      
      print fn
    f = open(fn)
    lno = 0
    l = f.readline()

    title = []
    rec = []
    row = l[0:-1].split("\t")
    if (not isNumber(row[0])):
      title = row
      lno += 1
      l = f.readline()

    while l != "":
      #skip empty lines
      if len(l)>1:
          srow = l[0:-1].split("\t")
          row = []
          for s in srow:
            if (isNumber(s)):
              row.append(float(s))
            else:
              hashmark = ""
              if format_code:
                  hashmark = "# "

              print "%s%s:%d - Could not parse \"%s\", skipping sample" % (hashmark, fn,lno+1,s)
              row.append(None)
          rec.append(row)
      lno += 1
      l = f.readline()

    # remove empty lines
    rec = filter( lambda x: x[0] != None, rec) 

    ncols = len(rec[0])

    if format_code:
        print "# range"
        print "[ " + str(rec[0][0]) + ", " + str(rec[-1][0]) + "], "
    else:
        print "RMin\t%d\tRMax\t%d" % (rec[0][0],rec[-1][0])

    fst = True

    for i in range(1,ncols):
      try:
        xcol = map(lambda x: x[0], rec)
        ycol = map(lambda x: x[i] if len(x)>i else None, rec)
      except IndexError:
        print rec
        raise
      set = zip(xcol, ycol)
      set = filter( lambda x : (x[1] != None and x[0] != None), set)

      t = ""
      if len(title) >= i - 1:
        t = title[i]
      else:
        t = "Column %d" % (i)

      #print set
      params = findCurve(set, order)

      if format_code:
          pre = ","
          if fst:
              pre = ""
              fst = False
          print pre + "[ \"" + t + "\", [" + reduce(lambda x,y: str(x)+", " + str(y), params) + "] ]"
      else:
          print t + "\t" + reduce(lambda x,y: str(x) + "\t" + str(y), params)

    if format_code:
        print "]"

def codify(s):
  return os.path.basename(s)

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def findCurve(values, n):
  if (n < 0 or values == None):
    return None

  if (n >= len(values)):
    n = len(values)-1

  coeffs = []
  powers = []
  powersums = []

  # x^k for all x and all 0<=k<=2n
  for i in range(len(values)):
    x = values[i][0]
    p = []
    for j in range(2 * n + 1):
      p.append(x**j)
    powers.append(p)

  # sum of x^k for all k
  for i in range(2*n+1):
    ps = 0
    for j in range(len(values)):
      ps += powers[j][i]
    powersums.append(ps)

  # coefficients of the linear system

  for i in range(n):
    cc = []
    for k in range(n+1):
      cc.append(powersums[i+k])

    c = 0.0
    for k in range(len(values)):
      c += powers[k][i] * values[k][1]

    cc.append(c)
      
    coeffs.append(cc)

  #print "powers"
  #print powers
  #print "powersums"
  #print powersums
  #print "coeffs"
  #print coeffs

  return solveLinearSystem(coeffs)



def solveLinearSystem(coefficients):
  variableResultRows = []
  for i in range(len(coefficients)):
    variableResultRows.append(-1)

  iOffset = 0
  jOffset = 0
  m = len(coefficients)
  n = len(coefficients[0])-1

  while jOffset < n:
    firstNonZeroRow = -1
    for i in range(iOffset, m):
      if coefficients[i][jOffset] != 0:
        firstNonZeroRow = i
        break

    if firstNonZeroRow != -1:
      if firstNonZeroRow > iOffset:
          swapRows(coefficients,iOffset,firstNonZeroRow)
      factor = coefficients[iOffset][jOffset]
      coefficients[iOffset][jOffset] = 1
      for j in range(jOffset + 1, n +1):
        coefficients[iOffset][j] /= factor
      for i in range(0,m):
        if (i != iOffset and coefficients[i][jOffset] != 0):
          factor = coefficients[i][jOffset]
          subMulRows(coefficients, i, iOffset, jOffset + 1, factor)
      variableResultRows[jOffset] = iOffset
      iOffset += 1

    jOffset += 1

  result = []
  for i in range(0,m):
    if variableResultRows[i] != -1:
      result.append(coefficients[variableResultRows[i]][n])
    else:
      result.append(None)

  return result

def subMulRows(coeffs, row1, row2, jOffset, factor):
  for j in range(jOffset, len(coeffs[0])):
    coeffs[row1][j] -= coeffs[row2][j] * factor

def swapRows(coeffs, row1, row2):
  temp = coeffs[row1]
  coeffs[row1] = coeffs[row2]
  coeffs[row2] = temp


if __name__ == "__main__":
  main(sys.argv)
