#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*
Button A: X+94, Y+20
Button B: X+57, Y+71
Prize: X=14573, Y=8929
*/
/*
Button A: X+30, Y+92
Button B: X+56, Y+47
Prize: X=3108, Y=9157
*/
int main(int argc, char* argv[]){
 float ax = atoi(argv[1]);
 float ay = atoi(argv[2]);
 float bx = atoi(argv[3]);
 float by = atoi(argv[4]);
 float px = atoi(argv[5]) + 10000000000000;
 float py = atoi(argv[6]) + 10000000000000;
 double a;

 a = (px - ((bx * py) / by)) / (ax - ((bx * ay)/by));
 printf("%f",a);
}
