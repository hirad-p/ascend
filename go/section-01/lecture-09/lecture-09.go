package main

import (
	"fmt"
)

func main() {
	var counter int
	counter = 0
	for counter < 10 {
		fmt.Printf("Hello, there")
		counter++
	}

	for counter := 0; counter < 10; counter++ {
		fmt.Printf("Hello, there")
	}

	for i, j := 0, 1; i < 10; i, j = i+1, j*2 {
		fmt.Printf("Hello, there")
		fmt.Printf("%d", j)
	}

	// infinite loop
	for {
		fmt.Printf("Hello, there")
	}
}
