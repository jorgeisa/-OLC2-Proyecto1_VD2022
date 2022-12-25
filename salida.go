/*----HEADER----*/
package main;

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8 float64;
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
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=104;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=108;
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
	/* Print - Comienzo */
	t6=H;
	heap[int(H)]=18;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=113;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=98;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=104;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t6=t6+0.12837;
	t7=P+0;
	t7=t7+1;
	stack[int(t7)]=t6;
	P=P+0;
	print_string();
	t8=stack[int(P)];
	P=P-0;
	fmt.Printf("%c", int(32));
	/* Print - Final */
	/* Print - Comienzo */
	fmt.Printf("%d", int(1));
	fmt.Printf("%c", int(32));
	/* Print - Final */
	/* Print - Comienzo */
	goto L2;
	/* goto para evitar errores */
	goto L3;
	L2:
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(101));
	goto L4;
	L3:
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(108));
	fmt.Printf("%c", int(115));
	fmt.Printf("%c", int(101));
	L4:
	fmt.Printf("%c", int(32));
	/* Print - Final */

}