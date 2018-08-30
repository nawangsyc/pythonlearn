import turtle as t
for i in range(4):
    t.seth(90 * (i+1))
    #90,180,270，360
    t.circle(200,90)
    #-90,0,90,180
    t.seth( -90+i*90)
    t.circle(200,90)