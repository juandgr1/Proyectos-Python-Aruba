file_direction="/Users/juand.gallego/Documents/Python/Meridian Maps/"
file_name="Apto1"
with open(file_direction+file_name+".svg", 'r') as rf:
    with open(file_direction+file_name+"-copy.svg", 'w') as wf:
        group = False
        for line in rf:
            if "<g" in line:
                group = True
                list=[]

            if group == True :
                if "inkscape:label" in line:
                    s = line.find("=")
                    t = line.find('"', s + 2)
                    id=line[s + 1:t+1]+"\n"
                    if ">" in line:
                        group = False
                        list.append("     id=" + id)
                        for i in list:
                            wf.write(i)
                    else:
                        list.append(line)
                elif ">" in line:
                    group = False
                    list.append("     id="+id)
                    for i in list:
                        wf.write(i)
                else:
                    if "id" in line:
                        pass
                    else:
                        list.append(line)

            if group == False:
                    wf.write(line)
