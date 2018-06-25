package main

import (
	"fmt"
	"os"
)

func main() {
	n, err := fmt.Printf("Hello, World!")

	switch {
	case err != nil:
		os.Exit(1)
	case n == 0:
		fmt.Printf("No input")
	default:
		fmt.Printf("OK!")
	}

	atoz := `the quick brown fox jumps over the lazy dog`
	v := 0
	c := 0

	for _, r := range atoz {
		switch r {
		case 'a', 'e', 'i', 'o', 'u':
			v++
		default:
			c++
		}
	}

	fmt.Printf("V %d C %d", v, c)
}
