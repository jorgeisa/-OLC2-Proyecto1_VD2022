/*----HEADER----*/
package main;

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

/*-----NATIVES-----*/
func print_string(){
	t1=P+1;
	t2=stack[int(t1)];
	L1:
	t3=heap[int(t2)];
	if t3 == -1 {goto L0;}
	fmt.Printf("%c", int(t3));
	t2=t2+1;
	goto L1;
	L0:
	return;
}


func main(){
	/* Print - Comienzo */
	t0=H;
	heap[int(H)]=6;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=98;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t0=t0+0.12837;
	t4=P+0;
	t4=t4+1;
	stack[int(t4)]=t0;
	P=P+0;
	print_string();
	t5=stack[int(P)];
	P=P-0;
	fmt.Printf("%c", int(32));
	/* Print - Final */

}