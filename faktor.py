num_articles, impact_factor = [int(x) for x in input().split()]

max_toBribe = num_articles * impact_factor

i = 0
while i <= max_toBribe:
    net_factor = i/num_articles
    ceiling_impactFactor = impact_factor -1
    if net_factor < ceiling_impactFactor:
        i +=1
    else:
        print(i + 1)
        break
        
    
