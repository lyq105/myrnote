size(200,200);
int level = 8;
for(int i = 0; i<=8; ++i)
{
	pair a = (0,i);
	pair b = (8,i);
	pair c = (i,0);
	pair d = (i,8);
	draw(a--b);
	draw(c--d);
}

for (int j = 0; j<6; ++j)
for (int k = 0; k<6; ++k)
{
	filldraw(shift((j,k))*unitsquare,yellow);
}

for(int j=2;j<=4;++j)
for (int k=2;k<=4;++k)
{
	filldraw(shift((j,k))*unitsquare,paleblue);
}
filldraw(shift((3,3))*unitsquare,blue);
