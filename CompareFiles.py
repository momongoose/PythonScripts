import mysql.connector

# this is gonna compare if Data from File A is in File B and if not then write it into file
fileA = "pathA"
fileB = "pathB"
OutputFile = "pathC"

def compareFiles(A, B, Out):
    with open(A, 'r', encoding="utf-8") as fileA:
        for line in fileA.readlines():
            li = str(line.replace('"', '').replace("\n", ""))
            count = 0
            with open(B, 'r', encoding="ANSI") as fileB:
                for lin in fileB.readlines():
                    l = str(lin.replace("\n", "").replace('"', ""))
                    if li in l:
                        count += 1
            if count == 0:
                with open(Out, 'a', encoding="utf-8") as Ou:
                    Ou.write(li + "\n")


compareFiles(fileA, fileB, OutputFile)