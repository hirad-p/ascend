package main

import (
	"fmt"
)

func main() {
	atoz := `the quick brown fox jumps over the lazy dog` // back quotes mean treat literally

	fmt.Printf("%s\n", atoz[0:9])
	fmt.Printf("%s\n", atoz[:9])
	fmt.Printf("%s\n", atoz[15:])

	for i, r := range atoz {
		fmt.Print("%d %c\n", i, r)
	}

	fmt.Printf("%d \n", len(atoz))
}
