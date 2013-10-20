// plot triangle mesh.


size(200);

file fin_node = input("elip1.txt");
file fin_elem = input("elip1.txt");

int nodenum;
int elemnum;

for (int i = 1;i>-1;++i)
{
	pair [] x;
	real c1 = fin;
	real c2 = fin;
  c = (c1*100,c2*100);
	if(eof(fin))break;
	draw(ellipse(c,a*100,b*100,alpha));
	label(scale(0.2,0.2)*Label(format("%d",i),c));
}
