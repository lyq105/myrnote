// this file is used to plot definition of ellipse equation.
//  2011-10-15 20:39:54

import graph;
import geometry;

pair ellipse_point(pair center, pair ab, real alpha, real scal )
{
	real x;
	real y;
	x = center.x + ab.x * cos(scal) * cos(alpha) - ab.y * sin(scal) * sin(alpha) ; 
	y = center.y + ab.x * cos(scal) * sin(alpha) + ab.y * sin(scal) * cos(alpha) ; 
	return (x,y);
}

size(200,200);
path ap;
path bp;
pair a0=ellipse_point((0.5,0.5),(0.4,0.2),35*3.14159265/180,0);
pair xp = (0.78,0.5);
pair c0=ellipse_point((0.5,0.5),(0.4,0.2),35*3.14159265/180,1);

ap = (-1,0)..(1,0);
bp = (0,-1)..(0,1);

draw(shift(0.5,0.5)*rotate(35)*scale(0.4,0.2)*unitcircle);
draw(shift(0.5,0.5)*rotate(35)*scale(0.4,0.2)*ap,dashed);
draw(shift(0.5,0.5)*rotate(35)*scale(0.4,0.2)*bp,dashed);
draw((0.5,0.5)..(0.78,0.5),dashed);
dot((0.5,0.5));

dot(c0);
draw((0.5,0.5)..c0,dashed);
draw(arc(a0,(0.5,0.5),xp,0.1));
draw(arc(a0,(0.5,0.5),c0,0.15));

label(scale(0.5)*Label("$(x_0,y_0)$",(0.5,0.4),S));
label(scale(0.5)*Label("$(x,y)$",c0,align=N));
label("$\theta$",c0-(-0.03,0.10));
label("$\nu$",(0.5,0.5)+(0.12,0.04));
xaxis("$x$",Arrow);
yaxis("$y$",Arrow);
