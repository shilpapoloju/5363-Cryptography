#########################################################
#Name: Shilpa Poloju
#Class: CMPS 5363 Cryptography
#Date: 4th august 2015
#Program 3 - Elliptical Curve
#########################################################
import argparse
import sys
import elliptical as e
import fractions


def main():
	#parse parameters
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + a*x + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + a*x + b")
    parser.add_argument("-x1",dest="x1", help="Part 'x1,y1' of elliptical curve: y1^2 = x1^3 + a*x1 + b ")
    parser.add_argument("-y1",dest="y1", help="Part 'x1,y1' of elliptical curve: y1^2 = x1^3 + a*x1 + b")
    parser.add_argument("-x2",dest="x2", help="Part 'x2,y2' of elliptical curve: y2^2 = x2^3 + a*x2 + b")
    parser.add_argument("-y2",dest="y2", help="Part 'x2,y2' of elliptical curve: y2^2 = x2^3 + a*x2 + b")

    args = parser.parse_args()

   
    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    
	
    a = fractions.Fraction(args.a)
    b = fractions.Fraction(args.b)
    x1 = fractions.Fraction(args.x1)
    y1 =  fractions.Fraction(args.y1)
    x2 =  fractions.Fraction(args.x2)
    y2 =  fractions.Fraction(args.y2)

   

    #loop for checking point on the curve
    if(y1**2 == x1**3+a*x1+b and y2**2 == x2**3+a*x2+b):
        print("point x1,y1 is  on the curve")
		
        #loop for finding the slope and third coordinate for same points
        if(x1==x2 and y1==y2):
            print("same points")
            m = (3*x1**2+a)/(2*y2)
            print(" m =",m)
            x3 = fractions.Fraction(m**2-x1-x2).limit_denominator(1000)
            y3 = fractions.Fraction(m*(x3-x1)+y1).limit_denominator(1000)
            print("x3 = ",x3,"y3 = ",y3)
            e.ellipticals(m,a,b,x1,y1,x2,y2,x3,y3)
			
			#loop for finding the slope and the third coordinate for different point
        else:
            print("different points")
            m = (y2-y1)/(x2-x1)
            print("m = ",m)
            x3 = fractions.Fraction(m**2-x1-x2).limit_denominator(1000)
            y3 = fractions.Fraction(m*(x3-x1)+y1).limit_denominator(1000)
            print("x3 = ",x3,"y3 = ",y3)
            e.ellipticals(m,a,b,x1,y1,x2,y2,x3,y3)
    else:
        print("point are not on the curve, enter different points")
       
	
    

    
if __name__ == '__main__':
    main()
