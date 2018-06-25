package main

import (
	"fmt"
)

const ( // could be var
	message = "The answer to life is %d\n"
	answer  = 42
)

func main() {
	// var message string
	// message = "Hello, World!\n"
	// fmt.Printf(message)

	message := "The answer to life is %d\n" // sets and infers type based on value
	answer := 42
	fmt.Printf(message, answer)

	var pi float64 = 3.14
	fmt.Printf("Value %.2f\n", pi)

}
