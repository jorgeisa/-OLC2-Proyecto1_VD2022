/*----HEADER----*/
package main;

import (
	"fmt"
)

var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;



func main(){
	/* Print - Comienzo */
	/* INICIO - Expresion Relacional */
	if 8 == 50 {goto L0;}
	goto L1;
	/* fin de la expression relacional */
	
	L0:
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(101));
	goto L2;
	L1:
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(108));
	fmt.Printf("%c", int(115));
	fmt.Printf("%c", int(101));
	L2:
	fmt.Printf("%c", int(32));
	/* Print - Final */

}