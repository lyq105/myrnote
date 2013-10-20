
path ellipse(pair c, real a, real b, real alpha)
{
	return shift(c)*rotate(alpha*180/3.14159)*scale(a,b)*unitcircle;
}

size(200);
//size(200,IgnoreAspect);
file fin = input("elip1.txt");
real a,b,alpha;
pair c;
for (int i = 1;i>-1;++i)
{
	//size(200);
	a = fin;
	b = fin;
	alpha = fin;
	real c1 = fin;
	real c2 = fin;
  c = (c1*100,c2*100);
	if(eof(fin))break;
	draw(ellipse(c,a*100,b*100,alpha));
	//Label l = Label()
	label(scale(0.2,0.2)*Label(format("%d",i),c));
//write(stdout,c);
//write(stdout);
//write(stdout,"\n");
}
//draw(unitcircle);
	//draw(ellipse((),a,b,alpha));
//draw(ellipse((3,30),1,2,0));
for (int j=1;j<10;++j)
{
	//draw(ellipse((3+j,3+j),2,1,j*5));
}
