teksts = input("Ievadiet teikumu: ")
def reversWords(teksts):
  sar1 = teksts.split()
  if len(sar1)>1:
    sar1.reverse()
    teksts=""
    for elements in sar1:
      teksts+=elements
      print(teksts)
  else:
    teksts = "Pārāk īss teikums!"
    print(teksts)
  return teksts
reversWords(teksts)